from django.contrib import admin
from UserApp.models import SomeUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(SomeUser, UserAdmin)