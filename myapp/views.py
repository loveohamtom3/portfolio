from http.client import HTTPResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from .forms import SearchForm

from myapp.models import Restaurants

# Create your views here.

def top(request):
    return render(request,'myapp/top.html')

def myapp_new(request):
    return HTTPResponse('登録')

def myapp_edit(request,myapp_id):
    return HTTPResponse('編集')

def myapp_detail(request,myapp_id):
    return HTTPResponse('詳細閲覧')

def myapp_search(request):
    restaurants = Restaurants.objects.order_by('-id')
    if request.method == 'GET':
       searchform = SearchForm(request.POST)
    """ 検索機能の処理 """
    print("aaa")
    print([a.name for a in restaurants])

    keyword = request.GET.get('keyword')

    if keyword:
        restaurants = restaurants.filter(
                 Q(name__icontains=keyword),
               ).all()
        print([a.name for a in restaurants])
        messages.success(request, '「{}」の検索結果'.format(keyword))

    return render(request, 'myapp/search.html', {'myapp': restaurants })
