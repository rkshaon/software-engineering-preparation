# API Version

API versioning is the practice of managing changes made to an API (Application Programming Interface) in a way that minimizes disruption for applications that use the API. It ensures a smooth transition between updates while also allowing for future growth and improvement.

## Key aspects of

- `Maintaining backward compatibility`:  The core principle is to avoid breaking changes in newer versions that would cause existing applications using the API to malfunction. This can be achieved through various versioning strategies like URI versioning (specifying the version in the URL) or query parameter versioning (including the version number as a parameter).
- `Versioning for new features and changes`: When introducing new features or functionalities, it's often done in a separate version to avoid impacting existing integrations. This gives developers flexibility to adopt the new features at their own pace.
- `Clear communication and documentation`: Effective API versioning requires clear communication to developers using the API. Documentation should highlight changes introduced in each version and deprecation plans for older versions.
- `Version deprecation and retirement`:  Eventually, older versions might be deprecated and ultimately retired. This allows for a controlled phase-out while encouraging users to migrate to newer versions with improved functionalities and security.

## Benefits & Importance

- `Reduced risk of breaking applications`: By carefully managing changes and maintaining compatibility, API versioning minimizes the risk of causing issues for existing applications that rely on the API.
- `Flexibility for developers`: Developers have the freedom to choose the API version that best suits their needs and can migrate to newer versions at their own pace.
- `Facilitates future development`: Versioning allows for introducing new features and functionalities without compromising existing integrations. It promotes ongoing improvement and innovation in the API.
- As APIs evolve, changes may occur in the data structure, behavior, or functionality.
- Proper versioning ensures that existing clients continue to work as expected while allowing new clients to use the latest features.

## Approaches
- `URL Path Versioning`: Include the version in the URL path (e.g., **/api/v1/resource/**).
- `Query Parameter Versioning`: Include the version as a query parameter (e.g., **/api/resource/?version=1**).
- `Header Versioning`: Determine the version based on a custom header (e.g., **Accept-Version: 1**).
- `Consumer-Based Versioning`: Let clients specify their desired version explicitly.

## Best Practices
- Clearly document your versioning strategy.
- Avoid breaking changes for existing clients.
- Maintain consistency across your API versions.
- Communicate changes effectively to consumers.

#### References
- [DRF Doc](https://www.django-rest-framework.org/api-guide/versioning/)
- [Versioning APIs in Django Rest Framework Guide with Examples](https://studygyaan.com/django/versioning-api-in-django-rest-framework)
- [How to version a REST API @ freecodecamp.org](https://www.freecodecamp.org/news/how-to-version-a-rest-api/)
- [How to version a REST API @ restfulapi.net](https://restfulapi.net/versioning/)
- [API versioning @ postman.com](https://www.postman.com/api-platform/api-versioning/)