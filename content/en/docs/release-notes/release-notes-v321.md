---
title: "Release Notes v3.2.1"
weight: 94
date: 2025-03-12
source_confluence_id: 119440333
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is a maintenance
release with a significant bug fix.

  

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

  

  

  

## **Bug Fixes**

  

**Code Analysis:** An issue was fixed that would lead to issues with
de-compiling Formula code. Formula code processing in general was not
impacted, but was limited to the relatively rare situations when Formula
code is exported in compiled format by the DXL exporter.

{{% callout type="info" %}}

This fix affects new design scans going forward, but previously
processed data will not be affected retroactively. Please note that data
does not need to be re-collected from servers if the design has not
changed since the previous collection, so this process should not create
load on the network or Domino Servers.

{{% /callout %}}

A re-scan of databases can be triggered manually by the menu item
\[Settings\] \> \[Design analysis status\]

  

  

  

## **Structural Changes / Upgrade Path**

  

### **Upgrade Procedure: Container Installer**

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](https://www.panagenda.com/kbase/display/IA/Upgrading+iDNA+Applications).

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  

  

  
