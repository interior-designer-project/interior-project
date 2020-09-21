from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . models import Profile, Profile
from . forms import *
from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .news import Web_Scraped_news
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
import csv, io
from datetime import datetime,timedelta
# import datetime
# import pytz  

from datetime import datetime, timedelta


class Display_object():
	def __init__(self, name, company_name, years_exp, lower_budget, higher_budget):
		self.name = name
		self.company_name = company_name
		self.years_exp = years_exp
		self.lower_budget = lower_budget
		self.higher_budget = higher_budget
		# self.images = images
		print(name, company_name, years_exp ,lower_budget, higher_budget)

	def set_img(self, images):
		self.images = images
		print(images)




def List(request):
	all_collections = Profile.objects.all()
	paginator = Paginator(all_collections, 3)
	# print(all_collections,"heyoo")
	# print(paginator.num_pages,"num pages")
	is_paginated = True if paginator.num_pages > 1 else False
	page = request.GET.get('page') or 1
	# print(page,"page")
	try:
	    current_page = paginator.page(page)
	except InvalidPage as e:
	    raise Http404(str(e))


	disp = []
	img = Images.objects.all()
	# k = 0
	for i in all_collections:
		disp.append(Display_object(i.name, i.company_name, i.years_exp ,i.lower_budget, i.higher_budget))

		for j in img:
			if i == j.post:
				set_img_obj = disp[-1].set_img(j.image)
		# k = k+1
				




	context = {
		'disp' : disp,
		# 'img': img,
	    'current_page': current_page,
	    'is_paginated': is_paginated,
	    'n':range(1,paginator.num_pages+1),

	}

	return render(request, 'woodrox/index.html', context)





def Interior_Designer_View(request):
	if (request.user.is_authenticated):
		user = User.objects.get(id = request.user.id)
		profile = Profile.objects.filter(user=user).get()
		images_uploaded = Images.objects.filter(post = request.user.profile)
		instance = profile
		video_of_prof = Video_upload_professional.objects.filter(post_video = request.user.profile).last()
		story_of_prof = Story_upload_professional.objects.filter(post_story = request.user.profile).last()
		current_timestamp = datetime.now()
		if story_of_prof is None:
			if video_of_prof is None:
					context = {'details' : instance, 'images' : images_uploaded}
			else:
				context = {'details' : instance, 'images' : images_uploaded, 'video': video_of_prof}
				
			return render(request, 'woodrox/display_interior_dashboard.html', context)

		else:
			if current_timestamp.date() >= story_of_prof.timestamp_of_story and current_timestamp.date() <= story_of_prof.story_expiration:
				print("STORY IS STILL WORKING")
				# print(video_of_prof)
				if video_of_prof is None:
					if story_of_prof is None:
						context = {'details' : instance, 'images' : images_uploaded}
					else:
						context = {'details' : instance, 'images' : images_uploaded, 'story': story_of_prof}
				else:
					if story_of_prof is None:
						context = {'details' : instance, 'images' : images_uploaded, 'video': video_of_prof}
					else:
						context = {'details' : instance, 'images' : images_uploaded, 'video': video_of_prof, 'story': story_of_prof}
				return render(request, 'woodrox/display_interior_dashboard.html', context) 

			else:
				story_of_prof.delete()#THIS IS TO FREE THE DB OF UNNECESSARY DATA.
				if video_of_prof is None:
						context = {'details' : instance, 'images' : images_uploaded}
				else:
					context = {'details' : instance, 'images' : images_uploaded, 'video': video_of_prof}
					
				return render(request, 'woodrox/display_interior_dashboard.html', context)
		



# def signup(request):
# 	if request.method == 'POST':
# 		form = SignupForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			raw_password = form.cleaned_data.get('password1')
# 			user = authenticate(username=username, password=raw_password)
# 			login(request, user)
# 			fname = form.cleaned_data.get('first_name')
# 			lname = form.cleaned_data.get('last_name')
# 			name = str(fname + " " + lname)
# 			contact = form.cleaned_data.get('phone_no')
# 			salary  = form.cleaned_data.get('expected_salary')
# 			total_cost = form.cleaned_data.get('overall_cost')
# 			years_exp  = form.cleaned_data.get('years')
# 			no_sites = form.cleaned_data.get('Number_sites')
# 			place  = form.cleaned_data.get('locality')
# 			img = form.cleaned_data.get('profile_image')
# 			profile = Profile(
# 				user_id = user.id,
# 				Name = name,
# 				contact_no = contact,													
# 				Years_of_experience = years_exp,
# 				Number_of_finished_projects = no_sites,
# 				Locality = place,
# 				Expected_salary = salary,
# 				Overall_cost = total_cost,
# 				profile_picture = img,
# 			)
# 			profile.save()
# 			return redirect('dashboard')
# 	else:
# 		form = SignupForm()

