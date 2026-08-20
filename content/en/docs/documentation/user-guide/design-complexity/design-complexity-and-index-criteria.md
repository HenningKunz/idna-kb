---
title: "Design Complexity and Index Criteria"
weight: 80
source_confluence_id: 28574824
draft: false
---
Based on the collected data panagenda iDNA Applications uses a wide
range of criteria to determine design complexity and index.  
Factors that for instance can influence the complexity are:

- Type and number of specific design elements occurring in the
  application design
- Specific combinations of design elements occurring in the application
  design
- Hardcoded references (for instance hard coded server names, etc.)
- Number of code blocks and code lines in the application
- Domino/Notes client dependencies
- Calls to local systems (for instance code that references a user's
  local hard disk or accesses specific files stored on the server)
- Occurrence of specific code elements that can cause potential
  migration/modernization challenges
- Occurrences of Author/Reader fields
- SMTP / mail / fax / etc. references that indicate a dependency on a
  specific system or server
- Third party software dependencies
- Encryption dependencies
- Mail dependencies
- Occurrences of specific code functions and snippets or combinations of
  such code functions and snippets.
- Etc. etc.

  

{{% callout type="info" %}}

**Custom Insights build by your own organization are not considered
while computing Design complexity and index scores. Deactivating one or
more of the standard provided rulesets (identifiable in the Manage
section by the panagenda logo behind them) can impact the complexity and
index scores. It is recommended not to do this.**

{{% /callout %}}

  

**Next Topic:**

[Weighted analysis](/kb/weighted-analysis/)

  

  
