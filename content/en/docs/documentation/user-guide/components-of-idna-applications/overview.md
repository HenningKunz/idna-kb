---
title: "Overview"
weight: 71
date: 2019-11-19
source_confluence_id: 28574770
draft: false
---
The overview section of panagenda iDNA Applications gives you a quick
overview of your complete application environment and the status of data
collection.

  

**In this topic:**

## Start Page - Metabase View

On the start page, you get a first glance of the detected saving
potential in your application environment. It also a good starting point
to drill down further in one of the three major areas:

- **Sunsetting of applications**: Applications with no or very low usage
  across all of its database instances are strong candidates for
  sunsetting or consolidation
- **Reduction of project scope**: Extensive insight into the application
  environment helps you to find the correct focus areas and starting
  points for your projects.
- **Minimization of license cost**: Precise identification of
  inactive/outdated users or groups. 

  

## Status Dashboard

The status Dashboard gives you an overview of the usage and design
insights status:

- **\# DB Instances Discovered**: The rounded number of database
  instances (individual database replicas) discovered on the servers
  being polled.

  
{{% callout type="info" %}}

  **If not all servers in the environment are included in the collection
  this number might be skewed. For accurate information, it is important
  to include at least all servers that might hold applications or
  mail-in databases but preferably all servers for proper visualizations
  across the entire Domino environment**

  
{{% /callout %}}

- **Databases Used in Last 90 Days**: The percentage of database
  instances (out of the discovered instances) accessed by users in the
  last 90 days

- **\# Focus DBs Identified**: The number of database instances
  identified as either a type "Mail-In" database or type "Application".
  Other databases are: user, server & orphaned mailboxes, system
  databases and Directories.

- **%FocusDBsUsedinLast90Days**: The percentage of focus database
  instances (out of the discovered instances) accessed by users in the
  last 90 days

- **% Focus DB Instances Unlocked**: Percentage of database instances
  considered "Focus databases" that are covered for analysis by your
  license agreement

- **\# Focus DBs Designs Collected and Analyzed**: The number of Focus
  databases for which design analysis was successfully performed. If
  this number is lower than the number of Focus DBs identified this
  could indicate that not all databases could be analyzed.

- **% Focus DBs with Design Insights in Source Code**: Percentage of the
  database instances analyzed for which design Insights were found.
  Design insights consist of "Findings" of specific code elements or
  combinations of code elements, based on predetermined rulesets.

- **\#UsersRegistered**: Total number of users registered in the Domino
  environment (taken from your Directory infrastructure)

- **\# Users Active in Last 90 Days**: Number of users who have shown
  activity in the Domino environment over the last 90 days

  

**User Activity Last 90 Days**: Shows you the activity generated for
focus versus non-focus databases based on the "user access days". A user
access day is the equivalent of a user accessing the database on a given
day. By using days instead of sessions, it prevents sudden spikes of
activity skewing the data. This graph gives you insights into which
types of databases most of your users are working in (focus versus
non-focus databases) and how they are accessing the databases (web
versus client).

**Usage History**: Each column in this chart represents the total number
of database instances which were accessed in the particular time frame.
A database instance that was accessed in the last 7 days will thus also
show up in all other 'used' columns. This graph will of course get more
meaningful over time as it will start to highlight how many are still in
daily use and how many are silently falling into disuse. 

**Design Complexity**: Indicates how the focus databases (databases of
type Applications or Mail-In databases) are categorized in terms of
design complexity. Design complexity depends on many factors which will
be further explained in [Design Complexity](/kb/design-complexity/).

  

## Environment Overview

The Environment overview provides you with a single overview of how the
infrastructure of your Domino Environment is set up. 

It lists information about the number of:

- Directories
- Servers
- Servers analyzed (by panagenda iDNA Applications)
- Number of Domino Releases (utilized by the servers)
- Number of Operating Servers (utilized by the servers)
- Registered Users
- Active Users
- Groups
- Group members
- ACL entries
- Databases deployed (focus & non-focus databases)
- Database storage used
- Databases touched by active users
- Views
- Views indexed
- View storage

  

## Inventory

The Inventory page will give you a global overview over the total number
of database instances, and replica sets you have.

By comparing these numbers against usage information and disk space used
you get a better insight into the actual capacity utilized by your
Domino environment.

  

## Scope Focus Funnel - Metabase View

This page helps you to reduce the project scope by focusing on the right
applications. 

  

## Remediation Overview - Metabase View

Discover the application remediation potential in your Domino
environment.

Which applications are used very rarely or not at all, which ones are
good candidates for quick wins, and which ones are the business critical
ones that needs special handling in your project.

Explore further details in Metabase by clicking on the following
button:  
  
![](/images/kb/28574770/28574771.png)

  

{{% callout type="info" %}}

Please refer to the article about the iDNA Applications [default
Metabase users](/kb/metabase-default-users/) and the [Metabase
documentation](https://metabase.com/docs/latest/getting-started.html)
for further help.

{{% /callout %}}

  
  

**Next Topic**:

[Catalog](/kb/catalog/)
