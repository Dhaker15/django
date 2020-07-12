
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, default='')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name






class Product(models.Model):
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


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id);
        else:
            return Product.get_all_products();