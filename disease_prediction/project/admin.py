from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LeafDisease
from .models import Review
admin.site.register(LeafDisease)
admin.site.register(Review)
