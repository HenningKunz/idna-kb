---
title: "Release Notes v3.3.0"
weight: 93
date: 2025-10-07
source_confluence_id: 119440899
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is a mix of new
features, improvements and maintenance tasks.

  

{{% callout type="warning" %}}

Our previous operating system CentOS Linux 7 has reached end of life
(EOL) on June 30, 2024. Please see the [official announcement by Red
Hat](https://www.redhat.com/en/topics/linux/centos-linux-eol) for more
details.

{{% /callout %}}

panagenda provides new virtual images based on Alma Linux 9, a RHEL
based open source Linux distribution. We encourage all customers to
migrate their installations to the new virtual image.

{{% callout type="info" %}}

From version 3.0.0 onward, iDNA Applications upgrade packages will not
be backward compatible with the previous CentOS-based appliances. Please
deploy a new v3 Alma Linux appliance to continue benefiting from iDNA's
latest and greatest features!

{{% /callout %}}

For a how-to on migrating your existing system and data please visit our
[iDNA Version 2 to Version 3 Migration
Guide](https://www.panagenda.com/kbase/x/uoAeBw).

  

  

  

## **New Features**

  

### **Retention Analysis**

  

Data retention analysis is a new feature in iDNA Applications version
3.3.0. It is the combination of collecting document age information from
databases and analyzing it based on data retention policies configured
for this database.

The obligation to retain data for varying periods of time is a legal
necessity in many industries and fields across the globe. Since
Notes/Domino applications have been an integral part in business
processes for companies of all industries over decades, this is a
critical topic for nearly any organization that aims to be compliant
with its legal requirements.

Please see this knowledge base article on [Content Age and Data
Retention
Analysis](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=119440769)
for more detailed information.

  

**Understand** which documents fall into the defined retention period
for a database:

![image2025-9-23_13-16-49.png](/images/kb/119440899/image2025-9-23_13-16-49.png?version=1&modificationDate=1758626209751&api=v2)

  

**Get insights** into when documents were last modified:

![image2025-9-23_13-10-42.png](/images/kb/119440899/image2025-9-23_13-10-42.png?version=1&modificationDate=1758625842106&api=v2)

  

Content Age analysis is licensed as a separate module and not included
in previous licenses. It can be purchased as an add-on to enhance your
current subscription and is compatible with all active and new licenses.

  

## **Improvements**

  

{{% callout type="info" %}}

  
Collecting Profile documents will now happen automatically in systems
where the license supports it. This functionality was previously
disabled by default and had to be enabled manually. The reason for this
change is that it's tied to the new Content Age feature.

{{% /callout %}}

**Important:** Profile Document collection [can still be
disabled](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=119439707),
but doing so will also disable Content Age collection. 

  

**Design Re-Scan Interface:** The UI component which displays the status
of previous design scans (System → Design Analysis Status) has been
overhauled with the introduction of Content Age scanning. It has been
improved substantially and will now display additional columns regarding
general DB Access, Profile Document scanning and Content Age scanning.  
  
![](/images/kb/119440899/119440910.png)

  

**Database Categorization:** We continuously improve how we recognize
system databases, templates and 3rd party tools. This version includes
an even larger refresh of this mechanism and will provide improved
database categorization.

  

  

## **Bug Fixes**

  

**Code Insights:** A missing indicator was added when scrolling through
code insights in Application Details. It is now clearly visible which
Insight is selected.

  

**Code Search:** A missing indicator was added when scrolling through
matches of source code full-text search. It is now clearly visible which
code block is selected.

  

**Localization:** Several typos were fixed throughout the solution.
Among them was an issue with filling in a placeholder in the Mail
Profile settings.

  

**Menu Navigation:** The dark navigation bar on the left side of the
main portal will now properly display a scroll bar when scaled to a
larger UI display size.

  

**Nightly Processing:** An issue was fixed in nightly processing where a
statement handling Name Variations could take a very long time and
potentially crash.

  

  

## **Structural Changes / Upgrade Path**

  

### **Component Upgrades inside Containers**

Virtually all Docker images/containers have undergone significant
updates in outward-facing components and underlying libraries. This
provides a significant improvement in performance, stability and
security.

  

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

  

  

  
