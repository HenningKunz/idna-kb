---
title: "Migrating iDNA Applications from version 2.4 to version 3.0"
weight: 20
date: 2025-06-24
source_confluence_id: 119439546
draft: false
---
  

From version 3.0.0 onward, iDNA Applications upgrade packages will not
be backward compatible with the CentOS-based appliance that was used
with iDNA v2.x. This article outlines the necessary steps to set up a v3
Alma Linux appliance and migrate data from the old appliance.

  

{{% callout type="warning" %}}

Our previous operating system CentOS Linux 7 will reach end of life
(EOL) on June 30, 2024. Please see the [official announcement by Red
Hat](https://www.redhat.com/en/topics/linux/centos-linux-eol) for more
details.

{{% /callout %}}

panagenda provides new virtual images based on Alma Linux 9, a
RHEL-based open-source Linux distribution. We encourage all customers to
migrate their installations to the new virtual image.

  

### **Download the new iDNA v3 Alma Appliance**

- **VMWare (recommended): [OVA
  File](https://files.panagenda.com/iDNAApplications/panagenda_idnaapplications_vmware_esx.ova)
  / [MD5
  Checksum](https://files.panagenda.com/iDNAApplications/panagenda_idnaapplications_vmware_esx.md5)**
- Hyper-V: [VM Image (7z
  Archive)](https://files.panagenda.com/iDNAApplications/panagenda_idnaapplications_hyperv_vhd.7z)
  / [MD5
  Checksum](https://files.panagenda.com/iDNAApplications/panagenda_idnaapplications_hyperv_vhd.md5)

  

### **Deploying the new Appliance**

- [Resource
  requirements](https://www.panagenda.com/kbase/display/IA/System+Requirements)
  are similar to the CentOS appliance so sizing should be similar as
  well  
  - The backup files created during the migration will take up 10-30% of
    additional disk space on the /opt/panagenda/pgdata partition of the
    new appliance and should be considered when sizing the new disk.  
      
  - Contrary to CentOS guidelines, the new recommendation for
    partitioning the Alma appliance is to extend a single disk to the
    required size. Adding additional disks is still possible, but there
    should be a slight performance edge with a single disk.  
      
- [Disk Partitioning Guide](/kb/extending-disk-space-alma-linux/)  
    
- [Initial OS Configuration Guide](/kb/starting-the-virtual-appliance/)

  

### **Data and Configuration Migration**

- Both appliances need to be running at the same time and the old
  appliance has to be reachable from the new appliance on ports 22 and
  5432  
    
- [![](/images/kb/119439546/119439609.png)](attachments/119439546/119439592.pdf) [iDNA_Applications_v3_MigrationGuide.pdf](attachments/119439546/119439592.pdf)

  

### **Post-migration Tasks**

- Like in conventional version updates, it will require one run of the
  nightly processing tasks on the new appliance for all features to be
  available.  
    
- After successful migration, iDNA should not be re-started on the old
  appliance. However, panagenda recommends not decommissioning the old
  appliance until all functionality (including data collection) has been
  verified on the new appliance.  
    
- To ensure iDNA doesn't start up unintentionally after the migration,
  you can issue the following commands on the console (e.g. via Putty)
  of the old appliance
  - ***ifa stop***
  - ***ifa down***

  
