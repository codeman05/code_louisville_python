from django import template

register = template.Library()


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def format_job_number(value):
    number = str(value)
    if len(number) == 1:
        return "17-000{}".format(number)
    elif len(number) == 2:
        return "17-00{}".format(number)
    elif len(number) == 3:
        return "17-0{}".format(number)
    else:
        return "17-{}".format(number)
