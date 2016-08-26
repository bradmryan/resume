from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

import weasyprint
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Language, Interest, Reference, Keyword, SkillKeyword, InterestKeyword, LogoImage
from .serializers import ResumeSerializer

# Create your views here.
@require_GET
def home(req):
    context = {}
    email = "brad.m.ryan@gmail.com"
    context["resume"] = get_object_or_404(Resume, user=get_object_or_404(User, email=email))
    phn = context["resume"].phone
    phn = "(" + phn[:3] + ") " + phn[3:6] + "-" + phn[6:10]

    context["resume"].phone = phn

    return render(req, 'main/home.html', context)

def get_resume(email, format_phone=False):
    resume = get_object_or_404(Resume, user=get_object_or_404(User, email=email))

    resumes_dict = {}
    resumes_rec = []
    resume_dict = {}
    profile_rec = []
    work_rec = []
    volunteer_rec = []
    education_rec = []
    award_rec = []
    publication_rec = []
    skill_rec = []
    language_rec = []
    interest_rec = []
    reference_rec = []

    profiles = resume.profile_set.all()
    works = resume.work_set.all()
    education = resume.education_set.all()
    awards = resume.award_set.all()
    publications = resume.publication_set.all()
    skills = resume.skill_set.all()
    languages = resume.language_set.all()
    interests = resume.interest_set.all()
    references = resume.reference_set.all()

    name = ' '.join([resume.firstname, resume.middleinitial, resume.lastname])

    if format_phone:
        phone = '(' + resume.phone[:3] + ') ' + resume.phone[3:6] + '-' + resume.phone[6:10]
    else:
        phone = resume.phone

    for profile in profiles:
        network = profile.get_network_display()
        profile_dict = {"network": network, "username": profile.username, "url": profile.url}
        profile_rec.append(profile_dict)

    for work in works:
        highlight_rec = []

        highlights = work.workhighlight_set.all()

        for highlight in highlights:
            highlight_rec.append(highlight.highlight)

        work_dict = {"position": work.position, "website": work.website, "startDate": work.startdate, "endDate": work.enddate, "summary": work.summary}

        work_dict["highlights"] = highlight_rec

        if work.volunteer:
            work_dict["organization"] = work.company
            volunteer_rec.append(work_dict)
        else:
            work_dict["company"] = work.company
            work_rec.append(work_dict)

    for edu in education:
        course_rec = []

        courses = edu.course_set.all()

        for course in courses:
            record = " - ".join([course.coursecode, course.description ])
            course_rec.append(record)

        edu_dict = {"institution": edu.institution, "area": edu.area, "studyType": edu.studytype, "startDate": edu.startdate, "endDate": edu.enddate, "gpa": edu.gpa}
        edu_dict["courses"] = course_rec
        education_rec.append(edu_dict)

    for award in awards:
        award_dict = {"title": award.title, "date": award.date, "awarder": award.awarder, "summary": award.summary}
        award_rec.append(award_dict)

    for publication in publications:
        publication_dict = {"name": publication.name, "publisher": publication.publisher, "releaseDate": publication.releasedate, "website": publication.website, "summary": publication.summary}
        publication_rec.append(publication_dict)

    for skill in skills:
        keyword_rec = []

        keywords = skill.skillkeyword_set.all()

        for keyword in keywords:
            keyword_rec.append(keyword.keyword.word)

        skill_dict = {"name": skill.name, "level": skill.level, "keywords": keyword_rec}
        skill_rec.append(skill_dict)

    for language in languages:
        language_dict = {"name": language.name, "level": language.level}
        language_rec.append(language_dict)

    for interest in interests:
        keyword_rec = []

        keywords = interest.interestkeyword_set.all()

        for keyword in keywords:
            keyword_rec.append(keyword.keyword.word)

        interest_dict = {"name": interest.name, "keywords": keyword_rec}
        interest_rec.append(interest_dict)

    for reference in references:
        reference_dict = {"name": reference.name, "reference": reference.reference}
        reference_rec.append(reference_dict)

    resume_dict["basics"] = { "name": name.title(), "label": resume.label, "picture": resume.picture.url, "email": resume.user.email, "phone": phone, "website": resume.website, "summary": resume.summary }
    resume_dict["basics"]["location"] = { "address": resume.address, "postalcode": resume.postalcode, "city": resume.city, "countrycode": resume.countrycode, "region": resume.region }
    resume_dict["basics"]["profiles"] = profile_rec
    resume_dict["volunteer"] = volunteer_rec
    resume_dict["work"] = work_rec
    resume_dict["education"] = education_rec
    resume_dict["awards"] = award_rec
    resume_dict["publications"] = publication_rec
    resume_dict["skills"] = skill_rec
    resume_dict["language"] = language_rec
    resume_dict["interests"] = interest_rec
    resume_dict["references"] = reference_rec

    return resume_dict

@require_GET
def get_resume_json(req):
    resume_dict = get_resume("brad.m.ryan@gmail.com")

    return JsonResponse(resume_dict)

@require_GET
def get_resume_pdf(req):
    template = get_template('main/resume.html')
    resume_dict = get_resume("brad.m.ryan@gmail.com", format_phone=True)
    html = template.render(RequestContext(req, resume_dict))
    pdf = weasyprint.HTML(string=html).write_pdf()
    res = HttpResponse(pdf, content_type="application/pdf")

    return res


#REST

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def resume_list(req):
    if req.method == 'GET':
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return JSONResponse(serializer.data)

    elif req.method == 'POST':
        return HttpResponse(status=403)

@csrf_exempt
def resume_detail(req, email):

    try:
        resume = Resume.objects.get(email=email)
    except Resume.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = ResumeSerializer(resume)
        return JSONResponse(serializer.data)

    elif req.method == 'PUT':
        return HttpResponse(status=403)

    elif req.method == 'DELETE':
        return HttpResponse(status=403)
