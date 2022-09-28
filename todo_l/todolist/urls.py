from django.urls import path
from . import views
urlpatterns = [
    path('', views.insert_task, name='home'),
    path('<int:pk>/', views.delete_task, name='delete_task'),
    path('update/<int:pk>', views.update_task, name='update_task'),
    path('signup/', views.user_register, name='signup'),
    path('login/', views.user_login, name='login')
]