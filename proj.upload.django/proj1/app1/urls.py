"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from.import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('upload1',views.upload1,name='upload1'),
    path('upload',views.upload,name='upload'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('view_book/<int:pk>/', views.view_book, name='view_book'),
]
