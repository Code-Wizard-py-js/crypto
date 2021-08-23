from django.contrib import admin
from .models import Sivan,Forest,Arctic,Mystic,Genesis
# Register your models here.
Models = (Sivan,Forest,Arctic,Mystic,Genesis)

admin.site.register(Models)