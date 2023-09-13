from django.urls import  path
from Size import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  



urlpatterns=[
    path('',views.show_size,name="show_size"),
    path('insert_size/',views.insert_size,name="insert_size"),
    path('size/edit_size/<int:id>/',views.edit_size,name="edit_size"),
    path('size/delete_size/<int:id>/',views.delete_size,name="delete_size")
]