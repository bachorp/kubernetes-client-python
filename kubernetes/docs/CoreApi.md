# kubernetes.client.CoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_versions**](CoreApi.md#get_api_versions) | **GET** /api/ | 


# **get_api_versions**
> V1APIVersions get_api_versions()

get available API versions

### Example

* Api Key Authentication (BearerToken):

```python
import kubernetes.client
from kubernetes.client.models.v1_api_versions import V1APIVersions
from kubernetes.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.CoreApi(api_client)

    try:
        api_response = api_instance.get_api_versions()
        print("The response of CoreApi->get_api_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_api_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1APIVersions**](V1APIVersions.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

