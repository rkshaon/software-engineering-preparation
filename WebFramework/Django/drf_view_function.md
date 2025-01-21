# Function-Based Views
Traditional Django function-based views enhanced with DRF utilities.

## Example
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def example_function_view(request):
    if request.method == 'GET':
        return Response({"message": "Hello, World!"})
    elif request.method == 'POST':
        return Response(request.data, status=201)
```

## Use Case
- For small, simple, or one-off endpoints with minimal logic.

## Where to Use
- Use for quick prototyping or lightweight endpoints.

## Where Not to Use
- Avoid for large-scale applications with complex logic or multiple actions.
