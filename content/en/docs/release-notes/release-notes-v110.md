---
title: "Release Notes v1.1.0"
weight: 110
date: 2019-08-07
source_confluence_id: 28575348
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

### **Department & Location Activity**

These new dashboards make it easier than ever to find out about
department and location activity. See which applications they accessed
when and how many users were active.  
  

![](/images/kb/28575348/28575352.png)  
*Department Activity Dashboard*

*  
*

### **Identifying Application Owners **

Similar to looking up activity by department, we have also added the
capability to drill down into activity by user and replica set:

- Enter a part of a username to search for matching users to see their
  activity history and which apps they accessed.
- Enter a part of a database title or Replica ID to see which users and
  departments/locations are active

**  
![](/images/kb/28575348/28575354.png)  
***Activity Lookup by Replica Set*

  
This feature is especially useful when trying to identify application
owners or responsible cost centers.

  

### **Replica Set Catalog **

Where previously a detailed catalog view only existed for database
instances, a fully featured grid is now available for replica sets as
well.  
  
![](/images/kb/28575348/28575351.png)  
*Replica Set Catalog*  
  
This new list contains over 150 columns around:

- Usage
- Design
- Source code
- Replication consistency
- Similarity
- ...

  

  

## **New Features **

  

### **Controlling what is considered a Focus DB**

After some much appreciated feedback from customers and partners, we
have added this new feature which gives control over database type
categorization. The main use case here is being able to determine what
is counted as Focus DBs and what is not. This was previously done
automatically and could not be changed.

See this [knowledge base article on the
topic](/kb/database-recategorization/) for more detailed information.

  

### **More granularity in Domlog collection configuration **

Web logs have always been a heavy hitter when it comes to disk usage.
With this new feature we allow some granularity around what is being
collected from Domlog and how many details are actually stored in our
data warehouse.  
  

{{% callout type="info" %}}

  
From this version going forward, iDNA Applications will use new default
configuration settings for Domlog collection. The new settings will
reduce disk usage caused by Domlog by over 50% in most customer
environments. As a trade-off some limitations now apply:

{{% /callout %}}

- Cookie and Referer information will not be available anymore in raw
  data. Since it was not used for data processing previously, no
  negative impact should be noticeable.
- Web log lines in the 3xx range (redirects) are not stored anymore in
  raw data. This should not have an impact on the main data points (e.g.
  number of sessions or bytes up/down), but will be visible in secondary
  data points (e.g. count of requests).

The old default settings can be restored using the settings described in
the [knowledge base article on the
topic](/kb/extend-domlog-data-collection/).

  

  

## **Improvements**

  

**Data Export:** Titles in CSV and Excel exports are now "flattened" if
they are displayed in multiple levels in the originating grid. This will
make it considerably easier and more comfortable to work with Excel
exports.  
  

**Database Catalog:** The default on-click behavior has changed. Where
it previously opened the database details it now selects the clicked row
and column. Opening database details is now achieved via clicking the
title. The database details will then be opened in a separate browser
tab.  
  

**Grid Interaction:** Usability of grids throughout the solutions has
been improved. It is now easier to select multiple lines to export or
copy content to the clipboard.  
  

**System Template Detection:** The flexibility of system template
detection rules has been extended to include more variants of standard
template names that would have previously counted as applications.  
  

**Usage Dashboard Performance:** Several data queries behind usage
dashboards have been materialized to significantly improve performance
in larger environments.  
  

**Usage KPIs:** A new dashboard "Usage Category KPIs" has been added
that gives insight on why applications are assigned their usage
categories and provides additional KPIs on the apps in these
categories.  
  

**Usage Overview Dashboard:** Drill-downs have been improved by adding
certain key fields to foundation level data rows that allow easier
identification of database instances and replica sets without the need
for additional joins.

  

  

## **Bug Fixes**

**  
**

**Content Search:** Content search would sometimes fail to display
matching content due to a timing issue in communication.  
  
**Data Purging:** The data purging algorithm has been improved.
Previously, purging DWH data could lead to very long processing times in
the following nightly DWH processing.  
  
**Database Inventory:** The usage by database type table will now
consistently display "0" values instead of a mix of "0" and "-".  
  
**Department Detection:** An issue was resolved that would lead to
inconsistent results if department/location source field configuration
was changed after data had already been collected.  
  
**Language Change:** An issue has been resolved that would lead to an
error if the UI language was changed multiple times in rapid
intervals.  
  

**Log Download:** The process of downloading log files has been
simplified and an issue with certain older browses has been fixed.  
  

**Pseudonymization:** In rare situations, department and location names
could be re-engineered even though they were obfuscated.  
  

**Session Timeouts:** Timeouts for the reverse proxy have been
increased, to allow for long running queries in DataMiner.  
  

**Similarity Clusters:** The UI will now properly display and calculate
if a custom similarity threshold is configured.  
  

**Usage Overview Dashboard:** An issue was fixed where the app history
chart would show the first N weeks instead of the last.  
  
**User Name Format:** Notes user names are now consistently
un-canonicalized before being displayed in dashboards.

  

  

## **Structural Changes / Upgrade Path**

  

### Data Warehouse Rebuild Required

{{% callout type="info" %}}

After installing the update, parts of the application may not be
available until the data warehouse is rebuilt. This process runs
automatically at night, but can be triggered manually after the update.
On the first login after the installation, more information on this
topic will be displayed, along with the option to trigger the rebuild.

{{% /callout %}}

  

### Upgrade Procedure: Container Installer

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](/kb/upgrading-idna-applications/).

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  
