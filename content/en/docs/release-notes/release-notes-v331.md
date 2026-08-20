---
title: "Release Notes v3.3.1"
weight: 92
date: 2026-03-05
source_confluence_id: 167313446
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is a mix of
improvements and maintenance tasks.

  

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

  

  

  

## **Improvements**

  

{{% callout type="info" %}}

  
As of version 3.3.0 collecting Profile documents will happen
automatically in systems where the license supports it. This
functionality was previously disabled by default and had to be enabled
manually. The reason for this change is that it's tied to the new
Content Age feature.

{{% /callout %}}

**Important:** Profile Document collection [can still be
disabled](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=119439707),
but doing so will also disable Content Age collection. 

  

**Retention Catalog:** Additional columns regarding Last Access, Edit
and Creation dates have been added to the grid

  

**Domlog Collection:** The X-Forwarded-For field has been added added to
raw data collection. Thereby allowing identification of originating IP
addresses in (reverse) proxy scenarios

  

**Code Search:** The "Source Code Preview by Code Hash ID" Metabase
dashboard now offers the ability to search the displayed code

  

**Findings in Templates:** Several improvements have been made in
identifying and outlining Code Findings in Domino Master Templates

  

  

## **Bug Fixes**

  

**Nightly Processing:** The SQL statement for Content Age nightly
processing could fail in a rare scenarios where an age calculation would
exceed integer limits

  

**Design Collection:** Resolved a mismatch between design analysis
status numbers and scan progress displayed in the title bar

  

  

  

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

  

  

  
