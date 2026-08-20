---
title: "Structure & definition"
weight: 84
source_confluence_id: 28574829
draft: false
---
**Ruleset**: Design insights consist of a structure that groups them
into logical sets. So called rulesets. Rulesets help identify the sort
of insights and give you ways to navigate the findings as rulesets show
up in the catalog column sets and on the Design Insights page.

**Insight**: Each ruleset contains one or more insights. Each Insight
can consist of either a single search pattern or one or many blocks of
advanced patterns. All patterns inside one block have an 'OR'
relationship to each other. Meaning that if any of the patterns in that
block is matched the result of that block results in a TRUE value for
the database that pattern was found in. If an insight has multiple
blocks the relationship between the blocks of patterns is that of an
'AND' relation. Meaning that if all blocks result in a TRUE value the
insight returns a value of TRUE and the database is listed as having
that design insight.

**Pattern**: A pattern is a search string that is fired on the
collective set of database designs and returns any code elements that
match the search string. The format of a pattern can be in either plain
text or in the form of a regex expression\*.

  

{{% callout type="info" %}}

**Keep in mind that newly added patterns, insights and rulesets will not
be evaluated until the next evening run which typically starts at 18:30
(depending on your iDNA Applications server's locale). Please allow for
at least one night for results to show up.**

{{% /callout %}}

  

**In this topic:**  

  

## Creating a Pattern

To create a design pattern, you first need to have the search string or
regular expression you want to test for. You can use the Code Search to
build and test a pattern and check whether it returns the results you
would expect. 

{{% callout type="info" %}}

Watch our [Code Insights Masterclass
(Video)](http://kbase-prod-01.panagenda.local:8090/kbase/pages/viewpage.action?pageId=24120345)
video to learn many details about Code Search.

{{% /callout %}}

  

After knowing what pattern to search for open the Custom Insights –
Manage view and switch to the "Patterns" tab in the left column. All
patterns are listed here.

To create a new one:

- Enter a name for your new pattern in the top search field and make
  sure the name isn't already in use (to prevent confusion). Use
  descriptive names as it will make it easier to identify it later in
  the process.
- Below the search value where you've entered the name a button will
  appear called "+ CLICK TO CREATE PATTERN". Click this to create the
  new pattern. The new pattern is created and added to the list.
- Enter details in the meta data fields for the pattern like an authors
  name, tags and a description to make it clear what the pattern is
  about.
- Enter the search pattern in the Pattern field. You can use the "Test"
  button behind this field to see quickly what would be returned but
  keep in mind that this test option is more limited than the Code
  Search view which will also give you information about the databases
  in which the results are found and links to those database design
  elements.
- Use the 'save changes' button to save your new pattern.

  

  
Instead of creating a new one you can also duplicate an existing pattern
by using the duplicate option behind the existing patterns name. This
will create a copy that you can then edit to extend or change.  
![](/images/kb/28574829/28574831.png)  
  
The new pattern will show in the list of patterns as unassigned (broken
link icon) until it is assigned to an Insight.

  

## Creating an Insight

To create a new insight, switch to the Insights tab on the left side of
the Manage page and follow the following steps:

- Enter the name of the new insight (again, use descriptive names for
  easy identification later) and make sure the name isn't already in
  use. When satisfied the name is unique press the "+ CLICK TO CREATE
  INSIGHT" button to have the new insight created.
- The insight is listed in the view and the details page is open. Use
  the "add meta data" option behind the name to add additional info
- Assign a severity to the insight. This will determine how it is
  weighted as well as which color is used to indicate its severity.
- At this moment, the insight has no assigned patterns yet. You can
  either enter a simple pattern directly in the Insight itself or click
  the "Advanced Insights" button to select one or more existing
  patterns, allowing you to reuse them.
- To assign an existing pattern simply drag it from the right hand side
  into the Assigned Pattern box that appears when you click the
  "Advanced Insights" button.
- Optionally add additional patterns into either the same block (all
  patterns in one block are evaluated as having an OR relation, meaning
  that if any pattern in that block returns TRUE the whole block is
  considered a TRUE - **a**) or into a new block (all blocks in an
  insight are evaluated as having an AND relation, meaning that each
  individual block would need to evaluate to a TRUE for the insight to
  return a TRUE - **b**).  
  ![](/images/kb/28574829/28574832.png)

  

  
Alternatively, you can also copy an insight by clicking the copy option
behind the name. This will create a copy of the insight and copies of
all the patterns in it. After copying you can then alter the new insight
to add or remove patterns and change the name.

{{% callout type="info" %}}

**As this copy action will also create new copies of all patterns
included in the copied insight it is wise to really think through what
is needed. Creating loads of copies of existing patterns might be
confusing to manage and it might be better to create a new insight and
reuse the existing patterns in combination with your new ones.**

{{% /callout %}}

  

Adding system patterns (marked by the panagenda icon) into a custom
insight will always result in copies of those system insights being
made. It is not possible to add a system pattern directly to a custom
insight.

  

## Creating a Ruleset

To create a new ruleset go to the ruleset tab

- Enter the name for the ruleset to be created. Verify the name isn't
  already in use and press the "+ CLICK TO CREATE RULESET" button.
- Update the name and meta data fields if required
- Select the insights that you want to include in the ruleset
- Enable the ruleset by clicking the red 'Disabled' button in front of
  the name (it will turn green when enabled)  
    
  ![](/images/kb/28574829/28574834.png)

  

  

**Next Topic**:

[Reusing existing and panagenda rulesets, insights &
patterns](/kb/reusing-existing-and-panagenda-rulesets-insights-patterns/)

  

------------------------------------------------------------------------

*\* A regular expression is a special text string for describing a
search pattern. More information about Regex can be found on the
internet*

  

  
