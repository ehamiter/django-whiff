# django-whiff

`django-whiff` is a simple Django template tag that combines the functionality of the `with` and `if` tags, inspired by the Python walrus operator (`:=`). It allows you to assign a variable and immediately check if it is truthy, rendering content if it is.

## Example

```django
{% load whiff %}

  {% whiff current_user as user %}
    <h1>Welcome back, {{ user.first_name }} {{ user.last_name }}!</h1>
    <p>Your last login was on {{ user.last_login|date:"F j, Y, g:i a" }}.</p>

      <h2>Your Profile</h2>
      <ul>
        <li>Email:  {{ user.email }}</li>
        <li>Joined: {{ user.date_joined|date:"F j, Y" }}</li>
        <li>Bio:    {{ user.bio }}</li>
      </ul>
  {% endwhiff %}
```

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

> Note *the underscore*, not hyphen.

### How It Works

- The `whiff` tag assigns the value of `some_obj` to `obj`.
- If `some_obj` is truthy, the content inside the `whiff` block is rendered.
- If `some_obj` is falsey, nothing is rendered.


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
