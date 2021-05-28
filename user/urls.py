from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('membership',views.membership),
    path('admin/',views.dashboard),
    path("A_login",views.Userlogin,name="login"),
]