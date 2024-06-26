from django.urls import path

from api_users.views import AccessView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('token/', AccessView.as_view(), name='access_token'),
]
