---
title: "Configuring Profile Document Collection in iDNA Applications"
weight: 4
date: 2025-10-07
source_confluence_id: 119439707
draft: false
---
### **Overview** 

Profile Documents are special documents in Domino databases that are
used to store configuration and other information, often user-based.
Profile documents are special in that they typically don't appear in
views but are mainly accessed through formulas and scripts.  

For more information on Profile Documents/Forms please refer to the [HCL
Documentation](https://help.hcltechsw.com/dom_designer/beta/12.0.1/basic/H_ABOUT_CREATING_PROFILE_FORMS.html).

 

### **Configuring iDNA to collect Profile Documents** 

By default, iDNA Applications versions prior to v3.3.0 do not collect
Profile documents from applications, but can be configured to do so.
This article takes you through the steps required to enable/disable
Profile Document collection.  

  

{{% callout type="info" %}}

As of iDNA Applications version 3.3.0, profile documents are collected
automatically if within he license scope. The steps below can still be
used to disable collection. However, should Profile Document collection
be disabled, Content Age collection will be disabled with it.

{{% /callout %}}

  

### **Steps to Update Configuration Files **

1.  Use the ssh client of your choice (e.g. putty on Windows) to connect
    to the appliance and log in as 'root'.   
     

2.  Navigate to iDNA config directory (using the following command):   

    **cd /opt/panagenda/appdata/volumes/idna **

     

3.  Edit the dda-config.properties file (Using the **nano** editor.
    Unlike vi, nano is a modeless editor, which means that you can start
    typing and editing the text immediately after opening the file)  
    ***nano dda-config.properties**** ***  
     

4.  Add a new line with the following configuration (true = enable
    collection / false = disable collection):   
    ***exporter.profiles=true** ***  
     

5.  Save and exit the file (In **nano**, ***use*** ***Ctrl+x***).  You
    can then optionally verify your change using the **cat** command:  
    ***cat dda-config.properties**** ***  
     

6.  Restart the DDA container:   
    ***docker restart panagenda_dda ***

 

### **Initiating the Design Re-Scan**

iDNA Applications collects design information in order to surface
complexity, insights, profile information and the various applications
in your environment. Once iDNA Applications has been configured to
aggregate Profile Documents, we recommend re-collecting the set of
applications that you may wish to have included in iDNA Applications
analytics. 

  

To initiate a re-scan, go to the "Settings" menu and select "Design
analysis status"

 ![](/images/kb/119439707/119439705.png)

  

There are a series of options to choose from when it comes to what
should be re-scanned: 

- Filtered Results (the DB list can be filtered by interacting with
  column headers. if no filters are applied, all DBs will be
  re-scanned) 

<!-- -->

- All Failed Databases (DBs where a scan failed previously) 

<!-- -->

- Previously inaccessible Databases (DBs where access was denied in
  previous attempts) 

 ![](/images/kb/119439707/119439706.png)

  

### **Issues with Design Collection **

   
In cases where errors have occurred with a design collection on a
database, whether DXL errors, or issues with the design in an
application, you may need to troubleshoot further. For more information
on Troubleshooting Design Collection Issues please reference the
technote:
[www.panagenda.com/kbase/display/IA/Troubleshooting+Design+Collection+Issues](http://www.panagenda.com/kbase/display/IA/Troubleshooting+Design+Collection+Issues)) 

 

### **Setting Up / Disabling Periodic Collection**

  
Per default, profile documents are collected when database design is
collected. With [iDNA version
3.1.0](https://panagenda.com/kbase/pages/viewpage.action?pageId=119439712)
a new feature was introduced that allows the periodic collection of
Profile Documents. The interval for this collection is configurable via
an ETL parameter

- Go to the ETL parameter configuration:
  https://\<your-server\>/idna/sys/etl
- Edit the value for parameter "ia_profile_rescan_interval_weeks":
  - 0 = disable periodic collection
  - 1 = every week
  - n = every n weeks  
    ![](/images/kb/119439707/119439725.png)

 

  
