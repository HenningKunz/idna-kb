---
title: "Downgrade Hardware Level of VMWare Appliance"
weight: 29
date: 2019-04-15
source_confluence_id: 28574361
draft: false
---
The minimum required hardware level of our iDNA Applications appliances
is 11. This means iDNA Applications supports VMWare from ESXi 6.0 and
Workstation 11.x and up.

  

If you are running older version, please follow these steps to downgrade
the virtual appliance (to level 8 in this example):

1.  **Open** the **.ova** file with 7zip

2.  Delete the **.cert** and **.mf** inside of the .ova

3.  **Edit** the **.ovf** file inside of the .ova and set
    the **VirtualSystemType** element to **vmx-08**:

    ``` text
    <vssd:VirtualSystemType>vmx-08</vssd:VirtualSystemType>
    ```

4.  **Import** the **.ova** file and startup the appliance

5.  **Uninstall** the **open-vm-tools** package:

    ``` text
    yum remove open-vm-tools
    ```

6.  **Install the correct** **open-vm-tools** version:

    
{{% callout type="info" %}}

    Pick open-vm-tools version depending on ESXi version:
    <https://packages.vmware.com/tools/versions>. If you can not find
    the required version on that page, please search the internet for
    it.  
    Open-vm-tools rpm downloads:
    <https://rpmfind.net/linux/rpm2html/search.php?query=open-vm-tools>.

    
{{% /callout %}}

    ``` text
    yum install ftp://ftp.pbone.net/mirror/ftp.scientificlinux.org/linux/scientific/7.4/x86_64/os/Packages/open-vm-tools-10.1.5-3.el7.x86_64.rpm
    ```

7.  Exclude open-vm-tools from yum upgrades:  
    **Add following line to */etc/yum.conf***

    ``` text
    exclude=open-vm-tools*
    ```

8.  **Reboot** the appliance to finish the downgrade
