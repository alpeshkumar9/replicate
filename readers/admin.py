from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Readers

# Register the Reader model with the default UserAdmin
admin.site.register(Readers)
