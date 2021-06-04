from django.urls import path
from django.contrib.auth import views as v

from.import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('college/',views.college,name='college'),
    path('gallery/',views.gallery,name='gallery'),
    # path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('login/',v.LoginView.as_view(template_name='dtl/login.html'),name='login')
   

]
