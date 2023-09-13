from django.urls import  path
from colors import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  



urlpatterns=[
    path('',views.show_colors,name="show_colors"),
    path('insert_colors/',views.insert_colors,name="insert_colors"),
    path('colors/edit_colors/<int:id>/',views.edit_colors,name="edit_colors"),
    path('colors/delete_colors/<int:id>/',views.delete_colors,name="delete_colors")
]