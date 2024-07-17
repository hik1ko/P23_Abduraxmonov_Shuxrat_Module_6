from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import CustomLoginView, RegistrationView, ProductListView, ProfileFormView, CategoryListView, \
    ProductDetailView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    path('product', ProductListView.as_view(), name='products'),
    path('profile', ProfileFormView.as_view(), name='profile'),
    path('home', CategoryListView.as_view(), name='home'),
    path('detail', ProductDetailView.as_view(), name='detail'),
    path('', LogoutView.as_view(), name='logout'),

]
