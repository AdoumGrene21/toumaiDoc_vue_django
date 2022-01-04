from django.contrib import admin


# Register your models here.
from .models import Type, Document

admin.site.register(Document)
admin.site.register(Type)
