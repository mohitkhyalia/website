from django.contrib import admin
from .models import main_ad,option,fb,foodlist

# Register your models here.
#user:Mohit pass:kumar123

admin.site.register(fb)
admin.site.register(option)
admin.site.register(main_ad)
admin.site.register(foodlist)