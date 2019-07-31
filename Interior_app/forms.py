from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.core.files.images import get_image_dimensions

class SignupForm(UserCreationForm):
	username = forms.CharField(label='Username', max_length=100)
	first_name = forms.CharField(label='First Name', max_length=32, required=False)
	last_name = forms.CharField(label='Last Name', max_length=32, required=False)                
	password1 = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=32)
	password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm', max_length=32)
	phone_no = forms.IntegerField(label='Phone No')
	# email = forms.CharField(label = 'Email id', max_length = 100, required = False)
	expected_salary = forms.CharField(label = 'Expected Salary/Pay')
	overall_cost = forms.CharField(label = 'Estimated Overall Cost')
	years = forms.IntegerField(label = 'Years of Experience')
	Number_sites = forms.IntegerField(label = 'Number of Finished Projects')
	locality = forms.CharField(label = 'Locality', max_length = 150, required = False)
	profile_image = forms.ImageField(required = False)

	

	class Meta:
		model = User
		fields = ('username','password1','password2','first_name','last_name','email','phone_no','expected_salary','overall_cost')



# class EditProfileForm(forms.ModelForm):
# 	username = forms.CharField(label='Username', max_length=100)
# 	phone_no = forms.IntegerField(label='Phone No')
# 	expected_salary = forms.IntegerField(label = 'Expected Salary/Pay')
# 	overall_cost = forms.IntegerField(label = 'Estimated Overall Cost')
# 	years = forms.IntegerField(label = 'Years of Experience')
# 	Number_sites = forms.IntegerField(label = 'Number of Finished Projects')
# 	locality = forms.CharField(label = 'Locality', max_length = 150, required = False)






class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )





class Search_Form(forms.Form):
	search = forms.CharField(label = "Search", max_length = 500)