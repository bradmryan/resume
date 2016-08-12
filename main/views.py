from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Resume, Profile, Work, WorkHighlight, Education


# Create your views here.
class ResumeList(ListView):
    model = Resume


class ResumeDetail(DetailView):
    model = Resume


class ResumeCreate(CreateView):
    model = Resume
    fields = '__all__'


class ResumeUpdate(UpdateView):
    model = Resume
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(ResumeUpdate, self).get_context_data(**kwargs)
        resume_pk = self.kwargs.get('pk')
        context['profiles'] = Profile.objects.filter(resume=resume_pk)
        context['work'] = Work.objects.filter(resume=resume_pk)
        context['education'] = Education.objects.filter(resume=resume_pk)
        return context


class ProfileCreate(CreateView):
    model = Profile
    fields = ['network', 'username', 'url']

    def get_resume(self):
        return get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))

    def get_context_data(self, **kwargs):
        context = super(ProfileCreate, self).get_context_data(**kwargs)
        context['resume'] = self.get_resume()
        return context

    def form_valid(self, form):
        form.instance.resume = self.get_resume()
        return super(ProfileCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['network', 'username', 'url']
    template_name_suffix = '_update_form'


class WorkCreate(CreateView):
    model = Work
    fields = ['volunteer', 'company', 'position', 'website', 'startdate', 'enddate', 'summary']

    def get_resume(self):
        return get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))

    def get_context_data(self, **kwargs):
        context = super(WorkCreate, self).get_context_data(**kwargs)
        context['resume'] = self.get_resume()
        return context

    def form_valid(self, form):
        form.instance.resume = self.get_resume()
        return super(WorkCreate, self).form_valid(form)


class WorkUpdate(UpdateView):
    model = Work
    fields = ['volunteer', 'company', 'position', 'website', 'startdate', 'enddate', 'summary']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(WorkUpdate, self).get_context_data(**kwargs)
        work_pk = self.kwargs.get('pk')
        context['workhighlights'] = WorkHighlight.objects.filter(work=work_pk)
        return context

class WorkHighlightCreate(CreateView):
    model = WorkHighlight

    fields = ['highlight']

    def get_work(self):
        return get_object_or_404(Work, pk=self.kwargs.get('work_pk'))

    def get_context_data(self, **kwargs):
        context = super(WorkHighlightCreate, self).get_context_data(**kwargs)
        context['work'] = self.get_work()
        return context

    def form_valid(self, form):
        form.instance.work = self.get_work()
        return super(WorkHighlightCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('work-update', kwargs={'pk':self.kwargs.get('work_pk')})


class WorkHighlightDelete(DeleteView):
    model = WorkHighlight

    def get_success_url(self):
        context = self.get_context_data()
        highlight = context['object']
        return reverse('work-update', kwargs={'pk':highlight.work.pk})

class EducationCreate(CreateView):
    model = Education
    fields = ['institution', 'area', 'studytype', 'startDate', 'endDate', 'gpa']

    def get_resume(self):
        return get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))

    def get_context_data(self, **kwargs):
        context = super(EducationCreate, self).get_context_data(**kwargs)
        context['resume'] = self.get_resume()
        return context

    def form_valid(self, form):
        form.instance.resume = self.get_resume()
        return super(EducationCreate, self).form_valid(form)

class EducationUpdate(UpdateView):
    model = Education
    fields = ['institution', 'area', 'studytype', 'startDate', 'endDate', 'gpa']
    template_name_suffix = '_update_form'

def get_all_json(req):
    resumes = Resume.objects.all()

    resumes_dict = {}
    resumes_rec = []

    for resume in resumes:
        name = ' '.join([resume.firstname, resume.middleinitial, resume.lastname])
        record = { "name": name.title(), "summary": resume.summary }

        resumes_rec.append(record)

    resumes_dict["Resumes"] = resumes_rec

    return JsonResponse(resumes_dict)