# 	return render(request, 'signup.html', {'form': form})




def SignUp(request):
	print("inside Professional SignUp")
	if request.method == 'POST':
		print("n3oenqe")
		form = SignupForm(request.POST, request.FILES)
		print("inside1")
		print(form.errors)
		# if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		print("inside", form.cleaned_data.get('username'))
		print(raw_password)
		user = authenticate(username=username, password=raw_password)
		login(request, user)
		fname = form.cleaned_data.get('fname')
		lname = form.cleaned_data.get('lname')
		name = str(fname + " " + lname)
		contact = form.cleaned_data.get('contact')
		email  = form.cleaned_data.get('email')
		companyName  = form.cleaned_data.get('companyName')
		companyGST  = form.cleaned_data.get('companyGST')
		streetaddres1=form.cleaned_data.get('streetaddress1')
		streetaddres2=form.cleaned_data.get('streetaddress2')
		city=form.cleaned_data.get('city')
		print(city)
		state=form.cleaned_data.get('state')
		zipcode=form.cleaned_data.get('zipcode')
		address=str(streetaddres1 +" "+streetaddres2+" "+city+" "+state+" "+zipcode)
		lower_budget = form.cleaned_data.get('lower_budget')
		higher_budget = form.cleaned_data.get('higher_budget')
		design_expertise=form.cleaned_data.get('design_expertise')
		design_area=form.cleaned_data.get('design_area')
		years_exp  = form.cleaned_data.get('years_exp')
		profileimg = form.cleaned_data.get('profileimage')
		projectimg = request.FILES.getlist('projectimage[]')
		# nproject=form.cleaned_data.get('projectname')
		facebook=form.cleaned_data.get('facebook')
		website=form.cleaned_data.get('website')
		instagram=form.cleaned_data.get('instagram')
		description=form.cleaned_data.get('description')	
		profile = Profile(
		user_id = user.id,
		name = name,
		contact_no = contact,
		email=email,
		company_name=companyName,
		company_gST  = companyGST,
		address=address,
		higher_budget = higher_budget,
		lower_budget = lower_budget,
		design_area=design_area,
		design_expertise=design_expertise,
		years_exp  = years_exp,
		name_of_project=nproject,
		profile_img = profileimg,
		# project_img=projectimg,
		facebook=facebook,
		website=website,
		instagram=instagram,	
		description=description,)
		profile.save()
		for i in projectimg:
			img_obj = Images(
						post = profile,
						image = i,
						
						)						
			img_obj.save()


		return redirect('dashboard')
	else:
		form = SignupForm()
	return render(request, 'woodrox/signup_woodrox.html' ,{'form': form})




def Customer_SignUp(request):
	print("inside Customer_SignUp")
	if request.method == 'POST':
		print("inside post")
		form = Customer_Signup_Form(request.POST, request.FILES)
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		# print("inside", form.cleaned_data.get('username'))
		# print(raw_password)
		user = authenticate(username=username, password=raw_password)
		login(request, user)
		Customer_fname = form.cleaned_data.get('Customer_fname')
		Customer_lname = form.cleaned_data.get('Customer_lname')
		Customer_name = str(Customer_fname + " " + Customer_lname)
		Customer_contact = form.cleaned_data.get('Customer_contact')
		Customer_email  = form.cleaned_data.get('Customer_email')
		Customer_address = form.cleaned_data.get('Customer_address')
		print(Customer_address)
		print(Customer_name)
		profile = Customer_Profile(
		user_id = user.id,
		customer_name = Customer_name,
		customer_contact_no = Customer_contact,
		customer_email=Customer_email,
		customer_address=Customer_address,
		)
		profile.save()

		# img_obj = Images(
		# 			post = profile,
		# 			image = projectimg,
					
		# 			)						
		# img_obj.save()


		return redirect('Customer_Dashboard')
	else:
		form = Customer_Signup_Form()
	return render(request, 'woodrox/signup_customer_woodrox.html' ,{'form': form})



