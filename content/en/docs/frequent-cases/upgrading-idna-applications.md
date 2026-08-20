---
title: "Upgrading iDNA Applications"
weight: 36
date: 2024-10-24
source_confluence_id: 28575350
draft: false
---
  

Once a new version is available, a popup message will appear in the iDNA
Applications user interface. This notification links the release notes
and download links for the new version.

  

## Download the Upgrade Package

  

Two upgrade packages are available:

- [Online Installer: ~1 MB
  download](https://files.panagenda.com/iDNAApplications/idnaapplications-upgrade-online.zip) (requires
  access to [docker.panagenda.com](http://docker.panagenda.com) on the
  virtual appliance)
- [Offline Installer: ~2 GB
  download](https://files.panagenda.com/iDNAApplications/idnaapplications-upgrade-offline.zip)

  

{{% callout type="info" %}}

The offline package also includes files that may not be required in your
installation. Significantly less data will be transferred if the
appliance has access to <u>docker.panagenda.com</u>, since only the
files necessary for the upgrade will be downloaded.

{{% /callout %}}

  
 

## Install Upgrade Package

**  
**

Please upload the upgrade package to the appliance's **/tmp/** directory
using the scp client of your choice (e.g.
[WinSCP](https://winscp.net/eng/downloads.php) or
[pscp](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
on Windows).

  

Use the ssh client of your choice (e.g.
[putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
on Windows) to connect to the appliance and execute the following
commands:

``` text
cd /tmp
unzip idnaapplications-upgrade-online/offline.zip
./ifa-upgrade.sh
```

  

Logs are available in the log directory, e.g.
/opt/panagenda/logs/ia-upgrade\_\<year\>-\<month\>-\<day\>\_\<timestamp\>.log.

  

  

## Troubleshooting

**  
**

In case there is not enough space left on the root partition (~8GB free
space are required), the installation will abort and one of the
following error messages will be displayed among the last few output
lines:

- tar: images.tar: Wrote only xxx of xxx bytes
- unexpected EOF
- Error response from daemon: failed to create task for container

  

An alternative method is to place the installer file on a partition that
has enough free space and set an environment variable to tell the
installer to also use this partition for temporary files. The
/opt/panagenda/appdata or /opt/panagenda/pgdata partitions should
typically have enough disk space available to hold the temporary files
during the upgrade process.

  

These are the recommended steps for the workaround using the pgdata
partition:

- Unzip the installer so you have the **ifa-upgrade-offline.sh** file
- Remove the original installer zip file
- Create a temporary directory on the pgdata partition:  
  ***mkdir /opt/panagenda/pgdata/tmp***
- Move the installer to this new tmp directory:  
  ***mv ./ifa-upgrade-offline.sh /opt/panagenda/pgdata/tmp/***
- Set an environment variable so the installer will use our new
  directory for temporary files during the upgrade process  
  ***declare -x TMPDIR="/opt/panagenda/pgdata/tmp/"***
- Execute the update file:***  
  /opt/panagenda/pgdata/tmp/ifa-upgrade-offline.sh***
- After successful upgrade, please remove all files from the temporary
  directory:***  
  **rm -Rf /opt/panagenda/pgdata/tmp/\****

  

  

## First Login After the Update

  

If major changes to the data warehouse occurred during the upgrade,
parts of the application may not be available until the data warehouse
is rebuilt. This process runs automatically at night, but can be
triggered manually after the update. On the first login after the
installation, more information on this topic will be displayed, along
with the option to trigger the rebuild. It's safe to ignore this message
until it vanishes by itself.

![](/images/kb/28575350/55247634.png)

  

You may also encounter an issue with Metabase dashboards after the first
login (see image below). Simply logging out (not just closing the
browser) and in again will resolve this issue.

![](/images/kb/28575350/55247637.png)

  

  

[Go to the current iDNA Applications Release
Notes](/kb/release-notes/)[.](https://www.panagenda.com/kbase/display/AI/Release+Notes+v1.6.0)
