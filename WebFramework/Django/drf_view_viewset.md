# ViewSets
Combine multiple actions into a single class. DRF automatically maps URLs to actions.

## Example
```python
from rest_framework.viewsets import ModelViewSet
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class ExampleViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

## Use Case
- When you need all CRUD operations in a single class.
- Works well with DRF’s routers for automatic URL generation.

## Where to Use
- Use for resources needing full CRUD functionality.

## Where Not to Use
- Avoid for non-resource-based endpoints or complex, unrelated actions.
