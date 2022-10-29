from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('login', views.LoginView.as_view(), name='login'),
    path('create_an_account', views.RegisterView.as_view(), name='new_account')
]
