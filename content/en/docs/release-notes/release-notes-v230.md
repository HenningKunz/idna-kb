---
title: "Release Notes v2.3.0"
weight: 101
date: 2022-10-21
source_confluence_id: 64618836
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is mainly a
maintenance release, but brings a lot of value with new features,
improvements and bug fixes.

  

  

  

## **New Features **

  

**Analytics Interface:** Three new tables have been added to the
publicly available data interface used in DataMiner and Metabase. These
provide important data sets that have been requested many times by our
customers:

- Condensed Replica Set List: limited to the most essential columns with
  verbose column names
  - Metabase: *Replica Set Abbreviated*
  - DataMiner: *cqx_data.replica_set_abbreviated  
    *
- User List with Activity: enriched with department, location and summed
  up usage data for different time periods (30 days, 90 days, all
  recorded history)
  - Metabase: *Person Activity Summary*
  - DataMiner: *cqx_data.person_activity_summary*

<!-- -->

- Activity on Replica Set by User: summarized activity per user and time
  period for every database
  - Metabase: *Repset Activity Summary Per User*
  - DataMiner: *cqx_data.repset_activity_summary_per_user  
    *  
    ![](/images/kb/64618836/64618870.png)

  

Together, these statements are the perfect combination to be used as a
data source for an external analysis by e.g. Power BI, Excel or Tableau.

  

  

## **Improvements**

  

**Code Search:** There is now a better visual indicator of which code
block is currently selected.  
  

**Department Usage:** We have improved the way department names are
displayed if hierarchical department structures are supplied. Instead of
the full name (e.g. Acme/Europe/Vienna) which may be too long to
comfortably read in many situations, the short form (e.g. Vienna) is now
used as default display method. For non-hierarchical org structures,
nothing has changed.  
  

**Design Collection:** The process of connecting to Domino servers has
been improved in situations where name resolution is not properly
configured. The occurrence of Notes errors 2055 previously seen in these
situations should drastically reduce.  
  

**Domlog Collection:** it is now possible to provide a custom cacerts
file so the Domlog web collector does not encounter issues when trying
to access self-certified web hosts.

  

  

## **Bug Fixes **

  

**Appliance Hardening:** an issue has been resolved that would lead to
the sshd config file being overwritten with default values on container
rebuild.

  

  

## **Structural Changes / Upgrade Path**

  

### **Upgrade Procedure: Container Installer**

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](https://www.panagenda.com/kbase/display/IA/Upgrading+iDNA+Applications).

  

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  

  

  

  

  

  
