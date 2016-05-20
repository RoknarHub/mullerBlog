"""mullerHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^locale/$', views.view_locale),
    url(r'^$', views.blog_index, name='blogIndex'),
    url(r'^(?P<pk>[0-9]+)/$', views.blog_entry(), name='blogEntry'),
    #url(r'^about/', views.about, name='about'),
    url(r'^about/curriculum', views.curriculum, name='curriculum'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
