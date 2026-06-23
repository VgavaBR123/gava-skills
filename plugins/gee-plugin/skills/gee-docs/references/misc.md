# Outros

> 7 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.apply`](#ee-apply)
- [`ee.call`](#ee-call)
- [`ee.initialize`](#ee-initialize)
- [`ee.reset`](#ee-reset)
- [`exports`](#exports)
- [`print`](#print)
- [`require`](#require)

---

## ee.apply

Call a function with a dictionary of named arguments.

Returns an object representing the called function. If the signature specifies a recognized return type, the returned value will be cast to that type.

| Usage | Returns |
|---|---|
| `ee.apply(func, namedArgs)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| `func` | Function\|String | The function to call. Either an ee.Function object or the name of an API function. |
| `namedArgs` | Object | A dictionary of arguments to the function. |

## ee.call

Call a function with the given positional arguments.

Returns an object representing the called function. If the signature specifies a recognized return type, the returned value will be cast to that type.

| Usage | Returns |
|---|---|
| `ee.call(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| `func` | Function\|String | The function to call. Either an ee.Function object or the name of an API function. |
| `var_args` | VarArgs\[Object\] | Positional arguments to pass to the function. |

## ee.initialize

Initialize the library. If this hasn't been called by the time any object constructor is used, it will be called then. If this is called a second time with a different baseurl or tileurl, this doesn't do an un-initialization of e.g.: the previously loaded Algorithms, but will overwrite them and let point at alternate servers.

If initialize() is first called in asynchronous mode (by passing a success callback), any future asynchronous mode calls will add their callbacks to a queue and all the callbacks will be run together.

If a synchronous mode call is made after any number of asynchronous calls, it will block and execute all the previously supplied callbacks before returning.

In most cases, an authorization token should be set before the library is initialized, either with ee.data.authorize() or ee.data.setAuthToken().

In Python, this method is named ee.Initialize, with a capital I. Note that some parameters differ between JavaScript and Python. In addition to opt_url and project below, Python also supports: credentials - a google.oauth2.Credentials object or 'persistent' to use stored credentials (the default); http_transport - a httplib2.Http client.

| Usage | Returns |
|---|---|
| `ee.initialize(*baseurl*, *tileurl*, *successCallback*, *errorCallback*, *xsrfToken*, *project*)` |   |

| Argument | Type | Details |
|---|---|---|
| `baseurl` | String, optional | The Earth Engine REST API endpoint. (Python argument name: opt_url) |
| `tileurl` | String, optional | The Earth Engine REST tile endpoint, this is optional and defaults to baseurl. (JavaScript only) |
| `successCallback` | Function, optional | An optional callback to be invoked when the initialization is successful. If not provided, the initialization is done synchronously. (JavaScript only) |
| `errorCallback` | Function, optional | An optional callback to be invoked with an error if the initialization fails. (JavaScript only) |
| `xsrfToken` | String, optional | A string to pass in the "xsrfToken" parameter of EE API XHRs. (JavaScript only) |
| `project` | String, optional | Optional client project ID or number to use when making API calls. (Python argument name: project) |

## ee.reset

Reset the library to its base state. Useful for re-initializing to a different server.

| Usage | Returns |
|---|---|
| `ee.reset()` |   |

**No arguments.**

## exports

The reserved namespace for exporting objects as module members.

| Usage | Returns |
|---|---|
| `exports()` |   |

**No arguments.**

## print

Prints the arguments to the console.

| Usage | Returns |
|---|---|
| `print(var_args)` |   |

| Argument | Type | Details |
|---|---|---|
| `var_args` | VarArgs\[Object\] | The objects to print. |

## require

Retrieves the script found at a given path as a module. The module is used to access exposed members of the required script.

Returns returns an object that represents exported members from the required module.

| Usage | Returns |
|---|---|
| `require(path)` | Object |

| Argument | Type | Details |
|---|---|---|
| `path` | String | The path to the script to include as a module. Paths must be absolute, such as: "users/homeFolder/repo:path/to/file". |

