from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('index/', views.index, name='index'),
    path('new_user/', views.new_user, name='new_user'),
    path('user/', views.user, name='user'),
    path('user_edit/<int:pk>/', views.user_edit, name='user_edit'),
    path('user_block/<int:pk>/', views.user_block, name='user_block'),
    path('user_delete/<int:pk>/', views.user_delete, name='user_delete'),

    path('user_login/', views.user_login, name='user_login'),
    path('dashbord/', views.dashbord, name='dashbord'),

    path('charts/', views.charts, name='charts'),
    path('info/', views.info, name='info'),
    # path('funds/', views.funds, name='funds'),

    path('profile/', views.profile, name='profile'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('transfer/', views.transfer, name='transfer'),
    path('send-funds/', views.send_funds, name="send-funds")

    # path('varify/<int:pk>/', views.varify, name='varify'),
]


