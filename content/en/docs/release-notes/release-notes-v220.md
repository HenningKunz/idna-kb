---
title: "Release Notes v2.2.0"
weight: 104
date: 2021-12-22
source_confluence_id: 55247667
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is mainly a
maintenance release, but brings a lot of value with new features,
improvements and bug fixes.

  

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

  

  

## **Highlights**

  

### **Mail Reporting**

An extensive set of reports around the topic of mail routing is now
available in Metabase. A Beta version of these reports has been
introduced in a previous version, but with v2.2, the functionality goes
Gold. iDNA Applications is now able to collect and process Mail Routing
Event data from Domino's log.nsf.

![](/images/kb/55247667/55247669.png)

Topics included are:

- Mail traffic history

- Inbound/Outbound mail statistics

- Mail recipient/size distributions

- Traffic by business hours

- Volume between departments

- Traffic per external mail domain

  

This set of features is not included in iDNA Applications standard
license. Please contact <sales@panagenda.com> for details on how to get
started with mail reporting in your environment.

  

  

## **New Features **

  

**Group Analytics:** Groups and group members are now available in the
cqx_data schema.

  

  

## **Bug Fixes**

  

**Update UI:** An issue has been fixed where localization for the "A new
version is available" dialog would in certain cases fail to load texts
properly.  

  

  

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

  

  

  

  

  

  
