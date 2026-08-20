---
title: "Data Collection and Time Constraints (Servers Being Polled_ Period Collected)"
weight: 65
source_confluence_id: 28574747
draft: false
---
iDNA Applications collects data continuously from the environment and
stores it in the virtual appliance's data warehouse. This ensures that
the data collected stays available even after server logs have been
cleaned up and allows handling and analysis of much larger amounts of
data than what would be possible on the Domino platform.

Right after the initial setup of iDNA Applications, data collection
begins and user activity data is collected from that time on. The
virtual appliance goes through three steps until the first data is
available four days after the initial setup: Usage Collection, Design
Complexity analysis and Design Insights analysis. Once at least a part
of the Focus DBs have gone through all stages, the iDNA Applications
interface becomes available. Until then, a status overview screen will
provide information about the current collection stage of the appliance.

In the iDNA Applications web interface, a small progress and status
indicator on the top right of the content area provides information
about the current status.  
To avoid spiky load on collected servers, the iDNA Applications
appliance spreads out collection over the day. Usage data has to be
collected on a continuous basis though, so constant activity of the
Notes ID used by iDNA Applications is to be expected.

  

# Why don't I see all info?/Why is part of the graph greyed out?

Much of what is displayed in iDNA Applications' reports and charts is
determined by the installed license key.

Certain graphs and reports will show data for all database instances
regardless of the license key, but certain details might be omitted.
Other elements will not show unlicensed content at all.

  

# Status is telling me Analysis failed on several databases. What do I do?

When analysis fails on a database, multiple causes can be the reason.
Most common reasons are:

1.  The iDNA Applications appliance cannot reach the server where the
    database resides (network issues)
2.  The ID used in iDNA Applications does not have enough access rights
    to access the server where the database resides
3.  The ID used in iDNA Applications does not have enough access rights
    to access the database
4.  The database has hidden design (often with third party tools)

  
Verify and correct if possible the above and then rerun the failed
databases as follows:

- Click in the right upper corner on the "Status" indicator or click the
  little cog wheel icon in the right upper corner and select "Design
  analysis Status". 

  

In this view all analyzed databases will be listed with their analysis
status (column: Design Collection). Click on the "Design Collection"
column to sort it and see all that have failed.

- Check the failed databases for accessibility as described above

<!-- -->

- Use the option in the top of the view called "Rescan All failed
  databases" (select from drop down) to perform a rescan of the failed
  databases, all databases or filter the view down to one or more
  specific databases and choose "filtered results" to run it on a subset
  only.

  

{{% callout type="info" %}}

**Rescanning databases is a multistep process, that will take up to 2
days before the newly rescanned databases will appear in the interface.
Do not rescan all databases unless absolutely necessary as it may run
over several days and put significant strain on the appliance and
infrastructure.**

{{% /callout %}}

  

**Next Topic:**

[Getting Started with iDNA
Applications](/kb/getting-started-with-idna-applications/)

Use the option in the top of the view called "Rescan All failed
databases" (select from drop down) to perform a rescan of the failed
databases, all databases or filter the view down to one or more specific
databases and choose "filtered results" to run it on a subset only.” 
