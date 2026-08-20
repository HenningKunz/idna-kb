---
title: "Deployment Steps"
weight: 12
date: 2021-10-13
source_confluence_id: 28578114
draft: false
---
1.  Access **[shell.azure.com](http://shell.azure.com/)** and login as
    Azure tenant administrator (alternatively it is also possible to use
    Azure CLI)  
      

2.  Clone this repository by executing:  
    **git
    clone [https://github.com/panagenda/idna-applications-on-azure  
    ![](/images/kb/28578114/28578172.png)](https://github.com/panagenda/idna-applications-on-azure)**  
      

3.  Export your **azure tenant id** by executing:  
    **export tenantId="{Azure Tenant ID}"  
      
    **

4.  Define your **azure subscription id** where the Azure resources
    should be assigned to by executing:  
    **export subscriptionId="{Azure Subscription ID}"  
      
    **

5.  Define the template URL we provided you with:  
    **export
    template="[https://xxxxx.blob.core.windows.net/xxxx](https://oestoresa43989365.blob.core.windows.net/oestoresc43989365/ifa120.vhd)"  
      
    **

6.  Customize the prep.sh file and adjust the location placeholder
    (default=westeurope) according to your requirements:  
    You can either use the [Azure Cloud Shell
    editor](https://docs.microsoft.com/en-us/azure/cloud-shell/using-cloud-shell-editor) or   
    **vi prep.sh**  
    **  
    **

7.  Execute:  
    **./prep.sh**  
    to prepare everything for Terraform  
      

8.  Customize the vars.tf based on your needs: (details can be found
    here: [Customize the Azure
    Deployment](/kb/customize-the-azure-deployment/))  
    You can either use the Azure Cloud Shell editor or  
    **vi vars.tf  
    **![](/images/kb/28578114/28578173.png)

9.  Execute the following to deploy iDNA Applications:  
    *****./up.sh  
      
    *****

10. The `up.sh` will print the IP address of the deployed Appliance.
    Please create a DNS entry for this IP address.  
      

11. Final steps:

- Execute Script: --\> for further details, please refer to [Azure
  Deployment Details](/kb/azure-deployment-details/)

`./config.sh "{FQDN of iDNA Applications}" "{TimeZone}" "{new root password}"`

**`Example`**`:./config.sh "my-ia.my-domain.com" "Europe/Berlin" "my-root-password"`

- The `config.sh` script will configure the appliance

- The Azure resources are now successfully deployed.

**![](/images/kb/28578114/28578174.png)  
**
