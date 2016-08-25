from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resumes/$', views.resume_list),
    url(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', views.resume_detail),
]
