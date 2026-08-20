---
title: "Troubleshooting Design Collection Issues"
weight: 25
date: 2021-03-19
source_confluence_id: 28576224
draft: false
---
  

  

## Overview

iDNA Applications collects design data in order to surface insights and
complexity about the various applications in your environment. To
determine if there are issues with design collections either

- Click on the area below **STATUS** area in the top menu bar  
  ![](/images/kb/28576224/28576262.png)
- Or select it from the menu **Settings \> Design analysis status**.

  

Here you will see a list with basic information about database instances
and their design collection scan results. Scan results (column "Design
Collection → Status") should be OK for most, but where it is not OK (or
status "FAILED"), additional information can be found in the column
"Design Collection → Message".

![](/images/kb/28576224/45351908.png)

  

The three most common issues are:

- Security access issues (server access, database access, database
  access level)
- Network access issues
- DXL Exporter issues

  

## Troubleshooting Access and Network Issues

Security and network issues should be relatively easy to solve, because
they are in direct control of the personnel who administers the Domino
servers and the network. After troubleshooting, the databases need to be
re-scanned manually using the re-scan options on the same page.

### Network Access Issues

To scan the application design, the Notes ID with which iDNA runs needs
access to the server the database resides on. The Domino server must be
accessible over the network from the appliance. In an optimal scenario,
the server's common name can be pinged from a console in the appliance
to avoid name resolution issues.

Common problems are:

- *"Unable to find path to server" / Error 2051*

- *"Server not responding" / Error 2055*

- *"You are not authorized to use the server" / Error 2350 or 18734*

- *"Remote system no longer responding" / Error 2562*

- *"Network operation did not complete in a reasonable amount of time" /
  Error 2567*

- *"The remote server is not a known TCP/IP host" / Error 7267*

- *"The connection has been reset by the remote TCP host" / Error 7285*

- *"The connection has timed out" / Error 7286*

- *"The server is not responding" / Error 18439*

  

The solution for these issues is to make sure the iDNA has a stable
network connection to the server and name resolution works flawlessly.
However, sometimes network hick-ups occur, so in many cases a simple
re-scan of databases with these errors might solve the issue.

Sometimes, what seems like network errors can in reality be access
issues. An example here is the well known behavior of the Notes Client
saying "Server not responding", when in reality a server access issue
exists (see next paragraph).

  

### Security Access Issues

To scan the application design, the Notes ID with which iDNA runs needs
access to the server and the database in question. In the DBs ACL it
should at least have Designer rights.

Common problems are:

- "*Insufficient access level \[EDITOR/READER/AUTHOR\]*": the Notes ID
  can access the DB, but does not have required Designer rights in ACL

- *"Insufficient permission access resource" / Error 4060*: the Notes ID
  can access the server, but cannot access the DB at all

- *"Unable to access server" / Error 4271*: the Notes ID does not have
  access to the server

- *"You are not authorized to perform that operation" / Error 4067*:
  general access error. The Notes ID has insufficient access.

  

The solution for both issues is to modify server security settings or
the database ACL and add the Notes ID with Designer rights.
Alternatively, if that is not possible, the Notes ID will utilize Full
Access Administrator if available.

  

  

## Troubleshooting DXL Exporter Issues

Sometimes, failures are caused by the DXL Exporter task that runs on the
IBM/HCL Domino Server. iDNA depends on this separate task to gather
design information from databases. It is not uncommon for the DXL
Exporter to have problems with what it considers corrupt data in design
elements.

### Clean Abort

Normally that results in a clean abort of the scan on Domino side with
an Error message like this:

``` text
Execution failed;
    at [ResourceIdentifier[server=NamedReference[name=server/acme], 
    database=NamedReference[name=test/database.nsf]]]; 
exporterLog=[
    <?xml version='1.0'?>
    <DXLExporterLog>
        <error id='7112'>Error occurred during processing of note ID 0x57A</error>
        <warning id='7034'>Inconsistent data encountered %s</warning>
        <error>DXL exporter operation failed</error>
    </DXLExporterLog>
]
```

Inconsistencies like that can usually be fixed by opening up the
database in question and navigating to the document identified by its
note ID in the XML (e.g. 0x57A in the error message above) and simply
re-saving it. To find a document by note ID, several 3rd party
development tools are available (e.g. [Noteman](http://www.noteman.com/)
by MartinScott). More details on fixing the issue can be found in the
following document:

[![](rest/documentConversion/latest/conversion/thumbnail/45352221/1)](/kbase/download/attachments/28576224/Troubleshooting_DXL_Export_Errors.pdf?version=1&modificationDate=1616149634496&api=v2)

### DXL Crash

  

More severe issues during DXL export will lead to a crash of the DXL
exporter. Even though it's not caused by iDNA, but the interaction
between the DXL task and the Notes database, iDNA helps buffering the
impact of such a crash with its multi-process scan architecture based on
Docker.

In such a case, an error message would show up in the column "System
Status" and provides additional information to the problem. Database
compact and fixup with recovery options are recommended to approach
solving these issues. If the problem persists, opening a PMR with HCL
might be required.

  

  

## Initiating a Re-Scan

The best practice is to simply re-scan failed databases. Therefore:

1.  Click on the **Status** column to display its column/filter options
2.  Select the **Filter **tab
3.  Deselect **OK** so that only FAILED databases will be displayed
4.  Make sure that **Filtered results** is selected in the Re-scan
    Database Designs field and click on **Start**

  

![](/images/kb/28576224/28576270.png)

![](/images/kb/28576224/28576271.png)

  

{{% callout type="info" %}}

Re-scanning databases is a multi-step process, that will take up to 2
days before the newly re-scanned databases will appear in the interface.
Do not re-scan all databases unless absolutely necessary as it may run
over several days and put significant strain on the appliance and
infrastructure. In some cases several re-scans might be required.

{{% /callout %}}

You can make use of further filter options in this view to restrict the
re-scan scope further down to DXL Exporter crashes.

  

  

## Troubleshooting Other Issues

**Insufficient access rights **are another frequent reason for the iDNA
Applications Design Collection to fail. To troubleshoot these kinds of
issues, the access rights of the corresponding databases or servers have
to be adapted for the ID that is used by iDNA Applications.

**Bad** or **hidden database design** (often with third-party tools)
will also cause failures in Design Collection. With tools like
[Noteman](http://www.noteman.com/), **[Ytria
scanEZ](https://www.ytria.com/ezsuite/scanez)** or **[HCL
Notespeek](https://support.hcltechsw.com/csm?id=kb_article&sysparm_article=KB0036425)**
one can usually locate these design documents and determine what may be
wrong with them. On the following websites you can search for details on
the error codes that are shown in the Collection grid: 

- <http://www.codestore.net/errors.nsf/all/>
- <https://invorx.com/lotus-notes-error-messages/>

Sometimes the iDNA Applications appliance cannot reach the server where
the database resides due to network issues. In these cases a simple
re-scan of the affected databases will fix the issue.

If you are not able to troubleshoot your database design issues with the
means described in this article, please consult
[support.panagenda.com](http://support.panagenda.com).  
  

  

  

  
