from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerSearchForm

# Create your views here.
# 管理メニュー
def MainMenu(request):
    params = {
        'mainTitle':'管理システム',
        'title':'管理メニュー',
    }
    return render(request, 'app/MainMenu.html', params)

# 得意先管理メニュー
def CustomerManagementMenu(request):
    params = {
        'mainTitle':'管理システム',
        'title':'得意先管理メニュー',
    }
    return render(request, 'app/CustomerManagementMenu.html', params)

# 得意先一覧
def CustomerList(request):
    data = Customer.objects.all()
    params = {
        'mainTitle':'管理システム',
        'title':'得意先一覧',
        'data': data,
    }
    return render(request, 'app/CustomerList.html', params)

# 得意先検索
def CustomerSearch(request):
    params = {
        'mainTitle':'管理システム',
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

# 得意先登録
def CustomerRegist(request):
    return HttpResponse("得意先登録")

# 得意先削除
def CustomerDelete(request):
    return HttpResponse("得意先削除")

# 得意先更新
def CustomerUpdate(request):
    return HttpResponse("得意先更新")

# 仮実装ログアウト(得意先検索画面にボタンの実装があるため)
def Logout(request):
    return HttpResponse("ログアウト")