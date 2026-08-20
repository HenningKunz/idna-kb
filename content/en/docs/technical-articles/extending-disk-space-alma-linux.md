---
title: "Extending Disk Space (Alma Linux)"
weight: 15
date: 2024-09-12
source_confluence_id: 119439396
draft: false
---
In order to provide more disk space on the iDNA appliance, the
underlying disk, partition and logical volume all have to be extended.

  

{{% callout type="info" %}}

*Please note that all virtual disks should be located on the same
physical storage for best performance.*

{{% /callout %}}

***In contrast to the old CentOS appliance, it is now recommended to
enlarge the existing VMWare disk, rather than adding new virtual
disks.***

  

  

## Extending the VMWare Disk

Extending the virtual disk is done using the VMWare host application.
Here are examples for VMWare Workstation and vSphere:  
![](/images/kb/119439396/119439394.png) 

![](/images/kb/119439396/119439393.png)![](/images/kb/119439396/119439392.png)

  

Please restart the virtual appliance after adding the new disk. 

  

## Extending the Hyper-V Disk

To extend the virtual disk, open the virtual machine properties and
follow the steps below:

1.  Navigate to *IDE Controller 0*, select *Hard drive* and
    click ***Add  
    ![](/images/kb/119439396/119439391.png)  
      
    ***
2.  Select ***New*** and finish the wizard:  
    ![](/images/kb/119439396/119439390.png)![](/images/kb/119439396/119439389.png)  
      
      
3.  After finishing the wizard click ***Ok*** to exit the Settings:  
    ![](/images/kb/119439396/119439388.png)

  

Please restart the virtual appliance after adding the new disk. 

  

  

## Enlarging the Partition on an Existing Disk in the Appliance

Perform the steps in this paragraph if an existing virtual disk was
enlarged. If a new disk was added, please skip this chapter and continue
with "Creating a Partition on a New Disk in the Appliance" instead.

The easiest way to enlarge a partition in the appliance is to use the
installed partition manager **GParted**. Please launch it using the
Applications or Activity menu (or using the shell command "gparted").  
  

After starting GParted, you may be prompted with a message about whether
the GPT partition should be resized to use all available space. Please
confirm this change by clicking "Fix"!

![](/images/kb/119439396/119439570.png)

  

1.  Right-click the partition that needs to be extended and click on
    Resize/Move  
    ![](/images/kb/119439396/119439475.png)  
      
      
2.  Draw the right border to the end, so that all fee space is taken up
    by the resized partition and click Resize  
    ![](/images/kb/119439396/119439476.png)  
      
      
3.  Confirm and apply the changes by clicking the green check-mark
    (Apply All Operations) in the tool bar  
    ![](/images/kb/119439396/119439477.png)  
      

## Creating a Partition on a New Disk in the Appliance

Perform the steps in this paragraph if a new virtual disk has been added
to the system and its space should be made available to iDNA. If an
existing disk has been enlarged, please continue with take a look at the
chapter "Enlarging the Partition on an Existing Disk in the Appliance"
instead.

The easiest way to enlarge a partition in the appliance is to use the
installed partition manager **GParted**. Please launch it using the
Applications or Activity menu (or using the shell command "gparted").

  

1.  Select the new physical disk:  
    ![](/images/kb/119439396/119439387.png)  
      

2.  Select the unallocated space, open the *Device* menu and on click
    on ***Create Partition Table***:  
    ![](/images/kb/119439396/119439386.png)  
      

3.  Select "gpt" as partition type and click on *Apply* in the
    warning:  
    ![](/images/kb/119439396/119439646.png)  
      
      

4.  Select the new *unallocated* space, right-click and select *New*:  
    ![](/images/kb/119439396/119439384.png)  
      
      

5.   From the *Createas* drop down menu,
    select ***Primary**Partition*** and chose ***lvm2**pv*** as *File
    system* (if needed, a *Label* can be defined):  
    ![](/images/kb/119439396/119439383.png)  
      

6.  Save your changes by clicking the **apply button** - also on the
    popup message  
    ![](/images/kb/119439396/119439382.png)  
      
      

    
{{% callout type="info" %}}

    The new disk is now available to the operating system, but still
    needs to be made available to logical volumes.

    
{{% /callout %}}

