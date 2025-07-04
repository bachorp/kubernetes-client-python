# kubernetes.client.OpenidApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_account_issuer_open_id_keyset**](OpenidApi.md#get_service_account_issuer_open_id_keyset) | **GET** /openid/v1/jwks | 


# **get_service_account_issuer_open_id_keyset**
> str get_service_account_issuer_open_id_keyset()

get service account issuer OpenID JSON Web Key Set (contains public token verification keys)

### Example

* Api Key Authentication (BearerToken):

```python
import kubernetes.client
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
    api_instance = kubernetes.client.OpenidApi(api_client)

    try:
        api_response = api_instance.get_service_account_issuer_open_id_keyset()
        print("The response of OpenidApi->get_service_account_issuer_open_id_keyset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenidApi->get_service_account_issuer_open_id_keyset: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwk-set+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

