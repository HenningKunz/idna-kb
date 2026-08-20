---
title: "DB Content Analysis - Concurrent Scans"
weight: 28
date: 2020-05-07
source_confluence_id: 28578010
draft: false
---
By default, the content analysis in iDNA Applications is limited to one
concurrent scan. However, this limit can be increased via a
configuration setting.

  

1.  Use the** ssh client** of your choice
    (e.g. [putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) on
    Windows) to connect to the appliance and **edit** the
    following **properties file** (e.g.
    using [vim](https://vimhelp.org/vim_faq.txt.html)):

    ``` text
    vim /opt/panagenda/appdata/volumes/idna/idna-config.properties
    ```

      

2.  **Change** the following property according to your needs (default =
    1):

    ``` text
    dca.aggregations.max_concurrent=1
    ```

    
{{% callout type="info" %}}

    ***Please note that increasing this value may lead to significantly
    increased load on your Domino servers, the network or the iDNA
    Applications server. Depending on the size, location and content of
    the database, some or all of these areas may be affected. It is
    strongly recommended that this setting is adapted with only great
    care!*** 

    
{{% /callout %}}

      

3.  **Save** the properties file and **exit  
      
    **

4.  **Restart** iDNA Applications with the following command:

    ``` text
    ifa restart
    ```
