from django.contrib import admin
from django.urls import path

# URLS DE APP BLOG

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("saludar-html", saludar_con_html),
]
