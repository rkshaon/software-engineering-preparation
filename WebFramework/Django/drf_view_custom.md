# Custom Views
Define views completely from scratch, bypassing DRF utilities.

## Example
```python
from django.http import JsonResponse

def custom_view(request):
    return JsonResponse({"message": "Hello, World!"})
```

## Use Case
- For endpoints requiring total flexibility or not fitting into DRF paradigms.

## Where to Use
- Use for legacy integrations or highly unique behavior.
## Where Not to Use
- Avoid when DRF utilities can simplify the implementation.
