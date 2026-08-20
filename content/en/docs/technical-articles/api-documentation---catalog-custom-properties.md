---
title: "API Documentation - Catalog & Custom Properties"
weight: 3
date: 2020-07-02
source_confluence_id: 28578201
draft: false
---
From verison 2.x on, iDNA Applications provides an external API for the
following scenarios:

- With the API you can extract database and replica set information
  collected by iDNA Applications to use it in other applications
- With the API you can assign or update custom properties to databases
  or replica sets so that you can use them within iDNA Applications.

  

## Postman

[![](download/resources/com.atlassian.confluence.plugins.confluence-view-file-macro:view-file-macro-resources/images/placeholder-medium-file.png)IFA
API.postman_collection.json](/kbase/download/attachments/28578201/IFA%20API.postman_collection.json?version=1&modificationDate=1591699244686&api=v2)

Use the Postman collection to test the API calls.

{{% callout type="info" %}}

**Note that you have to set the host variable in the postman (under
settings → manage environments).**

{{% /callout %}}

**The authorization headers in the postman collection are configured to
use the *mdapi* user with the password *mdapi*. Either you will have to
create a user with this username / password combination as described in
the next section, or you will have to update it based on your existing
user.**

  
The external API is located under
<u>https:/\<IFA_host_name\>/api/external/xxx</u>

<u>  
</u>

### Authorization

A user is required which can be created
under <u>https:/\<IFA_host_name\>/idna/sys/accounts</u>

<u>![](/images/kb/28578201/28578208.png)</u>

{{% callout type="info" %}}

**Please note that you have to select "API" from the Authority drop down
list.**

{{% /callout %}}

<u>  
</u>

In order to use the API an authorization header needs to be sent. We are
using Basic Authentication, so the header should look like this:

Authorization: Basic base64encode (username:password)

if your credentials are for example user:password, then the header
should be:

- Authorization: Basic dXNlcjpwYXNzd29yZA==

  
the API returns 401 if

- No Authorization header is provided
- User credentials are wrong
- User Authority is insufficient

  

### Database Instances

<table>
<tbody>
<tr class="header">
<th>Description</th>
<th>URL</th>
<th>Payload</th>
<th>Response</th>
<th>Response Json</th>
</tr>
&#10;<tr class="odd">
<td>Get a list of all databases</td>
<td><p>GET {{host}}/api/external/databases</p>
<p><br />
</p>
<p><strong>Parameters:</strong></p>
<p><em>focus</em> - boolean: filter focus databases</p>
<p>e.g.: {{host}}/api/external/databases?focus=true</p>
<p><br />
</p></td>
<td><p>-</p></td>
<td>Returns an array of database objects with basic information.</td>
<td><pre class="text"><code>[
    {
        &quot;res_id&quot;: 469,
        &quot;server_name&quot;: &quot;server/panagenda&quot;,
        &quot;file_name&quot;: &quot;test/testlog.nsf&quot;,
        &quot;title&quot;: &quot;iDNAlog&quot;,
        &quot;replicaid&quot;: &quot;C1245D0E15534F18&quot;,
        &quot;database_type&quot;: &quot;Application&quot;,
        &quot;size_bytes&quot;: &quot;1290240&quot;,
        &quot;is_focus_db&quot;: true
    }
]</code></pre></td>
</tr>
<tr class="even">
<td>Get a list of all databases with custom properties</td>
<td><p>GET {{host}}/api/external/databases/all/customProperties</p>
<p><br />
</p>
<p><strong>Parameters:</strong></p>
<p><em>resIds</em> - string: comma separated list of res_id values that
can be used to select specific databases</p>
<p><br />
</p>
<p>e.g.: {{host}}/api/external/databases/all/customProperties?resIds=402,403,404</p></td>
<td>-</td>
<td>Returns an array of database objects with custom properties</td>
<td><pre class="text"><code>{
        &quot;res_id&quot;: 330,
        &quot;customProperties&quot;: {
            &quot;ts&quot;: &quot;2020-06-03T21:06:14.217848+00:00&quot;,
            &quot;source&quot;: &quot;web&quot;,
            &quot;values&quot;: {
                &quot;1001001&quot;: &quot;Dormant&quot;,
                &quot;1001002&quot;: &quot;Cher&quot;,
                &quot;1001003&quot;: &quot;classification&quot;,
                &quot;1001004&quot;: &quot;Yes&quot;,
                &quot;1001005&quot;: &quot;Low&quot;,
                &quot;1001006&quot;: &quot;435&quot;,
                &quot;1001008&quot;: &quot;Development&quot;,
                &quot;1001009&quot;: &quot;user@panagenda.com&quot;,
                &quot;1001010&quot;: &quot;developer@panagenda.com&quot;,
                &quot;1001011&quot;: &quot;known interfaces&quot;,
                &quot;1001012&quot;: &quot;Mars&quot;,
                &quot;1001013&quot;: &quot;www.google.com&quot;,
                &quot;1001014&quot;: 1593180000000,
                &quot;1001020&quot;: &quot;comment&quot;
            },
            &quot;comment&quot;: null,
            &quot;modifier&quot;: &quot;config&quot;
        }
    },</code></pre></td>
