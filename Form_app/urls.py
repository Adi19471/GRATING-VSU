from django.urls import path
from Form_app import views


urlpatterns = [
    path('ft/',views.data,name='data'),
    path('dis/',views.display,name='display'),
    path('update/<int:id>',views.Update,name='update'),
    path('delete/<int:id>',views.Delete,name='delete'),
    

]