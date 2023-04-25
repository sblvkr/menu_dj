from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('menu.urls', 'menu'), namespace='menu')),
    path('admin/', admin.site.urls),
]
