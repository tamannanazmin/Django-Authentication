from django.urls import path
from account.views import UserPasswordResetView, SendPasswordResetEmailView, UserChangePasswordView, UserRegistrationView, UserLoginView, UserProfileView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('profile/', UserProfileView.as_view(), name = 'profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name = 'changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name = 'send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name = 'reset-password'),

]
'''
for register/ api
type: post
Headers: 
1. KEY: Accept  
   VALUE: application/json
body: {
    "email" : "naz10@gmail.com",
    "name" : "naznin10",
    "password" : "123456",
    "password2" : "123456",
    "tc" : "True"
}


for login/ api
type: post
Headers: 
1. KEY: Accept  
   VALUE: application/json
body: {
    "email" : "tamanna.naz98@gmail.com",
    "password" : "123456"
}


for profile/ api
type: get
Headers: 
1. KEY: Accept  
   VALUE: application/json
2. KEY: Authorization
   VALUE: Bearer Token


for changepassword/ api
type: post
Headers: 
1. KEY: Accept  
   VALUE: application/json
2. KEY: Authorization
   VALUE: Bearer Token
body: {
    "password" : "new",
    "password2" : "new"
}

for send-reset-password-email/ api
type: post
Headers: 
1. KEY: Accept  
   VALUE: application/json
body: {
    "email" : "tamanna.naz98@gmail.com"
}

for reset-password/<uid>/<token>/ api
type: post
Headers: 
1. KEY: Accept  
   VALUE: application/json
body: {
    "password" : "123456",
    "password2" : "123456"
}
'''