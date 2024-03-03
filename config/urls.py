"""ChemistryComplex URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from reaction_kinetics_solver_module.reaction_kinetics_solver import kinetics_solver_module_solution
from utils.json_service import with_request_data

urlpatterns = [
    path('api/v1/reaction_kinetics_solver',  with_request_data(kinetics_solver_module_solution)),
    path('admin/', admin.site.urls),
]
