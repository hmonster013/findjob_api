SELECT 'django_celery_beat_periodictasks' AS table_name, 
          (SELECT COUNT(*) FROM public.django_celery_beat_periodictasks) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_celery_beat_periodictasks) AS myjob_db_count
UNION ALL
SELECT 'findjob_findjob_feedback' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_findjob_feedback) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_findjob_feedback) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_advanced_skill' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_advanced_skill) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_advanced_skill) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_company_image' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_company_image) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_company_image) AS myjob_db_count
UNION ALL
SELECT 'findjob_authentication_user_groups' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_authentication_user_groups) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_authentication_user_groups) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_resume' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_resume) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_resume) AS myjob_db_count
UNION ALL
SELECT 'django_celery_beat_periodictask' AS table_name, 
          (SELECT COUNT(*) FROM public.django_celery_beat_periodictask) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_celery_beat_periodictask) AS myjob_db_count
UNION ALL
SELECT 'oauth2_provider_refreshtoken' AS table_name, 
          (SELECT COUNT(*) FROM public.oauth2_provider_refreshtoken) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.oauth2_provider_refreshtoken) AS myjob_db_count
UNION ALL
SELECT 'django_celery_beat_solarschedule' AS table_name, 
          (SELECT COUNT(*) FROM public.django_celery_beat_solarschedule) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_celery_beat_solarschedule) AS myjob_db_count
UNION ALL
SELECT 'social_auth_partial' AS table_name, 
          (SELECT COUNT(*) FROM public.social_auth_partial) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.social_auth_partial) AS myjob_db_count
UNION ALL
SELECT 'social_auth_nonce' AS table_name, 
          (SELECT COUNT(*) FROM public.social_auth_nonce) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.social_auth_nonce) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_language_skill' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_language_skill) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_language_skill) AS myjob_db_count
UNION ALL
SELECT 'oauth2_provider_application' AS table_name, 
          (SELECT COUNT(*) FROM public.oauth2_provider_application) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.oauth2_provider_application) AS myjob_db_count
UNION ALL
SELECT 'auth_permission' AS table_name, 
          (SELECT COUNT(*) FROM public.auth_permission) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.auth_permission) AS myjob_db_count
UNION ALL
SELECT 'oauth2_provider_accesstoken' AS table_name, 
          (SELECT COUNT(*) FROM public.oauth2_provider_accesstoken) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.oauth2_provider_accesstoken) AS myjob_db_count
UNION ALL
SELECT 'findjob_job_saved_job_post' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_job_saved_job_post) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_job_saved_job_post) AS myjob_db_count
UNION ALL
SELECT 'django_session' AS table_name, 
          (SELECT COUNT(*) FROM public.django_session) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_session) AS myjob_db_count
UNION ALL
SELECT 'findjob_job_job_post_notification' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_job_job_post_notification) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_job_job_post_notification) AS myjob_db_count
UNION ALL
SELECT 'social_auth_association' AS table_name, 
          (SELECT COUNT(*) FROM public.social_auth_association) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.social_auth_association) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_experience_detail' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_experience_detail) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_experience_detail) AS myjob_db_count
UNION ALL
SELECT 'findjob_common_career' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_common_career) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_common_career) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_company_followed' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_company_followed) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_company_followed) AS myjob_db_count
UNION ALL
SELECT 'findjob_authentication_forgot_password_token' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_authentication_forgot_password_token) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_authentication_forgot_password_token) AS myjob_db_count
UNION ALL
SELECT 'findjob_authentication_user' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_authentication_user) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_authentication_user) AS myjob_db_count
UNION ALL
SELECT 'django_celery_beat_clockedschedule' AS table_name, 
          (SELECT COUNT(*) FROM public.django_celery_beat_clockedschedule) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_celery_beat_clockedschedule) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_certificate' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_certificate) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_certificate) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_job_seeker_profile' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_job_seeker_profile) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_job_seeker_profile) AS myjob_db_count
UNION ALL
SELECT 'findjob_common_location' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_common_location) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_common_location) AS myjob_db_count
UNION ALL
SELECT 'auth_group' AS table_name, 
          (SELECT COUNT(*) FROM public.auth_group) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.auth_group) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_resume_viewed' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_resume_viewed) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_resume_viewed) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_contact_profile' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_contact_profile) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_contact_profile) AS myjob_db_count
UNION ALL
SELECT 'django_migrations' AS table_name, 
          (SELECT COUNT(*) FROM public.django_migrations) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_migrations) AS myjob_db_count
UNION ALL
SELECT 'findjob_authentication_user_user_permissions' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_authentication_user_user_permissions) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_authentication_user_user_permissions) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_education_detail' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_education_detail) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_education_detail) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_company' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_company) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_company) AS myjob_db_count
UNION ALL
SELECT 'oauth2_provider_grant' AS table_name, 
          (SELECT COUNT(*) FROM public.oauth2_provider_grant) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.oauth2_provider_grant) AS myjob_db_count
UNION ALL
SELECT 'findjob_job_job_post' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_job_job_post) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_job_job_post) AS myjob_db_count
UNION ALL
SELECT 'social_auth_usersocialauth' AS table_name, 
          (SELECT COUNT(*) FROM public.social_auth_usersocialauth) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.social_auth_usersocialauth) AS myjob_db_count
UNION ALL
SELECT 'auth_group_permissions' AS table_name, 
          (SELECT COUNT(*) FROM public.auth_group_permissions) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.auth_group_permissions) AS myjob_db_count
UNION ALL
SELECT 'social_auth_code' AS table_name, 
          (SELECT COUNT(*) FROM public.social_auth_code) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.social_auth_code) AS myjob_db_count
UNION ALL
SELECT 'django_content_type' AS table_name, 
          (SELECT COUNT(*) FROM public.django_content_type) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_content_type) AS myjob_db_count
UNION ALL
SELECT 'django_celery_beat_crontabschedule' AS table_name, 
          (SELECT COUNT(*) FROM public.django_celery_beat_crontabschedule) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_celery_beat_crontabschedule) AS myjob_db_count
UNION ALL
SELECT 'findjob_common_city' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_common_city) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_common_city) AS myjob_db_count
UNION ALL
SELECT 'findjob_info_resume_saved' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_info_resume_saved) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_info_resume_saved) AS myjob_db_count
UNION ALL
SELECT 'findjob_findjob_banner' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_findjob_banner) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_findjob_banner) AS myjob_db_count
UNION ALL
SELECT 'findjob_job_job_post_activity' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_job_job_post_activity) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_job_job_post_activity) AS myjob_db_count
UNION ALL
SELECT 'findjob_common_district' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_common_district) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_common_district) AS myjob_db_count
UNION ALL
SELECT 'django_admin_log' AS table_name, 
          (SELECT COUNT(*) FROM public.django_admin_log) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_admin_log) AS myjob_db_count
UNION ALL
SELECT 'oauth2_provider_idtoken' AS table_name, 
          (SELECT COUNT(*) FROM public.oauth2_provider_idtoken) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.oauth2_provider_idtoken) AS myjob_db_count
UNION ALL
SELECT 'findjob_files' AS table_name, 
          (SELECT COUNT(*) FROM public.findjob_files) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.findjob_files) AS myjob_db_count
UNION ALL
SELECT 'django_celery_beat_intervalschedule' AS table_name, 
          (SELECT COUNT(*) FROM public.django_celery_beat_intervalschedule) AS public_count, 
          (SELECT COUNT(*) FROM myjob_db.django_celery_beat_intervalschedule) AS myjob_db_count
          
 