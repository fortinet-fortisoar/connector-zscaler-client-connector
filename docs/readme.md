## About the connector
Zscaler Client Connector™ is a lightweight agent for user endpoints, enabling hybrid work through secure, fast, reliable access to any app over any network.
<p>This document provides information about the Zscaler Client Connector Connector, which facilitates automated interactions, with a Zscaler Client Connector server using FortiSOAR&trade; playbooks. Add the Zscaler Client Connector Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Zscaler Client Connector.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-zscaler-client-connector`

## Prerequisites to configuring the connector
- You must have the URL of Zscaler Client Connector server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Zscaler Client Connector server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Zscaler Client Connector</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>The service-based URL of the Zscaler Client Connector to which you connect and perform the automated operations.<br>
<tr><td>Client ID<br></td><td>Unique ID of the Zscaler Client Connector that is used to create an authentication token required to access the API.<br>
<tr><td>Client Secret<br></td><td>Unique Client Secret of the Zscaler Client Connector that is used to create an authentication token required to access the API.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Enrolled Device List<br></td><td>Retrieve a list of all enrolled devices of your organization and their basic details from Zscaler Client Connector based on input parameters that you have specified.<br></td><td>get_enrolled_device_list <br/>Investigation<br></td></tr>
<tr><td>Get Enrolled Device Details<br></td><td>Retrieve a device details of enrolled devices of your organization from Zscaler Client Connector based on input parameters that you have specified.<br></td><td>get_enrolled_device_details <br/>Investigation<br></td></tr>
<tr><td>Get Device OTP<br></td><td>Retrieve the one-time password (OTP) for a specific device. These single-use passwords are unique and tied to the device Unique Device Identifier (UDID). It is made of 10 random alphanumeric characters and can only be used once.<br></td><td>get_device_otp <br/>Investigation<br></td></tr>
<tr><td>Get Device App Profile Password<br></td><td>Retrieve the app profile password for a specific device. You can determine the assigned global passwords by using the username and os type of a device.<br></td><td>get_device_app_profile_password <br/>Investigation<br></td></tr>
<tr><td>Download Device Details<br></td><td>Downloads or exports device information as a CSV file from Zscaler Client Connector based on input parameters that you have specified.<br></td><td>download_device_details <br/>Investigation<br></td></tr>
<tr><td>Download Service Status of Devices<br></td><td>Downloads service status of all devices as a CSV file from Zscaler Client Connector based on input parameters that you have specified.<br></td><td>download_service_status_of_devices <br/>Investigation<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>execute_an_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Enrolled Device List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Username<br></td><td>Filter devices by enrolled user name in the Zscaler Client Connector portal to identify and manage devices associated with a specific user.<br>
</td></tr><tr><td>OS Type<br></td><td>Filter by device operating system type in the Zscaler Client Connector.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve results when pagination is applied. This parameter is used to fetch a specific subset of results based on the page number, helping to break large datasets into manageable chunks.<br>
</td></tr><tr><td>Page Size<br></td><td>Specify the maximum number of results this operation should return, per page, in the response. If not provided, the default page size is 50. The max page size is 5000.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Enrolled Device Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Unique Device Identifier (UDID)<br></td><td>Filter by unique device identifier in the Zscaler Client Connector.<br>
</td></tr><tr><td>Username<br></td><td>Filter devices by enrolled user name in the Zscaler Client Connector portal to identify and manage devices associated with a specific user.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Device OTP
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Unique Device Identifier (UDID)<br></td><td>Filter by unique device identifier in the Zscaler Client Connector.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Device App Profile Password
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Username<br></td><td>Filter devices by enrolled user name in the Zscaler Client Connector portal to identify and manage devices associated with a specific user.<br>
</td></tr><tr><td>OS Type<br></td><td>Filter by device operating system type in the Zscaler Client Connector.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Download Device Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>OS Types<br></td><td>Filter the list of devices by operating systems. The default value is null, which represents ALL OS types. The following values represent different OS types: iOS, Android, Windows, macOS and Linux.<br>
</td></tr><tr><td>Registration Types<br></td><td>Filter the list of devices by registration types or states. The following values represent different device states: All States Except Removed, Registered, Removal Pending, Unregistered, Removed, and Quarantined.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Download Service Status of Devices
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>OS Types<br></td><td>Filter the list by operating systems. The default value is null, which represents ALL OS types. The following values represent different OS types: iOS, Android, Windows, macOS and Linux.<br>
</td></tr><tr><td>Registration Types<br></td><td>Filter the list by registration types or states. The following values represent different device states: All States Except Removed, Registered, Removal Pending, Unregistered, Removed, and Quarantined.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE

GET

PATCH

POST 

PUT <br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be /images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

## Included playbooks
The `Sample - Zscaler Client Connector - 1.0.0` playbook collection comes bundled with the Zscaler Client Connector connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Zscaler Client Connector connector.

- Download Device Details
- Download Service Status of Devices
- Execute an API Request
- Get Device App Profile Password
- Get Device OTP
- Get Enrolled Device Details
- Get Enrolled Device List

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
