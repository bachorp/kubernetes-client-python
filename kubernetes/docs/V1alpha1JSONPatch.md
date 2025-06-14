# V1alpha1JSONPatch

JSONPatch defines a JSON Patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | expression will be evaluated by CEL to create a [JSON patch](https://jsonpatch.com/). ref: https://github.com/google/cel-spec  expression must return an array of JSONPatch values.  For example, this CEL expression returns a JSON patch to conditionally modify a value:     [      JSONPatch{op: \&quot;test\&quot;, path: \&quot;/spec/example\&quot;, value: \&quot;Red\&quot;},      JSONPatch{op: \&quot;replace\&quot;, path: \&quot;/spec/example\&quot;, value: \&quot;Green\&quot;}    ]  To define an object for the patch value, use Object types. For example:     [      JSONPatch{        op: \&quot;add\&quot;,        path: \&quot;/spec/selector\&quot;,        value: Object.spec.selector{matchLabels: {\&quot;environment\&quot;: \&quot;test\&quot;}}      }    ]  To use strings containing &#39;/&#39; and &#39;~&#39; as JSONPatch path keys, use \&quot;jsonpatch.escapeKey\&quot;. For example:     [      JSONPatch{        op: \&quot;add\&quot;,        path: \&quot;/metadata/labels/\&quot; + jsonpatch.escapeKey(\&quot;example.com/environment\&quot;),        value: \&quot;test\&quot;      },    ]  CEL expressions have access to the types needed to create JSON patches and objects:  - &#39;JSONPatch&#39; - CEL type of JSON Patch operations. JSONPatch has the fields &#39;op&#39;, &#39;from&#39;, &#39;path&#39; and &#39;value&#39;.   See [JSON patch](https://jsonpatch.com/) for more details. The &#39;value&#39; field may be set to any of: string,   integer, array, map or object.  If set, the &#39;path&#39; and &#39;from&#39; fields must be set to a   [JSON pointer](https://datatracker.ietf.org/doc/html/rfc6901/) string, where the &#39;jsonpatch.escapeKey()&#39; CEL   function may be used to escape path keys containing &#39;/&#39; and &#39;~&#39;. - &#39;Object&#39; - CEL type of the resource object. - &#39;Object.&lt;fieldName&gt;&#39; - CEL type of object field (such as &#39;Object.spec&#39;) - &#39;Object.&lt;fieldName1&gt;.&lt;fieldName2&gt;...&lt;fieldNameN&gt;&#x60; - CEL type of nested field (such as &#39;Object.spec.containers&#39;)  CEL expressions have access to the contents of the API request, organized into CEL variables as well as some other useful variables:  - &#39;object&#39; - The object from the incoming request. The value is null for DELETE requests. - &#39;oldObject&#39; - The existing object. The value is null for CREATE requests. - &#39;request&#39; - Attributes of the API request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). - &#39;params&#39; - Parameter resource referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind. - &#39;namespaceObject&#39; - The namespace object that the incoming object belongs to. The value is null for cluster-scoped resources. - &#39;variables&#39; - Map of composited variables, from its name to its lazily evaluated value.   For example, a variable named &#39;foo&#39; can be accessed as &#39;variables.foo&#39;. - &#39;authorizer&#39; - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request.   See https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz - &#39;authorizer.requestResource&#39; - A CEL ResourceCheck constructed from the &#39;authorizer&#39; and configured with the   request resource.  CEL expressions have access to [Kubernetes CEL function libraries](https://kubernetes.io/docs/reference/using-api/cel/#cel-options-language-features-and-libraries) as well as:  - &#39;jsonpatch.escapeKey&#39; - Performs JSONPatch key escaping. &#39;~&#39; and  &#39;/&#39; are escaped as &#39;~0&#39; and &#x60;~1&#39; respectively).  Only property names of the form &#x60;[a-zA-Z_.-/][a-zA-Z0-9_.-/]*&#x60; are accessible. Required. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_json_patch import V1alpha1JSONPatch

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1JSONPatch from a JSON string
v1alpha1_json_patch_instance = V1alpha1JSONPatch.from_json(json)
# print the JSON string representation of the object
print(V1alpha1JSONPatch.to_json())

# convert the object into a dict
v1alpha1_json_patch_dict = v1alpha1_json_patch_instance.to_dict()
# create an instance of V1alpha1JSONPatch from a dict
v1alpha1_json_patch_from_dict = V1alpha1JSONPatch.from_dict(v1alpha1_json_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