</tr>
<tr class="odd">
<td>Get a list of all databases with detailed information</td>
<td><p>GET {{host}}/api/external/databases/all/details</p>
<p><br />
</p>
<p><strong>Parameters</strong>:</p>
<p><em>resIds</em> - string: comma separated list of res_id values that
can be used to select specific databases</p>
<p><br />
</p>
<p>e.g.: {{host}}/api/external/databases/all/details?resIds=402,403,404</p></td>
<td>-</td>
<td>Returns an array of database objects with detailed
information (including custom properties)</td>
<td><pre class="text"><code> {
        &quot;usage&quot;: null,
        &quot;views&quot;: null,
        &quot;design&quot;: null,
        &quot;res_id&quot;: 402,
        &quot;catalog&quot;: {
            &quot;id&quot;: 402,
            &quot;size&quot;: 3932160,
            &quot;type&quot;: 0,
            &quot;title&quot;: &quot;Domino Change Control (6)&quot;,
            &quot;server&quot;: {
                &quot;node_id&quot;: 6,
                &quot;hostname&quot;: &quot;test.somedomain.com&quot;,
                &quot;data_path&quot;: &quot;D:/Domino/Data&quot;,
                &quot;exec_path&quot;: &quot;C:/Domino/Server/&quot;,
                &quot;server_os&quot;: &quot;Windows/2003 5.2 Intel Pentium&quot;,
                &quot;servername&quot;: &quot;server/panagenda&quot;,
                &quot;clustername&quot;: null,
                &quot;server_tags&quot;: [
                    &quot;panagenda&quot;
                ],
                &quot;domino_version&quot;: &quot;Release 8.5.3FP6 HF646&quot;,
                &quot;collection_active&quot;: true,
                &quot;domino_buildnumber&quot;: &quot;390&quot;,
                &quot;max_collection_date&quot;: &quot;2020-05-11&quot;,
                &quot;min_collection_date&quot;: &quot;2016-06-12&quot;,
                &quot;server_architecture&quot;: &quot;32 Bit&quot;,
                &quot;tasks_running_count&quot;: 15,
                &quot;server_access_status&quot;: 0
            },
            &quot;created&quot;: 1089210821000,
            &quot;size_mb&quot;: 3.8,
            &quot;filename&quot;: &quot;filename.ntf&quot;,
            &quot;licensed&quot;: true,
            &quot;modified&quot;: 1591521362406.52,
            &quot;best_type&quot;: null,
            &quot;replicaid&quot;: &quot;85256AE30062503A&quot;,
            &quot;sizequota&quot;: 0,
            &quot;act_period&quot;: 3009,
            &quot;categories&quot;: null,
            &quot;in_catalog&quot;: true,
            &quot;odsversion&quot;: null,
            &quot;volumename&quot;: &quot;D&quot;,
            &quot;act_dayuses&quot;: 0,
            &quot;is_focus_db&quot;: false,
            &quot;percentused&quot;: 0,
            &quot;sizewarning&quot;: 0,
            &quot;storagepath&quot;: &quot;D:\\Domino\\Data\\filename.ntf&quot;,
            &quot;act_dayreads&quot;: 0,
            &quot;act_weekuses&quot;: 0,
            &quot;created_date&quot;: &quot;2004-07-07&quot;,
            &quot;lastmodified&quot;: 1588998889000,
            &quot;templatename&quot;: &quot;DominoChangeControl&quot;,
            &quot;act_daywrites&quot;: 0,
            &quot;act_monthuses&quot;: 1,
            &quot;act_weekreads&quot;: 0,
            &quot;documentcount&quot;: 78,
            &quot;acl_adminnames&quot;: false,
            &quot;act_monthreads&quot;: 0,
            &quot;act_perioduses&quot;: 80,
            &quot;act_weekwrites&quot;: 0,
            &quot;count_replicas&quot;: 13,
            &quot;filename_lower&quot;: &quot;domchange.ntf&quot;,
            &quot;in_dbdirectory&quot;: true,
            &quot;server_node_id&quot;: 6,
            &quot;type_on_server&quot;: 300,
            &quot;act_monthwrites&quot;: 14,
            &quot;act_periodreads&quot;: 0,
            &quot;design_modified&quot;: 1397774744000,
            &quot;fulltextindexed&quot;: false,
            &quot;identified_type&quot;: 300,
            &quot;listindbcatalog&quot;: true,
            &quot;acl_author_count&quot;: 0,
            &quot;acl_editor_count&quot;: 0,
            &quot;acl_reader_count&quot;: 1,
            &quot;act_periodwrites&quot;: 1082,
            &quot;cat_doc_modified&quot;: 1591140117000,
            &quot;created_datetime&quot;: &quot;2004-07-07T14:33:41+00:00&quot;,
            &quot;idna_instance_id&quot;: 6699374546818320000,
            &quot;log_doc_modified&quot;: 1591498842000,
            &quot;acl_manager_count&quot;: 4,
            &quot;inmultidbindexing&quot;: false,
            &quot;acl_designer_count&quot;: 0,
            &quot;acl_noaccess_count&quot;: 5,
            &quot;designtemplatename&quot;: null,
            &quot;acl_depositor_count&quot;: 0,
            &quot;design_num_documents&quot;: 182,
            &quot;replication_disabled&quot;: false,
            &quot;replication_priority&quot;: 2,
            &quot;is_template_candidate&quot;: true,
            &quot;acl_defaultaccesslevel&quot;: 2,
            &quot;db_usage_history_start&quot;: null,
            &quot;db_usage_history_until&quot;: null,
            &quot;idna_domino_catalog_id&quot;: 7862820,
            &quot;design_collection_state&quot;: &quot;Not Collected&quot;,
            &quot;acl_administrationserver&quot;: null,
            &quot;acl_anonymousaccesslevel&quot;: 0,
            &quot;best_type_server_node_id&quot;: null,
            &quot;created_catalog_datetime&quot;: &quot;2004-07-07T14:33:41+00:00&quot;,
            &quot;replication_cutoffdelete&quot;: false,
            &quot;replication_ignoredeletes&quot;: true,
            &quot;db_usage_history_available&quot;: false,
            &quot;replication_cutoffinterval&quot;: 0,
            &quot;server_max_collection_date&quot;: &quot;2020-05-11&quot;,
            &quot;server_min_collection_date&quot;: &quot;2016-06-12&quot;,
            &quot;replication_receivesummaries&quot;: false,
            &quot;replication_sendtitleandcatalog&quot;: true,
            &quot;desgin_minimum_addedtofile_datetime&quot;: null,
            &quot;usage_collection_log_sessions_start&quot;: 1465689600000,
            &quot;usage_collection_log_sessions_until&quot;: 1589155200000
        },
        &quot;insights&quot;: null,
        &quot;similarity&quot;: null,
        &quot;customProperties&quot;: {
            &quot;ts&quot;: &quot;2020-06-08T07:47:05.162921+00:00&quot;,
            &quot;source&quot;: &quot;external-api&quot;,
            &quot;values&quot;: {
                &quot;1001004&quot;: &quot;Yes&quot;,
                &quot;1001005&quot;: &quot;Very High&quot;,
                &quot;1001009&quot;: &quot;NodeJs&quot;
            },
            &quot;comment&quot;: null,
            &quot;modifier&quot;: null
        }
    }</code></pre></td>
