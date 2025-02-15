from django import template

register = template.Library()

@register.filter(name='format_currency')
def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value
