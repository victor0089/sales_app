# sales/urls.py

from django.urls import path
from .views import add_sale, add_product, add_customer, add_branch, add_accounting, add_expense, expenses_list
from .views import add_general_journal, general_journals_list, add_ledger, ledgers_list, add_trial_balance, trial_balances_list
from .views import add_income_summary, income_summaries_list

urlpatterns = [
    path('add-sale/', add_sale, name='add_sale'),
    path('add-product/', add_product, name='add_product'),
    path('add-customer/', add_customer, name='add_customer'),
    path('add-branch/', add_branch, name='add_branch'),
    path('add-accounting/', add_accounting, name='add_accounting'),
    path('add-expense/', add_expense, name='add_expense'),
    path('expenses-list/', expenses_list, name='expenses_list'),
    path('add-general-journal/', add_general_journal, name='add_general_journal'),
    path('general-journals-list/', general_journals_list, name='general_journals_list'),
    path('add-ledger/', add_ledger, name='add_ledger'),
    path('ledgers-list/', ledgers_list, name='ledgers_list'),
    path('add-trial-balance/', add_trial_balance, name='add_trial_balance'),
    path('trial-balances-list/', trial_balances_list, name='trial_balances_list'),
    path('add-income-summary/', add_income_summary, name='add_income_summary'),
    path('income-summaries-list/', income_summaries_list, name='income_summaries_list'),
    # Add URLs for other views
]

