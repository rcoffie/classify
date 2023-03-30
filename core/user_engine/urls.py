from django.urls import path

from . import views

urlpatterns = [
   path("dashboard/",views.dashboard,name="dashboard"),
   path("signup/",views.signup,name="signup"),
   path("login_request/",views.login_request,name="login"),
]
