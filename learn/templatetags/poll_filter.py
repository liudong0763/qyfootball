from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def my_filter(value, arg):
    return value.replace(arg, '')


# @register.filter()
# @stringfilter
# def lower(value):
#     return value.lower()


# 效果一样
@register.filter()
def lower(value):
    return value.lower()


# @register.filter(is_safe=True)
# def add(value, arg):
#     return '%s %s' % (value, arg)


@register.filter(is_safe=True)
def add(value, arg):
    return '%s %s' % (value, arg)
    # return mark_safe('%s %s' % (value, arg))
