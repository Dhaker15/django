from django.db import models

class News(models.Model):
    heading = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/', default='')



    def __str__(self):
        return self.heading
