from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_router = DefaultRouter()

router = DefaultRouter()
router.register('private-job-posts', views.PrivateJobPostViewSet, basename='private-web-job-posts')
router.register('job-posts', views.JobPostViewSet, basename="web-job-posts")
router.register('job-seeker-job-posts-activity', views.JobSeekerJobPostActivityViewSet,
                    basename='web-job-seeker-job-posts-activity')
router.register('employer-job-posts-activity', views.EmployerJobPostActivityViewSet,
                    basename='web-employer-job-posts-activity')
router.register('job-post-notifications', views.JobPostNotificationViewSet,
                    basename='web-job-post-notifications')

urlpatterns = [
    path('web/', include([
        path('seach/job-suggest-title/', views.job_suggest_title_search),
        path('', include(router.urls)),
        path('statistics/', include([
            path('employer-general-statistics/', views.EmployerStatisticViewSet.as_view({
                'get': 'general_statistics',
            })),
            path('employer-recruitment-statistics/', views.EmployerStatisticViewSet.as_view({
                'post': 'recruitment_statistics',
            })),
            path('employer-candidate-statistics/', views.EmployerStatisticViewSet.as_view({
                'post': 'candidate_statistics',
            })),
            path('employer-application-statistics/', views.EmployerStatisticViewSet.as_view({
                'post': 'application_statistics',
            })),
            path('employer-recruitment-statistics-by-rank/', views.EmployerStatisticViewSet.as_view({
                'post': 'recruitment_statistics_by_rank',
            })),

            path('job-seeker-general-statistics/', views.JobSeekerStatisticViewSet.as_view({
                'get': 'general_statistics',
            })),
            path('job-seeker-total-view/', views.JobSeekerStatisticViewSet.as_view({
                'get': 'total_view',
            })),
            path('job-seeker-activity-statistics/', views.JobSeekerStatisticViewSet.as_view({
                'get': 'activity_statistics',
            })),
        ])),
    ]))
]
