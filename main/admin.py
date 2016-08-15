from django.contrib import admin
from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Language, Interest, Reference

REGISTER_MODELS = [
    Resume,
    Profile,
    Work,
    WorkHighlight,
    Education,
    Course,
    Award,
    Publication,
    Skill,
    Language,
    Interest,
    Reference,
]

# Register your models here.
admin.site.register(REGISTER_MODELS)
