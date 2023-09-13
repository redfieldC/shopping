from django.urls import  path
from polls import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns=[
    path('',views.showemp,name="showemp"),
    #show clothes
    path('show/',views.show,name="show"),
    #insert clothes
    path('insert/',views.insert,name="insert"),
    path('Insert',views.Insertemp,name="Insertemp"),
    #eidt clothes information
    path('update/',views.update,name="update"),
    path('Edit/<int:id>/',views.Editemp,name="Editemp"),
    # path('Update/<int:id>/',views.updateemp,name="updateemp"),
    path('Delete/<int:id>/',views.Delemp,name="Delemp"),
]

