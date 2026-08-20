#!/usr/bin/env python3
"""
Rebuilds content/en/docs/ as a properly nested Hugo section tree,
mirroring the original Confluence page hierarchy, with card overviews
on every section landing page (like the TrueDEM reference site).
"""
import re
import shutil
from pathlib import Path

SRC = Path("/home/claude/hugo_output/content/kb")
DST = Path("/home/claude/kb-site/content/en/docs")

ICONS = {
    "documentation": "document", "setup-guide": "cog", "user-guide": "bookmark",
    "frequent-cases": "support", "release-notes": "clipboard",
    "technical-articles": "code", "components-of-idna-applications": "cube",
    "building-your-own-custom-insights": "sparkles", "data-collection": "database",
    "design-complexity": "chip", "general-information": "identification",
    "getting-started-with-idna-applications": "flag", "user-management": "users",
    "deploy-idna-applications-on-azure-beta": "cloud", "catalog": "library",
}
DEFAULT_ICON = "document"

def load_pages():
    pages = {}
    for f in SRC.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n\n(.*)", text, re.DOTALL)
        fm_text, body = m.group(1), m.group(2)
        fm = {}
        for line in fm_text.split("\n"):
            mm = re.match(r"^(\w+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip().strip('"')
        pages[f.stem] = {"fm": fm, "body": body}
    return pages

def strip_leading_banner_image(body):
    """Confluence overview pages often start with a decorative banner image
    (e.g. a generic stock photo) as the very first line - this clashes with
    the card-grid landing page style, so drop it if it's the first thing."""
    lines = body.split("\n")
    idx = 0
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx < len(lines) and re.match(r"^!\[\]\(/images/", lines[idx].strip()):
        del lines[idx]
        # also drop the blank line that follows, if any
        while idx < len(lines) and lines[idx].strip() == "":
            del lines[idx]
    return "\n".join(lines)

def convert_shortcodes(body):
    def open_repl(m):
        typ = {"note": "info", "warning": "warning", "tip": "info"}.get(m.group(1), "info")
        return f'{{{{% callout type="{typ}" %}}}}'
    body = re.sub(r"\{\{% (note|warning|tip) %\}\}", open_repl, body)
    body = re.sub(r"\{\{% /(note|warning|tip) %\}\}", "{{% /callout %}}", body)
    return body

def build_children_map(pages):
    children = {}
    for slug, d in pages.items():
        p = d["fm"].get("parent")
        if p:
            children.setdefault(p, []).append(slug)
    return children

def write_node(slug, pages, children, out_dir, is_root_docs_index=False):
    data = pages[slug]
    title = data["fm"].get("title", slug)
    weight = data["fm"].get("weight", "999")
    date = data["fm"].get("date", "")
    source_id = data["fm"].get("source_confluence_id", "")
    body = convert_shortcodes(data["body"])
    body = strip_leading_banner_image(body)

    kids = sorted(children.get(slug, []), key=lambda s: int(pages[s]["fm"].get("weight", 999)))

    front = ["---"]
    front.append(f'title: "{title}"')
    front.append(f"weight: {weight}")
    if date:
        front.append(f"date: {date}")
    front.append(f"source_confluence_id: {source_id}")
    front.append("draft: false")
    front.append("---")
    front.append("")
    content = "\n".join(front) + body

    if kids:
        # This node becomes a SECTION (folder + _index.md), with a card
        # overview of its children appended after its own text content.
        section_dir = out_dir / slug
        section_dir.mkdir(parents=True, exist_ok=True)

        cards = ["", "## In this section", "", "{{< cards >}}"]
        for k in kids:
            k_title = pages[k]["fm"].get("title", k)
            icon = ICONS.get(k, DEFAULT_ICON)
            cards.append(f'  {{{{< card link="{k}" title="{k_title}" icon="{icon}" >}}}}')
        cards.append("{{< /cards >}}")
        content += "\n".join(cards) + "\n"

        (section_dir / "_index.md").write_text(content, encoding="utf-8")
        for k in kids:
            write_node(k, pages, children, section_dir)
    else:
        # Leaf page -> plain markdown file in the current folder
        (out_dir / f"{slug}.md").write_text(content, encoding="utf-8")

def main():
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True, exist_ok=True)

    pages = load_pages()
    children = build_children_map(pages)
    roots = [s for s, d in pages.items() if not d["fm"].get("parent")]
    print(f"Root-Seite(n): {roots}")

    # docs/_index.md itself = content of the single root page (Dashboard),
    # its own children become the top-level sections under /docs/.
    root_slug = roots[0]
    root_data = pages[root_slug]
    title = root_data["fm"].get("title", "Documentation")
    body = convert_shortcodes(root_data["body"])
    body = strip_leading_banner_image(body)
    kids = sorted(children.get(root_slug, []), key=lambda s: int(pages[s]["fm"].get("weight", 999)))

    front = [
        "---",
        f'title: "{title}"',
        "cascade:",
        "  type: docs",
        "draft: false",
        "---",
        "",
    ]
    cards = ["", "## Sections", "", "{{< cards >}}"]
    for k in kids:
        k_title = pages[k]["fm"].get("title", k)
        icon = ICONS.get(k, DEFAULT_ICON)
        cards.append(f'  {{{{< card link="{k}" title="{k_title}" icon="{icon}" >}}}}')
    cards.append("{{< /cards >}}")

    (DST / "_index.md").write_text("\n".join(front) + body + "\n".join(cards) + "\n", encoding="utf-8")

    for k in kids:
        write_node(k, pages, children, DST)

    total = sum(1 for _ in DST.rglob("*.md"))
    print(f"Fertig: {total} Markdown-Dateien geschrieben (inkl. Section-Index-Seiten)")

if __name__ == "__main__":
    main()
