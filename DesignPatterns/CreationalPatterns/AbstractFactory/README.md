# Abstrct Factory
Abstract Factory Method is a [Creational Design pattern](./../../CreationalPatterns/README.md) that allows you to produce the families of related objects without specifying their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type of many objects. 

It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.

The **Abstract Factory Pattern** provides an **interface for creating families of related or dependent objects** without specifying their concrete classes.

**Think of it like**: _"A GUI factory that can create Windows-style or Mac-style buttons and checkboxes — all matching a theme."_

## ✅ Use Cases
- When you need to create multiple related objects (like UI components) with a consistent style.

- To switch families of products easily (e.g., from Light to Dark mode UI components).

- Helps maintain consistency and separation of concerns.

## 🖼️ Real-Life Analogy
Imagine a UI toolkit factory:

- WindowsFactory → makes **WindowsButton**, **WindowsCheckbox**

- MacFactory → makes **MacButton**, **MacCheckbox**

You just switch the factory, and the whole look-and-feel changes!

## Example
```python
from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows Button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering a Windows Checkbox"

class MacButton(Button):
    def render(self):
        return "Rendering a Mac Button"

class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering a Mac Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Usage
def render_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

render_ui(WindowsFactory())
render_ui(MacFactory())
```

