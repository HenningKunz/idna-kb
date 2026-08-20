---
title: "Import Hyper-V Image on Older Windows Server Editions"
weight: 18
date: 2019-12-13
source_confluence_id: 28576341
draft: false
---
  

On older Hyper-V server versions you might encounter issues while
importing the iDNA Applications virtual machine.

  

The following steps describe a workaround:  
  

- Extract the file **panagenda_idnaapplications_hyperv_vhd.7z  
    
  **
- Start Hyper-V Manager  
    
- Right-click on your server and select “New -\> Virtual Machine”  
  ![](/images/kb/28576341/28576367.png)  
    
- Click **Next** on “Before you Begin” screen  
    
- Enter a name for the virtual machine, e.g.
  **panagenda_idnaapplications  
  ![](/images/kb/28576341/28576349.png)  
    
  **
- Select **Generation 1** on the “Specify Generation” screen  
  ![](/images/kb/28576341/28576351.png)  
    
- Specify the startup memory on the “Assign Memory” screen -\> **minimum
  required are 8092 MB  
  ![](/images/kb/28576341/28576352.png)  
    
  **
- Specify a network connection -\> e.g. **Default Switch  
    
  **
- On the Connect “Virtual Hard Disk” screen select **Use an existing
  virtual hard disk  
  ![](/images/kb/28576341/28576353.png)  
    
  **
- Select the the virtual hard disk file from the
  **panagenda_idnaapplications\Virtual Hard Disks** directory  
  ![](/images/kb/28576341/28576354.png)  
    
- On the “Completing the new Virtual Machine Wizard” click **Finish** to
  create the virtual machine  
  ![](/images/kb/28576341/28576355.png)  
    
    
