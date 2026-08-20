---
title: "Definitions"
weight: 64
date: 2022-04-11
source_confluence_id: 28574746
draft: false
---
**In this topic:**

  

# Determination of Database Types & Focus Databases

The appliance automatically categorizes a found NSF/NTF instance into
one of the following types of categories:

1.  User Mail database(identified by a person document pointing to the
    instance)
2.  Mail-In database(identified by a non-system mail-in document …)
3.  System database(identified via well-known file or template name)
4.  mail.box database(identified from Domino server configuration
    settings)
5.  Directory(identified from Domino server configuration/used template)
6.  Orphaned User Mail(user mail files no longer associated with a
    person document)
7.  Application databases(all remaining not categorized into cat 1-6)

  
If a NSF/NTF instance is categorized once on one server, all existing
instances with the same replica ID get categorized into the same
category. This indication will not change once an instance is scanned
for the first time unless things change in the infrastructure, servers
are added, the design or ACL is changed, or the calculation algorithm is
optimized (for instance with a new release of iDNA Applications).

Based on the identified types, the DBs are divided into two groups:
„**Focus Databases**" (consisting of Applications and Mail-in Dbs) and
„**Other Databases**" (consisting of the remaining database types).

The majority of detailed usage and design analysis is performed on Focus
DBs, but there is a variety of charts and reports with information about
the other types.

Additional information outside the scope of iDNA Applications regarding
these other DB types and infrastructure topics is available in panagenda
iDNA. Please [check our
website](https://www.panagenda.com/idna-applications/) or contact us for
additional information.

  

# User access days versus sessions

Each time a user accesses an application a session is set up. During the
day users can have multiple sessions, as sessions get closed, users log
out/login again or because they use multiple windows or clients. So, one
user accessing an application over the day can result in multiple
sessions. Sessions can also occur when servers and processes access
database instances.

A User Access Day is identified as a unique user accessing an
application on any given day within the analyzed period.

So, there could be 20 sessions for User A accessing application Z in a
period of 7 days but if that user only accessed the application on day 1
and 5 of that period with 14 sessions occurring on the first day and 6
on the fifth day the User Access Days number will still only be 2. And,
say if 100 unique users accessed 100 different applications on one day,
the “User Access Days” count for that day would be 10,000.

In several graphs (For example, the Usage → By Department/Location →
The top 25 Active Departments/Locations dashboard) this distinction is
used to eliminate the risk of skewed numbers and to allow you to make a
more balanced decision when it comes to usage numbers.

  

# Design Complexity, Design Complexity score, Design Similarities and Design Insights

**Design Complexity** is based on the magnitude of design elements and
the amount of source code in these elements. The calculation is refined
by several considerations like code language type, usage of
Reader/Author fields, custom XPages control, etc.

**Design Similarity** analysis identifies how much alike a database is
to all other analyzed databases. Databases with high similarity are
grouped into design clusters, which allows for quick identification of
replicas that might deviate from a common design. It also provides means
to identify 'template candidates' for databases that have no template
specified.

**Design Insights** are combinations of certain patterns occurring in
the source code. These combinations are called "Findings" and can be
anything from identifying platform dependencies when local DLLs are
referenced to understanding if a piece of code interacts with other
databases.

**Design Complexity score** is a categorization of seven levels from
"Insignificant" to "Exceptional" that indicate the impact redesigning or
migrating the application would have. The Design impact is calculated
from three main sources: Complexity, Insights and Similarity.

  

**Next Topic:**

[Data Collection and Time Constraints (Servers Being Polled\_ Period
Collected)](/kb/data-collection-and-time-constraints-servers-being-polled-period-collected/)

  

  
