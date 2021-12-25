from django.urls import path
from . import views

urlpatterns = [
    path('product_register/', views.PostProduct, name='register-product')
]
