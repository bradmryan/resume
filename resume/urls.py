"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ResumeList.as_view(), name='resume-list'),
    url(r'^create/', views.ResumeCreate.as_view(), name='resume-create'),
    url(r'^resume/(?P<pk>[0-9]+)/$', views.ResumeUpdate.as_view(), name='resume-update'),
    url(r'^profile/create/(?P<resume_pk>[0-9]+)/$', views.ProfileCreate.as_view(), name='profile-create'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name='profile-update'),
    url(r'^work/create/(?P<resume_pk>[0-9]+)/$', views.WorkCreate.as_view(), name='work-create'),
    url(r'^work/(?P<pk>[0-9]+)/$', views.WorkUpdate.as_view(), name='work-update'),
    url(r'^workhighlight/create/(?P<work_pk>[0-9]+)/$', views.WorkHighlightCreate.as_view(), name='workhighlight-create'),
    url(r'^workhighlight/delete/(?P<pk>[0-9]+)/$', views.WorkHighlightDelete.as_view(), name='workhighlight-delete'),
    url(r'^education/create/(?P<resume_pk>[0-9]+)/$', views.EducationCreate.as_view(), name='education-create'),
    url(r'^education/(?P<pk>[0-9]+)/$', views.EducationUpdate.as_view(), name='education-update'),
    url(r'^course/create/(?P<edu_pk>[0-9]+)/$', views.CourseCreate.as_view(), name='course-create'),
    url(r'^course/update/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name='course-update'),
    url(r'^award/create/(?P<resume_pk>[0-9]+)/$', views.AwardCreate.as_view(), name='award-create'),
    url(r'^award/(?P<pk>[0-9]+)/$', views.AwardUpdate.as_view(), name='award-update'),
    url(r'^publication/create/(?P<resume_pk>[0-9]+)/$', views.PublicationCreate.as_view(), name='publication-create'),
    url(r'^publication/(?P<pk>[0-9]+)/$', views.PublicationUpdate.as_view(), name='publication-update'),
    url(r'^resume.json', views.get_all_json, name="get-all-json"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
