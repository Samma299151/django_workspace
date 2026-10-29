# アプリケーション作成
python manage.py startapp app

## URL初期設定
1. 作成したアプリケーションに「urls.py」を追加
1. 作成したurls.pyにインポートなどを記述
```Python
from django.urls import path
urlpatterns = []
```
1. cconfig/urls.pyに移動し、内容を変更
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]

```
## HTMl初期設定
app配下に「templates」フォルダを作成し、その中に「app」フォルダを作成

## setting.py設定
appを追加する
```python
INSTALLED_APPS = [
...
'app',]
```


# 検索機能追加

## URL設定と画面表示
1. app/urls.pyに下記内容を追加
```python
urlpatterns =[
    path('CustomerManagementMenu', views.CustomerManagementMenu, name='CustomerManagementMenu'),
    path('CustomerSearch', views.CustomerSearch, name='CustomerSearch'),
]
```

1. app/views.pyに内容を追加(画面が表示されるかの確認)
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 得意先管理メニュー
def CustomerManagementMenu(request):
    return HttpResponse("得意先管理メニュー")

# 得意先検索
def CustomerSearch(request):
    return HttpResponse("得意先検索メニュー")
```

1. サーバーを動かし、該当URLで画面が表示されるかを確認する

## 得意先管理メニュー⇔得意先検索の遷移を追加する

### HTMLを使用しての画面表示P70
1. HTMLを作成する
1. app/templates/app配下にそれぞれのHTMLを作成する
1. h1タグで適当な文字を入力する
1. app/views.pyで関数の中身を書き換える
```python
def CustomerManagementMenu(request):
    return render(request, 'app/CustomerManagementMenu.html')
```
1. 画面が表示されているかを確認する

### ボタンを追加して画面遷移を行うP75
1. HTMLを修正する→{{title}}などに書き換えを行う
1. onclickでURLを追加
url名を使用することでURLの変更に対応
```html
    <button onclick="location.href='{% url 'CustomerManagementMenu' %}'">
        得意先管理メニュー
    </button>
```
エラーが出るけど遷移できているので問題ない

1. app/views.pyの関数を修正する
```python
def CustomerManagementMenu(request):
    params = {
        'title':'得意先管理メニュー',
    }
    return render(request, 'app/CustomerManagementMenu.html', params)

```

## DBからデータを全件取得する(P138~141参照)

### モデルを作成する
1. models.pyを作成する
1. Customerモデルを作成
**設計書の型、桁数に従って作成すること**
```python
class Customer(models.Model):
    customer_code = models.CharField(
        max_length=6,
        primary_key=True)
    customer_name = models.CharField(max_length=20)
    customer_telno = models.CharField(max_length=13)
    customer_postalcode = models.CharField(max_length=8)
    customer_address = models.CharField(max_length=40)
    class Meta:
        db_table = 'customer'
```

### views.pyを書き換えて全件取得する
```python
def CustomerSearch(request):
    data = Customer.objects.all()
    params = {
        'mainTitle':'管理システム',
        'title':'得意先検索',
        'data': data,
    }
    return render(request, 'app/CustomerList.html', params)
```