from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=255)
    middleinitial = models.CharField(max_length=5)
    lastname = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='images/', max_length=50)
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

    def get_full_name(self):
        return ' '.join([self.firstname, self.middleinitial, self.lastname]).title()


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

    def __str__(self):
        return self.network + " " + self.resume.email

class Work(models.Model):
    resume = models.ForeignKey(Resume)

    volunteer = models.BooleanField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    website = models.URLField()
    startdate = models.DateField()
    enddate = models.DateField()
    summary = models.TextField()

    class Meta:
        ordering = ['-startdate']

    def __str__(self):
        return self.resume.email + " - " + self.company

class WorkHighlight(models.Model):
    work = models.ForeignKey(Work)

    highlight = models.TextField()

    def __str__(self):
        return self.highlight[:30] + " - " + self.work.company + " - " + self.work.resume.email


class Education(models.Model):
    resume = models.ForeignKey(Resume)

    institution = models.CharField(max_length=150)
    area = models.CharField(max_length=100)
    studytype = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()
    gpa = models.CharField(max_length=3)

    class Meta:
        ordering = ['-startdate']

    def __str__(self):
        return self.area + " - " + self.institution + " - " + self.resume.email

class Course(models.Model):
    education = models.ForeignKey(Education)

    coursecode = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.coursecode + " - " + self.education.institution

class Award(models.Model):
    resume = models.ForeignKey(Resume)

    title = models.CharField(max_length=100)
    date = models.DateField()
    awarder = models.CharField(max_length=100)
    summary = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.resume.email + " - " + self.title + " - " + self.awarder


class Publication(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    releasedate = models.DateField()
    website = models.URLField()
    summary = models.TextField()

    class Meta:
        ordering = ['-releasedate']

    def __str__(self):
        return self.resume.email + " - " + self.name + " - " + self.publisher


class Skill(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.resume.email + " - " + self.name


class Keyword(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class SkillKeyword(models.Model):
    skill = models.ForeignKey(Skill)
    keyword = models.ForeignKey(Keyword)

    class Meta:
        unique_together = ('skill', 'keyword')

    def __str__(self):
        return self.skill.resume.email + " - " + self.skill.name + " - " + self.keyword.word


class Language(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.resume.email + " - " + self.name

class Interest(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.resume.email + " - " + self.name

class InterestKeyword(models.Model):
    interest = models.ForeignKey(Interest)
    keyword = models.ForeignKey(Keyword)

    class Meta:
        unique_together = ('interest', 'keyword')

    def __str__(self):
        return self.interest.resume.email + " - " + self.interest.name + " - " + self.keyword.word

class Reference(models.Model):
    resume = models.ForeignKey(Resume)

    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.resume.email + " - " + self.name

class LogoImage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/logos/', max_length=50)
    alt_image = models.ImageField(upload_to='images/logos/', max_length=50, null=True, blank=True)
    attribution = models.TextField(blank=True)

    def __str__(self):
        return self.name
