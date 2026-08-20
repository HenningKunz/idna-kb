---
title: "Content Packages - Basic Configuration"
weight: 50
date: 2020-06-19
source_confluence_id: 28578371
draft: false
---
The basic configuration in this section of the iDNA Applications user
interface includes:

## 1. HCL Notes User ID File Upload

In the iDNA Applications configuration portal, click on the *Setup User
ID* button beside the User ID section, to open a dialog for uploading
your ID file.

- Please ensure that the HCL Notes User ID meets the [System
  Requirements](/kb/system-requirements/)

To upload the new User ID file, please open the file selection dialog by
clicking the *Browse* button. Select the desired HCL Notes User ID,
enter the appropriate password and click on *Upload*. "Success" means
that you uploaded a properly configured HCL Notes User ID:  
![](/images/kb/28578371/28578372.png)

**  
**

## 2. Domino Server Settings

Click the *Discovery* button in the in the iDNA Applications
configuration portal ([https://*\<FQDN or IP\>*/idna/cfgc]()) to open
the Domino Server Settings:  
![](/images/kb/28578371/28578373.png)

  
There are two ways to set up your Domino servers for iDNA Applications:

1.  *Start new Domino Server Discovery* – this option provides a
    comfortable way to add several servers to the iDNA Applications
    analysis
2.  *Add new server* – this section offers the possibility to add
    (further) servers manually. Just enter the FQDN of the servers iDNA
    Applications is supposed to analyze

### Start new Domino Server Discovery

The Domino server discovery starts at the server that you enter in
the *Entry server host name/ IP* field. This server's Domino Directory
will be scanned for further server documents.   
After entering the FQDN or IP of your desired entry server, you can
start your Domino server discovery (by clicking on the *Start
Discovery* button) which means that the iDNA Applications Notes client
tries to access the server and reads the other server names from the
server documents in its Domino directory. You will get a notification in
case the iDNA Applications Notes ID doesn't have sufficient rights to
access the defined entry server. Depending on your infrastructure and
settings, the duration of the discovery can vary. When it is done, the
results of the discovery are displayed:   
![](/images/kb/28578371/28578374.png)   
  
In this list, all servers which have been found (in the directory of the
entry server of the discovery) will appear together with some
information about the access status of:

- the server itself
- the log file
- the Domino Directory
- the console
- the statistics
- the domlog.nsf

  
If there are any access issues, they should be solved before configuring
the content packages. Clicking on the red X deletes the respective
server from the list. You can make use of this when you want to delete
decommissioned servers that are still listed in the address book.

{{% callout type="info" %}}

***Please note that there is a list of all certifiers displayed, which
have to be included in the license file for a successful measurement.***

{{% /callout %}}

  

If there are servers which could not be found in the Domino Directory of
the Discovery Server you can add to them by using the ***Add new
Server*** option.

  

### Check Server Access

Clicking on the link ***Check Server Access*** on the *Domino Server
Settings Result* page leads to the following screen:  
![](/images/kb/28578371/28578375.png)   
Please ensure that columns *SrV* (Server Access), *LA* (Log.nsf
Access), *CaA* (Catalog.nsf Access), *NA* (Domino Directory
Access), *StA* (Statlog.nsf access) and *CA* (Console Access) are
showing "OK".   
After fixing missing access rights for a particular server, select the
server in first column and click on ***perform check*** in the
line *Check access to selected servers*. This will repeat the initial
access check which was done during Server Discovery.  
If all access right requirements of all servers are fulfilled, please
check all servers in the first column and run a ***perform check*** in
the line *Check extended access to selected servers*. This will examine
several entries in the servers *notes.ini* file via console command in
order to verify configuration parameters and come back with this screen:

![](/images/kb/28578371/28578376.png)

Please ensure that all requirements for *LC* (Log configuration)
and *CaC* (Catalog Configuration) are met by all servers. If there is an
issue in one of those columns, hover over the entry and a pop up will
display the issue found. Every time a found issue has been fixed on a
server, please do a recheck **extended access** on that specific server.
If the customer has scheduled Catalog and *Statlog* tasks via program
document(s), it is OK for *CaC* (Catalog Config) to remain in warning
state. It is always OK for *MRC* (Mail Routing Config) to remain in
warning state, since mail routing information is not processed in iDNA
Applications.
