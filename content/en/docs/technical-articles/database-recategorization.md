---
title: "Database Recategorization"
weight: 7
date: 2019-07-22
source_confluence_id: 28575235
draft: false
---
panagenda iDNA Applications uses a proven algorithm to categorize all
databases in the environment into the following categories (see
[Definitions](/kb/definitions/) for details):

1.  User Mail database (identified by a person document pointing to the
    instance)
2.  Mail-In database (identified by a non-system mail-in document)
3.  System database (identified via well-known system file or template
    names)
4.  mail.box database (identified from Domino server configuration
    settings)
5.  Directory (identified from Domino server configuration/used
    template)
6.  Orphaned User Mail (user mail files no longer associated with a
    person document)
7.  Application databases (all remaining not categorized into cat 1-6)

  

All further analysis in iDNA Applications is based on this
categorization.

There might be certain use cases in which, for example, a database was
categorized as System database, but it would be more appropriate to
treat it as Orphaned User Mail file in your environment. For such cases,
iDNA Applications provides the option to recategorize databases based on
custom rules. Starting from...

## 1) Configuration View: "Settings \> Database Recategorization Rules"

Follow these steps if you need to recategorize databases:

1.  Select **Database Recategorization Rules **from
    the **Settings **menu  
    ![](/images/kb/28575235/28575246.png)  
      
2.  Click on the **Create New Rule **button  
    ![](/images/kb/28575235/28575247.png)  
      
3.  Recategorization Rule Settings:  
    You have the option to apply rules for single or sets of databases
    based on filtering by Replica ID, Template, or File Path. The
    filtering string can either be entered as search expression or Regex
    (Regular Expression).**  
      
    **

**Rule Name**: Please name your rule in a meaningful way

**Filter field**: Select one of the following options from the Filter
drop down menu:

1.  - *Replica ID*
    - *Template (Inherits From)*
    - *File Path*

**Search expression**:  Enter a search expression or regex for your
filter  - the field recognizes Regex automatically.

**New DB type**: Please select a category (for details, please refer
to [Definitions](/kb/definitions/))

**Test Rule**: Clicking on this button will list you all databases that
match your rule.

**Save Rule**: Hit this button if "Test Rule" displayed the expected
results in order to save the rule. 

![](/images/kb/28575235/28575316.png)

  

{{% callout type="info" %}}

***Please note that if a database is matched by more than one rule, the
resulting recategorization will depend on the internal priorities of
database types, which is defined as follows (descending from highest to
lowest priority):***

{{% /callout %}}

1.  ***Directory***
2.  ***Mailbox***
3.  ***User Mail***
4.  ***Mailin DB***
5.  ***System DB***
6.  ***Orphaned User Mail***
7.  ***Application***

***Example: If you have a rule A that recategorizes a system database X
as "Orphaned User Mail" file and a rule B that recategorizes the same
system database X as "User Mail" file, ***iDNA Applications will
treat*** database X as "User Mail" file.***

  

## 2) "Catalog \> Databases" view

If you identify a database in the** **Catalog \> Databases view that is
not categorized according to your requirements, just **right click** on
the corresponding database and select "**Assign new DB type..." **\> 

- "**...based on Replica ID**"
- "**...based on Template**"
- "**...based on File Name**"

![](/images/kb/28575235/28575303.png)

{{% callout type="info" %}}

***Please note that some options might be grayed out if the
corresponding field is NOT available for the selected database. ***

{{% /callout %}}

  

You will be redirected directly to the configuration view (DB
Recategorization Rules) with all data pre-filled in the respective
fields. You only have to specify the **Name** of the rule before you can
save it.

  

If you want to modify the pre-filled fields, you will find all you need
to know in this section of the article:

  

  
