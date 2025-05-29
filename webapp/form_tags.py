from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})


@register.simple_tag
def custom_tag():
    return "Hello, world!"

@register.simple_tag
def custom_form_tag():
    return "Custom form tag content"


@register.filter(name='add_class')
def add_class(field, class_name):
    return field.as_widget(attrs={'class': class_name})
