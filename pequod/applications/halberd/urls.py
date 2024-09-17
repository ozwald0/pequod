from django.urls import path

from .views import (usersList, 
                    userDetailView, 
                    newUserView, 
                    panelView, 
                    userUpdateView, altavariosmodelosprueba, 
                    userLevelView, userLevelDetailView, userlevelUpdateView, newuserlevelView, 
                    userstatusView, userstatusUpdateView, newuserstatusView, userstatusDetailView,
                    userTypeView, userTypeUpdateView, newusersTypeView, usersTypeDetailView, loginUser, logoutUser)

app_name = "halberd_app"

urlpatterns = [

    path('panel', panelView.as_view(), name='halberd_panel'),
    path('login', loginUser.as_view(), name='login'),
    path('logout', logoutUser.as_view(), name='logout'),
    path('users_list/', usersList.as_view(), name='users_list'),
    path('user_detail/<pk>', userDetailView.as_view(), name='user_detail'),
    path('new_user', newUserView.as_view(), name='new_user'),
    path('user_update/<pk>', userUpdateView.as_view(), name='user_update'),
    path('prueba', altavariosmodelosprueba.as_view(), name='prueba'),
    path('user_level', userLevelView.as_view(), name='user_level_list'),
    path('user_level_details/<pk>', userLevelDetailView.as_view(), name='user_level_details'),
    path('user_level_update/<pk>', userlevelUpdateView.as_view(), name='user_level_update'),
    path('new_user_level', newuserlevelView.as_view(), name='new_user_level'),
    path('user_status', userstatusView.as_view(), name='user_status_list'),
    path('user_status_details/<pk>', userstatusDetailView.as_view(), name='user_status_details'),
    path('user_status_update/<pk>', userstatusUpdateView.as_view(), name='user_status_update'),
    path('new_user_status', newuserstatusView.as_view(), name='new_user_status'),
    path('user_type', userTypeView.as_view(), name='user_type_list'),
    path('user_type_details/<pk>', usersTypeDetailView.as_view(), name='user_type_details'),
    path('user_type_update/<pk>', userTypeUpdateView.as_view(), name='user_type_update'),
    path('new_user_type', newusersTypeView.as_view(), name='new_user_type'),    
    ]
   