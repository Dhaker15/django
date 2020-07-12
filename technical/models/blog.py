
from django.db import models








class Product(models.Model):
    product_id = models.AutoField
    heading = models.CharField(max_length=50,default='')
    price = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=200, default='', null=True , blank=True)
    description2 = models.CharField(max_length=200, default='', null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/',default='')


    def __str__(self):
        return self.heading


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