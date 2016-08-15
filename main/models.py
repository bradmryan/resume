from django.db import models
from django.urls import reverse

# Create your models here.
class Resume(models.Model):
    firstname = models.CharField(max_length=255)
    middleinitial = models.CharField(max_length=5)
    lastname = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='images/', max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    website = models.URLField()
    summary = models.TextField()
    address = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    countrycode = models.CharField(max_length=2)
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Profile(models.Model):
    resume = models.ForeignKey(Resume)

    FACEBOOK = 'FB'
    TWITTER = 'TW'
    LINKEDIN = 'LI'
    NETWORK_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (LINKEDIN, 'Linkedin'),
    )

    network = models.CharField(max_length=2, choices=NETWORK_CHOICES)
    username = models.CharField(max_length=150)
    url = models.URLField()


    class Meta:
        unique_together = ('resume', 'network')

class Work(models.Model):
    resume = models.ForeignKey(Resume)

    volunteer = models.BooleanField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    website = models.URLField()
    startdate = models.DateField()
    enddate = models.DateField()
    summary = models.TextField()


class WorkHighlight(models.Model):
    work = models.ForeignKey(Work)

    highlight = models.TextField()

    def __str__(self):
        return self.highlight[:15]


class Education(models.Model):
    resume = models.ForeignKey(Resume)

    institution = models.CharField(max_length=150)
    area = models.CharField(max_length=100)
    studytype = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()
    gpa = models.CharField(max_length=3)


class Course(models.Model):
    education = models.ForeignKey(Education)

    coursecode = models.CharField(max_length=10)
    description = models.CharField(max_length=100)


class Award(models.Model):
    resume = models.ForeignKey(Resume)

    title = models.CharField(max_length=100)
    date = models.DateField()
    awarder = models.CharField(max_length=100)
    summary = models.TextField()


class Publication(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    releasedate = models.DateField()
    website = models.URLField()
    summary = models.TextField()


class Skill(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=25)


class Keyword(models.Model):
    word = models.CharField(max_length=25)

    def __str__(self):
        return self.word


class SkillKeyword(models.Model):
    skill = models.ForeignKey(Skill)
    keyword = models.ForeignKey(Keyword)

    class Meta:
        unique_together = ('skill', 'keyword')


class Language(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)



class Interest(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=50)


class InterestKeyword(models.Model):
    interest = models.ForeignKey(Interest)
    keyword = models.ForeignKey(Keyword)

    class Meta:
        unique_together = ('interest', 'keyword')


class Reference(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=255)
