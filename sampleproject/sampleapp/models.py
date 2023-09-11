from django.db import models

# Create your models here.
# this table is  for Why Choose Us? in index.html
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    # this is to get the name that you given in the table instead of objects in the Admin panel
    def __str__(self):
        return self.name

# here the creating table is for store the img, name, and about(about them) of the teamates
class Team(models.Model):
    img=models.ImageField(upload_to='picture')
    name=models.CharField(max_length=250)
    about=models.TextField()

    def __str__(self):
        return self.name