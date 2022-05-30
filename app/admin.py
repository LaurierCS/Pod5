# Imports
from django.contrib import admin
from app.models import *
from django.apps import apps


admin.site.register(Todo)
admin.site.register(User_Data)
admin.site.register(Notion_DB)
admin.site.register(User_Rewards)