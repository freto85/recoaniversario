from django.contrib import admin
from accounts.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username','last_login')

admin.site.register(User,UserAdmin)