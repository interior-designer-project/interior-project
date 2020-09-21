from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views



# from .views import *
urlpatterns = [
    url(r'^$', views.List, name = 'list'),
    url(r'^dashboard',views.Interior_Designer_View, name = 'dashboard'),
    url(r'^customer_dashboard',views.Customer_Dashboard, name = 'Customer_Dashboard'),
    # url(r'^signup',views.signup ,name = "signup"),
    url(r'^signup',views.SignUp ,name = "signup"),
    url(r'^customer_signup',views.Customer_SignUp ,name = "signup_customer"),
    url(r'^customer_login',views.Customer_login_request ,name = "customer_login"),
	url(r'^login',auth_views.LoginView.as_view(),{'next_page': '/'}, name = "login"),
	url(r'^logout',auth_views.LogoutView.as_view(), {'next_page': '/'} ,name = "logout"),
	url(r'^(?P<User_id>[0-9]+)/$',views.display_professional_profile, name = 'display_profile'),
	url(r'^Overall_Price_Low_to_High', views.Overall_Price_Low_to_High, name = "Overall_Price_Low_to_High"),
	url(r'^Experience_filter',views.Experience_filter, name = "Experience_filter"),
	url(r'^Project_filter',views.Project_filter, name = "Project_filter"),
	url(r'^img',views.post, name = "img"),
	url(r'^search',views.search, name = "search"),
	url(r'^Overall_Price_High_to_Low', views.Overall_Price_High_to_Low, name = "Overall_Price_High_to_Low"),
	url(r'^news',views.Print_news, name = "Print_news"),
	url(r'^profile/edit/$', views.Edit_username, name='edit_profile'),
	# url(r'^edit_contact', views.Edit_contactno, name='edit_contact'),
	# url(r'^edit_years', views.Edit_years, name='edit_years'),
	# url(r'^edit_locality', views.Edit_locality, name='edit_locality'),
	# url(r'^edit_cost', views.Edit_cost, name='edit_cost'),
	# url(r'^edit_salary', views.Edit_salary, name='edit_salary'),
	# url(r'^edit_finsite', views.Edit_finsite, name='edit_finsite'),
	url(r'^edit_dashboard', views.edit_dashboard, name='edit'),
	url(r'^about', views.about_us_page, name='about_us_page'),
	url(r'^blog', views.blog_page, name='blog_page'),
	url(r'^contact', views.query_contact_us, name='contact_page'),
	url(r'^edit_interior_dashboard', views.edit_interior, name='edit_interior'),
	url(r'^video_page', views.showvideo, name = 'video_page'),
	url(r'^story_upload', views.Story_of_professional, name = 'story_page')

] 