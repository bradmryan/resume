from django.forms import ModelForm
from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Keyword, Language, Interest, Reference


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'

class WorkHighlightForm(ModelForm):
    class Meta:
        model = WorkHighlight
        fields = '__all__'

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class KeywordForm(ModelForm):
    class Meta:
        model = Keyword
        fields = '__all__'

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'

class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
