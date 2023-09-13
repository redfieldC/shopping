"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.urls import  path
from polls import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('polls/',include(('polls.urls','polls'),namespace='polls')),
    path('categories/',include(('categories.urls','categories'),namespace="categories")),
    path('colors/',include(('colors.urls','colors'),namespace="colors")),
    path('size/',include(('Size.urls','Size'),namespace="size")),
    path('sub_categories/',include(('sub_categories.urls','sub_categories'),namespace="sub_categories")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  