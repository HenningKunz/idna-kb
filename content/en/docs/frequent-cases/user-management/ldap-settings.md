---
title: "LDAP Settings"
weight: 40
date: 2021-01-26
source_confluence_id: 28576203
draft: false
---
In addition to the internal user management, existing corporate LDAP
directories can be integrated in iDNA Applications.

This article explains how to configure the integration with an Active
Directory and Domino LDAP.

{{% callout type="info" %}}

Please note that the default iDNA Applications user accounts (e.g.
Config) remain active and are valid parallel to all LDAP objects.

{{% /callout %}}

## Active Directory

- Click on S*ettings - LDAP Settings  
  *

![](/images/kb/28576203/28576210.png)

- LDAP Settings

![](/images/kb/28576203/28576239.png)

**LDAP security:** Select unsecure (ldap://) or secure (ldaps://),
depending on your environment

**LDAP host:** Enter the directory URL

**LDAP port**: Type in the server port

**Bind DN**: Enter the canonical name of the bind user

Example: 
CN=\_bindusername,OU=Functional,OU=Users,OU=acme,DC=acme,DC=local

**IMPORTANT**:  The  binduser has to see at least one of the following
member attributes:  memberOf, isMember, member

**Bind DN Password:** Enter the password of the bind user account

**User Search Base**: Enter the Search Base where the User Objects are
located

**User Filter:** For Active Directory please enter the following string:

sAMAccountName={{username}}

**Role Mapping** (Administrators - Monitoring- Viewer)

Assign an AD Group to the respective role

Example:  Office365Admins is an AD group with certain members (all these
members would gain administrator access to iDNA Applications)

**IMPORTANT**:

- - - If a user is member of an Administrator group and Viewer group,
      then the User gets the higher permission → Administrator
    - If a user which is NOT member of any assigned group, tries to
      login, the user will not be able to login.

  

## Domino LDAP

- LDAP Settings

![](/images/kb/28576203/28576240.png)

**LDAP security:** Select unsecure (ldap://) or secure (ldaps://),
depending on your environment

**LDAP host:** Enter the directory URL

**LDAP port**: Type in the server port

**Bind DN**: Enter the canonical name of the bind user

Example: 
CN=\_bindusername,OU=Functional,OU=Users,OU=acme,DC=acme,DC=local

**IMPORTANT**:  The  bind user has to see the attribute: 
dominoaccessgroups

**Bind DN Password:** Enter the password of the bind user account

**User Search Base**: Enter the Search Base where the user objects are
located

**User Filter:** for Domino LDAP please enter the following string:

cn={{username}}

**Role Mapping** (Administrators - Monitoring- Viewer)

Assign a Domino group to the respective role

Example:  DominoAdmins is a Domino group with certain members (all these
members would gain administrator access to iDNA Applications)

**IMPORTANT**:

- - - If a user is member of an Administrator group and Viewer group,
      then the User gets the higher permission → Administrator
    - If a user which is NOT member of any assigned group, tries to
      login, the user will not be able to login.
