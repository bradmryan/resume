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

from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view
from django.contrib.auth import views as auth_views


from main import views
from main.models import Resume

# Serializers define the API representation.
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = ('firstname', 'lastname', 'email', 'label')

# ViewSets define the view behavior.
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'resumes', ResumeViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^form/', views.resume_form, name="resume_form"),
    url(r'^api/', include('main.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/logout/$', auth_views.logout, name="account_logout"),
    url(r'^resume.json', views.get_resume_json, name="get-resume-json"),
    url(r'^resume.pdf', views.get_resume_pdf, name="get-resume-pdf"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
