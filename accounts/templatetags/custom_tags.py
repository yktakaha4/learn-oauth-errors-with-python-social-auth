from copy import deepcopy
from json import dumps

from django import template

register = template.Library()


@register.filter
def to_json(value):
    try:
        secure_value = deepcopy(value)
        if "access_token" in secure_value:
            token = secure_value["access_token"]
            show_length = int(len(token) * 0.3)
            secure_value["access_token"] = token[0:show_length] + ("*" * 3)
        return dumps(secure_value, indent=2)
    except Exception:
        return value
