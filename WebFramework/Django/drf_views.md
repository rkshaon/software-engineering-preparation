# DRF: Views

- [APIView](./drf_view_apiview.md)
- [GenericAPIView](./drf_view_genericapiview.md)
- [Mixin](./drf_view_mixins.md)
- [Generic View](./drf_view_genericview.md)
- [ViewSets](./drf_view_viewset.md)
- [Function Based View](./drf_view_function.md)

## Summary Table
| View Type | Use Case	| Pros	| Cons |
| --------- | --------- | ----- | ----- |
| APIView	| Custom endpoints, full control | Flexible	| Verbose, boilerplate code |
| GenericAPIView | Queryset/serializer handling	| Flexible, DRF utilities | Requires customization |
| Mixins | Specific CRUD actions | Reusable, less boilerplate | Limited customization |
| Generic Views	| Standard CRUD operations	| Simple, minimal boilerplate	| Limited flexibility |
| ViewSets	| Full CRUD in one class | Router integration, compact	| Overkill for simple endpoints |
| Function Views | Quick, simple views	|Lightweight	| Limited scalability, harder to extend |
| Custom Views	| Highly custom behavior	| Total flexibility	| No DRF utilities, more prone to errors |

