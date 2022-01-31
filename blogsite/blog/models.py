from django.db import models

# Create your models here.

class Clients(models.Model):
    username = models.CharField( max_length=50)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username



#class BlogData(models.Model):
#    id=models.CharField(max_length=50)
#    blogtitle = models.TextField()
#    blogbody= models.TextField()
#    blogdate = models.DateField()
#    blogimage = models.TextField()
#    blogtags = models.TextField()
#    username= models.CharField( max_length=50)
#    email = models.EmailField(max_length=200)
    

