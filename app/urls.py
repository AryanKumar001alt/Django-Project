from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('form/', views.fill_form, name='form'),

    path('edit/<int:id>/', views.edit_form, name='edit'),

    path('approve/<int:id>/', views.approve_form, name='approve'),
    path('reject/<int:id>/', views.reject_form, name='reject'),
    path('delete/<int:id>/', views.delete_form, name='delete'),

    path('logout/', views.logout_view, name='logout'),
]