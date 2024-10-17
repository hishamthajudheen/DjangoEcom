from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register'),
    path("product/<int:pk>", views.product, name='product'),
    path("category/<str:foo>", views.category, name='category'),
    
]

