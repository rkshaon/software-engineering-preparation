# HTTP Status Code
**HTTP response status codes** indicate whether a specific **HTTP request** has been successfully completed.

Responses are grouped in five classes:

- Informational responses ***(100 – 199)***
- Successful responses ***(200 – 299)***
- Redirection messages ***(300 – 399)***
- Client error responses ***(400 – 499)***
- Server error responses ***(500 – 599)***

## Informational responses
- [**100 Continue**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100): This interim response indicates that the client should continue the request or ignore the response if the request is already finished.

- [**101 Switching Protocols**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/101): This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.

- [**102 Processing (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/102): This code indicates that the server has received and is processing the request, but no response is available yet.

- [**103 Early Hints**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/103): This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response or preconnect to an origin from which the page will need resources.

## Successful responses
- [**200 OK**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200): The request succeeded. The result meaning of "success" depends on the HTTP method:
    - `GET`: The resource has been fetched and transmitted in the message body.
    - `HEAD`: The representation headers are included in the response without any message body.
    - `PUT` or `POST`: The resource describing the result of the action is transmitted in the message body.
    - `TRACE`: The message body contains the request message as received by the server.

- [**201 Created**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201): The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.

- [**202 Accepted**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202): The request has been received but not yet acted upon. It is noncommittal, since there is no way in `HTTP` to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.

- [**203 Non-Authoritative Information**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/203): This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status.

- [**204 No Content**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204): There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones.

- [**205 Reset Content**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/205): Tells the user agent to reset the document which sent this request.

- [**206 Partial Content**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/2006): This response code is used when the [`Range`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) header is sent from the client to request only part of a resource.

- [**207 Multi-Status (WebDAV)**]((https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/207)): Conveys information about multiple resources, for situations where multiple status codes might be appropriate.

- [**208 Already Reported (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/208): Used inside a `<dav:propstat>` response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.

- [**226 IM Used (HTTP Delta encoding)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/226): The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.

## Redirection messages
- [**300 Multiple Choices**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/300): The request has more than one possible response. The user agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)

- [**301 Moved Permanently**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301): The URL of the requested resource has been changed permanently. The new URL is given in the response.

- [**302 Found**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302): This response code means that the URI of requested resource has been changed temporarily. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests.

- [**303 See Other**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/303): The server sent this response to direct the client to get the requested resource at another URI with a GET request.

- [**304 Not Modified**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304): This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.

- [**305 Use Proxy Deprecated**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/305): Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy.

- [**306 unused**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/306): This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification.

- [**307 Temporary Redirect**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/307): The server sends this response to direct the client to get the requested resource at another URI with the same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request.

- [**308 Permanent Redirect**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/308): This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request.

## Client error responses
- [**400 Bad Request**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400): The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

- [**401 Unauthorized**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401): Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.

- [**402 Payment Required Experimental**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/402): This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.

- [**403 Forbidden**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403): The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server.

- [**404 Not Found**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404): The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.

- [**405 Method Not Allowed**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405): The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling `DELETE` to remove a resource.

- [**406 Not Acceptable**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406): This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.

- [**407 Proxy Authentication Required**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/407): This is similar to 401 Unauthorized but authentication is needed to be done by a proxy.

- [**408 Request Timeout**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408): This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message.

- [**409 Conflict**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409): This response is sent when a request conflicts with the current state of the server.

- [**410 Gone**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410): This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for "limited-time, promotional services". APIs should not feel compelled to indicate resources that have been deleted with this status code.

- [**411 Length Required**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/411): Server rejected the request because the Content-Length header field is not defined and the server requires it.

- [**412 Precondition Failed**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/412): The client has indicated preconditions in its headers which the server does not meet.

- [**413 Payload Too Large**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413): Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field.

- [**414 URI Too Long**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414): The URI requested by the client is longer than the server is willing to interpret.

- [**415 Unsupported Media Type**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415): The media format of the requested data is not supported by the server, so the server is rejecting the request.

- [**416 Range Not Satisfiable**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416): The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data.

- [**417 Expectation Failed**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/417): This response code means the expectation indicated by the Expect request header field cannot be met by the server.

- [**418 I'm a teapot**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418): The server refuses the attempt to brew coffee with a teapot.

- [**421 Misdirected Request**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421): The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.

- [**422 Unprocessable Content (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422): The request was well-formed but was unable to be followed due to semantic errors.

- [**423 Locked (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/423): The resource that is being accessed is locked.

- [**424 Failed Dependency (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/424): The request failed due to failure of a previous request.

- [**425 Too Early Experimental**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/425): Indicates that the server is unwilling to risk processing a request that might be replayed.

- [**426 Upgrade Required**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/426): The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s).

- [**428 Precondition Required**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/428): The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client `GETs` a resource's state, modifies it and `PUTs` it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.

- [**429 Too Many Requests**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429): The user has sent too many requests in a given amount of time ("rate limiting").

- [**431 Request Header Fields Too Large**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/431): The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.

- [**451 Unavailable For Legal Reasons**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/451): The user agent requested a resource that cannot legally be provided, such as a web page censored by a government.

## Server error responses
- [**500 Internal Server Error**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500): The server has encountered a situation it does not know how to handle.

- [**501 Not Implemented**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501): The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.

- [**502 Bad Gateway**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502): This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.

- [**503 Service Unavailable**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503): The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached.

- [**504 Gateway Timeout**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504): This error response is given when the server is acting as a gateway and cannot get a response in time.

- [**505 HTTP Version Not Supported**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/505): The HTTP version used in the request is not supported by the server.

- [**506 Variant Also Negotiates**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/506): The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.

- [**507 Insufficient Storage (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/507): The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.

- [**508 Loop Detected (WebDAV)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/508): The server detected an infinite loop while processing the request.

- [**510 Not Extended**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/510): Further extensions to the request are required for the server to fulfill it.

- [**511 Network Authentication Required**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/511): Indicates that the client needs to authenticate to gain network access.

#### References
- [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [HTTP Status Code](https://restfulapi.net/http-status-codes/)
- [WebDAV](https://developer.mozilla.org/en-US/docs/Glossary/WebDAV)
- [HTTP Delta encoding](https://datatracker.ietf.org/doc/html/rfc3229)