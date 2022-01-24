from django import template

register = template.Library()

@register.filter(name='show')
def show(value, args):
    return format(value, args)