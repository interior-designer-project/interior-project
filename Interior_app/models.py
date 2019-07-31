from django.db import models
from django.contrib.auth.models import User
#from django_extensions.db.models import TimeStampedModel
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify




class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	Name = models.CharField(max_length = 50)
	contact_no = models.IntegerField(default = 0)
	Years_of_experience = models.IntegerField(default = 0)
	Number_of_finished_projects = models.IntegerField(default = 0)
	Locality = models.CharField(max_length = 50, null = True)
	Expected_salary = models.CharField(default = 0, max_length = 10)
	Overall_cost = models.IntegerField(default = 0)
	profile_picture = models.ImageField(upload_to = 'profile_image', blank = True, default = 0)



	def __str__(self):
		return self.user.username
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  


class Images(models.Model):
    post = models.ForeignKey(Profile, default=None, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = get_image_filename,
                              verbose_name='Image')



# https://us04web.zoom.us/j/571679912
