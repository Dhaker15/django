from django.contrib import admin

# Register your models here.
from . models import Category,Product
from .models import laptop
from .models import tv
from  .models import speaker
from  .models import News

admin.site.register(Category),
admin.site.register(Product),

admin.site.register(laptop),
admin.site.register(tv),
admin.site.register(speaker),
admin.site.register(News),




