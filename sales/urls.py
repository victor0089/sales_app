# sales/urls.py

from django.urls import path
from .views import add_sale, add_product, add_customer, add_branch, add_accounting

urlpatterns = [
    path('add-sale/', add_sale, name='add_sale'),
    path('add-product/', add_product, name='add_product'),
    path('add-customer/', add_customer, name='add_customer'),
    path('add-branch/', add_branch, name='add_branch'),
    path('add-accounting/', add_accounting, name='add_accounting'),
    # Add URLs for other views
]