def Customer_Dashboard(request):
	if (request.user.is_authenticated):
		user = User.objects.get(id = request.user.id)
		profile = Customer_Profile.objects.filter(user=user).get()
		return render(request, 'woodrox/customer_dashboard.html', {'details' : profile}) 
	



def display_professional_profile(request, User_id):
	get_data = Profile.objects.get(id = User_id)
	images = Images.objects.filter(post = get_data)
	instance = get_data
	video_of_prof = Video_upload_professional.objects.filter(post_video = get_data).last()
	if video_of_prof is None:
		context = {'details' : get_data, 'images' : images }
	else:
		context = {'details' : get_data, 'images' : images , 'video': video_of_prof}
	return render(request, 'woodrox/display_profile.html', context)



#FILTERS
def Overall_Price_Low_to_High(request):
	all_data = Profile.objects.all().order_by('-years_exp')
	# all_data = Profile.objects.all()
	paginator = Paginator(all_data, 3)
	is_paginated = True if paginator.num_pages > 1 else False
	page = request.GET.get('page') or 1
	print(page,"page")
	try:
	    current_page = paginator.page(page)
	except InvalidPage as e:
	    raise Http404(str(e))

	context = {
	    'current_page': current_page,
	    'is_paginated': is_paginated,
	    'n':range(1,paginator.num_pages+1),
	}

	return render(request, 'woodrox/index.html', context)
	

def Overall_Price_High_to_Low(request):
	all_data = Profile.objects.all()
	all_data = Profile.objects.all().order_by('-higher_budget')
	paginator = Paginator(all_data, 3)
	is_paginated = True if paginator.num_pages > 1 else False
	page = request.GET.get('page') or 1
	print(page,"page")
	try:
	    current_page = paginator.page(page)
	except InvalidPage as e:
	    raise Http404(str(e))

	context = {
	    'current_page': current_page,
	    'is_paginated': is_paginated,
	    'n':range(1,paginator.num_pages+1),
	}

	return render(request, 'woodrox/index.html', context)





def Experience_filter(request):
	all_data = Profile.objects.all().order_by('-years_exp')
	# all_data = Profile.objects.all()
	paginator = Paginator(all_data, 3)
	is_paginated = True if paginator.num_pages > 1 else False
	page = request.GET.get('page') or 1
	print(page,"page")
	try:
	    current_page = paginator.page(page)
	except InvalidPage as e:
	    raise Http404(str(e))

	context = {
	    'current_page': current_page,
	    'is_paginated': is_paginated,
	    'n':range(1,paginator.num_pages+1),
	}

	return render(request, 'woodrox/index.html', context)
	# context = context = {'current_page' : all_data}
	# return render(request, 'woodrox/index.html', context)





def Project_filter(request):
	all_data = Profile.objects.all().order_by('-Number_of_finished_projects')
	context = context = {'all_collections' : all_data}
	return render(request, 'woodrox/index.html', context)






@login_required
def post(request):
	# ImageFormSet = modelformset_factory(Images, form=ImageForm)
	# 	#'extra' means the number of photos that you can upload   ^
	# if request.method == 'POST':
	# 	print(request.FILES)
	# 	formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
	# 	print("cnqndnidnpqmdpndpqdpqnndp")
	# 	print(formset)
	# 	print("this is request post")
	# 	print(request.POST.get('image'))
	# 	if formset.is_valid():
	# 		for form in formset.cleaned_data:
	# 			if form:
	# 				print(form)
	# 				image = form.get('image')
	# 				print(image)
	# 				img_obj = Images(
	# 				post = request.user.profile,
	# 				image = image,
	# 				)						
	# 				img_obj.save()
	# 		all_collections = Images.objects.filter(post = request.user.profile)
	# 		data = Profile.objects.get(user = request.user)
	# 		return render(request, 'display_interior_dashboard.html', {'images': all_collections, 'details' : data})
	

	# 	else:
	# 		return HttpResponse("ERROR!")
	# else:
	# 	formset = ImageFormSet(queryset=Images.objects.none())
	# 	return render(request, 'img.html', {'formset': formset})



	if request.method == 'POST':
		print('inside if')
		print(request.FILES.getlist('projectiamge[]'))
		# post=Post()
		# img= request.POST.get('projectiamge')
		print(request.POST)
		image = request.FILES.getlist('projectimage[]')
		for i in image:
			img_obj = Images(
			post = request.user.profile,
			image = i,
			)						
			img_obj.save()

		# print(img_obj)
		# print(img_obj.url)
		all_collections = Images.objects.filter(post = request.user.profile)
		data = Profile.objects.get(user = request.user)
		return render(request, 'display_interior_dashboard.html', {'images': all_collections, 'details' : data})
	
	else:
		print('inside else')
		return render(request, 'img.html')




