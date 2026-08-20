---
title: "System Requirements"
weight: 46
date: 2024-06-26
source_confluence_id: 28578348
draft: false
---
## Host Software

panagenda iDNA Applications comes as a virtual appliance including its
own operating system based on the popular CentOS Linux distribution. No
operating system needs to be prepared for the installation on the
virtualization software side.   
Virtual appliances are available for:

- ****VMWare vSphere - ESXi** **(recommended for production)**  
  **

  
{{% callout type="info" %}}

  ***For compatibility reasons, our appliances are configured for ESXi
  6.7 and Workstation 14. If you run a newer version, we recommend to
  upgrade the virtual machine hardware version after image
  deployment.***

  
{{% /callout %}}

- **Microsoft Hyper-V**

The underlying hardware and OS need to have VT-x support enabled (in
BIOS). This is mainly relevant in scenarios where Workstation act as
host software. Detailed information about operating system requirements
can be found on the respective product
pages: [**www.vmware.com/products/**](http://www.vmware.com/products/)

## Virtual Hardware

**Minimum hardware requirements for production environment:**

- Enterprise grade server hardware for all components
- CPU: 4 Cores
- RAM: 8 GB
- Disk: 120 GB

  

**Adapting virtual hardware to the environment size:**

Most system requirements scale with the collection period and
environment size. CPU is the exception, where the four cores are
adequate for most customer sizes.   
Baseline Requirements:

|                     |         |                         |
|---------------------|---------|-------------------------|
| **Amount of Users** | **RAM** | **Disk Space (1 year)** |
| Up to 5k (minimum)  | 8 GB    | 120+ GB                 |
| Up to 25k           | 16 GB   | 200+ GB                 |
| Up to 50k           | 32 GB   | 250+ GB                 |
| Up to 75k           | 48 GB   | 300+ GB                 |
| 100k and above      | 64 GB   | ~5+ GB per 1k users     |

  
Disk Space per Application:  
In addition to the baseline requirements, the appliance requires 75MB of
disk space per database.

  

**Partitions and disk growth:**

The virtual appliance consists of several partitions for the operating
system, applications, log files and the database. The database
partition **/opt/panagenda/pgdata** is the only one where usage will
continuously increase over time.  
The application partition **/opt/panagenda/appdata** will fill quickly
during the initial design collection, but usage will hardly increase
after that phase.   
Accordingly, disk space should be assigned as follows:

- **/opt/panagenda/appdata**: 5 MB per database
- **/opt/panagenda/pgdata**: Remainder of the disk space

  
See [Extending Disk Space (Alma
Linux)](/kb/extending-disk-space-alma-linux/) for instructions.

{{% callout type="info" %}}

***Best Practice: Leaving 10-20 GB of disk space unassigned offers a
certain amount of flexibility and can help speeding up database recovery
times significantly.***

{{% /callout %}}

  

<u>Deployment Example</u>: 40k user environment with 10k database
instances

- 32GB RAM
- 1 TB disk space: 250 GB (baseline) + 750 GB (10k DBs x 75 MB)
  - Leave 15 GB unassigned
  - Enlarge /opt/panagenda/appdata by 50 GB
  - Enlarge /opt/panagenda/pgdata by remaining 935 GB

## Access and Permissions

**HCL Domino Notes:**

The following access to the Domino environment is required:

- **Single Notes ID file with access (cross certification) to all
  servers in scope**
  - **Reader access to at least one Domino Directory per Domain**

  - **Reader access to all servers' log.nsf databases**

  - **Reader access to all servers' catalog.nsf databases**

  - **Reader access to all servers' domlog.nsf databases where enabled**

  - **"Full Remote Console Administrator" access on all servers**

  - **Designer access to all databases where design should be analyzed  
    **

    
{{% callout type="info" %}}

    ***In environments where it is not possible to grant Designer access
    to the uploaded Notes ID file on all focus databases, the
    administrator can choose to give this ID Full Administration Access
    per Domino server (via server document). iDNA Applications will use
    this access method by default if available.***

    
{{% /callout %}}

Domino server requirements:

- Statlog task scheduled on all servers
- Catalog task scheduled on all servers
- INI entry LOG_DISABLE_SESSION_INFO must not be set to 1
- "Domlog.nsf" enabled and "Access log format" set to "Extended
  Common"  
  (*names.nsf* \> *Server Document* \> *Internet Protocols*...
  \> *HTTP*)  
  MIME types "image/\*", "text/css" and "text/javascript" can be
  excluded

  

**Network (Firewall/Ports):**

Connections to and from the appliance need to be allowed for the
following services:  
*Outbound (originating in virtual appliance):*

- Notes **RPC** to Domino servers for data collection (TCP 1352)
- **HTTP/HTTPS** to Domino servers for data collection (TCP 80/443)

  
*Inbound (accessing virtual appliance):*

- **HTTP/HTTPS** for configuration and reports (TCP 80/443)
- **SSH** for system configuration and application tuning (TCP 22)
- **VNC** for system configuration and Notes client access (TCP 5901)
- Optional: PostgreSQL for data warehouse access where enabled (TCP
  5432)

  
It is recommended that the iDNA Applications owner has access to the
console of the virtual machine (e.g. via vSphere client).  
Internet access for the appliance is not mandatory, but it is
recommended to grant at least proxy access to
\*.[panagenda.com](http://panagenda.com) and your defined CentOS
repository for security and application updates.

{{% callout type="info" %}}

 ***iDNA Applications requires the following network segments for
internal communication:***

{{% /callout %}}

**192.168.237.0/24**  
**192.168.238.0/24**

***These two IP address ranges MUST NOT be routable in your production
network! Please see [Customize Docker IP
Settings](/kb/customize-docker-ip-settings/) if they are in use in your
network.***

  

## Client System Requirements

**Hardware, Operating System and Software Requirements:**

The panagenda iDNA Applications web interface is based on HTML5 and
therefore accessible on any **HTML5 capable** **device**.

- We recommend the following browsers in
  latest **64-bit** versions: **Chrome** and **Firefox**

  

**Browser Security and Network Access:**

No special web browser security settings are required to run the
panagenda iDNA Applications web interface.  
To access the web interface, you need to have access to the panagenda
iDNA Applications appliance via TCP/IP, Port 80 (HTTP) and Port 443
(HTTPS).
