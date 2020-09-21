from django.db import models
from django.contrib.auth.models import User
#from django_extensions.db.models import TimeStampedModel
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from datetime import date


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 50)
	contact_no = models.IntegerField(default = 0)
	years_exp = models.IntegerField(default = 0)
	address = models.CharField(max_length = 75 , default = '')
	lower_budget = models.CharField(default = 0, max_length = 10)
	higher_budget = models.CharField(default = 0, max_length = 10)
	profile_img = models.ImageField(upload_to = 'profile_image', blank = True, default = 0)
	email=models.CharField(max_length=30,default = '')
	company_name = models.CharField(max_length = 50, default = '')
	description=models.CharField(max_length = 1000 ,default='')
	company_gST = models.CharField(max_length = 50,default = '')
	design_expertise=models.CharField(default='',max_length = 1000)
	design_area=models.CharField(default='',max_length = 1000)
	# name_of_project = models.CharField(max_length=100, default='')
	# project_img=models.ImageField(upload_to = 'project_image', blank = True, default = 0)
	facebook = models.CharField(max_length = 1000,default = '')
	website=models.CharField(max_length = 1000, default = '')
	instagram=models.CharField(max_length = 1000,default = '')

	def __str__(self):
			return self.user.username



# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete = models.CASCADE)
# 	Name = models.CharField(max_length = 50)
# 	contact_no = models.IntegerField(default = 0)
# 	Years_of_experience = models.IntegerField(default = 0)
# 	Number_of_finished_projects = models.IntegerField(default = 0)
# 	Locality = models.CharField(max_length = 50, null = True)
# 	Expected_salary = models.CharField(default = 0, max_length = 10)
# 	Overall_cost = models.IntegerField(default = 0)
# 	profile_picture = models.ImageField(upload_to = 'profile_image', blank = True, default = 0)



# 	def __str__(self):
# 		return self.user.username

def get_image_filename(instance, filename):
	name = instance.post.name
	slug = slugify(name)
	return "post_images/%s-%s" % (slug, filename)  


class Images(models.Model):
	post = models.ForeignKey(Profile, default=None, on_delete = models.CASCADE)
	image = models.ImageField(upload_to = get_image_filename, verbose_name='Image')

	def __str__(self):
		return self.post.user.username + ' - ' + str(self.image)



class Query_contact_us(models.Model):
	query = models.ForeignKey(Profile, default=None, on_delete = models.CASCADE)
	query_text = models.TextField(default = None)
	def __str__(self):
		return self.query.user.username + ' - ' + str(self.query_text)




class Customer_Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	customer_name = models.CharField(max_length = 50)
	customer_contact_no = models.IntegerField(default = 0)
	customer_address = models.CharField(max_length = 75 , default = '')
	customer_email=models.CharField(max_length=30,default = '')


	def __str__(self):
			return self.user.username


class Video_upload_professional(models.Model):
	post_video = models.ForeignKey(Profile, default=None, on_delete = models.CASCADE)
	videofile = models.FileField(upload_to='videos/', null=True, verbose_name="", blank = True)

	def __str__(self):
		return self.post_video.user.username + ' - ' + str(self.videofile)




class Story_upload_professional(models.Model):
	post_story = models.ForeignKey(Profile, default=None, on_delete = models.CASCADE)
	story = models.FileField(upload_to='videos/', null=True, verbose_name="", blank = True)
	timestamp_of_story = models.DateField(default=date.today)
	story_expiration = models.DateField(default=date.today)
	

	def __str__(self):
		return self.post_story.user.username + ' - ' + str(self.story)