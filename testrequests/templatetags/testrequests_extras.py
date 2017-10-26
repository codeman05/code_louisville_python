from django import template

register = template.Library()


@register.filter
def get_class_name(value):
    return value.__class__.__name__


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def format_job_number(value):
    if len(str(value)) == 1:
        return "17-000{}".format(value)
    elif len(str(value)) == 2:
        return "17-00{}".format(value)
    elif len(str(value)) == 3:
        return "17-0{}".format(value)
    elif len(str(value)) == 4:
        return "17-{}".format(value)
    else:
        return ""