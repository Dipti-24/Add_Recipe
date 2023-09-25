from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.db.models.signals import post_save
#from django.dispatch import receiver

'''class CustomUser(AbstractUser):

    username=None
    phone_number=models.CharField(max_length=100,unique=True)
    
    email=models.EmailField(unique=True)
    user_bio=models.CharField(max_length=50)
    user_profile_image=models.ImageField(upload_to="profile")

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
'''
    #objects=UserManager()


# Create your models here.
class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models. EmailField()
    file = models.FileField()

'''class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)

    def __str__(self)->str:
        return self.car_name

@receiver(post_save,sender=Car)  
def call_car_api(sender,instance,**kwargs):
    print("car objected created")
    print(sender,instance,kwargs)'''
