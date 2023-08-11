from django.urls import path

from .views import home, logout_user, register_user, customer_record, delete_redord, update_redord, add_record

urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    path('record/<int:pk>', customer_record, name="customer_record"),
    path('add_record', add_record, name="add_record"),
    path('delete/<int:pk>', delete_redord, name="delete_redord"),
    path('update/<int:pk>', update_redord, name="update_redord"),
]
