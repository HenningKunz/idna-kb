# iDNA Applications Knowledge Base – Hugo/Hextra Setup

Nachbau der Optik/Struktur von https://truedemkbpoc.z6.web.core.windows.net/en/
(Hugo + Theme "Hextra"), befüllt mit euren migrierten Confluence-Inhalten.

## Was hier drin ist
```
hugo.yaml              - Hauptkonfiguration (Menü, Suche, Theme-Optionen)
content/en/             - alle 111 KB-Seiten + Startseite (Sprache: Englisch)
static/images/kb/       - alle Bilder/Anhänge aus dem Confluence-Export
assets/js/              - lokal gehostetes FlexSearch (kein CDN-Aufruf nötig)
themes/hextra/          - das Hugo-Theme selbst (unverändert, Stand: aktueller main-Branch)
public/                 - FERTIG GEBAUTE Website, direkt deploybar
```

## Lokal ansehen / weiterentwickeln

Voraussetzung: Hugo **extended**, Version >= 0.146.0
(die per `apt` installierbare Version 0.123 reicht NICHT, siehe unten)

```bash
# Hugo extended aktuell laden, falls apt-Version zu alt ist:
curl -sL https://github.com/gohugoio/hugo/releases/download/v0.147.9/hugo_extended_0.147.9_linux-amd64.tar.gz -o hugo.tar.gz
tar -xzf hugo.tar.gz hugo && sudo mv hugo /usr/local/bin/

# Im Projektordner:
hugo server -D
# -> http://localhost:1313/en/
```

Neuen Build erzeugen (z. B. nach Content-Änderungen):
```bash
hugo --minify
# Ergebnis liegt danach wieder in public/
```

## Deployment auf Azure Static Website Hosting
(genau die Hosting-Art, auf der auch die Referenzseite läuft –
erkennbar am `*.web.core.windows.net`-URL-Muster = Azure Storage
Static Website)

1. **Storage Account mit Static Website Feature aktivieren** (falls noch nicht
   vorhanden): Azure Portal → Storage Account → "Static website" → Enabled,
   Index-Dokument: `index.html`, Error-Dokument: `404.html`

2. **Inhalt von `public/` hochladen** – entweder:
   - Azure Portal → `$web`-Container → Dateien manuell hochladen, oder
   - Azure CLI:
     ```bash
     az storage blob upload-batch \
       --account-name <euer-storage-account> \
       --destination '$web' \
       --source public
     ```

3. **CDN/Cache** (optional, aber empfohlen für Produktion): Azure CDN oder
   Azure Front Door vor den Storage Account schalten – Azure Storage Static
   Websites liefern sonst ohne eigenes CDN aus, was für interne KB meist
   ausreichend, für öffentliche Kunden-KB aber langsamer ist.

4. **Eigene Domain** (z. B. `kb.panagenda.com` statt `*.web.core.windows.net`):
   CNAME auf den Static-Website-Endpunkt, dann in Azure als Custom Domain
   hinterlegen (HTTPS erfordert zusätzlich Azure CDN oder Front Door, da
   Storage Static Websites selbst kein Custom-Domain-HTTPS anbieten).

## Bekannte offene Punkte (Nacharbeit)

1. **Nur Englisch vorhanden.** Referenzseite hat EN/DE/FR. Für weitere
   Sprachen: `content/de/`, `content/fr/` anlegen (gleiche Dateinamen wie
   in `content/en/`) und in `hugo.yaml` unter `languages:` ergänzen.
2. **Logo/Branding**: aktuell Platzhalter-Textlogo ("iDNA Applications KB").
   Für ein echtes Logo: `static/img/logo.svg` ablegen und in `hugo.yaml`
   unter `params.navbar.logo.path` referenzieren.
3. **FlexSearch-Version eingefroren** auf 0.8.143 (lokal in `assets/js/`
   abgelegt, da der Standard-CDN-Weg in dieser Umgebung blockiert war).
   Bei Bedarf aktualisieren: neue Version von npm ziehen, Datei ersetzen.
4. **Icons der Card-Übersichten** sind grob nach Themenpassung gewählt
   (`rebuild_hierarchy.py`, Dict `ICONS`) - bei Bedarf gegen die Liste in
   `themes/hextra/data/icons.yaml` austauschen.

## Seitenhierarchie (jetzt echte Hugo-Sections, nicht mehr flach)

Die komplette Confluence-Seitenhierarchie wurde als verschachtelte
Ordnerstruktur unter `content/en/docs/` nachgebaut - inkl. Card-Übersicht
auf jeder Section-Landingpage (genau wie bei der Referenzseite):

```
content/en/docs/_index.md                              (Docs-Startseite mit Cards)
content/en/docs/documentation/_index.md                 (Cards: Privacy Policy, Setup Guide, User Guide)
content/en/docs/documentation/setup-guide/_index.md      (Cards: 11 Setup-Unterseiten)
content/en/docs/documentation/user-guide/_index.md       (Cards: 6 Bereiche)
content/en/docs/documentation/user-guide/components-of-idna-applications/...
content/en/docs/frequent-cases/_index.md                 (Cards: Troubleshooting-Themen)
content/en/docs/frequent-cases/user-management/...
content/en/docs/release-notes/_index.md                  (Cards: alle Versions-Releases)
content/en/docs/technical-articles/_index.md              (Cards: technische Deep-Dives)
content/en/docs/technical-articles/deploy-idna-applications-on-azure-beta/...
```

Neu erzeugen (z. B. nach weiteren Confluence-Exports): `rebuild_hierarchy.py`
im Projekt-Root ausführen (liest aus `../hugo_output/content/kb/`, schreibt
nach `content/en/docs/`).
