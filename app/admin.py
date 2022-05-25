# Imports
from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Todo)
admin.site.register(User_Data)
admin.site.register(Notion_DB)
admin.site.register(User_Rewards)