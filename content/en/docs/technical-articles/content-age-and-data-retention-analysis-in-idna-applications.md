---
title: "Content Age and Data Retention Analysis in iDNA Applications"
weight: 5
date: 2025-10-07
source_confluence_id: 119440769
draft: false
---
  

  

## **Overview**

  
Data retention analysis is a new feature in iDNA Applications version
3.3.0. It is the combination of collecting document age information from
databases and analyzing it based on data retention policies configured
for this database.

The obligation to retain data for varying periods of time is a legal
necessity in many industries and fields across the globe. Since
Notes/Domino applications have been an integral part of business
processes for companies of all industries over decades, this is a
critical topic for nearly any organization that aims to be compliant
with its legal requirements.  
  

Here is a brief excerpt of common retention periods by industry in the
European Union:

- Financial Services: 5–10 years (e.g., accounting records, transaction
  logs)
- Healthcare: 10–30 years (patient records, depending on country)
- Telecommunications: 6 months to 2 years (metadata, call logs—subject
  to national laws)
- Employment/HR: 2–10 years (contracts, payroll, disciplinary records)
- Tax Records: typically 7–10 years (subject to national laws)
- Construction & Real Estate: 10+ years (project documentation, safety
  records)

  

#### Example:

- Our database has approximately 141k documents which were last modified
  between 2009 and 2025.  
  (If no later modification occurred, the creation time of a document is
  the last modification time)  
    
- We set a retention policy of 4 years (starting at the current date),
  for which documents have to be retained  
    
- That results in a retention cutoff date of September 23, 2021
  (assuming the current date is September 23, 2025)  
  ![test](/images/kb/119440769/119440814.png)  
    
- Looking at that history, iDNA summarizes that approximately 115k of
  documents (~82%) are still within the retention period  
  ![](/images/kb/119440769/119440824.png)  
    
- Organizations benefit immediately by understanding which databases are
  ready for archiving right away. Applications where most documents are
  nearing the end of their retention period - even if not all are - may
  be suitable for read-only mode, ensuring no new edits "reset" the
  earliest archiving date.  
    
  On the flip side, an organization can gain insights quickly and
  transparently as to which applications are still active elements in
  their business processes from the content angle, rather than iDNA's
  usual user activity recording. This provides great value in scenarios
  where iDNA has been running for a shorter period of time and no
  extensive usage history is available. It also shows which applications
  may be a challenge when considering migration scenarios. Re-developing
  an existing application in a new target system is one thing; making
  sure a decade's worth of data is migrated flawlessly is quite another.
  The data must not only be accessible within the application but must
  also be available to other components of the business process without
  any loss of information.

 

## **Configuration**

  

### **Prerequisites**

  

- **License:** Content Age analysis is licensed as a separate module and
  not included in previous licenses. The new module can be purchased as
  an add-on for all currently active subscription licenses and new
  licenses.  
    
- **DB Access:** A minimum of Reader access is required on databases
  which should be analyzed.

  

### **Content Age Collection and Processing**

  

- **License:** Content Age data collection will only be performed if a
  valid license is found that includes the Content Age module.  
    
- **Initial Collection:** After the new license is applied, the initial
  content age collection will occur. We recommend restarting iDNA
  immediately after the license is uploaded using the command "ifa
  restart" via Putty.  
  *Note: databases that are in FAILED/CRASHED state due to previous
  collection errors will not be re-scanned at this time. A scan for
  those DBs must be performed manually (see bullet point
  "(Re-)Collection" below)*  
    
- **Default Schedule:** The content age collection is linked to the
  design analysis process. As such, periodic content age scans will
  adhere to the defined schedule for designs. The default and
  recommended setting for design updates is "Weekly, on Saturday", but
  may be different in your installation. Please check the menu item
  \[Settings\] → \[Database design re-scan options\] for details.  
    
