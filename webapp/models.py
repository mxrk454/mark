from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    date_started = models.DateField(null=True)


class Employee(models.Model):  
    name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True)
    group = models.ManyToManyField(Group, related_name='employees')

    def __str__(self):
        return self.name 

class Client(models.Model):   
    title =  models.CharField(max_length=50, null=True)    
    description =  models.TextField(blank=True)    
    photo =  models.ImageField(upload_to='albums/', blank=True)    
    release_date =  models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.title       

class Contract(models.Model):   
    start_date =  models.DateField(null=True)    
    end_date =  models.DateField(null=True)    
    terms =  models.TextField(blank=True)    
    payment =  models.IntegerField(null=True) 


class EmployeeContractStatus(models.Model):
    STATUS = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('D', 'Denied'),
    )
    status = models.CharField(max_length=1, choices=STATUS)

