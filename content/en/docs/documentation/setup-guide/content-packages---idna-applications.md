---
title: "Content Packages - iDNA Applications"
weight: 51
date: 2021-05-04
source_confluence_id: 28578378
draft: false
---
iDNA Applications contains the following Content Packages:

- **Domino Server Basics**
- **Database Catalog**
- **Session Activity**
- **Domino Web Log**
- **Directory/NAB Content**

  
With the exception of Directory/NAB and Domino Web Log content, all of
them are configured as described in the following section. Directory/NAB
and Domino Web Log configurations are explained in separate sections.

## Configure Domino Server Basics/Database Catalog/Session Activity

![](/images/kb/28578378/28578379.png)   
To configure the Content Packages Domino Server Basics, Database
Catalog, and Session Activity you only have to choose your desired
servers from the list of *Available Servers*. To do so, please use drag
and drop or double click on the respective servers. When you are facing
a longer server list, you will also find a filter option in this
configuration form as well as buttons to *Add selected* or to *Add
all* servers. From the moment you click on the *Save & Close* button,
iDNA Applications will start to measure your desired servers according
to the Content Package you just configured.

  

## Configure Domino Web Log Content

To configure the Domino Web Log Content, you will need to choose the
desired servers from the list of *Available Servers*. Note that the list
of available servers will contain only those Domino servers that have
Domino Web Log enabled. 

Note: from the [Domino Server requirements
chapter](https://www.panagenda.com/kbase/display/IA/System+Requirements)
the following settings MUST be enabled on your Domino server
→  (names.nsf \> Server Document \> Internet Protocols... \> HTTP)

- **"Domlog.nsf" enabled**
- **"Access log format" set to "Extended Common"**
- Optional space-saving settings:  **MIME types "image/\*", "text/css"
  and "text/javascript" can be excluded**

For more information on configuring Domino Web Log please refer to HCL
documentation:

- ### [The Domino Web server log (DOMLOG.NSF)](https://help.hcltechsw.com/domino/12.0.0/admin/admn_thedominowebserverlogdomlognsf_c.html)

- ### [Domino Web server logging to text files](https://help.hcltechsw.com/domino/12.0.0/admin/admn_dominowebserverloggingtotextfiles_r.html)

  

Use drag and drop or double-click on the respective servers to add them
to the list:  When you have a longer server list that fills the existing
dialog box, you'll find a filter option in the configuration form as
well as buttons to *Add selected* or to *Add all* servers. As soon as
you click on the *Save & Close* button, iDNA Applications will start to
measure your desired servers according to the Content Package you just
configured.

![](/images/kb/28578378/45352920.png)

  

## Configure Directory/NAB Content

This content package collects all Person, Group and Mail-In documents
from selected Domino directories.  
Different from most other content packages, which collect information
from multiple to all servers, usually only one server per Notes Domain
is selected for this content package. Typical candidates are admin
servers, hubs or dedicated directory servers.   
There are two options when selecting which directories are collected:

1.  All address books listed in Directory Assistance (DA) of this
    server   
    This option is the default but may lead to undesired results if
    address books are part of DA which hold external persons. Only
    address books should be included that contain the company's own
    Notes users.  
      
    ![](/images/kb/28578378/28578380.png)  
      
2.  Comma-separated list of databases  
    Sometimes the better option is selecting address books manually via
    this option. Simply gathering "names.nsf" databases from desired
    Notes Domains will often provide everything that is needed.  
      
    ![](/images/kb/28578378/28578381.png)

  

  

  
