from django.urls import path
from .views import index, contact, product


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product')
]