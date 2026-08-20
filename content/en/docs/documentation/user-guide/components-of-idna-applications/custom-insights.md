---
title: "Custom Insights"
weight: 76
source_confluence_id: 28574818
draft: false
---
The Custom Insights section is visible only to those authorized for its
use and allows you to see how the provided Insights are build up as well
as provide options to create new, organization specific insights.

  

**In this topic:**

## Manage

The manage section contains an overview of all Rulesets, Insights and
Patterns that are available in your iDNA Applications environment. These
can be both system insights provided with the tool (identifiable by the
panagenda icon behind the name) as well as custom elements created by
your own organization. You can hide the panagenda items and focus in on
custom elements by simply clicking the icon behind the search field: 

![](/images/kb/28574818/28574819.png)   
  
*The view is divided into three tabs holding*:

**Tab Rulesets**: Design insights consist of a structure that groups
them into logical sets. So called rulesets. This tab shows all available
rulesets and whether or not they are enabled. Rulesets help identify the
sort of insights and give you ways to navigate the findings as rulesets
show up in the catalog column sets and on the Design Insights page. The
color indicator before each ruleset indicates if it is enabled or
disabled at that moment. Meaning that it is included in the design
analysis or not. By clicking on a ruleset you get to see the assigned
Insights and their severity levels (indicated by the colored bar in
front of it).

**Tab Insights**: Each ruleset contains one or more insights. This tab
lists all Insights and below them the rulesets these Insights are
associated with.  
An insight is a simple search key or a collection of blocks of patterns
to be matched. Each Insight can consist of one or many blocks. All
patterns inside one block have an 'OR' relationship to each other.
Meaning that if any of the patterns in that block is matched the result
of that block results in a TRUE value for the database that pattern was
found in. If an insight has multiple blocks the relationship between the
blocks of patterns is that of an 'AND' relation. Meaning that if all
blocks result in a TRUE value the insight returns a value of TRUE and
the database is listed as having that design insight.

**Tab Patterns**: This tab shows the patterns. Otherwise known as
advanced insights that make up a single insight element. Each individual
pattern can be linked to more than one Insight which are portrayed below
the pattern when clicked on. A pattern is a search string that is fired
on the collective set of database designs and returns any code elements
that match the search string. The format of a pattern can be in either
plain text or in the form of a regex expression\*.  
To understand how custom insights work and how to create new ones please
refer to [Building your own Custom
Insights ](/kb/building-your-own-custom-insights/)[ ](/kb/building-your-own-custom-insights/)on
building your own custom Insights.

  

## Code Search

The code Search tab allows you to quickly do ad-hoc searches across all
your analyzed database instance designs for specific code or to test
search queries you would like to use as Insight patterns. Searches can
be entered either as free text, whole word or regular expressions.

The results are shown below the search field whereby each unique code
element is shown separately. The number in front of each code element
indicates how often the code element is being used.

{{% callout type="info" %}}

**Note that a code element can be in a database multiple times.**

{{% /callout %}}

  

By clicking on the code element, the actual code becomes visible for
review. The search key findings are highlighted to make it easier to
identify the exact location. In the details panel on the right hand side
the top 25 databases are listed that contain this code element with
their location, the design element / field holding the code and the
number of elements in that database with this exact code. Additionally
export options are available in the top to export the full list of
database instances and locations to an EXCEL or CSV file. 

If you have the panagenda Application Launcher\*\* installed you can
also click the design element to open it directly in the Notes
Designer. 

  

For more details on Code Search, [watch the masterclass video from
panagenda CEO Florian
Vogler](http://kbase-prod-01.panagenda.local:8090/kbase/pages/viewpage.action?pageId=24120345) (this
was originally produced for panagenda ApplicationInsights but works
similar for iDNA Applications).

  

**Next Topic:**

[Custom Content](/kb/custom-content/)

  

------------------------------------------------------------------------

*\* A regular expression is a special text string for describing a
search pattern. More information about Regex can be found on the
internet*

*\*\* Information about the application launcher can be found
here: [https://www.panagenda.com/2017/10/open-in-
designer/](https://www.panagenda.com/2017/10/open-in-%20designer/)*

  
