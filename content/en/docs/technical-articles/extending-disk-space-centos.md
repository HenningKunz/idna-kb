---
title: "Extending Disk Space (CentOS)"
weight: 16
date: 2024-06-04
source_confluence_id: 28574336
draft: false
---
Depending on your environment you may need to enlarge the virtual disk
on which the data is stored.

{{% callout type="info" %}}

***Please note that all virtual disks have to be located on the same
physical storage. Please also note that extending disk space ALWAYS
means that you have to add a new disk on virtual hardware level. I. e.
extending disk space never means enlarging existing disks.***

{{% /callout %}}

  

  

## Extending VMWare Disk

Extending the virtual disk is done using the VMWare host application.
Here are examples for VMWare Workstation and vSphere:  
![](/images/kb/28574336/28574338.png) 

![](/images/kb/28574336/28574339.png)![](/images/kb/28574336/28574340.png)

  

Please restart the virtual appliance after adding the new disk. 

  

## Extending Hyper-V Disk

To extend the virtual disk, open the virtual machine properties and
follow the steps below:

1.  Navigate to *IDE Controller 0*, select *Hard drive* and
    click ***Add  
    ![](/images/kb/28574336/28574341.png)  
      
    ***
2.  Select ***New*** and finish the wizard:  
    ![](/images/kb/28574336/28574342.png)![](/images/kb/28574336/28574343.png)  
      
      
3.  After finishing the wizard click ***Ok*** to exit the Settings:  
    ![](/images/kb/28574336/28574344.png)

  

Please restart the virtual appliance after adding the new disk. 

##  Enlarging the Partition in the Appliance

1.  The easiest way to enlarge a partition in the appliance is to use
    the installed partition manager **GParted**. Please launch it using
    the Applications menu (you can also start GParted from the Terminal
    with "sudo gparted"):  
      
2.  Select the new physical disk:  
    ![](/images/kb/28574336/28574345.png)  
      
3.  Select the unallocated space, open the *Device* menu and on click
    on ***Create Partition Table***:  
    ![](/images/kb/28574336/28574346.png)  
      
4.  Click on *Apply* in the warning:  
    ![](/images/kb/28574336/28574347.png)  
      
5.  Select the new *unallocated* space, right-click and select *New*:  
    ![](/images/kb/28574336/28574348.png)  
      
      
6.   From the *Createas* drop down menu,
    select ***Primary**Partition*** and chose ***lvm2**pv*** as *File
    system* (if needed, a *Label* can be defined):  
    ![](/images/kb/28574336/28574349.png)  
      
7.  Save your changes by clicking the **apply button** - also on the
    popup message  
    ![](/images/kb/28574336/28574350.png)  
      
8.  Start the **Logical Volumes Manager** from the Applications menu  
      
9.  Open the *Logical View* on the left hand side, select *Physical
    View* and click ***Extend Volume**Group***:  
    ![](/images/kb/28574336/28574351.png)  
      
10. Select your new volume and click *OK*:  
    ![](/images/kb/28574336/28574352.png)  
      
11. After this, select the logical volume ***opt_panagenda_appdata***:  
    ![](/images/kb/28574336/28574353.png)  
      
12. Resize the logical volume as needed (initial dimensioning: 5MB x
    database instances - for more details, please refer to the [**Setup
    Guide**](https://www.panagenda.com/download/ConnectionsExpert/ConnectionsExpert_SetupGuide_EN.pdf)):  
    ![](/images/kb/28574336/28574354.png)'  
      
13. Select the logical volume opt_panagenda_pgdata (for more details on
     initial dimensioning, please refer to the [**Setup
    Guide**](https://www.panagenda.com/download/ConnectionsExpert/ConnectionsExpert_SetupGuide_EN.pdf)):   
    ![](/images/kb/28574336/28574355.png)  
      
14. Resize the logical volume as needed (see step 12) 

  

{{% callout type="info" %}}

You can repeat this enlargement whenever you need more space.

{{% /callout %}}

  
