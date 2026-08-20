---
title: "Instances versus Databases"
weight: 63
source_confluence_id: 28574745
draft: false
---
iDNA Applications looks at individual instances when collecting data. An
instance is defined as a nsf/ntf container living on a server having a
replica ID. A Domino application or 'database' is determined by a unique
replica id and can be represented by more than one instance
(replicas).  
  
**Why are we collecting info about different instances instead of just
one?**  
By looking at the instances we can give you more granular and detailed
information about the application. Like on which servers it exists,
which instances are being used by which users and if there are
differences in design between replicas (for instance when replication is
broken).

It also allows us to indicate differences in design between application
instances and problems with replication, the design task, design
inheritance settings and duplicate templates that could cause
differences in design.

  

# Database / application:

If in this documentation the term 'database' or in some cases
'application'\* is used, it represents a unique database identified as a
file with extension .NSF or .NTF and all its analyzed\*\* instances
(replicas) on other servers. Also, if in this document the term
'application' is used in reference to analyzed databases, it refers to
databases of both type Mail-In databases and Applications.

  

# Instance:

If the term instance is used, a single replica of that database is
meant. Note that more than one instance with the same replica ID may
exist on any given server.

  

**Next Topic:**

[Definitions](/kb/definitions/)

  

------------------------------------------------------------------------

*\* The term 'application' is also used to indicate a category type of
databases as defined in the topic [Definitions](/kb/definitions/).*

*\*\* As panagenda iDNA Applications only has insights into the
instances on servers it is analyzing it is important to ensure all
servers are included in your discovery set. For details about this
please refer to the technical documentation.*
