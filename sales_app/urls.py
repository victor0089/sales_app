"""
URL configuration for sales_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import add_sale, add_product, add_customer, add_branch, add_accounting, add_expense, expenses_list
from .views import add_general_journal, general_journals_list, add_ledger, ledgers_list, add_trial_balance, trial_balances_list
from .views import add_income_summary, income_summaries_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-sale/', add_sale.site.urls, name='add_sale'),
    path('add-product/', add_product.site.urls, name='add_product'),
    path('add-customer/', add_customer.site.urls, name='add_customer'),
    path('add-branch/', add_branch.site.urls, name='add_branch'),
    path('add-accounting/', add_accounting.site.urls, name='add_accounting'),
    path('add-expense/', add_expense.site.urls, name='add_expense'),
    path('expenses-list/', expenses_list.site.urls, name='expenses_list'),
    path('add-general-journal/', add_general_journal.site.urls, name='add_general_journal'),
    path('general-journals-list/', general_journals_list.site.urls, name='general_journals_list'),
    path('add-ledger/', add_ledger.site.urls, name='add_ledger'),
    path('ledgers-list/', ledgers_list.site.urls, name='ledgers_list'),
    path('add-trial-balance/', add_trial_balance.site.urls, name='add_trial_balance'),
    path('trial-balances-list/', trial_balances_list.site.urls, name='trial_balances_list'),
    path('add-income-summary/', add_income_summary.site.urls, name='add_income_summary'),
    path('income-summaries-list/', income_summaries_list.site.urls, name='income_summaries_list'),
    # Add URLs for other views
]
]
