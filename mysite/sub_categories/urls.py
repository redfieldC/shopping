from django.urls import  path
from sub_categories import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  



urlpatterns=[
    path('',views.show_sub_categories,name="show_sub_categories"),
    path('insert_sub_categories/',views.insert_sub_categories,name="insert_sub_categories"),
    path('sub_categories/edit_sub_categories/<int:id>/',views.edit_sub_categories,name="edit_sub_categories"),
    path('sub_categories/delete_sub_categories/<int:id>/',views.delete_sub_categories,name="delete_sub_categories")
]