from django import template
register=template.Library()

@register.filter()
def convert_to_lower(value):
    return value.lower()

@register.filter(name='rep')
def replace_char(value,arg):
    return value.replace(arg,'D')

#register.filter('mine',convert_to_lower)