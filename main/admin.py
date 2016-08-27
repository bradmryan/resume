from django.contrib import admin
from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Language, Interest, Reference, Image, SkillKeyword, InterestKeyword, Keyword

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
    Image,
    SkillKeyword,
    InterestKeyword,
    Keyword,
]

# Register your models here.
admin.site.register(REGISTER_MODELS)
