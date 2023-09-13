from django.urls import  path
from categories import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  



urlpatterns=[
    path('',views.show_cat,name="show_cat"),
    path('insert_cat/',views.insert_cat,name="insert_cat"),
    path('categories/edit_cat/<int:id>/',views.edit_cat,name="edit_cat"),
    path('categories/del_cat/<int:id>/',views.del_cat,name="del_cat")
]