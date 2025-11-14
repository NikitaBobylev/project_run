"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from project_run.apps.company.urls import urlpatterns as app_run_pattenrs
from project_run.apps.runs.urls import urlpatterns as runs_pattrns


result_patterns = []
result_patterns.extend(app_run_pattenrs)
result_patterns.extend(runs_pattrns)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(result_patterns)),
]