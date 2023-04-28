from django import template
from menu.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = Menu.objects.prefetch_related('children').filter(parent=None)
    return render_menu_items(menu_items)


def render_menu_items(menu_items):
    result = '<ul>'
    if menu_items:
        for item in menu_items:
            result += f'<li>{item.name}'
            children = item.children.all()
            if children:
                result += render_menu_items(children)
            result += '</li>'
    result += '</ul>'
    return result
