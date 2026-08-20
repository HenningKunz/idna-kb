---
title: "Release Notes v3.2.0"
weight: 95
date: 2025-01-10
source_confluence_id: 119440121
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

  

### **Revamped user access and role framework **

Several improvements were made in this area. The main improvements are
that we have introduced the new Editor role, offering more privileges
than the existing Viewer role but fewer than Administrator. All roles
are now verified through LDAP credentials (if configured) for accessing
iDNA application components. Please see the [LDAP Setup
Guide](https://www.panagenda.com/kbase/display/IA/LDAP+Settings) for
more details on how to configure LDAP authentication.

  

**New Role: Editor**  
The editor role has all the rights of the Viewer role and many
additional capabilities that were previously restricted to
Administrators (excluding system configuration options):

- - Create/Manage Source Code Insights
  - Edit custom properties for DB Instances and Replica Sets
  - Create/Manage DataMiner queries
  - Create/Manage Metabase dashboards and questions

  

**Revamped LDAP Access**  
The existing option to access the iDNA portal with LDAP credentials has
been improved and extended to the Admin Client and DataMiner. The
configuration dialog remains largely unaltered within the iDNA portal
under [\[Settings → LDAP
Settings\]](https://www.panagenda.com/kbase/display/IA/LDAP+Settings).

Metabase continues to use its own authentication system, which is
configured separately in the Metabase Admin portal.  
  

The one small change that was made to the config dialog was the addition
of the role mapping for the new Editor role.

![](/images/kb/119440121/119440120.png)

  

### **Major Metabase upgrade to new version**

Metabase has been upgraded to version 50.x in this release. The main
purpose was implementing bug fixes and security updates, but also an
updated look and feel as well as several usability improvements are also
available in this new version. See the [Metabase 50 Release
Notes](https://www.metabase.com/releases/metabase-50) for more
information.

![](/images/kb/119440121/119440126.png)

A significant change in version 50 is a revamp of Metabase's permission
system, which aligns with iDNA's own, as described above. For this
reason, the first time an iDNA version \>= 3.2.0 is installed, a reset
of Metabase permissions is performed automatically in the background.
This should not inconvenience the majority of iDNA customers. In rare
cases where custom permissions for non-panagenda dashboards or questions
are defined, these permissions have to be re-created using the new
Metabase access control interface.

  

### **Optional Addon: SNMP discoverability package**

In order to make iDNA Applications discoverable by applications like
Service Now, an optional package has been created that will install an
SNMP server on the appliance and publish a set of configurable
properties. Please see this [SNMP Setup and Config
Guide](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=119440133)
for additional information.

  

  

## **Bug Fixes**

  

**Metabase Access:** Users with Viewer access previously had issues with
accessing all dashboards. This was fixed as part of the above-mentioned
Metabase access structure changes.

  

  

## **Known Issues**

  

**Metabase LDAP Role Mapping:** Depending on the LDAP server's schema,
automatic role mapping may not function as expected. A simple workaround
is to manually assign users to the appropriate groups inside Metabase.
LDAP authentication in general is not affected.

  

  

## **Structural Changes / Upgrade Path**

  

### **Upgrade Procedure: Container Installer**

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](https://www.panagenda.com/kbase/display/IA/Upgrading+iDNA+Applications).

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  

  

  
