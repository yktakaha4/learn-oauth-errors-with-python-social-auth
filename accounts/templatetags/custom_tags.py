from json import dumps
from django import template

register = template.Library()


@register.filter
def to_json(value):
    try:
        return dumps(value, indent=2)
    except Exception:
        return value
