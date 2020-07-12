
from django.db import models
from .phone import Category










class laptop(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50,default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    price = models.CharField(max_length=50,default='')
    description_made_in = models.CharField(max_length=200, default='', null=True , blank=True)
    description2 = models.CharField(max_length=200, default='', null=True , blank=True)
    description3 = models.CharField(max_length=200, default='', null=True , blank=True)
    description4 = models.CharField(max_length=200, default='', null=True , blank=True)
    description5 = models.CharField(max_length=200, default='', null=True , blank=True)
    description6 = models.CharField(max_length=200, default='', null=True , blank=True)
    description7 = models.CharField(max_length=200, default='', null=True , blank=True)
    description8 = models.CharField(max_length=200, default='', null=True , blank=True)
    description9 = models.CharField(max_length=200, default='', null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/',default='')


    def __str__(self):
        return self.name

