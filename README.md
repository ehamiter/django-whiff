```markdown
# django-whiff

`django-whiff` is a simple Django template tag that combines the functionality of the `with` and `if` tags, inspired by the Python walrus operator (`:=`). It allows you to assign a variable and immediately check if it is truthy, rendering content if it is.

## Features

- Combines `with` and `if` in a single template tag.
- Simplifies template logic by reducing the need for nested tags.
- Easy to use and integrate into existing Django projects.

## Caveats

- Not a great contender to replace multiple pipes or conditions in an existing template tag

## Installation

You can install `django-whiff` via pip:

```bash
pip install django-whiff
```

## Usage

Once installed, add `django_whiff` to your `INSTALLED_APPS` in your Django settings:

```python
INSTALLED_APPS = [
    ...
    'django_whiff',
    ...
]
```

### How It Works

- The `whiff` tag assigns the value of `some_obj` to `obj`.
- If `some_obj` is truthy, the content inside the `whiff` block is rendered.
- If `some_obj` is falsey, nothing is rendered.

## Example

```django
{% load whiff %}

{% whiff user as current_user %}
  <p>Welcome back, {{ current_user.username }}!</p>
{% endwhiff %}
```

In this example, if `user` is present and truthy, a welcome message is displayed. Otherwise, nothing is rendered.


## Tests
```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the [GitHub repository](https://github.com/ehamiter/django-whiff).

## Acknowledgements

Inspired by the Python walrus operator (`:=`) and the need for cleaner, more concise template logic.