</tr>
</tbody>
</table>

### ReplicaSets

<table>
<tbody>
<tr class="header">
<th>Description</th>
<th>URL</th>
<th>Payload</th>
<th>Response</th>
<th>Response Json</th>
</tr>
&#10;<tr class="odd">
<td>Get a list of all replica sets</td>
<td><p>GET {{host}}/api/external/replicaSets</p>
<p><br />
</p>
<p><strong>Parameters:</strong></p>
<p><em>focus</em> - boolean: filter focus databases</p>
<p>e.g.: {{host}}/api/external/replicaSets?focus=true</p>
<p><br />
</p></td>
<td>-</td>
<td>Returns an array of replica set objects with basic information</td>
<td><pre class="text"><code>[
    {
        &quot;replicaid&quot;: &quot;C14576C5113CCE73&quot;,
        &quot;title&quot;: &quot;&quot;,
        &quot;server_names&quot;: [
            &quot;server/panagenda&quot;
        ],
        &quot;replicas_count&quot;: 1,
        &quot;db_type_name&quot;: &quot;System Database&quot;,
        &quot;is_focus_db&quot;: false
    }
]</code></pre></td>
</tr>
<tr class="even">
<td>Get a list of all replica sets with custom properties</td>
<td><p>GET {{host}}/api/external/replicaSets/all/customProperties</p>
<p><br />
</p>
<p><strong>Parameters:</strong></p>
<p>replicaIds- string: comma separated list of replicaid values that can
be used to select specific replica sets</p>
<p><br />
</p>
<p>e.g.: {{host}}/api/external/databases/all/customProperties?replicaIds=C2357E4B127EDE78,C23579AE0125A4B3,C2258814004555A9</p></td>
<td>-</td>
<td>Returns an array of replica set objects with custom properties</td>
<td><pre class="text"><code>[
    {
        &quot;replicaid&quot;: &quot;C14576C5113CCE73&quot;,
        &quot;customProperties&quot;: {
            &quot;ts&quot;: &quot;2020-06-08T10:01:39.29916+00:00&quot;,
            &quot;values&quot;: {
                &quot;1002009&quot;: &quot;Very High&quot;,
                &quot;1002012&quot;: &quot;NodeJS&quot;
            },
            &quot;comment&quot;: null,
            &quot;modifier&quot;: null,
            &quot;resource&quot;: &quot;external-api&quot;
        }
    }
]</code></pre></td>
</tr>
<tr class="odd">
<td>Get a list of all replica sets with detailed information</td>
<td><p>GET {{host}}/api/external/replicaSets/all/details</p>
<p><br />
</p>
<p><strong>Parameters:</strong></p>
<p>replicaIds- string: comma separated list of replicaid values that can
be used to select specific replica sets</p>
<p><br />
</p>
<p>e.g.: {{host}}/api/external/databases/all/details?replicaIds=C2357E4B127EDE78,C23579AE0125A4B3,C2258814004555A9</p></td>
<td>-</td>
<td>Returns an array of replica set objects with detailed information
(including custom properties)</td>
<td><pre class="text"><code>[
    {
        &quot;title&quot;: &quot;&quot;,
        &quot;replicaid&quot;: &quot;C14576C5113CCE73&quot;,
        &quot;db_type_id&quot;: 300,
        &quot;db_type_name&quot;: &quot;System Database&quot;,
        &quot;is_focus_db&quot;: false,
        &quot;design_collection_status&quot;: &quot;Not Collected&quot;,
        &quot;design_collection_status_detail&quot;: &quot;Not Collected&quot;,
        &quot;replicas_count&quot;: 1,
        &quot;replicas_encrypted_count&quot;: 0,
        &quot;server_names&quot;: [
            &quot;server/panagenda&quot;
        ],
        &quot;replica_paths&quot;: [
            &quot;server/panagenda!!filename.nsf&quot;
        ],
        &quot;server_adminserver&quot;: null,
        &quot;categories&quot;: null,
        &quot;application_created_date&quot;: &quot;2010-04-29&quot;,
        &quot;application_lastmodified_date&quot;: &quot;2020-06-06&quot;,
        &quot;db_usage_history_start_date&quot;: null,
        &quot;usage_collection_log_sessions_start_date&quot;: &quot;2017-03-08&quot;,
        &quot;usage_collection_log_sessions_until_date&quot;: &quot;2020-05-29&quot;,
        &quot;last_accessed&quot;: null,
        &quot;last_accessed_user&quot;: null,
        &quot;last_accessed_on_server&quot;: null,
        &quot;last_write_access&quot;: null,
        &quot;last_write_user&quot;: null,
        &quot;usage_category_simplified&quot;: &quot;No / Low&quot;,
        &quot;usage_display_index&quot;: 0,
        &quot;usage_all_time&quot;: &quot;No Usage&quot;,
        &quot;user_access_days_all_time&quot;: 0,
        &quot;users_active_all_time&quot;: 0,
        &quot;days_active_all_time&quot;: 0,
        &quot;sessions_all_time&quot;: 0,
        &quot;sessions_web_all_time&quot;: 0,
        &quot;sessions_write_all_time&quot;: 0,
        &quot;usage_last365d&quot;: &quot;No Usage&quot;,
        &quot;user_access_days_last365d&quot;: 0,
        &quot;users_active_last365d&quot;: 0,
        &quot;days_active_last365d&quot;: 0,
        &quot;sessions_last365d&quot;: 0,
        &quot;sessions_web_last365d&quot;: 0,
        &quot;sessions_write_last365d&quot;: 0,
        &quot;usage_last90d&quot;: &quot;No Usage&quot;,
        &quot;user_access_days_last90d&quot;: 0,
        &quot;users_active_last90d&quot;: 0,
        &quot;days_active_last90d&quot;: 0,
        &quot;sessions_last90d&quot;: 0,
        &quot;sessions_web_last90d&quot;: 0,
        &quot;sessions_write_last90d&quot;: 0,
        &quot;usage_last30d&quot;: &quot;No Usage&quot;,
        &quot;user_access_days_last30d&quot;: 0,
        &quot;users_active_last30d&quot;: 0,
        &quot;days_active_last30d&quot;: 0,
        &quot;sessions_last30d&quot;: 0,
        &quot;sessions_web_last30d&quot;: 0,
        &quot;sessions_write_last30d&quot;: 0,
        &quot;usage_last7d&quot;: &quot;No Usage&quot;,
        &quot;user_access_days_last7d&quot;: 0,
        &quot;users_active_last7d&quot;: 0,
        &quot;days_active_last7d&quot;: 0,
        &quot;sessions_last7d&quot;: 0,
        &quot;sessions_web_last7d&quot;: 0,
        &quot;sessions_write_last7d&quot;: 0,
        &quot;documents_count_min&quot;: 48,
        &quot;documents_count_avg&quot;: 48,
        &quot;documents_count_max&quot;: 48,
        &quot;size_mb_min&quot;: 67,
        &quot;size_mb_avg&quot;: 67.5,
        &quot;size_mb_max&quot;: 67,
        &quot;design_complexity&quot;: &quot;Not Analyzed&quot;,
        &quot;design_complexity_simplified&quot;: &quot;Not Analyzed&quot;,
        &quot;design_complexity_score&quot;: null,
        &quot;design_complexity_display_index&quot;: 0,
        &quot;design_insights_score&quot;: null,
        &quot;is_template_candidate&quot;: false,
        &quot;templates_inherits_from_count&quot;: 1,
        &quot;templates_inherits_from&quot;: [
            &quot;StdR85Mail&quot;
        ],
        &quot;templates_acts_as_master_count&quot;: 0,
        &quot;templates_acts_as_master&quot;: null,
        &quot;remediation_classification&quot;: null,
        &quot;remediation_display_index&quot;: null,
        &quot;design_consistency&quot;: &quot;OK&quot;,
        &quot;design_age_difference_hours&quot;: 0,
        &quot;design_modified_newest_design&quot;: &quot;2015-11-10T00:00:57+00:00&quot;,
        &quot;design_modified_oldest_design&quot;: &quot;2015-11-10T00:00:57+00:00&quot;,
        &quot;database_id_newest_design&quot;: 72,
        &quot;replica_newest_design&quot;: &quot;server/panagenda!!filename.nsf&quot;,
        &quot;database_id_oldest_design&quot;: 72,
        &quot;replica_oldest_design&quot;: &quot;server/panagenda!!filename.nsf&quot;,
        &quot;most_similar_template_name_newest_design&quot;: null,
        &quot;most_similar_template_similarity_newest_design&quot;: null,
        &quot;most_similar_template_name_oldest_design&quot;: null,
        &quot;most_similar_template_similarity_oldest_design&quot;: null,
        &quot;design_is_similar_to_standard_template&quot;: null,
        &quot;template_similarity_ranking_list&quot;: null,
        &quot;design_cluster_count&quot;: null,
        &quot;design_cluster_ids&quot;: null,
        &quot;database_id_design_reference&quot;: null,
        &quot;design_formula_elements&quot;: null,
        &quot;design_formula_loc&quot;: null,
        &quot;design_lotusscript_elements&quot;: null,
        &quot;design_lotusscript_loc&quot;: null,
        &quot;design_javascript_elements&quot;: null,
        &quot;design_javascript_loc&quot;: null,
        &quot;design_java_elements&quot;: null,
        &quot;design_java_loc&quot;: null,
        &quot;design_agents_elements&quot;: null,
        &quot;design_agents_loc&quot;: null,
        &quot;design_folders_elements&quot;: null,
        &quot;design_folders_loc&quot;: null,
        &quot;design_forms_elements&quot;: null,
        &quot;design_forms_loc&quot;: null,
        &quot;design_views_elements&quot;: null,
        &quot;design_views_loc&quot;: null,
        &quot;design_scriptlibraries_elements&quot;: null,
        &quot;design_scriptlibraries_loc&quot;: null,
        &quot;design_xpages_elements&quot;: null,
        &quot;design_xpages_customcontrols&quot;: null,
        &quot;mailin_names&quot;: null,
        &quot;customProperties&quot;: {
            &quot;ts&quot;: &quot;2020-06-08T10:01:39.29916+00:00&quot;,
            &quot;values&quot;: {
                &quot;1002009&quot;: &quot;Very High&quot;,
                &quot;1002012&quot;: &quot;NodeJS&quot;
            },
            &quot;comment&quot;: null,
            &quot;modifier&quot;: null,
            &quot;resource&quot;: &quot;external-api&quot;
        }
    }
]</code></pre></td>
</tr>
</tbody>
</table>

