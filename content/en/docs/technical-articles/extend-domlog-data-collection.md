---
title: "Extend DomLog Data Collection"
weight: 14
date: 2020-05-06
source_confluence_id: 28575220
draft: false
---
In order to save resources, the collection of DomLog data in iDNA
Applications is limited to its essentials. Cookie and referrer data, as
well as status codes 302 and 304 are not collected per default.

  

If you need to extend data collection to its full scope, please follow
these steps:  
  

1.  Use the **ssh client** of your choice
    (e.g. [putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) on
    Windows) to connect to the appliance and **edit** the following
    **properties file** (e.g.
    using [vim](https://vimhelp.org/vim_faq.txt.html)):

    ``` text
    vim /opt/panagenda/appdata/volumes/idna/idna-config.properties
    ```

2.  **Add** the following **settings** at the end of the properties
    file:

    ``` text
    domino.server.domlog.import.accesslog.exclude_cookie_data=false
    domino.server.domlog.import.accesslog.exclude_referer_data=false
    domino.server.domlog.import.accesslog.exclude_status_codes=
    ```

    ``` text
    domino.server.domlog.import.ndb.exclude_cookie_data=false
    domino.server.domlog.import.ndb.exclude_referer_data=false
    domino.server.domlog.import.ndb.exclude_status_codes=
    ```

3.  **Save** the properties file and **exit**  
      

4.  **Reboot** the iDNA Application appliance with the following
    command:

    ``` text
    ifa restart
    ```
