from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.core.files.images import get_image_dimensions

# class SignupForm(UserCreationForm):
# 	username = forms.CharField(label='Username', max_length=100)
# 	first_name = forms.CharField(label='First Name', max_length=32, required=False)
# 	last_name = forms.CharField(label='Last Name', max_length=32, required=False)                
# 	password1 = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=32)
# 	password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm', max_length=32)
# 	phone_no = forms.IntegerField(label='Phone No')
# 	# email = forms.CharField(label = 'Email id', max_length = 100, required = False)
# 	expected_salary = forms.CharField(label = 'Expected Salary/Pay')
# 	overall_cost = forms.CharField(label = 'Estimated Overall Cost')
# 	years = forms.IntegerField(label = 'Years of Experience')
# 	Number_sites = forms.IntegerField(label = 'Number of Finished Projects')
# 	locality = forms.CharField(label = 'Locality', max_length = 150, required = False)
# 	profile_image = forms.ImageField(required = False)

	

# 	class Meta:
# 		model = User
# 		fields = ('username','password1','password2','first_name','last_name','email','phone_no','expected_salary','overall_cost')



DESIGN_EXPERTISE=[
    (' Residential homes', ' Residential homes'),
    ('Offices', 'Offices'),
    ('Hotel', 'Hotel'),
    ('Industrial','Industrial'),
]
DESIGN_AREA=[
    (' Modern', ' Modern'),
    ('Contemporary', 'Contemporary'),
    ('Minimalist', 'Minimalist'),
    ('Traditional','Traditional'),
    ('Rustic','Rustic'),
    ('Glam','Glam'),
]

class SignupForm(UserCreationForm):
	fname = forms.CharField(label='fname',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First  name....'}),required=True)
	lname =forms.CharField(label='lname',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Last  name....'}))
	contact = forms.IntegerField(label='contactno',widget=forms.TextInput(attrs={'placeholder': 'Contact +91....'}))
	email  = forms.CharField(label='email',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Email....'}))
	companyName  = forms.CharField(label='cname',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Company name....'}))
	companyGST  = forms.CharField(label='cgst',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Company GST....'}))
	streetaddress1= forms.CharField(label='astreet1',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Street Address Line 1....'}))
	streetaddress2= forms.CharField(label='astreet2',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Street Address Line 2....'}))
	city= forms.CharField(label='city',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'City....'}))
	state= forms.CharField(label='state',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'State......'}))
	zipcode= forms.CharField(label='zipcode',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Zipcode....'}))
	design_expertise = forms.MultipleChoiceField(
       	required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=DESIGN_EXPERTISE)
	design_area = forms.MultipleChoiceField(
		required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=DESIGN_AREA)
	lower_budget = forms.CharField(label='budget',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Minimum Budget....'}))
	higher_budget = forms.CharField(label='budget',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Maximum Budget....'}))
	description = forms.CharField(label='description',max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Description....'}))
	years_exp  = forms.IntegerField(label='years',widget=forms.TextInput(attrs={'placeholder': 'Years of Experience....'}))
	username = forms.CharField(label='username',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'User name....'}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password...'}),label='password',max_length=32)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password...'}), label='password', max_length=32)
	# password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm', max_length=32)
	profileimage = forms.ImageField()
	# projectname= forms.CharField(label='projectname',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Project  name....'}))
	# projectimage= forms.ImageField()
	facebook= forms.CharField(label='facebook',max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Facebook....'}))
	website= forms.CharField(label='website',max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Website....'}))
	instagram= forms.CharField(label='instagram',max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Instagram....'}))

	class Meta:
		model = User
			# # fields = ('username','password1','password2','first_name','last_name','email','phone_no','expected_salary','overall_cost')
		fields= ('fname','lname','email','contact','companyName','companyGST','streetaddress1','streetaddress2','city','state','zipcode','design_expertise','design_area',
		'lower_budget','higher_budget','years_exp','username','password1','password2','profileimage','facebook','website','instagram')




class EditProfileForm(forms.ModelForm):
	username = forms.CharField(max_length = 100, label = 'username')
	class Meta:
		model = User
		fields = ['username']



class EditProfileForm_contact(forms.ModelForm):
	phone_no = forms.IntegerField(label='Phone No')
	class Meta:
		model = User
		fields = ['phone_no']



class EditProfileForm_years(forms.ModelForm):
	years = forms.IntegerField(label = 'Years of Experience')
	class Meta:
		model = User
		fields = ['years']




class EditProfileForm_locality(forms.ModelForm):
	locality = forms.CharField(label = 'Locality', max_length = 150, required = False)
	class Meta:
		model = User
		fields = ['locality']



class EditProfileForm_cost(forms.ModelForm):
	overall_cost = forms.CharField(label = 'Estimated Overall Cost')
	class Meta:
		model = User
		fields = ['overall_cost']





class EditProfileForm_salary(forms.ModelForm):
	expected_salary = forms.CharField(label = 'Expected Salary/Pay')
	class Meta:
		model = User
		fields = ['expected_salary']





class EditProfileForm_finsite(forms.ModelForm):
	Number_sites = forms.IntegerField(label = 'Number of Finished Projects')
	class Meta:
		model = User
		fields = ['Number_sites']


# label='Image', widget=forms.ClearableFileInput(attrs={'multiple': True})
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image', widget=forms.ClearableFileInput(attrs={'multiple': True}))    
#     class Meta:
#         model = Images
#         fields = ('image', )





class query_form(forms.ModelForm):
	query_text_form = forms.CharField(widget=forms.Textarea(attrs={ 'required': 'false', 'placeholder': 'Enter your query here' }), label = "Stuck somewhere? Drop an email, we shall assist you shortly!!", required = False)
	class Meta:
		model = Query_contact_us
		fields = ['query_text_form']


class Customer_Signup_Form(UserCreationForm):
	Customer_fname = forms.CharField(label='fname',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First  name....'}),required=True)
	Customer_lname =forms.CharField(label='lname',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Last  name....'}))
	Customer_contact = forms.IntegerField(label='contactno',widget=forms.TextInput(attrs={'placeholder': 'Contact +91....'}))
	Customer_email  = forms.CharField(label='email',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Email....'}))
	Customer_address= forms.CharField(label='astreet1',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Street Address Line 1....'}))
	username = forms.CharField(label='username',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'User name....'}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password...'}),label='password',max_length=32)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password...'}), label='password', max_length=32)
	
	class Meta:
		model = User
			# # fields = ('username','password1','password2','first_name','last_name','email','phone_no','expected_salary','overall_cost')
		fields= ('Customer_fname','Customer_lname','Customer_email','Customer_contact','Customer_address','username','password1','password2')




class Customer_Login_Form(forms.Form):
	username = forms.CharField(label='username',max_length=300,widget=forms.TextInput(attrs={'placeholder': 'User name....'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password...'}), label='password', max_length=300)

	class Meta:
		# model = User
		fields = ('username', 'password')


class VideoForm(forms.ModelForm):
	videofile = forms.FileField() 
	class Meta:
		model= Video_upload_professional
		fields= ('videofile',)



class Story_Form(forms.ModelForm):
	story = forms.FileField() 
	class Meta:
		model= Story_upload_professional
		fields= ('story',)