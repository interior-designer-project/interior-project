from django.http import HttpResponse
from . models import Profile, Profile
from . forms import *
from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .news import Web_Scraped_news
from django.shortcuts import get_object_or_404

def List(request):
	all_collections = Profile.objects.all()
	context = {'all_collections' : all_collections}
	return render (request , 'list.html', context)




def Interior_Designer_View(request):
	if (request.user.is_authenticated):
		user = User.objects.get(id = request.user.id)
		profile = Profile.objects.filter(user=user).get()
		images_uploaded = Images.objects.filter(post = request.user.profile)
		instance = profile
		return render(request, 'display_interior_dashboard.html', {'details' : instance, 'images' : images_uploaded}) 
	



def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			fname = form.cleaned_data.get('first_name')
			lname = form.cleaned_data.get('last_name')
			name = str(fname + " " + lname)
			contact = form.cleaned_data.get('phone_no')
			salary  = form.cleaned_data.get('expected_salary')
			total_cost = form.cleaned_data.get('overall_cost')
			years_exp  = form.cleaned_data.get('years')
			no_sites = form.cleaned_data.get('Number_sites')
			place  = form.cleaned_data.get('locality')
			img = form.cleaned_data.get('profile_image')
			profile = Profile(
				user_id = user.id,
				Name = name,
				contact_no = contact,													
				Years_of_experience = years_exp,
				Number_of_finished_projects = no_sites,
				Locality = place,
				Expected_salary = salary,
				Overall_cost = total_cost,
				profile_picture = img,
			)
			profile.save()
			return HttpResponse("Thank you for registering")
	else:
		form = SignupForm()

	return render(request, 'signup.html', {'form': form})







def display_profile(request, User_id):
	get_data = Profile.objects.get(id = User_id)
	images = Images.objects.filter(post = get_data)
	return render(request, 'display_profile.html', {'details' : get_data, 'images' : images})

#FILTERS
def Overall_Price_Low_to_High(request):
	all_data = Profile.objects.all()
	all_data = Profile.objects.all().order_by('Overall_cost')
	context = {'all_collections' : all_data}
	return render(request, 'list.html', context)




def Overall_Price_High_to_Low(request):
	all_data = Profile.objects.all()
	all_data = Profile.objects.all().order_by('-Overall_cost')
	context = {'all_collections' : all_data}
	return render(request, 'list.html', context)





def Experience_filter(request):
	all_data = Profile.objects.all().order_by('-Years_of_experience')
	context = context = {'all_collections' : all_data}
	return render(request, 'list.html', context)





def Project_filter(request):
	all_data = Profile.objects.all().order_by('-Number_of_finished_projects')
	context = context = {'all_collections' : all_data}
	return render(request, 'list.html', context)






@login_required
def post(request):
	ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=2)
		#'extra' means the number of photos that you can upload   ^
	if request.method == 'POST':
		formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
		if formset.is_valid():
			for form in formset.cleaned_data:
				if form:
					# return HttpResponse("IN VALID IF")
					image = form.get('image')
					img_obj = Images(
					post = request.user.profile,
					image = image,
					
					)						
					img_obj.save()
					# print(img_obj)
					# print(img_obj.url)



			all_collections = Images.objects.filter(post = request.user.profile)
			data = Profile.objects.get(user = request.user)
					# image = form['image']
					# photo = Images(image=image)
					# photo.save()
			return render(request, 'display_interior_dashboard.html', {'images': all_collections, 'details' : data})
		

		else:
			return HttpResponse("ERROR!")
	else:
		formset = ImageFormSet(queryset=Images.objects.none())
		return render(request, 'img.html', {'formset': formset})





def search(request):        
	if request.method == 'GET': # this will be GET now      
		person =  request.GET.get('search') # do some research what it does       
		searched_person = Profile.objects.filter(Name__icontains = person) # filter returns a list so you might consider skip except part
		return render(request,'list.html', {'all_collections' : searched_person} )
	
	else:
		return render(request,"list.html",{})





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
		return render(request, 'Edit/edit_dashboard.html', {'details' : instance}) 




