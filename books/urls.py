from django.urls import path,re_path
from . import views
from . import models

urlpatterns = [
    path('',views.login,name = "login"),
    path('signup/',views.signup,name = "signup"),
    path('temp/',views.temp,name = "temp"),
    path('adminpage/',views.admin,name="admin"),
    path('requestconfirmation/<int:value>/',views.requestconfirmation,name = "requestconfirmation"),

]
