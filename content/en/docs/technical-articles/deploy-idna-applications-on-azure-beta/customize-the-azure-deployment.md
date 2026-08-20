---
title: "Customize the Azure Deployment"
weight: 11
date: 2020-06-08
source_confluence_id: 28578120
draft: false
---
You can customize your deployment by editing the `vars.tf` file.

<table>
<thead>
<tr class="header">
<th>Variables</th>
<th>Default value</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>prefix</td>
<td>panaifa<br />
</td>
<td>Prefix used for different resources</td>
</tr>
<tr class="even">
<td>resource_group_name</td>
<td>pana-ifa-rg<br />
</td>
<td>Resource Group name</td>
</tr>
<tr class="odd">
<td>vm_size</td>
<td>Standard_B2ms</td>
<td><a
href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-general">VM
size</a></td>
</tr>
<tr class="even">
<td>data_disk</td>
<td>100</td>
<td>size of the data disk (GB)</td>
</tr>
<tr class="odd">
<td>location</td>
<td>westeurope</td>
<td>Resource Location</td>
</tr>
<tr class="even">
<td>source_address_prefixes</td>
<td>-</td>
<td>External IPs allowed to access iDNA Applications</td>
</tr>
<tr class="odd">
<td>rg</td>
<td>-</td>
<td>Resource Group of an existing VNet</td>
</tr>
<tr class="even">
<td>vnet</td>
<td>-</td>
<td>Name of an existing VNet</td>
</tr>
<tr class="odd">
<td>subnet</td>
<td>-</td>
<td>Subnet name of an existing VNet</td>
</tr>
<tr class="even">
<td>ip</td>
<td>-</td>
<td>IP of an existing VNet</td>
</tr>
</tbody>
</table>

Everything related to the Azure Vault and Storage Account for Terraform
can be customized in `prep.sh`.
