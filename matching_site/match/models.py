from django.db import models
from django.contrib.auth.models import User
# Import pillow library to manipulate images
from PIL import Image
from django.utils.timezone import now
import math


# Create Hobby table to add a predefined set of hobbies
class Hobby(models.Model):
    hobby = models.CharField(max_length=30)

    def __str__(self):
        return self.hobby


# Create Profile table to extend User table fields
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6,choices=(('Male', 'Male'), ('Female', 'Female')))
    date_of_birth = models.DateField(null=True,blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')
    hobbies = models.ManyToManyField(Hobby)

    def __str__(self):
        return str(self.username)

    # Calculate age from Date of Birth
    def age(self):
        current = now().date()
        birthday = self.date_of_birth
        test = current - birthday
        return math.floor(int(test.days)/365.25)

    # Overwrite save method to resize images using Pillow Library
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            size = (150, 150)
            img.thumbnail(size)
            img.save(self.image.path)
