from django import template

register = template.Library()

@register.tag(name="whiff")
def do_whiff(parser, token):
    try:
        # Split the tag contents into tokens
        tag_name, variable, as_text, context_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly three arguments" % token.contents.split()[0]
        )

    nodelist = parser.parse(('endwhiff',))
    parser.delete_first_token()

    return WhiffNode(variable, context_name, nodelist)


class WhiffNode(template.Node):
    def __init__(self, variable, context_name, nodelist):
        self.variable = template.Variable(variable)
        self.context_name = context_name
        self.nodelist = nodelist

    def render(self, context):
        try:
            value = self.variable.resolve(context)
            if value:
                context[self.context_name] = value
                return self.nodelist.render(context)
        except template.VariableDoesNotExist:
            pass
        return ''  # Return an empty string if the variable does not exist or is falsey
