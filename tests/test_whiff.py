import django
from django.template import Context, Template
from django.test import SimpleTestCase

django.setup()

class WhiffTagTests(SimpleTestCase):

    def render_template(self, template_string, context=None):
        context = context or {}
        return Template(template_string).render(Context(context))

    def test_whiff_tag_renders_content_when_variable_is_truthy(self):
        template_string = """
        {% load whiff %}
        {% whiff some_obj as obj %}
            Title: {{ obj.title }}
        {% endwhiff %}
        """
        context = {'some_obj': {'title': 'Test Title'}}
        rendered = self.render_template(template_string, context)
        self.assertIn('Title: Test Title', rendered)

    def test_whiff_tag_renders_nothing_when_variable_is_falsy(self):
        template_string = """
        {% load whiff %}
        {% whiff some_obj as obj %}
            Title: {{ obj.title }}
        {% endwhiff %}
        """
        context = {'some_obj': None}
        rendered = self.render_template(template_string, context)
        self.assertNotIn('Title:', rendered)
        self.assertEqual(rendered.strip(), '')

    def test_whiff_tag_handles_nonexistent_variable_gracefully(self):
        template_string = """
        {% load whiff %}
        {% whiff nonexistent_obj as obj %}
            Title: {{ obj.title }}
        {% endwhiff %}
        """
        context = {}
        rendered = self.render_template(template_string, context)
        self.assertNotIn('Title:', rendered)
        self.assertEqual(rendered.strip(), '')

    def test_whiff_tag_renders_content_when_variable_is_not_none(self):
        template_string = """
        {% load whiff %}
        {% whiff some_obj as obj %}
            Title: {{ obj.title }}
        {% endwhiff %}
        """
        context = {'some_obj': {'title': 'Another Test Title'}}
        rendered = self.render_template(template_string, context)
        self.assertIn('Title: Another Test Title', rendered)
