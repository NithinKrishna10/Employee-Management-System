from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    
    path('settings/', views.settings_view, name='settings'),
    path('settings/edit/<int:field_id>/', views.edit_field_view, name='edit_field'),
    path('settings/delete/<int:field_id>/', views.delete_field_view, name='delete_field'),
]