def search(request):        
	if request.method == 'GET': # this will be GET now      
		person =  request.GET.get('search') # do some research what it does 
		print(person)      
		searched_person = Profile.objects.filter(name__icontains = person) # filter returns a list so you might consider skip except part
		return render(request,'woodrox/index.html', {'current_page' : searched_person} )
	
	else:
		return render(request,"woodrox/index.html",{})





def Print_news(request):
	# context = {'news' : news}
	news = Web_Scraped_news.run()
	context = {'articles' : news}

	return render(request,'news.html',context)


def Edit_username(request):
	user = request.user
	form = EditProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
	if request.method == 'POST':
		if form.is_valid():
			username = request.POST['username']
			person = Profile.objects.get(user = user)
			print(username)
			print(person.user.username)
			person.user.username = username
			person.user.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_username.html', context)




def Edit_contactno(request):
	user = request.user
	form = EditProfileForm_contact(request.POST) #or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
	if request.method == 'POST':
		if form.is_valid():
			contact = request.POST['phone_no']
			person = Profile.objects.get(user = user)
			person.contact_no = contact
			person.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_contact.html', context)




def Edit_years(request):
	user = request.user
	form = EditProfileForm_years(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			years_exp = request.POST['years']
			person = Profile.objects.get(user = user)
			person.Years_of_experience = years_exp
			person.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_years.html', context)






def Edit_locality(request):
	user = request.user
	form = EditProfileForm_locality(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			area = request.POST['locality']
			person = Profile.objects.get(user = user)
			person.Locality = area
			person.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_locality.html', context)





def Edit_cost(request):
	user = request.user
	form = EditProfileForm_cost(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			cost = request.POST['overall_cost']
			person = Profile.objects.get(user = user)
			person.Overall_cost = cost
			person.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_cost.html', context)





def Edit_salary(request):
	user = request.user
	form = EditProfileForm_salary(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			sal = request.POST['expected_salary']
			person = Profile.objects.get(user = user)
			person.Expected_salary = sal
			person.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_salary.html', context)





def Edit_finsite(request):
	user = request.user
	form = EditProfileForm_finsite(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			n = request.POST['Number_sites']
			person = Profile.objects.get(user = user)
			person.Number_of_finished_projects = n
			person.save()
			# profile = Profile(
			# Name = name,

			# )   
			# profile.save()
			return redirect('list')

	context = {'form' : form}
	return render(request, 'Edit/edit_finsite.html', context)




def edit_dashboard(request):
	if (request.user.is_authenticated):
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.filter(user=user).get()
		instance = profile
		images_uploaded = Images.objects.filter(post = request.user.profile)
		# instance = profile
		return render(request, 'woodrox/edit_dashboard.html', {'details' : instance,'images' : images_uploaded})


def query_contact_us(request):
	user = request.user
	if user.id == None:
		pass
	else:
		person = Profile.objects.get(user = user)#this is to get email id of the person who is logged in.
	form = query_form(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			text_query = request.POST['query_text_form']
			contact_Form = Query_contact_us(
					query = request.user.profile,
					query_text = text_query,
					
					)						
			contact_Form.save()

			if request.method == 'POST':
				#https://myaccount.google.com/lesssecureapps
				# ALLOW THE LESS SECURE APPS TO ACCESS
				send_mail('from python',text_query, settings.EMAIL_HOST_USER, ['heeketmehta@gmail.com'], fail_silently=False)
			return redirect('list')

	context = {'form' : form}
	return render(request, 'woodrox/contact.html', context)


def about_us_page(request):
	return render(request, 'woodrox/about-us.html')

def blog_page(request):
	return render(request, 'woodrox/blog.html')

def contact_page(request):
	return render(request, 'woodrox/contact.html')



def edit_interior(request):
	if (request.user.is_authenticated):
		user = request.user
		person = Profile.objects.get(user = user)
		person.contact_no = request.POST.get('contact_no')
		person.email  = request.POST.get('email')
		person.company_name  = request.POST.get('company_name')
		person.company_gST  = request.POST.get('company_gST')
		person.address = request.POST.get('address')
		person.lower_budget = request.POST.get('lower_budget')
		person.higher_budget = request.POST.get('higher_budget')
		person.design_expertise= request.POST.get('design_expertise')
		person.design_area=request.POST.get('design_area')
		person.years_exp  = request.POST.get('years_exp')
		# person.profileimg = request.POST.get('profileimage')
		# person.projectimg = request.POST.get('projectimage')
		person.name_of_project=request.POST.get('name_of_project')
		person.facebook=request.POST.get('facebook')
		person.website=request.POST.get('website')
		person.instagram=request.POST.get('instagram')
		person.description=request.POST.get('description')
		person.save()
		
	return redirect('dashboard')


# def upload_csv(request):
# 	data = {}
# 	if "GET" == request.method:
# 		return render(request, "upload_csv.html", data)
#     # if not GET, then proceed
# 	try:
# 		csv_file = request.FILES["csv_file"]
# 		if not csv_file.name.endswith('.csv'):
# 			messages.error(request,'File is not CSV type')
# 			return HttpResponseRedirect(reverse("myapp:upload_csv"))
#         #if file is too large, return
# 		if csv_file.multiple_chunks():
# 			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
# 			return HttpResponseRedirect(reverse("myapp:upload_csv"))

# 		file_data = csv_file.read().decode("utf-8")		

# 		lines = file_data.split("\n")
# 		#loop over the lines and save them in db. If error , store as string and then display
# 		for line in lines:						
# 			fields = line.split(",")
# 			data_dict = {}
# 			data_dict["Hours"] = fields[0]
# 			data_dict["Scores"] = fields[1]
# 			# data_dict["end_date_time"] = fields[2]
# 			# data_dict["notes"] = fields[3]
# 			try:
# 				form = EventsForm(data_dict)
# 				if form.is_valid():
# 					form.save()					
# 				else:
# 					logging.getLogger("error_logger").error(form.errors.as_json())												
# 			except Exception as e:
# 				logging.getLogger("error_logger").error(repr(e))					
# 				pass

# 	except Exception as e:
# 		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
# 		messages.error(request,"Unable to upload file. "+repr(e))

# 	return HttpResponseRedirect(reverse("upload_csv"))


def Customer_login_request(request):
	# print("envorenununurn c4v ")
	if request.method == 'POST':
		print("inside post")
		form = Customer_Login_Form(request.POST, request.FILES)
		print(form.errors)
		if form.is_valid():
			print("insinde is VALID")
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print("USERNAME IS  ----- ", username)
			print("PASSWORD IS ------", password)
			user = authenticate(username=username, password=password)
			if user is not None:
				print("inside user not none")
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('Customer_Dashboard')
			else:
				messages.error(request, "Invalid username or password.")
		# else:
		# 	messages.error(request, "Invalid username or password.")
	else:
		form = Customer_Login_Form()
	return render(request = request, template_name = "woodrox/customer_login.html",
				context={"form":form})




def showvideo(request):
	if request.method == 'POST':
		# print("in post")
		form= VideoForm(request.POST or None, request.FILES or None)
		print(form.is_valid())
		if form.is_valid():
			person_of_video = Video_upload_professional.objects.filter(post_video = request.user.profile)
			# print(person_of_video)
			if person_of_video == None:
				pass
			else:
				person_of_video.delete()
			videofile = form.cleaned_data.get('videofile')
			video = Video_upload_professional(
				videofile = videofile,
				post_video = request.user.profile,
				)
			video.save()
			# form.save()
			return redirect('dashboard')
	else:
		form = VideoForm(request.POST or None, request.FILES or None)

	    
	context= {'form': form}
	return render(request, 'woodrox/video.html', context)




def Story_of_professional(request):
	if request.method == 'POST':
		# print("in post")
		form= Story_Form(request.POST or None, request.FILES or None)
		print(form.is_valid())
		if form.is_valid():
			story_data = form.cleaned_data.get('story')
			time_now = datetime.now()
			twentyfour_hours_from_now = datetime.now() + timedelta(hours=48)
			story_feature = Story_upload_professional(
				post_story = request.user.profile,
				story = story_data,
				timestamp_of_story = time_now,
				story_expiration = twentyfour_hours_from_now,
				)
			story_feature.save()
			return redirect('dashboard')
	else:
		form = Story_Form(request.POST or None, request.FILES or None)

	    
	context= {'form': form}
	return render(request, 'woodrox/story_upload.html', context)
