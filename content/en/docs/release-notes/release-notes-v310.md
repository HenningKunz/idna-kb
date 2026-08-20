---
title: "Release Notes v3.1.0"
weight: 97
date: 2024-09-03
source_confluence_id: 119439712
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. 

This new version is a feature update for the critical milestone release
3.0.0. It requires panangeda's new base operating system Alma Linux.

  

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

  

  

## **New Features **

  

### **Explore Insights Findings and Code Blocks **

New code Insights and analyzing their findings is a big focus in iDNA
v3.0.0. With the new features in this version, we aim to make that even
better by introducing overall performance improvements and several new
dashboards to work with the results.

  

- **Dashboard: Insights Findings by Code Element in Database  
  **This dashboard has drastically improved performance and
  functionality**.** Not only does it now indicate if the database is
  similar to a standard template, it also allows drilling down into
  details and occurrences of a code block.  
    
  ![](/images/kb/119439712/119439719.png)  
    
    
- **Dashboard: Insights Findings by Unique Code Block**  
  This new dashboard is essentially a list of code blocks ranked by
  their impact on the environment with regards to terms of Insights
  Findings. Imagine you are preparing for the Notes 64-bit client
  migration. This dashboard makes it very easy to compile a list of code
  blocks that needs to be investigated and possibly re-developed.  
    
  ![](/images/kb/119439712/119439720.png)

  

### **Collecting and Analyzing Profile Documents **

Several have been made in this version regarding the collection and
analysis of Profile Documents (PD). Please note that PD collection still
needs to be enabled manually. See this [knowledge base article on
setting up and configuring profile document
collection](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=119439707).
PD collection was previously tied to design collection. With this new
version, the two have been somewhat separated, so profile documents can
now be updated periodically independent on design. See configuration
options regarding this in the above-linked article as well.

  

- - **Dashboard: Catalog\Profile Documents  
    **This new dashboard provides the ability to search through PD
    content across servers and databases.  
    **  
    ![](/images/kb/119439712/119439728.png)  
    **

  

## **Improvements**

  

**LDAP Login across all UI components:** All UI components (user portal,
config interface, DataMiner and Metabase) can now be configured to work
with LDAP credentials. Previously, the config interface and DataMiner
could not be accessed via configured LDAP credentials.**  
**

  

**Metabase Links:** Many links embedded Metabase dashboards are now
clickable without first opening the dashboard in Metabase. As many
dashboards get more and more interactive, we are aiming to improve the
experience with drill-down capabilities. However, with certain
specialized dashboards, you need to open them directly to access the
full drill-down and drill-through capabilities, as some features are not
available in embedded Metabase dashboards.

  

  

## **Bug Fixes**

  

**Dashboard Display:** A bug has been fixed that would lead to issues
with displaying embedded Metabase dashboards resulting in the message
"Unauthenticated / Not Found".

  

**DWH Configuration:** A bug prevented the PostgreSQL auto-tuning
feature from working properly and the RDB would always use un-tuned
default configuration parameters. Now that this has been fixed, the
Postgres container will automatically adapt tuning parameters according
to available memory.

  

**Weblog File Collection:** An issue has been resolved that would lead
to problems when collecting web logs from files. This issue did not
affect collection from domlog.nsf via Notes channels.

  

  

  

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

  

  

  
