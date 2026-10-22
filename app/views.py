from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerSearchForm

# Create your views here.
# 得意先管理メニュー
def CustomerManagementMenu(request):
    params = {
        'title':'得意先管理メニュー',
    }
    return render(request, 'app/CustomerManagementMenu.html', params)

# 得意先検索
def CustomerSearch(request):
    params = {
        'title':'得意先検索',
        'form': CustomerSearchForm(),
        'data': [],
    }
    if(request.method == "POST"):
        char = request.POST['customer_code']
        params['data'] = Customer.objects.filter(
            customer_code = char
        )
        params['form'] = CustomerSearchForm(request.POST)
    return render(request, 'app/CustomerSearch.html', params)