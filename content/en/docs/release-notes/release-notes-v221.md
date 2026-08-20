---
title: "Release Notes v2.2.1"
weight: 103
source_confluence_id: 55247806
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is a maintenance
release.

  

**IMPORTANT** Given the recent vulnerabilities created all over the IT
world and the subsequent library updates that were necessary to address
these issues, we would like to remind all our customers to apply a
foundation of security and safety measures when using our virtual
appliances.

A simple and short but important list of boxes to check:

- **Enable automatic Linux package updates (at least security fixes)**
- Change default password for Linux root user
- Change default password for Web config user
- Change default password for VNC Server connections

  

We provide our appliances with root access to make it easy to apply and
adhere to your company's security policies for e.g. password quality,
retention, etc. We strongly urge you to implement these guidelines. Not
only vulnerabilities that make the news can pose a significant security
threat.

  

  

  

## **Improvements**

  

**Metabase / log4j:** The Metabase component has been upgraded to
version 0.41.6, which includes log4j version 2.17.1.

  

  

## **Bug Fixes**

  

**Data Processing:** An issue has been fixed where canonicalized user
names would show up as separate entries and thereby duplicating users in
certain views.

  

  

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

  

  

  

  

  

  
