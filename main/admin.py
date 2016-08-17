from django.contrib import admin
from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Language, Interest, Reference, LogoImage, SkillKeyword, Keyword

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
    LogoImage,
    SkillKeyword,
    Keyword,
]

# Register your models here.
admin.site.register(REGISTER_MODELS)
