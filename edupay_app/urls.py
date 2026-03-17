from django.urls import path
from . import views
from .views import admin_login
from django.urls import path
from . import views
from .views import vendor_login



urlpatterns = [

    # Admin
    path('admin/login/', admin_login),

    # Students
    path('students/', views.get_students),
    path('students/add/', views.add_student),
    path('students/update/<int:id>/', views.update_student),
    path('students/delete/<int:id>/', views.delete_student),

    # Vendors
    path('vendors/', views.get_vendors),
    path('vendors/add/', views.add_vendor),
    path('vendors/update/<int:id>/', views.update_vendor),
    path('vendors/delete/<int:id>/', views.delete_vendor),
    path('vendors/status/<int:id>/', views.toggle_vendor_status),

    # Parents
    path('parents/', views.get_parents),
    path('parents/add/', views.add_parent),
    path('parents/delete/<int:id>/', views.delete_parent),

    path('check-parent-email/', views.check_parent_email),
    path('get-student-details/', views.get_student_details),
    path('add-money/', views.add_money),
path('vendor-login/', vendor_login),



]


