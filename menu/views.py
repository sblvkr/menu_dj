from django.views.generic import TemplateView


class MenuView(TemplateView):
    """View for menus page."""
    template_name = 'menu/index.html'
