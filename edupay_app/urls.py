from django.urls import path
from . import views
from .views import admin_login

urlpatterns = [

    path('admin/login/', admin_login),
     path('students/', views.get_students),
    path('students/add/', views.add_student),
    path('students/update/<int:id>/', views.update_student),
    path('students/delete/<int:id>/', views.delete_student),
    path('vendors/', views.get_vendors),
    path('vendors/add/', views.add_vendor),
    path('vendors/update/<int:id>/', views.update_vendor),
    path('vendors/delete/<int:id>/', views.delete_vendor),
    path('parents/', views.get_parents),
    path('parents/add/', views.add_parent),
    path('parents/delete/<int:id>/', views.delete_parent),
    
]