- **Schedule Customization:** iDNA typically avoids accessing individual
  non-system DBs on a regular basis. That is why DB design is set by
  default to be re-scanned on weekends and then only changed since the
  last scan. Since this Content Age collection would connect to each
  Focus DB every week, we added a config parameter that allows
  specifying an interval in weeks that should pass between scans.  
    
  For example: setting the ETL parameter
  "ia_profile_rescan_interval_weeks" to "2" will basically mean "Only
  scan every second week on Saturday". ETL parameters can be configured
  in the admin interface (\[Settings\] → \[System configuration...\]) in
  the menu item \[Advanced Settings\] → \[ETL\] → \[ETL Properties\]
  (see paragraph "Setting up Periodic Collection" in our [Profile
  Documents
  Configuration](https://www.panagenda.com/kbase/pages/viewpage.action?pageId=119439707)
  knowledge base article for more details).  
    
  ![](/images/kb/119440769/119440905.png)  
    
- **(Re-)Collection** can be triggered manually for one or more
  databases via the menu item \[Settings\] → \[Design analysis
  status\].  
  *Note: if code analysis is licensed, using this option will also
  trigger a re-collection and re-processing of design data. This may
  take several days, depending on the number of databases to process.
  The regular scheduled scan on Saturday will only re-collect design
  data if changes in DB design occurred.*  
    
  ![](/images/kb/119440769/119440896.png)  
    
- **DB Scope:** Content Age information will be collected from all Focus
  DBs (database categories "Application" and "Mail-in DB"), excluding
  files with the NTF extension.  
    
- **Processing:** Before collected data is visible in iDNA's user
  interface, it needs to be processed by the nightly data warehouse
  update.

  

### **Retention Period Configuration**

  

To enable Retention Analysis for a database, the collected Content Age
data needs to be set in context with the Retention Period configuration.

  

Three factors are part of this configuration:

- **Retention Years (mandatory):** specifies how many years the data has
  to be retained
- **Retention Mode (mandatory):** defines how the retention start date
  is determined 
- Retention Manager (optional): the person responsible for determining
  the appropriate Retention Configuration

  

For the Retention Mode, several options are available:

- Simple Document Age (Years prior to current date)
- Start of Year: January (Years prior to selected month)
- Start of Year:  ...
- Start of Year: December (Years prior to selected month)

  
The "Start of Year: \<Month\>" options are intended to cover situations
where the fiscal year starts in a specific month. For example, if the
fiscal year starts in October (USA, Thailand, ...) or April (UK, India,
Canada, Japan).

  

Retention Configuration options are part of database configuration
parameters and can be set in two main ways:

- Database Catalog: multiple databases can be selected to configure
  settings  
    
  ![](/images/kb/119440769/119440877.png)

  

- Application Details → Custom DB Instance properties: open a single
  database via the Database Catalog  
    
  ![](/images/kb/119440769/119440878.png)

  

- Both options will show a similar input form where Retention
  Configuration for one or multiple DBs can be set  
  *Note: when setting properties for multiple DBs, a comment is
  mandatory when saving*  
    
  ![](/images/kb/119440769/119440879.png)

  

Once these settings are applied, a nightly processing run of iDNA's data
warehouse is necessary to combine content age data with the retention
settings.

  

Database properties can also be set programmatically. Please see the
knowledge base article [API Documentation - Catalog & Custom
Properties](/kb/api-documentation---catalog-custom-properties/) for
further details.

  

### **Summary (Example Scenario)**

  

- A new Content Age analysis license is applied on Wednesday and iDNA is
  restarted afterwards  
    
- Initial scan starts a few minutes (up to an hour) after the license is
  uploaded  
    
- Nightly processing from Wednesday to Thursday generates the first
  content age data, visible in the UI on Thursday  
    
- Retention config for the first half of the databases is configured on
  Thursday  
    
- Nightly processing from Thursday to Friday combines the two sets of
  data  
    
- Retention analysis for configured DBs is visible in the UI for the
  first time on Friday  
    
- Scheduled Content Age collection is automatically triggered on the
  following Saturday   
    
- Nightly processing on the weekend combines the two sets of data
  again  
    
- Retention config is added for another batch of DBs on Monday  
    
- Nightly processing from Monday to Tuesday combines the two sets of
  data again  
    
- On Tuesday morning, the UI displays updated information based on the
  most recent Retention Config changes

  

  

## **Evaluating Results**

  

### **Overview Dashboards**

  

Several dashboards regarding Content Age and Retention Analysis are
available in the left navigation bar below the category "Content":  
  

- The **"Retention Overview"** dashboard summarizes retention settings
  and shows how many documents for each Retention Mode are outside their
  retention period  
    
  ![](/images/kb/119440769/119440885.png)

  

- The **"Data Retention Analysis"** dashboard visually presents
  retention analysis insights  
    
  - Each bubble represents an Application
  - Display modes include showing DB Instances or grouping by Replica
    Set
  - Bubble size is determined by the number of documents in a database
  - x-axis is determined by usage: the further to the right a bubble is,
    the more used it is (time range for usage calculation is
    configurable)
  - y-axis is determined by content age: the higher up a bubble is, the
    older content of a DB is (determined by average document age)
  - Color is determined by the percentage of documents in retention  
      

![](/images/kb/119440769/119440886.png)

  

- The **"Retention Catalog"** is a somewhat simplified version of the
  database catalog. It is a tabular representation of the bubble chart
  and has similar options to group by Replica Set.  
  Filtering by "Collection Status" also provides a quick way to
  understand which databases may have issues with content scanning  
    
  ![](/images/kb/119440769/119440888.png)

  

  

### **Application Details**

  

A new tab, "Content Age" is available in Application Details for
databases where content age data was collected.  
  

![](/images/kb/119440769/119440894.png)

  

Detailed information on several topics can be found in four sub-tabs
here:  
  

- **Overview**: A summary of content retention analysis  
    
- **History:** Document modification and creation history  
    
- **Profile Documents:** Profile document modification and creation
  history  
    
- **DB Instances:** a summary table with content age KPIs on other DB
  instances of the same Replica Set

  

  

## **Licensing**

  

Content Age analysis is licensed as a separate module and not included
in previous licenses. The new module can be purchased as an add-on for
all currently active subscription licenses and new licenses.

  

  

  
