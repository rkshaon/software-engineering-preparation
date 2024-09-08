# Signal

Django provides a powerful signal framework that allows you to get notified when certain actions occur within the framework, means Django signals allow decoupled applications to get notified when certain events happen elsewhere in the framework. 

## Key Concepts
- `Sender`: The entity that sends the signal. This could be a model, a view, or any other component in your application.
- `Receiver`: The function (or method) that receives and handles the signal. This function performs a specific action in response to the signal.
- `Signal Dispatcher`: Manages the connections between senders and receivers. When a signal is sent, the dispatcher ensures that all connected receivers are called with the appropriate arguments.
- `Connecting Signals`: Signals are connected to receivers using the @receiver decorator or the connect() method.

## Types of Signals
- `pre_save`: Sent just before a model's save() method is called.
- `post_save`: Sent just after a model's save() method is called.
- `pre_delete`: Sent just before a model's delete() method is called.
- `post_delete`: Sent just after a model's delete() method is called.

## Built-in Signals in Django
Django comes with several built-in signals, including but not limited to:

- `pre_save`: Sent just before a model’s save() method is called.
- `post_save`: Sent just after a model’s save() method is called.
- `pre_delete`: Sent just before a model’s delete() method is called.
- `post_delete`: Sent just after a model’s delete() method is called.
- `m2m_changed`: Sent when a ManyToManyField is changed.
- `request_started`: Sent when Django starts processing an HTTP request.
- `request_finished`: Sent when Django finishes processing an HTTP request.

## Use
### Define a Receiver Function
A receiver function takes at least two arguments: sender and **kwargs. The sender is the model class sending the signal, and **kwargs contains additional information about the signal.

```
from django.db.models.signals import pre_save
from django.dispatch import receiver

from myapp.models import MyModel

@receiver(pre_save, sender=MyModel)
def mymodel_pre_save_handler(sender, instance, **kwargs):
    print(f"Pre-save signal received for {instance}")
    // custom logic

```

### Connect the Receiver to the Signal
Using the @receiver decorator is a common and convenient way to connect a receiver to a signal.

```
from django.db.models.signals import post_save

@receiver(post_save, sender=MyModel)
def mymodel_post_save_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Post-save signal received for a new instance: {instance}")
    else:
        print(f"Post-save signal received for an updated instance: {instance}")

```

Alternatively, you can use the `connect()` method to connect the receiver.

```
from django.db.models.signals import pre_delete
from django.dispatch import receiver

def mymodel_pre_delete_handler(sender, instance, **kwargs):
    print(f"Pre-delete signal received for {instance}")

pre_delete.connect(mymodel_pre_delete_handler, sender=MyModel)
```

### Ensure Signal Handlers are Imported
To avoid issues with signals not being connected, ensure that signal handlers are imported at an appropriate point in your application, typically in the ready() method of your app's configuration class in `apps.py`.

```
// myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Ensure your signals are imported
```

## Custom Signal
You can also create custom signals for more specific use cases.

### Define a Custom Signal
```
from django.dispatch import Signal

// Define the custom signal
my_custom_signal = Signal(providing_args=["instance", "created"])

```
### Send the Custom Signal
```
from .signals import my_custom_signal

// Send the custom signal
my_custom_signal.send(sender=MyModel, instance=my_instance, created=True)
```

### Connect a Receiver to the Custom Signal
```
from django.dispatch import receiver
from .signals import my_custom_signal

@receiver(my_custom_signal)
def my_custom_signal_handler(sender, instance, created, **kwargs):
    print(f"Custom signal received: {instance}, created: {created}")
```
