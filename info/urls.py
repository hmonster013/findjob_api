from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'job-seeker-profiles', views.JobSeekerProfileViewSet, basename='web-job-seeker-profile')
router.register(r'private-resumes', views.PrivateResumeViewSet, basename='private-resume')
router.register(r'resumes', views.ResumeViewSet, basename='resume')
router.register(r'resumes-saved', views.ResumeSavedViewSet, basename='resume-saved')
router.register(r'experiences-detail', views.ExperienceDetailViewSet, basename='experience-detail')
router.register(r'educations-detail', views.EducationDetailViewSet, basename='education-detail')
router.register(r'certificates-detail', views.CertificateDetailViewSet, basename='certificate-detail')
router.register(r'language-skills', views.LanguageSkillViewSet, basename='language-skill')
router.register(r'advanced-skills', views.AdvancedSkillViewSet, basename='advanced-skill')

router.register(r'private-companies', views.PrivateCompanyViewSet, basename='private-company')
router.register(r'companies', views.CompanyViewSet, basename='web-company')
router.register(r'company-images', views.CompanyImageViewSet, basename='company-image')

urlpatterns = [
    path('', include([
        path("profile/", views.ProfileView.as_view({
            'get': 'get_profile_info',
            'put': 'update_profile_info'
        })),
    ])),
    path('web/', include([
        path("company/", views.CompanyView.as_view({'get': 'get_company_info'})),
        path("company/job-posts/<int:pk>/", views.CompanyView.as_view({'get': 'get_job_post_detail'})),
        path("", include(router.urls)),
        path("resume-views/", views.ResumeViewedAPIView.as_view()),
        path("companies-follow/", views.CompanyFollowedAPIView.as_view()),
    ])),
]
