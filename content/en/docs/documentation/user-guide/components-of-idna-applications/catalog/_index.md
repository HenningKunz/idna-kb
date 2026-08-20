---
title: "Catalog"
weight: 72
date: 2019-11-19
source_confluence_id: 28574773
draft: false
---
The Catalog section of panagenda iDNA Applications is where you can get
deep dive information about a specific database instances and servers.
Both in terms of usage as well as design.

  

**In this topic:**

  

## Working with the Catalog

{{% callout type="info" %}}

Please note that this description only applies for the views that are
NOT based on Metabase.

{{% /callout %}}

Refer to the article about the iDNA Applications [default Metabase
users](/kb/metabase-default-users/) and the [Metabase
documentation](https://metabase.com/docs/latest/getting-started.html)
for further help.

**  
**

**Instances Listed**

The Databases view lists all instances your license entitles you to
access for analysis. As this list displays instances, it is possible
that you see several instances of the same replica set (for further
details, please see [Definitions](/kb/definitions/)). 

![](/images/kb/28574773/28574790.png)

  

**Search**

Use the search field to find certain database instances or servers:

![](/images/kb/28574773/28574796.png)

  
**Sorting & Filtering**

To find a specific instance or server you can also sort the list on
various elements. For example, on the name of the database, the server
the instance is located on, or even on a type or complexity score if you
are interested in finding databases of a specific type or complexity. To
sort simply click on the column header. 

Alternatively, you can also filter the list on any of the columns by
clicking "Burger" icon that appears when hovering the mouse over a
column an then clicking on the filter icon:

![](/images/kb/28574773/28574792.png)

In the filter text field you can enter the search term or value you want
to filter on.

To clear a set filter click on the number icon that appears on the top
when filters are active:

![](/images/kb/28574773/28574793.png)

{{% callout type="info" %}}

**Keep in mind that if you switch between column sets after filtering
the filtering is maintained!**

{{% /callout %}}

  

**Filter by Insights**

When clicking on the "FILTER" button an additional option becomes
available to filter databases by Insight:

![](/images/kb/28574773/28574794.png)

This allows you to make selections based on what type of designs you
want to review or to easily export a list of databases containing a
certain type of finding.  
To clear the filter by insight filter simply click on the number icon
that appears on the top when filters are active.

  

**Exporting Data**

To export the filtered data set as either a CSV or EXCEL file just click
on the corresponding button:

![](/images/kb/28574773/28574795.png)

All columns for the filtered databases will be exported.

  

**Column Controls**

Clicking on the icon left to the Default Columnset selection field
allows you to customize the displayed columns:

<u>![](/images/kb/28574773/28574797.png)</u>

  

The Catalog views also provide several predefined Default Columnsets
which can be selected in the corresponding field. 

To fit the columns to the respective character length, click on the
arrow button to the right of the selection field.

  

## Databases

The Database view of the Catalog lists all instances your license
entitles you to access for analysis. Use the options described
under [Working with the Catalog ](#Catalog-WorkingwiththeCatalog)above
to get the deep dive information you need.

  

**Database Instance Details**

To open the details of any instance simply click on the table row for
the instance you are interested in. Please refer to [Instance
Details](/kb/instance-details/) for more information about this
component.

  

## Replica Sets

In this view you will see a list of** **applications / replica sets with
a number of key columns regarding usage, complexity and remediation
classification.

  

## Servers

In this view details to all analyzed servers are displayed. Use the
options described under [Working with the
Catalog ](#Catalog-WorkingwiththeCatalog)above to get the deep dive
information you need.

  

## Discrepancies

This view shows discrepancies, which signify a difference in certain
properties among database instances of the same replica set. Depending
on the type of discrepancy this may be anything from intended to
critical.

## Consolidation Potential - Metabase View

The Metabase based Consolidation Potential view shows you Replica Sets
with no or very low usage in recorded history and no usage in the last
90 days across all of its database instances.

  

  

**Next Topic**:

[Instance Details](/kb/instance-details/)

## In this section

{{< cards >}}
  {{< card link="instance-details" title="Instance Details" icon="document" >}}
{{< /cards >}}
