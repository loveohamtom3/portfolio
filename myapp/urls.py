from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views 

app_name = 'myapp'

urlpatterns = [
  path("", views.base, name="base"),
  path("search/",views.myapp_search,name="myapp_search"),
  path("<int:Restaurant_id>/",views.myapp_detail, name='detail'),
  path("<int:Menu_id>/",views.myapp_detail, name='detail'),
  path('signup/',views.SignUp.as_view(), name='signup'),
  path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
  path('logout/',views.Logout.as_view(), name='logout'),
  path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),
  path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),
  ]