from django import template
from django.utils.html import format_html
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, User):  # Use User here instead of user_model
        # return empty string as safe default
        return ""

    if current_user and author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
