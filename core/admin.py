from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import User

admin.site.unregister(Group)
admin.register(User)

