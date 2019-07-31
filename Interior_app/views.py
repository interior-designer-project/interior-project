from django.http import HttpResponse
from . models import Profile, Profile
from . forms import *
from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from nltk.tokenize import word_tokenize
from .news import Web_Scraped_news

def List(request):
	all_collections = Profile.objects.all()
	context = {'all_collections' : all_collections}
	return render (request , 'list.html', context)




def Interior_Designer_View(request):
	if (request.user.is_authenticated):
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.filter(user=user).get()
		instance = profile
		return render(request, 'display_interior_dashboard.html', {'details' : instance})
	



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





def test(request):
	return HttpResponse("login works")


def display_profile(request, User_id):
	get_data = Profile.objects.get(id = User_id)
	return render(request, 'display_profile.html', {'details' : get_data})

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
	ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=5)
		#'extra' means the number of photos that you can upload   ^
	if request.method == 'POST':
		formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
		if formset.is_valid():
			for form in formset.cleaned_data:
				if form:
					image = form['image']
					photo = Images(post=post_form, image=image)
					photo.save()
					messages.success(request, "Yeeew, check it out on the home page!")
					return HttpResponseRedirect("/")
		else:
			print(formset.errors)
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








# def Edit_Profile_Information(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	if request.method == "POST":
# 		form = EditProfileForm(request.POST, instance=post)
# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.author = request.user
# 			post.save()
# 			userName = form.cleaned_data.get('username')
# 			salary  = form.cleaned_data.get('expected_salary')
# 			total_cost = form.cleaned_data.get('overall_cost')
# 			years_exp  = form.cleaned_data.get('years')
# 			no_sites = form.cleaned_data.get('Number_sites')
# 			place  = form.cleaned_data.get('locality')
# 			profile = Profile(
				
# 				user_id = user.id,
# 				Years_of_experience = years_exp,
# 				Number_of_finished_projects = no_sites,
# 				Locality = place,
# 				Expected_salary = salary,
# 				Overall_cost = total_cost,
# 				username = userName,

# 				)
# 			profile.save()
# 			return redirect('dashboard', pk=post.pk)
# 		else:
# 			form = EditProfileForm(instance=post)
# 			return render(request, 'edit.html', {'form': form})



def Print_news(request):
	# context = {'news' : news}
	news = Web_Scraped_news.run()
	context = {'articles' : news}

	return render(request,'news.html',context)


	