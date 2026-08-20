---
title: "Release Notes v3.0.0"
weight: 98
date: 2024-07-02
source_confluence_id: 119439536
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. 

This new version is a critical milestone release, as it requires
panangeda's new base operating system Alma Linux and packs a ton of
updates in underlying components along with lots of new features,
improvements and bug fixes.

  

{{% callout type="warning" %}}

Our previous operating system CentOS Linux 7 will reach end of life
(EOL) on June 30, 2024. Please see the [official announcement by Red
Hat](https://www.redhat.com/en/topics/linux/centos-linux-eol) for more
details.

{{% /callout %}}

panagenda provides new virtual images based on Alma Linux 9, a RHEL
based open source Linux distribution. We encourage all customers to
migrate their installations to the new virtual image.

{{% callout type="info" %}}

From version 3.0.0 onward, iDNA Applications upgrade packages will not
be backwards compatible with the previous CentOS-based appliance. Please
deploy a new v3 Alma Linux appliance to continue benefiting from iDNA's
latest and greatest features!

{{% /callout %}}

For a how-to on migrating your existing system and data please visit our
[iDNA Version 2 to Version 3 Migration
Guide](https://www.panagenda.com/kbase/x/uoAeBw).

  

  

## **New Features **

  

**Notes 64-bit Readiness and Nomad Web/Android/iOS Compatibility  
**

The new 64-bit Notes client brings a lot of new opportunities as well as
challenges with it. However, as discussed our [Webinar on Preparing for
the 64-bit Notes
Client](https://www.panagenda.com/webinars/developer-special-how-to-prepare-applications-for-notes-64-bit-clients/)
there is some work to be done in order to be ready for it. One of the
key areas to look at will be application code.

We see a similar story developing for the new platforms for Nomad on
Web, Android and iOS. They offer tremendous value for next level user
experience and portability, but with they also come with a number of
[LotusScript
Restrictions](https://help.hcltechsw.com/dom_designer/12.0.0/basic/LSAZ_NOMAD_PLATFORM_DIFFERENCES.html)
and [Compatibility
Limitations](https://help.hcltechsw.com/nomad/1.0/hcln_limitations.html)
to consider.

iDNA Applications supports you with a wide array of new Code Insights to
help you prepare for these new platforms. After all, ignoring these
topics may mean that your applications' functionality and associated
business processes might be at risk!

![](/images/kb/119439536/119439562.png)

  

**Code Search Results Exploration  
**

After performing a code search, a new button will now appear that allows
exploring the results in a Metabase dashboard. 

![](/images/kb/119439536/119439581.png)

  

This new Metabase dashboard was added to give a more summarized result
of a search that is easier to export and requires less interaction when
used, for example, to create a task list.

![](/images/kb/119439536/119439585.png)

  

**Insights Findings Exploration  
**

Similar to the previous new feature, this new Dashboard accessible from
iDNAs left-side navigation menu via "Design" → "Insights Findings by
Code Element in Database" gives a way to explore the results (or
Findings) of Insights. 

It displays the findings in a summarized, tabular structure that makes
it easy to filter and export a list of Findings by code element for
further processing.

![](/images/kb/119439536/119439588.png)

  

## **Improvements**

  
**Code Insights:** Insights were previously only re-calculated if at
least one database design was re-scanned since the last nightly
processing. This could create a delay for results of newly created
Insights appearing in the UI. Changes have been added so that Insights
are re-calculated if an Insight was added or modified, or a database has
been re-scanned.

  

**DLAU Integration:** Recent updates in DLAU have been incorporated.

  

**Usage Cluster Calculation:** The default parameters for the processing
of usage clusters have been changed due to a significant impact on the
duration of the nightly processing task in large environments. The
previous setting that essentially said "calculate for the entire
recorded history" has been changed to "calculate for the last 90 days".
This setting can be modified by setting the ETL parameter
"ai_usage_cluster_last_activity_max_days" (navigate to
https://\<your-idna-host\>/idna/sys/etl → ETL Properties).

  

## **Bug Fixes**

  

**Code/Design Collection:** A issue has been fixed that would lead to
compiled Formula code not being properly decoded during design
collection.

{{% callout type="info" %}}

Design will have to be re-collected for each database that contains
Formula code and may be affected by this issues.

{{% /callout %}}

Even though our observations internally and at customers point to this
being a comparatively rare occurrence, we recommend re-collecting the
entire application landscape to make sure no potentially relevant code
blocks are being ignored. A re-scan can be started by going to
"Settings" → "Design Analysis Status". There, the default filtered
results will include all relevant DBs and selecting "Start" will trigger
a re-scan. 

**  
Design Re-scan:** An issue has been resolved that would lead to an
internal error if more than 999 DBs were submitted for design re-scan in
"Settings" → "Design Analysis Status". There was no UI message
indicating an issue, even though the underlying action would fail.

  

**DLAU Collection:** Collection from the DLAU database may fail due to a
previous inconsistency in IFA's internal database structure. If you are
currently facing issue with collecting from the DLAU database, we
recommend removing the current content package configuration, saving the
settings and re-creating it afterwards in a second step.

  

**Insights Code Highlighting:** Minor inconsistencies with code
highlighting have been fixed and code highlighting overall has been
improved.

  

**Insights Processing:** An issue has been resolved that would lead to
custom insights processing failing in rare cases. Overall processing for
insights has been improved and it now allows for the creation of more
complex regular expression patterns.

  

**Person Document Data:** An inconsistency has been removed where
advanced details in person documents would not be available due to an
error in syncing nightly processed data with latest collected data.

  

## **Structural Changes / Upgrade Path**

  

### **Component Upgrades inside Containers**

Virtually all Docker images/containers have undergone significant
updates in outward facing components and underlying libraries. This
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

  

  

  
