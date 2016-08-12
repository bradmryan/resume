from django.contrib import admin
from .models import Resume, Profile, Work

REGISTER_MODELS = [
    Resume,
    Profile,
    Work
]

# Register your models here.
admin.site.register(REGISTER_MODELS)