### Custom Properties

<table>
<tbody>
<tr class="header">
<th>Description</th>
<th>URL</th>
<th>Payload</th>
<th>Response</th>
<th>Response Json</th>
</tr>
&#10;<tr class="odd">
<td>Get all custom properties</td>
<td><p>GET {{host}}/api/external/customProperties</p>
<p><br />
</p>
<p><strong>Parameters</strong>:</p>
<p><em>type</em> - string: can be used to filter for database ('db') or
replica set ('rs') custom properties</p>
<p>e.g.: </p>
<p>{{host}}/api/external/customProperties?type=rs</p>
<p>{{host}}/api/external/customProperties?type=db</p></td>
<td>-</td>
<td>Returns an array of custom property objects</td>
<td><pre class="text"><code>[
    {
        &quot;type&quot;: &quot;db&quot;,
        &quot;id&quot;: 33,
        &quot;name&quot;: &quot;1241234&quot;,
        &quot;metadata_type&quot;: &quot;text&quot;,
        &quot;options&quot;: {
            &quot;values&quot;: []
        },
        &quot;created_by&quot;: &quot;config&quot;,
        &quot;description&quot;: null,
        &quot;custom&quot;: true,
        &quot;enabled&quot;: false
    },
    {
        &quot;type&quot;: &quot;rs&quot;,
        &quot;id&quot;: 1002004,
        &quot;name&quot;: &quot;VIP Attention&quot;,
        &quot;metadata_type&quot;: &quot;oneof&quot;,
        &quot;options&quot;: {
            &quot;values&quot;: [
                &quot;Yes&quot;,
                &quot;No&quot;
            ]
        },
        &quot;created_by&quot;: &quot;panagenda&quot;,
        &quot;description&quot;: null,
        &quot;custom&quot;: false,
        &quot;enabled&quot;: true
    }
]</code></pre></td>
</tr>
</tbody>
</table>

