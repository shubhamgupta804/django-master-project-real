from django.db import models

# Create your models here.
# create student model and field name ,email and age
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class AutoCapture(models.Model):
    image = models.ImageField(upload_to="captures/")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)