from rest_framework import serializers
from .models import Resume, Profile, Work, Education, Award, Publication, Skill, Language, Interest, Reference, WorkHighlight, Course, SkillKeyword, InterestKeyword

class ResumeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Resume

        fields = ('name', 'picture', 'email', 'phone', 'website', 'summary', 'location')

    def get_name(self, obj):
        return obj.get_full_name()

    def get_email(self, obj):
        return obj.__str__()

    def get_location(self, obj):
        loc_dict = {
            'address': obj.address,
            'postalcode': obj.postalcode,
            'city': obj.city,
            'countrycode': obj.countrycode,
            'region': obj.region
            }
        return loc_dict


class BasicSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Resume

        fields = ('name', 'picture', 'email', 'phone', 'website', 'summary', 'location')

    def get_name(self, obj):
        return obj.get_full_name()

    def get_email(self, obj):
        return obj.__str__()

    def get_location(self, obj):
        loc_dict = {
            'address': obj.address,
            'postalcode': obj.postalcode,
            'city': obj.city,
            'countrycode': obj.countrycode,
            'region': obj.region
            }
        return loc_dict


class ProfileSerializer(serializers.ModelSerializer):
    network = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('network', 'username', 'url')

    def get_network(self, obj):
        return obj.get_network_display()


class WorkSerializer(serializers.ModelSerializer):
    highlights = serializers.SerializerMethodField()

    class Meta:
        model = Work
        fields = ('company', 'position', 'website', 'startDate', 'endDate', 'summary', 'highlights')

    def get_highlights(self, obj):
        highlights_list = []
        work_highlights = WorkHighlight.objects.filter(work=obj)
        for highlight in work_highlights:
            highlights_list.append(highlight.highlight)

        return highlights_list

class VolunteerSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()
    highlights = serializers.SerializerMethodField()

    class Meta:
        model = Work
        fields = ('organization', 'position', 'website', 'startDate', 'endDate', 'summary', 'highlights')

    def get_organization(self, obj):
        return obj.company

    def get_highlights(self, obj):
        highlights_list = []
        work_highlights = WorkHighlight.objects.filter(work=obj)
        for highlight in work_highlights:
            highlights_list.append(highlight.highlight)

        return highlights_list


class EducationSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = ('institution', 'area', 'studyType', 'startDate', 'endDate', 'gpa', 'courses')

    def get_courses(self, obj):
        course_list =[]
        courses = Course.objects.filter(education=obj)
        for course in courses:
            name = " - ".join([course.coursecode, course.description])
            course_list.append(name)
        return course_list


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('title', 'date', 'awarder', 'summary')


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('name', 'publisher', 'releaseDate', 'website', 'summary')


class SkillSerializer(serializers.ModelSerializer):
    keywords = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ('name', 'level', 'keywords')

    def get_keywords(self, obj):
        keywords_list = []
        skillkeywords = SkillKeyword.objects.filter(skill=obj)
        for keyword in skillkeywords:
            keywords_list.append(keyword.keyword.word)
        return keywords_list

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'level')


class InterestSerializer(serializers.ModelSerializer):
    keywords = serializers.SerializerMethodField()

    class Meta:
        model = Interest
        fields = ('name', 'keywords')

    def get_keywords(self, obj):
        keywords_list = []
        interestkeywords = InterestKeyword.objects.filter(interest=obj)
        for keyword in interestkeywords:
            keywords_list.append(keyword.keyword.word)
        return keywords_list


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('name', 'reference')
