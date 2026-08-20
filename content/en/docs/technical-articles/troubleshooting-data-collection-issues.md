---
title: "Troubleshooting Data Collection Issues"
weight: 24
date: 2020-09-10
source_confluence_id: 28576215
draft: false
---
In case iDNA Applications detects collection issues on severs, you will
see the following notification on the top-right of your screen right
after login:

![](/images/kb/28576215/28579317.png)

To see what collection issues occurred, just click on the notification
to get directly to the **Catalog \> Servers** view.

  

Here you will find an overview on what problems exist on which servers
in the **Issues** column:  
![](/images/kb/28576215/28579319.png)

  

There are five types of issues that may be pointed out:

- **Catalog** - an issue exists with collecting data from catalog.nsf
  (access issues) or with the collected data itself. Check the column
  **Catalog → Last Collection Date** and verify that your Catalog Domino
  task is updating catalog.nsf daily.  
    
- **Domlog** - an issue exists with collecting data from domlog.nsf
  (access issue) or with the available data. Check the column **Domlog →
  Last Collection Date** and verify that your domlog.nsf (or log files)
  are updated daily.  
    
- **Sessions** - an issue exists with collecting session data from
  log.nsf (access issue) or with the available data. Check the column
  **Sessions → Last Collection Date** and verify that session data is
  being collected in your log.nsf.  
    
- **INI Config** - an issue exists with a Domino server INI value that
  disables the collection of user sessions. Make sure the
  value **LOG_DISABLE_SESSION_INFO** does not exist or is not set to 1.
  Note: this warning will only occur if an extended access check has
  been performed for the server in iDNA's advanced settings
  (https://\<your-server\>/idna/sys/servers) and will only be as current
  as the last extended access check.  
    
- **Data Processing** - an issue exists with nightly processing in the
  data warehouse. Restarting iDNA Applications (by rebooting the
  appliance or issuing the command "*ifa restart*") usually resolves
  this issue. If the message persists for more than two or three days
  after the restart, please contact <support@panagenda.com> with logs
  (https://\<your-server\>/pac/logs) and a screen shot of the ETL log
  screen (https://\<your-server\>/idna/sys/etl) in advanced properties.

  

The previously mentioned Servers page
(https://\<your-server\>/idna/sys/servers) in iDNA's advanced settings
will have additional information on server status and gives the ability
to re-scan servers:  
![](/images/kb/28576215/28579322.png)  
  
Two re-scan options are available:

- **Check access** is a relatively quick check that will make sure the
  servers and all critical DBs are available
- **Check extended access** will perform a more in-depth analysis that
  includes looking at server INI parameters and will require Domino
  Console access

  

  

If this article was not able to resolve your issue, please contact us at
<https://support.panagenda.com> and include log
files (https://\<your-server\>/pac/logs) in your message.

  

  
