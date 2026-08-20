---
title: "Release Notes v1.2.0"
weight: 109
date: 2020-02-24
source_confluence_id: 28577099
draft: false
---
  

panagenda is proud to announce this new release of iDNA Applications.
Whether you’re modernizing or migrating Notes/Domino, iDNA gives you the
knowledge to deliver the most difficult projects efficiently, on time
and on budget. This new version brings a lot of value with many new
features, improvements and bug fixes.

  

  

## **Highlights**

**  
**

### **Usage Pattern Similarity**

The goal of this new feature is to find small groups of databases that
have a large impact on the user population. For example, modernize a few
key databases and reach a lot of users with the improvements or
archive/migrate a few key databases and free up a lot of user licenses.

![](/images/kb/28577099/28577104.png)

  

### **Application Discrepancies**

This new dashboard compares five common KPIs between the database
instances of the same replica set in order to identify discrepancies
between the databases. The KPIs point out common replication issues by
analyzing data on document count, design age and template inheritance.

![](/images/kb/28577099/28577101.png)

  

### **LDAP Authentication**

A long requested feature by enterprise customers is LDAP integration.
You now have the ability to integrate with your directory infrastructure
and use enterprise credentials to log into iDNA Applications.

![](/images/kb/28577099/28577103.png)

  

  

## **New Features**

  

**Metabase:** it is now possible to create nested folders in the
navigation menu by creating sub-collections in Metabase  
  

**Notes Client Information:** if connected to a [MarvelClient
Analyze](https://www.panagenda.com/products/marvelclient/) database,
information on users and Notes clients can now be analyzed in DataMiner
and Metabase.  
  

**UI Languages:** Swedish has been added as user interface language.
Heja Sverige!  
  
**Design Re-scan Configuration:**

{{% callout type="info" %}}

The interval of design collection upon design change has been reset to
the new default and recommended setting "Weekly, on Saturday
(Recommended)"

{{% /callout %}}

The previous default configuration of "Next day" may cause a continuous
design re-scan of a large amount of databases if certain design refresh
settings in Domino are enabled. This continuous re-scan may have
negative impact on performance while creating little to no benefits.

Changing this setting in a compulsory way was a highly exceptional
action and not done lightly. Of course, it can be freely (re-)configured
using the page \[Settings\] → \[Database design re-scan options\].

  

  

## **Improvements**

**  
**

**Consolidation Potential:** the calculation for this category has been
updated and streamlined throughout iDNA. The new calculation works as
follows: no or very low usage in recorded history and no usage in the
last 90 days across all DB instances.  
  

**Data Collection:** several improvements were made around detecting
issues with data collection (e.g. expired Notes ID password) earlier. A
weekly warning email has been added and it's now easier to recover from
a collection outage.  
  

**Database Types:** the interface for database re-categorization has
received a number of improvements. It can be accessed via \[Settings\] →
\[Database Recategorization Rules\].  
  

**Metabase:** the application has been upgraded to version 0.34.1.
Please see the [release
notes](https://github.com/metabase/metabase/releases/tag/v0.34.1) for
more details.  
  

**Server Catalog:** this grid has undergone a re-design to help with
identifying collection issues. What used to be the "Details" column set
has been enhanced and is now the "Default" column set and vice versa.

  

  

## **Bug Fixes**

  

**DB Details:** a bug has been resolved that would lead to a wrong "last
modified" date to be displayed in Database Details  
  

**Domlog Collection:** an issue has been resolved where too much text in
the "user_agent" column could cause and issue when storing data to the
database  
  

**Duplicate DBs:** a bug has been fixed that could, in rare situations,
lead to databases being displayed twice in Catalog  
  

**Metabase:** a misconfiguration has been resolved that lead to the
default user accounts being unable to ask custom questions  
  

**Metabase:** several typos have been corrected in dashboards in the
Usage category  
  

**User Activity:** a bug has been fixed that lead to counting certain
users twice if user anonymization/pseudonymization was enabled  
  

**User Rename:** an issue has been fixed around handling user renames.
Upon rename, the new name will now be properly reflected in iDNA
Applications

  

  

## **Structural Changes / Upgrade Path**

  

### **Data Warehouse Rebuild Required**

{{% callout type="info" %}}

After installing the update, parts of the application may not be
available until the data warehouse is rebuilt. This process runs
automatically at night, but can be triggered manually after the update.
On the first login after the installation, more information on this
topic will be displayed, along with the option to trigger the rebuild.

{{% /callout %}}

  

### **Upgrade Procedure: Container Installer**

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](/kb/upgrading-idna-applications/).

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  
  
