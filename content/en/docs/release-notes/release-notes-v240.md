---
title: "Release Notes v2.4.0"
weight: 99
date: 2023-12-06
source_confluence_id: 103546979
draft: false
---
panagenda is proud to announce this new release of iDNA Applications.
Whether you’re in a Notes/Domino modernization or migration project,
iDNA gives you the knowledge to deliver the most difficult projects
efficiently, on time and on budget. This new version is a mix of new
features and maintenance tasks.

  

  

## **New Features **

  

**User Licensing Optimization Dashboard**

This new feature integrates data from [HCL's Domino License Analysis
Utility
(DLAU)](https://opensource.hcltechsw.com/domino-license-analysis-utility-DLAU/)
and identifies licensing optimization candidates, based on the licensing
requirements DLAU calculates. If certain criteria in activity or
security settings are matched, iDNA points out which actions are
necessary to remove the user's ability to access Domino servers (aka
[Authorization](https://opensource.hcltechsw.com/domino-license-analysis-utility-DLAU/results/#authorized-users)).
By doing so, we help you to find inactive users that may be restricted
even more thoroughly, so DLAU no longer counts them as users who require
a license.

  

- Recognize users who might not require a license after all, as
  optimization candidates

![](/images/kb/103546979/103546978.png)

  

- Learn about necessary actions to remove user license requirement from
  optimization candidates  
  ![](/images/kb/103546979/103546986.png)

  

  

## **Improvements**

  

**Nightly Processing:** The nightly data warehouse update process has
been optimized to reduce runtime.  
  

**Agent Overview Dashboard:** It is now possible to filter the agent
list by signer without opening the dashboard in Metabase.  
  

**Metabase:** Metabase has been upgraded to the latest major version.
This brings a variety of security, usability and overall visual
improvements.

  

**Profile Documents:** Several improvements were made during collection
and processing of profile documents.

  

  

## **Bug Fixes**

  

**Nightly Processing:** A bug has been fixed that could lead to a
database constraint violation in rare situations.

  

  

## **Structural Changes / Upgrade Path**

  

### **Upgrade Procedure: Container Installer**

Details on how to update to this new version can be found in the
knowledge base article [Upgrading iDNA
Applications](https://www.panagenda.com/kbase/display/IA/Upgrading+iDNA+Applications).

  

  

  

  

***[Visit our site to start your evaluation right
now!](https://www.panagenda.com/products/idna/)***

  

  

  

  

  

  
