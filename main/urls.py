from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resumes/$', views.resume_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.resume_detail),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/basic/', views.basic_detail),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/profiles/', views.profile_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/work/', views.work_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/volunteer/', views.volunteer_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/education/', views.education_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/awards/', views.awards_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/publications/', views.publications_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/skills/', views.skills_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/languages/', views.languages_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/interests/', views.interests_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/references/', views.references_list),
]
