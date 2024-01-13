# sales/views.py

from django.shortcuts import render, redirect
from .models import Product, Customer, Sale, Inventory, Branch, Accounting, Expense, GeneralJournal, JournalEntry
from .models import Ledger, TrialBalance, IncomeSummary, Deposit, Withdraw, CashDiscount, SalesReturnsAllowances
from .models import Purchases, PurchasesReturnsAllowances, NotesReceivable, AccountsReceivable, InventoryAdjustingEntry, AdjustingEntry
from .forms import SaleForm, ProductForm, CustomerForm, ExpenseForm, GeneralJournalForm, JournalEntryForm
from .forms import LedgerForm, TrialBalanceForm, IncomeSummaryForm, DepositForm, WithdrawForm, CashDiscountForm, SalesReturnsAllowancesForm
from .forms import PurchasesForm, PurchasesReturnsAllowancesForm, NotesReceivableForm, AccountsReceivableForm, InventoryAdjustingEntryForm, AdjustingEntryForm

def add_income_summary(request):
    if request.method == 'POST':
        form = IncomeSummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_summaries_list')
    else:
        form = IncomeSummaryForm()

    return render(request, 'sales/add_income_summary.html', {'form': form})

def income_summaries_list(request):
    summaries = IncomeSummary.objects.all()
    return render(request, 'sales/income_summaries_list.html', {'summaries': summaries})

def add_branch(request):
    if request.method == 'POST':
        # Handle form submission and add branch to the database
        # Remember to validate the form data and handle errors
        # ...

    return render(request, 'sales/add_branch.html')

def add_accounting(request):
    if request.method == 'POST':
        # Handle form submission and add accounting record to the database
        # Remember to validate the form data and handle errors
        # ...

    return render(request, 'sales/add_accounting.html')

# Implement views for other modules similarly
def add_ledger(request):
    if request.method == 'POST':
        form = LedgerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledgers_list')
    else:
        form = LedgerForm()

    return render(request, 'sales/add_ledger.html', {'form': form})

def ledgers_list(request):
    ledgers = Ledger.objects.all()
    return render(request, 'sales/ledgers_list.html', {'ledgers': ledgers})

def add_trial_balance(request):
    if request.method == 'POST':
        form = TrialBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trial_balances_list')
    else:
        form = TrialBalanceForm()

    return render(request, 'sales/add_trial_balance.html', {'form': form})

def trial_balances_list(request):
    trial_balances = TrialBalance.objects.all()
    return render(request, 'sales/trial_balances_list.html', {'trial_balances': trial_balances})

# Implement views for other financial statements similarly
