from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
]