### Custom Property Assignments

<table>
<tbody>
<tr class="header">
<th>Description</th>
<th>URL</th>
<th>Payload</th>
<th>Response</th>
<th>Response Json</th>
</tr>
&#10;<tr class="odd">
<td>Assign x custom properties to y databases</td>
<td><p>POST {{host}}/api/external/customPropertyAssignment/database</p>
<p><br />
</p>
<p><strong>Headers</strong>:</p>
<p>Content-Type: application/json</p>
<p><br />
</p></td>
<td><pre class="text"><code>{
    &quot;targetIds&quot;: [402, 403, 404],
    &quot;customProperties&quot;: {
        &quot;1001009&quot;: &quot;NodeJs&quot;,
        &quot;1001005&quot;: &quot;Very High&quot;
    }
}</code></pre>
<p><em>targetIds</em> - comma separated list of database <em>res_id</em>
values</p>
<p><em>customProperties</em> - an object with key / value pairs of
custom property id and custom property value</p></td>
<td><p><em>updated - </em>An array of created / updated custom
properties</p>
<p><br />
</p>
<p>error - Contains error information. e.g. if certain targetIds does
not exist</p></td>
<td><pre class="text"><code>{
    &quot;updated&quot;: [
        {
            &quot;res_id&quot;: 402,
            &quot;customProperties&quot;: {
                &quot;ts&quot;: &quot;2020-06-08T13:20:05.541693+00:00&quot;,
                &quot;source&quot;: &quot;external-api&quot;,
                &quot;values&quot;: {
                    &quot;1001004&quot;: &quot;Yes&quot;,
                    &quot;1001005&quot;: &quot;Very High&quot;,
                    &quot;1001009&quot;: &quot;NodeJs&quot;
                },
                &quot;comment&quot;: null,
                &quot;modifier&quot;: null
            }
        },
        {
            &quot;res_id&quot;: 404,
            &quot;customProperties&quot;: {
                &quot;ts&quot;: &quot;2020-06-08T13:20:05.541693+00:00&quot;,
                &quot;source&quot;: &quot;external-api&quot;,
                &quot;values&quot;: {
                    &quot;1001004&quot;: &quot;Yes&quot;,
                    &quot;1001005&quot;: &quot;Very High&quot;,
                    &quot;1001009&quot;: &quot;NodeJs&quot;
                },
                &quot;comment&quot;: null,
                &quot;modifier&quot;: null
            }
        },
        {
            &quot;res_id&quot;: 403,
            &quot;customProperties&quot;: {
                &quot;ts&quot;: &quot;2020-06-08T13:20:05.541693+00:00&quot;,
                &quot;source&quot;: &quot;external-api&quot;,
                &quot;values&quot;: {
                    &quot;1001004&quot;: &quot;Yes&quot;,
                    &quot;1001005&quot;: &quot;Very High&quot;,
                    &quot;1001009&quot;: &quot;NodeJs&quot;
                },
                &quot;comment&quot;: null,
                &quot;modifier&quot;: null
            }
        }
    ],
    &quot;error&quot;: {
        &quot;message&quot;: &quot;The following resources were not updated because the ids does not exist&quot;,
        &quot;notUpdated&quot;: [
            9999
        ]
    }
}</code></pre></td>
</tr>
<tr class="even">
<td>Assign x custom properties to y replica sets</td>
<td><p>POST {{host}}/api/external/customPropertyAssignment/replicaSet</p>
<p><br />
</p>
<p><strong>Headers</strong>:</p>
<p>Content-Type: application/json</p></td>
<td><pre class="text"><code>{
    &quot;targetIds&quot;: [&quot;C2357E4B127EDE78&quot;, &quot;C23579AE0035A477&quot;, &quot;C2357714004455A9&quot;],
    &quot;customProperties&quot;: {
        &quot;1001009&quot;: &quot;NodeJs&quot;,
        &quot;1001005&quot;: &quot;Very High&quot;
    }
}</code></pre>
<p><em>targetIds</em> - comma separated list of replicaset
<em>replicaid</em> values</p>
<p><em>customProperties</em> - an object with key / value pairs of
custom property id and custom property value</p></td>
<td><p><em>updated - </em>An array of created / updated custom
properties</p>
<p><br />
</p>
<p>error - Contains error information. e.g. if certain targetIds does
not exist</p></td>
<td><pre class="text"><code>{
    &quot;updated&quot;: [
        {
            &quot;replicaid&quot;: &quot;C2357E4B127EDE78&quot;,
            &quot;customProperties&quot;: {
                &quot;ts&quot;: &quot;2020-06-08T13:24:37.128571+00:00&quot;,
                &quot;values&quot;: {
                    &quot;1002009&quot;: &quot;Very High&quot;,
                    &quot;1002012&quot;: &quot;NodeJS&quot;
                },
                &quot;comment&quot;: null,
                &quot;modifier&quot;: null,
                &quot;resource&quot;: &quot;external-api&quot;
            }
        },
        {
            &quot;replicaid&quot;: &quot;C23579AE0035A477&quot;,
            &quot;customProperties&quot;: {
                &quot;ts&quot;: &quot;2020-06-08T13:24:37.128571+00:00&quot;,
                &quot;values&quot;: {
                    &quot;1002009&quot;: &quot;Very High&quot;,
                    &quot;1002012&quot;: &quot;NodeJS&quot;
                },
                &quot;comment&quot;: null,
                &quot;modifier&quot;: null,
                &quot;resource&quot;: &quot;external-api&quot;
            }
        },
        {
            &quot;replicaid&quot;: &quot;C2357714004455A9&quot;,
            &quot;customProperties&quot;: {
                &quot;ts&quot;: &quot;2020-06-08T13:24:37.128571+00:00&quot;,
                &quot;values&quot;: {
                    &quot;1002009&quot;: &quot;Very High&quot;,
                    &quot;1002012&quot;: &quot;NodeJS&quot;
                },
                &quot;comment&quot;: null,
                &quot;modifier&quot;: null,
                &quot;resource&quot;: &quot;external-api&quot;
            }
        }
    ],
    &quot;error&quot;: {
        &quot;message&quot;: &quot;The following resources were not updated because the ids does not exist&quot;,
        &quot;notUpdated&quot;: [
            &quot;C1257E4B007EDEAA&quot;
        ]
    }
}</code></pre></td>
</tr>
</tbody>
</table>
