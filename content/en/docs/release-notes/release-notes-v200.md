---
title: "Release Notes v2.0.0"
weight: 108
date: 2020-07-14
source_confluence_id: 28578250
draft: false
---
  

panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new major version brings a ton
of value with many new features, improvements and bug fixes.

  

  

## **Highlights**

**  
**

### **Content Analysis **

With the analysis of database content, iDNA Applications now provides a
crucial new insight into the challenges that come with transforming an
application. Document metadata (e.g. date created, last modifier, form
name) is analyzed and reported on for a variety of use cases around
migrating and modernizing your applications.

Topics analyzed include:

- Attachments (amount, size, file types ...)
- Content age (creation and modification history)
- Content editors
- Document structure and used Forms
- Encryption and signature
- Reader and Author fields
- Special objects in Richtext

  

![](/images/kb/28578250/28578256.png)

  

The new Content Analysis feature also brings an update to the licensing
system. Content scans are licensed on a per database basis, so you can
pinpoint exactly for which databases you require this in-depth analysis.
See [this
article](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=28578161)
in our knowledge base for additional information on how to get your free
licenses.

  

  

### **Custom Application Properties **

A feature that many customers and partners have been asking for is the
ability to enrich the application catalog with your own information
inside iDNA Applications. The new version comes with a set of
pre-defined properties like e.g. "Complexity Estimation" or "Business
Owner", but the system is fully flexible and allows the creation of
custom properties depending on your specific needs. There are several
different types available for these fields to make user interaction as
smooth and comfortable as possible: selection boxes with pre-defined
value lists or a name picker based on your own user, group, department
and location names are two that will come especially handy.

  

![](/images/kb/28578250/28578710.png)

  

These new properties are available for database instances and replica
sets. Both can be configured individually for maximum flexibility. This
feature comes with a brand new API to access and edit these properties
from external sources. See [this knowledge base
article](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=28578201)
for more details on the API.

  

  

### **Instant Usage History**

We have added a new source of usage history by reading a DBs own
activity records (DB Properties \> Info \> Activity \> User Detail). The
data collected that way will seamlessly integrate with session data,
which will remain the main data source for usage related information.
The main benefit with this feature is that basic usage information
spanning weeks or months of history will be available a few days after
the setup of iDNA Applications.

  

![](/images/kb/28578250/28578260.png)  
  

This data source has several caveats though. Collection might not be
enabled for all databases. Only a few hours of history might be
available on very busy databases, while months of history is available
for others which are rarely used. Data quality in general is not on par
with session information from log.nsf, which is the main data source for
usage information.

To gather this data, a design re-scan has to be performed on each
database. This can be triggered manually on the "Design Analysis Status"
page which can be accessed via the "Settings" menu.

  

  

### **teamWorkr Integration **

In an exciting new collaboration between panagenda and our partner [Team
Technology](https://www.teamworkr.com/), iDNA Applications now comes
with the ability to deploy applications directly in teamWorkr. With
teamWorkr you are able to transform your existing, desktop-optimized,
sometimes old fashioned Notes applications within a few minutes into a
true mobile user experience. This highly automated web application
deployment offers an extremely powerful rapid development framework.
teamWorkr also gives you the ability to to transfer your proven business
logic and code base into the mobile world and display it with beautiful
user interface.

  

![](/images/kb/28578250/28578714.png)

  

To use this new feature, you need an installation of teamWorkr, which is
not included in iDNA Applications. See [this knowledge base
article](https://www.panagenda.com/kbase/display/IA/teamWorkr+Integration+in+iDNA+Applications)
for more details on how to get started.

  

  

## **New Features**

**  
**

**Agent List:** A new dashboard is available that displays details on
agents in a database.  
  

**Database ACL:** A new dashboard is available that displays details on
the access control list.  
  

**Database Encryption:** A new property in database instance details
will display the encryption state of the database.**  
  
**

**Database ODS:** A new property in database instance details will
display the ODS version of the database.  
  

**Database Types:** New ETL properties have been added that make it
possible to prevent the detection of user mail files and
orphans/archives. This can be especially useful in situations where
Notes is not the primary mail system anymore.  
  

**Language Support:** With French, an additional language has been added
to the user interface.  
  

**Server Decommissioning:** New ETL properties have been added that now
give control over how iDNA Applications handles DBs that are on server
with no recent activity.  
  

**  
**

  

  

## **Improvements**

  

**Design Similarity:** It is now possible to export a list of all
databases that belong to a certain cluster or sub-cluster directly from
the Similarity interface.  
  

**Design Similarity:** The database instance grid now contains columns
that show which similarity cluster and sub-cluster a database belongs
to.  
  

**ETL Actions:** The ETL action interface has been slightly re-designed
to avoid triggering unintentional actions.  
  

**Excluded Users:** A new functionality has been added in ETL actions
that allows triggering the deletion of user activity that belongs to
excluded users who were previously not excluded.  
  

**Metabase Upgrade:** Metabase has been updated to version v0.35.x  
  

**Org-Structure Reset:** A new functionality has been added on the “Org
Structure” page that allows resetting of user, department and location
connections.

  

  

## **Bug Fixes**

  

**Catalog Grids:** Database types will now be handled the same way in
both the database instance as well as the replica set grid.  
  

**Catalog Grids:** Databases without a title will now be displayed in a
similar fashion in both grids.  
  

**DB Type Filter:** A bug has been resolved that resulted in not showing
DBs of type “User Mailfile” and “Orphans/Archives” even after the “Show
only Focus DBs” filter was removed.  
  

**License Notification:** An issue has been resolved in a license expiry
email that would lead to displaying programming placeholders instead of
the values behind them.  
  

**Server Status:** A bug has been fixed where the “Data Processed \>
Max” column would show no data.  
  

**Server Status:** An issue has been resolved where the server status
would display OK if no data had ever been collected from a server.  
  

**Stability:** Additional measures have been taken to improve and scale
nightly data warehouse processing.  
  

**Stability:** An issue has been resolved where in rare situations the
nightly rebuild of Domino View information would cause a crash in
database backend.  
  

**Usage Similarity:** Fixed an issue where in specific situations the
mouse-over a bubble would show “undefined” instead of the Cluster ID.  
  

**XPages Code:** An issue has been resolved where Custom XPages Controls
would be displayed as XPages lines of code. Note: lines of code are not
available for XPages.

  

  

## **Structural Changes / Upgrade Path**

  

### **Data Warehouse Rebuild Required**

{{% callout type="info" %}}

After installing the update, parts of the application may not be
available until the data warehouse is rebuilt. This process runs
automatically at night, but can be triggered manually after the update.
On the first login after the installation, more information on this
topic will be displayed, along with the option to trigger the rebuild.

{{% /callout %}}

  

### **Content Analysis License - Connecting to panagenda.com **

{{% callout type="info" %}}

This new licensing method requires a previously extremely rare
connection to panagenda servers in order to verify the per-database
license. This connection **WILL NOT** originate on the appliance, but
rather be initiated from the users web browser during the first scan of
a database. No information except a customer identification and the
application's Replica ID will be transmitted.

{{% /callout %}}

Thus, an internet connection is required from the web browser that
initiates the first content scan of a database. If this should not be
possible in your environment, please contact <support@panagenda.com> for
an alternative solution with manual assistance.

**  
**

### **Upgrade Procedure: Container Installer**

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](https://www.panagenda.com/kbase/display/IA/Upgrading+iDNA+Applications).

  

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  
  
