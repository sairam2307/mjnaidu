from django.db import models

# Create your models here.

class Chairman(models.Model):
    chairman_name = models.CharField(max_length=200,null=True,blank=True)
    specialization = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    document = models.FileField(upload_to='chairman/')
    
    def __str__(self):
        return self.chairman_name
