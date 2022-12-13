from django.urls import path
from myapp import views
from .import views

app_name = 'myapp'

urlpatterns = [
  path("", views.top, name="top"),
  path("search/",views.myapp_search,name="myapp_search"),
  path("<int:Restaurant_id>/",views.myapp_detail_search, name='detail_search'),
  path("<int:Menu_id>/",views.myapp_detail_search, name='detail_search'),
  path('signup/', views.SignUp.as_view(), name='signup'),
  path('login/', views.Login.as_view(), name='login'),
  path('logout/', views.Logout.as_view(), name='logout'),
  ]