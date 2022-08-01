from django.urls import path
from . import views

app_name='account'
urlpatterns = [
  
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('profile/<int:user_id>/',views.UserProfileView.as_view(),name='user_profile'),
    path('reset/',views.UserPasswordResetView.as_view(),name='password_reset'),
    path('reset/done/',views.UserPAsswordResetDonView.as_view(),name='password_reset_done'),
    path('confirm/<uidb64>/<token>/',views.UserPasswordresetConfirmView.as_view(),name='password_reset_confirm'),
    path('confirm/complete',views.UserPasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('follow/<int:user_id>',views.UserFollowView.as_view(),name='user_follow'),

    path('unfollow/<int:user_id>',views.UserUnfollowView.as_view(),name='user_unfollow'),
    path('edit_user/',views.EditUserView.as_view(),name='edit_user'),

   
   
]


