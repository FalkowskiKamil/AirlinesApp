"""AirlinesApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from airline import views as airline_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

import debug_toolbar

urlpatterns = [
    path("", airline_views.main, name="main"),
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    path("airline/", include("airline.urls")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('airline/favicon.ico'))),
    path("api/v1/", include("airline.api.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
