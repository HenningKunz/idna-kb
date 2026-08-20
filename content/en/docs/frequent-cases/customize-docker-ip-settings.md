---
title: "Customize Docker IP Settings"
weight: 27
date: 2024-06-24
source_confluence_id: 28574360
draft: false
---
panagenda iDNA Applications uses the following Docker networks per
default:

  

**Bridge (Docker internal)**

- IP segment: 192.168.237.0/24

**panagenda Network (Docker internal)**

- IP segment: 192.168.238.0/24

## Customization

To change the default settings, please create an
"*/opt/panagenda/appdata/ifa/config*" file with the following content
(adapt the IP segments as required):

``` text
# defines the default Docker bridge ip segment
PANAGENDA_DOCKER_BRIDGE=172.30.0.1/16
# defines the panagenda Docker network ip segment
PANAGENDA_COMPOSE_NETWORK_SUBNET=172.31.0.0/16
```

  

Afterwards execute the following command:

``` text
ifa customize
```

  

  

{{% callout type="info" %}}

Please note: If you adapt the IP segments in the DEFAULT
*/opt/panagenda/appdata/ifa/config.default* file, your customization
will be overwritten with any iDNA Applications upgrade.

{{% /callout %}}

