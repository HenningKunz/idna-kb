---
title: "Weighted analysis"
weight: 81
source_confluence_id: 28574826
draft: false
---
An important part of the design analysis is that criteria are not just
analyzed on their own but also used in combination with others. Meaning
that the design analysis is based on weighted criteria, not just
individual elements. What does this mean? Well let's say an application
sends out a mail when a user performs a certain action. In the code this
is identified by, for example, a formula like @mailsend. However, if
that mail is also encrypted in the same code block before being send out
the complexity is much higher as this means that it hits at least three
different criteria:

a\) It uses mail functionality

b\) It uses encryption

c\) It has a Notes client dependency (for the encryption to work)

  
The total weighted complexity of the combination of all three is higher
than the sum of each individual element would be and therefore panagenda
iDNA Applications will give it a higher complexity rating.

  

**Next Topic:**

[Design Complexity Ruleset](/kb/design-complexity-ruleset/)
