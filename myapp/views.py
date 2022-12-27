from audioop import reverse
from django.views.generic import CreateView,DetailView,UpdateView
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404,resolve_url
from .models import Restaurants,Menu,Review
from .forms import SignUpForm,LoginForm,ReviewForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import UserForm

# Create your views here.

def base(request):
    return render(request, 'base.html')
  

def myapp_search(request):
    # session
    request.session['aaa'] = 'keyword'
    keyword = request.GET.get('keyword')
    request.session['aaa'] = keyword
    session_data = request.session['aaa']

    # search
    restaurants = Restaurants.objects.all().order_by('-id')
    menu = Menu.objects.all().order_by('-id')
    """ 検索機能の処理 """
    if keyword:
        keywords = keyword.split()
        for k in keywords:
            restaurants = Restaurants.objects.filter(
                Q(name__icontains=k) |
                Q(description__icontains=k) |
                Q(address__icontains=k)
            )
    else:
        restaurants = Restaurants.objects.filter(
            Q(name__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(address__icontains=keyword)
        )
        print("aaa")
        print([a.name for a in restaurants])
        messages.success(request, '「{}」の検索結果'.format(keyword))
    
    param = {
      'myapp':restaurants,
      'keyword':session_data,
    }
    return render(request, 'myapp/search.html', param)
  

def myapp_detail(request, Restaurant_id):
    restaurant = get_object_or_404(Restaurants, pk=Restaurant_id)
    menus = Menu.objects.filter(
        Q(restaurant_id=Restaurant_id)
    )
    print(menus)
    
    review_list = Review.objects.all()[:10]
    review_count = Review.objects.filter(restaurant_id=Restaurant_id).count()
    score_ave = Review.objects.filter(restaurant_id = Restaurant_id).aggregate(Avg('score'))
    average = score_ave['score__avg']
    if average:
        average_rate = average / 5 * 100
    else:
        average_rate = 0

    if request.method == 'GET':        
       review_form = ReviewForm()
       review_list = Review.objects.filter(restaurant_id = Restaurant_id)
    else:
        form = ReviewForm(data=request.POST)
        score = request.POST['score']
        comment = request.POST['comment']
        
        if form.is_valid():
            review = Review()
            review.restaurant_id = Restaurant_id
            review.restaurant_name  
            review.user = request.user
            review.score = score
            review.comment = comment
            review.save()
            return redirect(reverse('myapp:detail.html',Restaurant_id))
        return render(request, 'myapp/detail.html', {})
    params = {
    'title': '店舗詳細',
    'review_count': review_count,
    'review_form': review_form,
    'review_list': review_list,
    'average': average,
    'average_rate': average_rate,
    'review_list': review_list,
    'restaurant': restaurant,
    'menus' : menus
    }
    return render(request, 'myapp/detail.html',params)
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'myapp/signup.html'

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(name=username, password=raw_password)
            login(request, user)
            return redirect('myapp:base')
        return render(request, 'myapp/signup.html', {'form': form})


def LoginView(request):
    print('ppp')
    if request.method == 'POST':
        print('ccc')
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
        if user:
            login(request, user)
        if next == 'None':
            print('aaa')
            return redirect(to='myapp/signup.html')
        else:
            print('bbb')
            return redirect(to=next)
    else:
        form = LoginForm()
        next = request.GET.get('next')
    
    param = {
        'form': form,
        'next': next,
    }
    return render(request, 'myapp/login.html', param)


class Logout(LogoutView):
    template_name = 'myapp/logout.html'
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser   
class UserDetailView(DetailView):
    model = User
    template_name = "myapp/users/user_detail.html"

class UserUpdateView(OnlyYouMixin,UpdateView):
  model = User
  template_name = "myapp/users/update.html"
  form_class = UserForm
  
  def get_success_url(self): 
    return resolve_url('myapp/users_detail',pk=self.kwargs['pk'])
