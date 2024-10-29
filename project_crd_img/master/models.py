from django.db import models

# Create your models here.
class MyModelInfo(models.Model):
    GENDER_CHOICE = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,blank=True)
    profile = models.ImageField(upload_to='Images/')

    def __str__(self):
        return self.name
