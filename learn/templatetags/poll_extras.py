from django import template
from datetime import datetime
from ..models import Book

register = template.Library()


class AllenDateNote(template.Node):
    def __init__(self, format_string, as_arg):
        self.format_string = format_string
        self.as_arg = as_arg

    def render(self, context):
        now = datetime.now().strftime(self.format_string)
        if self.as_arg:
            context[self.as_arg] = now
            return ''
        return now


@register.tag()
def date_allen(parse, token):
    # tagname, format_string = token.split_contents()
    args = token.split_contents()
    as_arg = None
    if len(args) == 4 and args[-2] == 'as':
        as_arg = args[-1]
    return AllenDateNote(args[1][1:-1], as_arg)


@register.assignment_tag()
def get_current_time(format_string):
    return datetime.now().strftime(format_string)


@register.inclusion_tag('res.html')
def res(publisher_name):
    books = Book.objects.filter(publisher__name=publisher_name)
    return locals()
