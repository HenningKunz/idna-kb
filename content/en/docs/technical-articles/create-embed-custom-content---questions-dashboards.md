---
title: "Create & Embed Custom Content - Questions & Dashboards"
weight: 6
date: 2020-09-11
source_confluence_id: 28574318
draft: false
---
  

In this article you will find a step by step instruction on how to
create custom content like charts and dashboards in Metabase and display
them in iDNA Applications.

  

1.  Open Metabase by entering **https://*\<iDNA Applications FQDN or
    IP\>*/metabase/ **into your browser  
      
      

2.  Log in with a Metabase **admin user** (e.g. admin@metabase.local)  
    (Please refer to [Metabase Default
    Users](/kb/metabase-default-users/) for details or ask your iDNA
    Applications administrator if you need access)  
      
      

3.  Create a **Question** (or **Dashboard)** in Metabase:  
    ![](/images/kb/28574318/28574326.png)  
    For details on that, please refer to the [Metabase
    documentation](https://metabase.com/docs/latest/getting-started.html).  

    
{{% callout type="warning" %}}

    **Please add your Questions and Dashboards you want to **embed in
    iDNA Applications** to the "Custom Content" collection in Metabase.
    Embedding also works if you add your content to the "panagenda"
    collection, but we can NOT guarantee that this content will still be
    available after upgrades of the iDNA Applications appliance.**

    
{{% /callout %}}

    
{{% callout type="info" %}}

    Give your custom questions and dashboards meaningful names and
    always add a description! Since the search function in iDNA
    Applications is based on names and descriptions, this will simplify
    the daily work for you and your colleagues considerably.

    
{{% /callout %}}

    ![](/images/kb/28574318/28574325.png)  
      

4.  Afterwards, click on the **Sharing and embedding** icon next to your
    Question or Dashboard:  
    ![](/images/kb/28574318/28574323.png)  

    
{{% callout type="warning" %}}

    If you are missing the "Sharing and embedding" button, please make
    sure you are using a Metabase account with admin rights (e.g.
    <admin@metabase.local>).

    
{{% /callout %}}

      
      

5.  Select the embed option:  
    ![](/images/kb/28574318/28574319.png)  

6.  Click on the **Publish** button in the following screen:  
      
    ![](/images/kb/28574318/28574322.png)

  

Questions and Dashboards added to the "Custom Content" collection (which
is highly recommended!) will be listed under "Custom Content" in the
iDNA Applications navigator:  
![](/images/kb/28574318/28574320.png)

  

Please reload the iDNA Applications page in your browser if newly
created contents are not displayed immediately. If the content does not
appear after a reload or two, try logging out of iDNA and logging back
in.
