from django.urls import path, include

from apps.account.views import LoginView, LogoutView, UserMeView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user/me/', UserMeView.as_view())
]
