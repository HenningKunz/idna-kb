---
title: "Configuration: Usage by Organizational Units"
weight: 52
date: 2020-06-19
source_confluence_id: 28578383
draft: false
---
By default, iDNA Applications automatically collects information about a
user's organizational unit. This information is gathered from the Field
"**Department**" in person documents in the Domino Directory. iDNA
Applications aggregates this data and shows the results in the
catalog:  
![](/images/kb/28578383/28578384.png)f

###  

## Specify a Different Field in Person Document

If you use another person document field for organizational information,
please configure iDNA Applications as follows:

- Open the
  file **/opt/panagenda/appdata/volumes/ai/idna/idna-config.properties** in
  the file system of the appliance in an editor  
    

- Add **domino.server.nab.userdocument.import.raw=true** to enable the
  collection of organizational info from your organizations custom
  field  
    

- Open the URL **https://***\<FQDN or* *IP\>***/idna/sys/etl  
    
  **

- Click on ***Show/Hide*** ***Properties  
  ***![](/images/kb/28578383/28578385.png)![](/images/kb/28578383/28578386.png)  
    

- **org_user_property_dep:** please enter the name of the field in the
  person document which holds the organizational information for that
  user  
    

- **org_import_property_delimiter:** please enter the character which
  separates the hierarchies in the case the organization files has
  hierarchical content (such as the "\\ in the following example
  "\department\team")  
    

- **org_import_property_parsebottomup:** id info is hierarchical default
  order is assumed as top down if the field holds the information bottom
  up like ( team\department\segment) please check this box

  
{{% callout type="info" %}}

  ***Important: After changing an entry you always have to click the
  corresponding update once to transfer the change into the
  configuration table.***

  
{{% /callout %}}

## Disabling the Collection of Organizational Information

If your Domino Directory's person documents do not hold valid
information in the department field, and there is no other field in the
person document holding that information, you can disable the collection
of organizational information. If disabled, the usage by department will
not be available.   
Please

- Open the URL **https://***\<FQDN or* *IP\>***/idna/sys/etl  
    
  **
- Click on ***Show/Hide*** ***Properties  
  ***![](/images/kb/28578383/28578385.png)  
    
- Check ai_department_disable_processing  
    
- After that you have to click the corresponding **update** link once to
  transfer the change into the configuration table

  
The changes and tweaks will be reflected in the iDNA Applications Portal
after the following ETL run at 6:30 PM.
