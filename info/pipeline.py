from configs import variable_system
from .models import (
    JobSeekerProfile,
    Resume
)

def save_profile(backend, user, response, *args, **kwargs):
    job_seeker_profile = JobSeekerProfile.objects.filter(user=user)
    if not job_seeker_profile.exists():
        job_seeker_profile = JobSeekerProfile.objects.create(user=user)
        Resume.objects.create(user=user,
                              job_seeker_profile=job_seeker_profile,
                              type=variable_system.CV_WEBSITE)