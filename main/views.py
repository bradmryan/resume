from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Language, Interest, Reference, Keyword, SkillKeyword, InterestKeyword


# Create your views here.
def get_all_json(req):
    resumes = Resume.objects.all()

    resumes_dict = {}
    resumes_rec = []

    for resume in resumes:
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

        profiles = Profile.objects.filter(resume=resume)
        works = Work.objects.filter(resume=resume)
        education = Education.objects.filter(resume=resume)
        awards = Award.objects.filter(resume=resume)
        publications = Publication.objects.filter(resume=resume)
        skills = Skill.objects.filter(resume=resume)
        languages = Language.objects.filter(resume=resume)
        interests = Interest.objects.filter(resume=resume)
        references = Reference.objects.filter(resume=resume)

        name = ' '.join([resume.firstname, resume.middleinitial, resume.lastname])

        for profile in profiles:
            network = profile.get_network_display()
            profile_dict = {"network": network, "username": profile.username, "url": profile.url}
            profile_rec.append(profile_dict)

        for work in works:
            highlight_rec = []

            highlights = WorkHighlight.objects.filter(work=work)

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

            courses = Course.objects.filter(education=edu)

            for course in courses:
                record = " - ".join([course.coursecode, course.description ])
                course_rec.append(record)

            edu_dict = {"institution": edu.institution, "area": edu.area, "studyType": edu.studytype, "startDate": edu.startdate, "endDate": edu.enddate, "gpa": edu.gpa}
            edu_dict["courses"] = course_rec
            work_rec.append(edu_dict)

        for award in awards:
            award_dict = {"title": award.title, "date": award.date, "awarder": award.awarder, "summary": award.summary}
            award_rec.append(award_dict)

        for publication in publications:
            publication_dict = {"name": publication.name, "publisher": publication.publisher, "releaseDate": publication.releasedate, "website": publication.website, "summary": publication.summary}
            publication_rec.append(publication_dict)

        for skill in skills:
            keyword_rec = []

            keywords = SkillKeyword.objects.filter(skill=skill)

            for keyword in keywords:
                keyword_rec.append(keyword.keyword)

            skill_dict = {"name": skill.name, "level": skill.level, "keywords": keyword_rec}
            skill_rec.append(skill_dict)

        for language in languages:
            language_dict = {"name": language.name, "level": language.level}
            language_rec.append(language_dict)

        for interest in interests:
            keyword_rec = []

            keywords = InterestKeyword.objects.filter(interest=interest)

            for keyword in keywords:
                keyword_rec.append(keyword.keyword)

            interest_dict = {"name": interest.name, "keyword": keyword_rec}
            interest_rec.append(interest_dict)

        for reference in references:
            reference_dict = {"name": reference.name, "reference": reference.reference}
            reference_rec.append(reference_dict)

        resume_dict["basics"] = { "name": name.title(), "label": resume.label, "picture": resume.picture.url, "email": resume.email, "phone": resume.phone, "website": resume.website, "summary": resume.summary }
        resume_dict["basics"]["location"] = { "address": resume.address, "postalcode": resume.postalcode, "city": resume.city, "countrycode": resume.countrycode, "region": resume.region }
        resume_dict["basics"]["profiles"] = profile_rec
        resume_dict["volunteer"] = volunteer_rec
        resume_dict["work"] = work_rec
        resume_dict["education"] = work_rec
        resume_dict["awards"] = award_rec
        resume_dict["publications"] = publication_rec
        resume_dict["skills"] = skill_rec
        resume_dict["language"] = language_rec
        resume_dict["interests"] = interest_rec
        resume_dict["references"] = reference_rec


        resumes_rec.append(resume_dict)

    resumes_dict["Resumes"] = resumes_rec


    return JsonResponse(resumes_dict)
