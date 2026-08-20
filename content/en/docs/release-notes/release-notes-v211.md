---
title: "Release Notes v2.1.1"
weight: 106
date: 2021-09-30
source_confluence_id: 55246964
draft: false
---
panagenda is proud to announce a new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is mainly a
maintenance release containing several important bug fixes.

  

  

## **Improvements & Bug Fixes**

  

**Data Collection:** A bug has been fixed that could lead to an issue
while collecting Person Documents from the Domino Directory.  
**  
**

**Data Export:** A date formatting issue has been fixed with data
exports from Catalog grids. Exported dates are now properly sortable
again.  
  

**Mail Reports:** Date filtering logic was harmonized across all
dashboards.  
  

**Mail Reports:** A calculation issue was fixed in the Mail Recipient
Distribution dashboard.  
  

**Metabase:** Metabase has been upgraded to the latest and greatest
version.  
  

**Metabase:** Help text regarding filtering options has been improved in
several dashboards.  
  

**Metabase:** An issue has been resolved with logging. Logs are now
available again in "/opt/panagenda/logs/metabase/".  
  

**Nightly Data Processing:** An issue during the processing of the name
variations has been fixed.

  

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
Applications](https://www.panagenda.com/kbase/display/IA/Upgrading+iDNA+Applications).

  

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  

  
