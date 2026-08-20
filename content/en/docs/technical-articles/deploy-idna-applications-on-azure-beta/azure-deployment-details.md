---
title: "Azure Deployment Details"
weight: 9
date: 2020-06-08
source_confluence_id: 28578118
draft: false
---
### prep.sh

iDNA Applications itself will be deployed using Terraform. This script
will deploy everything needed to run Terraform.

- Resource Group (pana-ifa-tf-rg)
- Storage Account which is used to store the Terraform statefile in a
  Blob Storage Container
- Vault to store all IDs and secrets for later use
- A Service Principal Terraform runs with

### up.sh

This will run the Terraform project to deploy everything related to iDNA
Applications. Depening on your configuration (var.tf) the Appliance will
be deployed either into an existing Azure virtual network or will create
a new one including a public IP.

- Storage Account to store Virtual Machine template in a Blob Storage
  Account
- Virtual Machine
- Disk
- Virtual Network Interface
- Network Interface (public IP only)
- Network Security Group (public IP only)

### config.sh

{{% callout type="info" %}}

The script will create a temporal Azure Security Group rule that allows
SSH connection from the Azure Shell to your appliance!

{{% /callout %}}

  
This Script does all the necessary steps which are mentioned
under Starting the Virtual Appliance in the Setup Guide - please refer
to this chapter for further information on how to configure the
Appliance manually.

- Sets Hostname and timezone
  ([Timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones))
- Sets a new root password
- Configures and starts iDNA Applications

example:
`./config.sh "{FQDN of iDNA Applications}" "{TimeZone}" "{new root password}"`

Execute `./config.sh "my-ia.my-domain.com" "Europe/Berlin" "my-root-password"`
