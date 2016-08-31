from django.forms import ModelForm
from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Keyword, Language, Interest, Reference


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        exclude = ('user',)

class WorkHighlightForm(ModelForm):
    class Meta:
        model = WorkHighlight
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class KeywordForm(ModelForm):
    class Meta:
        model = Keyword
        fields = '__all__'
