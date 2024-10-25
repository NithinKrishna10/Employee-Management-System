from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'), 
    path('employee/delete/<int:emp_id>/', views.employee_delete_view, name='delete_employee'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/edit/<int:field_id>/', views.edit_field_view, name='edit_field'),
    path('settings/delete/<int:field_id>/', views.delete_field_view, name='delete_field'),
]