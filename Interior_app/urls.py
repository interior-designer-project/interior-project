from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views



# from .views import *
urlpatterns = [
    url(r'^$', views.List, name = 'list'),
    url(r'^dashboard',views.Interior_Designer_View, name = 'dashboard'),
    url(r'^signup',views.signup ,name = "signup"),
	url(r'^login',auth_views.LoginView.as_view(),{'next_page': '/'}, name = "login"),
	url(r'^test', views.test, name = "test"),
	url(r'^logout',auth_views.LogoutView.as_view(), {'next_page': '/'} ,name = "logout"),
	url(r'^(?P<User_id>[0-9]+)/$',views.display_profile, name = 'display_profile'),
	url(r'^Overall_Price_Low_to_High', views.Overall_Price_Low_to_High, name = "Overall_Price_Low_to_High"),
	url(r'^Experience_filter',views.Experience_filter, name = "Experience_filter"),
	url(r'^Project_filter',views.Project_filter, name = "Project_filter"),
	url(r'^img',views.post, name = "img"),
	url(r'^search',views.search, name = "search"),
	url(r'^Overall_Price_High_to_Low', views.Overall_Price_High_to_Low, name = "Overall_Price_High_to_Low"),
	url(r'^news',views.Print_news, name = "Print_news"),
	# url(r'^search',views.post, name = "img"),
] 