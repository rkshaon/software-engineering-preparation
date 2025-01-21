# Mixins
Provide reusable methods for common actions like `list`, `create`, `retrieve`, `update`, and `destroy`.

## Example
```python
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class ExampleMixinView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

## Use Case
- When you need only specific CRUD operations without implementing everything manually.

## Where to Use
- Use for endpoints with a mix of common CRUD operations.

## Where Not to Use
- Avoid for endpoints requiring non-standard actions or full CRUD.