from django.contrib import admin
from .models import User, file


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ['id', 'is_ops_user', 'is_client_user',]

@admin.register(file)
class fileAdmin(admin.ModelAdmin):
    list_display = [ 'uploaded_by', 'file', 'uploaded_at']
    


