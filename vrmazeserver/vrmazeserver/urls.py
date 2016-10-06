"""vrmazeserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from maze import views

urlpatterns = [
    url(r'^last_maze', views.last_maze, name='last_maze' ),
    url(r'^generate_maze', views.generate_maze, name='generate_maze' ),
    url(r'^update_person_position', views.update_person_position, name='update_person_position' ),
    url(r'^get_person_position', views.get_person_position, name='get_person_position' ),
    url(r'^admin/', include(admin.site.urls)),
]
