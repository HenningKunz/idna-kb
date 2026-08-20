---
title: "Metabase Default Users"
weight: 41
date: 2019-07-08
source_confluence_id: 28574593
draft: false
---
panagenda iDNA Applications is delivered with two default Metabase
users:

- **Admin: ***admin@metabase.local* (password: *config*)  
  User rights: 
  - Create, edit, delete Metabase contents (Questions and Dashboards)
  - Publish and embed newly created Metabase contents into iDNA
    Applications
  - Change Metabase settings  
      
- **User: ***user@metabase.local *(password: *metabase*)
  - Create, edit, delete Metabase contents (Questions and Dashboards)

  

{{% callout type="warning" %}}

It is highly recommended to change the passwords for both default
Metabase users.

{{% /callout %}}

  

{{% callout type="warning" %}}

**It is also highly recommended NOT to change Metabase contents within
the "panagenda" Collection. All changes will be lost after
updating/upgrading the iDNA Applications appliance.  
If you want to use panagenda default contents (from the "panagenda"
Collection) as a starting point for your own Questions or Dashboards,
please duplicate them and save them to the "Custom content" Collection
in Metabase.**

{{% /callout %}}