7.  Start the "**LVM Manager"** (Logical Volumes Manager) from the
    Applications/Activities menu and select the original disk **"sda"**
    on the left hand navigation bar,  
    right-click **"cl-pan"** in the device list, select **"Edit"** and
    click **"Modify parents"**  
    ![](/images/kb/119439396/119439647.png)  
      

8.  Click **"Add a parent"** and select your new disk in the list of
    available devices and click OK.  
    ![](/images/kb/119439396/119439648.png)  
      

9.  Apply the changes using the check-mark symbol (Apply pending
    actions) in the top tool bar  
    ![](/images/kb/119439396/119439485.png)  
      
    You can leave the LVM Manager application open, as we will need it
    during the next steps.

  

## Adding the new Disk Space to Logical Volume Groups

Now that new disk space is available to the operating system, we need to
make it available to the appropriate volumes inside their volume groups.

There are two main volumes that may need resizing:

- appdata (mounted to /opt/panagenda/appdata): mainly storage for DB
  design export files (DXL)
- pgdata (mounted to /opt/panagenda/pgdata): storage for Postgres
  database files

  
In this guide we will be using **"pgdata"** as an example, since it's
the most likely volume that may need resizing. Whenever referred to the
volume "pgdata", please look for the mountpoint "/opt/panagenda/pgdata"
or the device name "cl-pan-opt_panagenda_pgdata".

  

{{% callout type="warning" %}}

In order to resize a volume, the volume needs to be unmounted. It is
critical to stop iDNA before unmounting volumes!

{{% /callout %}}

  

1.  Start a **"Terminal"** from the Applications/Activities menu,
    execute the command **"systemctl stop docker"** and wait for the
    command to finish (this may take several minutes).  
    ![](/images/kb/119439396/119439780.png)  
      
2.  Start the "**LVM Manager"** (Logical Volumes Manager) from the
    Applications/Activities menu and select the volume group
    **"cl-pan"** on the left hand navigation bar.  
    ![](/images/kb/119439396/119439478.png)  
      
      
3.  Select the **"pgdata"** volume, right-click it and execute
    **"Unmount"  
    **![](/images/kb/119439396/119439481.png)  
      
      
4.  The unmount process will reset the selection in the device list, so
    please select **"pgadata"** again.  
    Tip: volumes can also be selected via the top navigation bar:  
    ![](/images/kb/119439396/119439482.png)  
      
      
5.  Right-click **"pgdata"**, go to the edit sub-menu and select
    **"Resize"**  
    ![](/images/kb/119439396/119439483.png)  
      
      
6.  Drag the indicator to the right to add disk space to this volume and
    confirm with **"Resize"**  
    ![](/images/kb/119439396/119439484.png)  
      
    **Note:** even though were are adding all disk space to one volume
    in this example, the new available disk space may be divided between
    multiple volumes. For more information on calculating disk space
    requirements, please refer to the [**Setup
    Guide**](https://www.panagenda.com/download/idnaApplications/iDNA_Applications_SetupGuide_EN.pdf).  
      
      
7.  Apply the changes using the check-mark symbol (Apply pending
    actions) in the top tool bar  
    ![](/images/kb/119439396/119439485.png)  
      
      
8.  After confirming the queue, you should see a success message like
    the one below and the new disk space will now be available to
    iDNA.  
    ![](/images/kb/119439396/119439490.png)  
      
      
9.  Depending on the size of the environment, the **"appdata"**
    partition may have to be resized as well. If that should be the
    case, please repeat the actions in steps 3 to 8 for this partition
    as well.  
    A likely reason for the "appdata" partition needing resizing as well
    is if you have a large environment with a lot of applications.
    Please see the [Virtual Hardware section in System
    Requirements](/kb/system-requirements/) for partition sizing
    recommendations.  
      
10. To complete the changes, we need to start iDNA Applications again.
    Since one or more partitions might be unmounted at this point, the
    easiest way to do this is execute the command **"reboot"** in the
    command line.

  
