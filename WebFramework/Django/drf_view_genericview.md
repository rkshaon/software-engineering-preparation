# Generic Views (e.g., ListAPIView, RetrieveAPIView)
Predefined views combining GenericAPIView and Mixins for common actions.

## Example of ListAPIView
```python
from rest_framework.generics import ListAPIView
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class ExampleListView(ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

```

## Example of RetrieveAPIView
```python
## Example 1
from rest_framework.generics import RetrieveAPIView
from myapp.models import User
from myapp.serializers import UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

## Example 2
from rest_framework.generics import RetrieveAPIView
from myapp.models import Blog
from myapp.serializers import BlogSerializer

class PublishedBlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer
```

## Use Case
- For standard CRUD endpoints where minimal customization is needed.
- When you need to fetch a single object by its primary key or slug (Fetch user details for a profile page)
- When you need to retrieve specific data but apply permissions or custom lookup logic (Retrieve a specific blog post but restrict access to only published posts).

## Where to Use
- Use for simple, predictable CRUD operations.
- Fetching the details of a single resource in RESTful APIs (e.g., `/users/1/` or `/posts/slug/`).

## Where Not to Use
- Avoid for endpoints requiring extensive customization or complex logic.
- For non-model-based or highly customized endpoints (If you need to return a computed result instead of model data, APIView or GenericAPIView would be more appropriate).
- When you need to fetch multiple objects.
