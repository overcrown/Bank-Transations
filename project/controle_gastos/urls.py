"""controle_gastos URL Configuration

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
from django.urls import path, include
from register import views as register_view
from contas.views import home, test, list_items, Insert, Update, Delete, Element, Create, view, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="url_home"),
    path('list/', list_items.as_view(), name="url_list"),
    path('insert/', Insert.as_view(), name="url_insert"),
    path('update/<int:pk>/', Update.as_view(), name="url_update"),
    path('delete/<int:pk>/', Delete.as_view(), name="url_delete"),
    path('listelement/', Element.as_view(), name="url_element"),
    path('register/', register_view.register.as_view(), name="register"),
    path('create/', Create.as_view(), name="url_create"),
    path('view/', view.as_view(), name='url_view'),
    path('<int:pk>/', index.as_view(), name='url_index'),
    path('', include("django.contrib.auth.urls")), #Add own django urls for login/logo
]
