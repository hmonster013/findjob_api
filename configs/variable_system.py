from django.conf import settings

ADMIN = "ADMIN"
EMPLOYER = "EMPLOYER"
JOB_SEEKER = "JOB_SEEKER"

CV_WEBSITE = 'WEBSITE'
CV_UPLOAD = "UPLOAD"

NOTIFICATION_TYPE = {
    "SYSTEM": "SYSTEM",
    "EMPLOYER_VIEWED_RESUME": "EMPLOYER_VIEWED_RESUME",
    "EMPLOYER_SAVED_RESUME": "EMPLOYER_SAVED_RESUME",
    "APPLY_STATUS": "APPLY_STATUS",
    "COMPANY_FOLLOWED": "COMPONY_FOLLOWED",
    "APPLY_JOB": "APPLY_JOB",
    "POST_VERIFY_REQUIRED": "POST_VERIRY_REQUIRED",
    "POST_VERIFY_RESULT": "POST_VERIFY_RESULT",
}

NO_IMAGE = "https://cdn-icons-png.flaticon.com/128/3460/3460724.png"
NOTIFICATION_IMAGE_DEFAULT = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngtree.com%2Fso%2Fnotification-icon&psig=AOvVaw2yoYBaHLFi62mwcbQTZtNF&ust=1743857462775000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMjGo7e1vowDFQAAAAAdAAAAABAE"

DATE_TIME_FORMAT = {
    "dmY": "%d/%m/%Y",
    "Ymd": "%Y-%m-%d",
    "ISO8601": "%Y-%m%dT%H:%M%S.%fZ"
}

AUTH_PROVIDERS = (('email', 'email'), ('facebook', 'facebook'), ('google', 'google'))

AVATAR_DEFAULT = {
    "AVATAR": "",
    "COMPANY_LOGO": "",
    "COMPANY_COVER_IMAGE": ""
}

COMPANY_INFO = {
    "DARK_LOGO_LINK": "",
    "LIGHT_LOGO_LINK": "",
    "EMAIL": "findjob.contact00000@gmail.com",
    "PHONE": "0976-543-210",
    "ADDRESS": "54 Triều Khúc, Thanh Xuân, TP. Hà Nội",
    "MY_COMPANY_NAME": "Find Job"
}

ABOUT_US_IMAGE_URLS = {
    "JOB_SEEKER": {
        "FEEDBACK_GUIDE": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
        "ACHIEVEMENTS": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    },
    "EMPLOYER": {
        "FEEDBACK_GUIDE": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
        "ACHIEVEMENTS": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    }
}

CHATBOT_ICONS = {
    # Job Seeker
    "job_seeker_search_job": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_search_company": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_manage_profile": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_track_application_status": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_manage_all_profile": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_myjob_profile": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_attached_profile": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_about_us_target_1": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_about_us_target_2": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_about_us_target_3": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "job_seeker_about_us_target_4": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    # Employer
    "employer_search_candidate": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "employer_manage_candidate": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "employer_update_company_info": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    # Common
    "common_feedback": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_support": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_about_us": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_notification": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_login": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_account_and_password": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_faq": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_how_to_use": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_chat_with_us": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_social": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_social_facebook": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_social_linkedin": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_social_youtube": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_social_instagram": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg",
    "common_privacy_policy": "https://ssl.cdn-redfin.com/system_files/media/793544_JPG/genLdpUgcMediaBrowserUrlComp/item_0.jpg"
}

# ABOUT_US_IMAGE_URLS = {
#     "JOB_SEEKER": {
#         "FEEDBACK_GUIDE": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['about_us']}job_seeker_feedback_guide.png",
#         "ACHIEVEMENTS": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['about_us']}job_seeker_achievements.png",
#     },
#     "EMPLOYER": {
#         "FEEDBACK_GUIDE": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['about_us']}job_seeker_feedback_guide.png",
#         "ACHIEVEMENTS": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['about_us']}employer_achievements.png",
#     }
# }

# CHATBOT_ICONS = {
#     # Job Seeker
#     "job_seeker_search_job": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_search_job.png",
#     "job_seeker_search_company": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_search_company.png",
#     "job_seeker_manage_profile": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_manage_profile.png",
#     "job_seeker_track_application_status": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_track_application_status.png",
#     "job_seeker_manage_all_profile": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_manage_all_profile.png",
#     "job_seeker_myjob_profile": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_myjob_profile.png",
#     "job_seeker_attached_profile": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_attached_profile.png",
#     "job_seeker_about_us_target_1": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_about_us_target_1.png",
#     "job_seeker_about_us_target_2": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_about_us_target_2.png",
#     "job_seeker_about_us_target_3": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_about_us_target_3.png",
#     "job_seeker_about_us_target_4": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}job_seeker_about_us_target_4.png",
#     # Employer
#     "employer_search_candidate": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}employer_search_candidate.png",
#     "employer_manage_candidate": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}employer_manage_candidate.png",
#     "employer_update_company_info": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}employer_update_company_info.png",
#     # Common
#     "common_feedback": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_feedback.png",
#     "common_support": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_support.png",
#     "common_about_us": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_about_us.png",
#     "common_notification": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_notification.png",
#     "common_login": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_login.png",
#     "common_account_and_password": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_account_and_password.png",
#     "common_faq": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_faq.png",
#     "common_how_to_use": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_how_to_use.png",
#     "common_chat_with_us": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_chat_with_us.png",
#     "common_social": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_social.png",
#     "common_social_facebook": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_social_facebook.png",
#     "common_social_linkedin": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_social_linkedin.png",
#     "common_social_youtube": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_social_youtube.png",
#     "common_social_instagram": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_social_instagram.png",
#     "common_privacy_policy": f"{settings.CLOUDINARY_PATH.format('1')}{settings.CLOUDINARY_DIRECTORY['icons']}common_privacy_policy.png"
# }

SOCIAL_MEDIA_LINKS = {
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "youtube": "https://www.youtube.com",
    "instagram": "https://www.instagram.com",
    "github": "https://github.com",
    "tiktok": "https://www.tiktok.com",
    "twitter": "",
    "telegram": "",
}

PLATFORM_CHOICES = (
    ('WEB', 'Website'),
    ('APP', 'Ứng dụng')
)

LINK_GOOGLE_PLAY = "https://play.google.com/store/apps?hl=en"
LINK_APPSTORE = "https://www.apple.com/vn/app-store/"

ROLE_CHOICES = (
    (ADMIN, 'Quản trị viên'),
    (EMPLOYER, 'Nhà tuyển dụng'),
    (JOB_SEEKER, 'Người tìm việc')
)

JOB_POST_STATUS = (
    (1, 'Chờ duyệt'),
    (2, 'Không duyệt'),
    (3, 'Đã duyệt')
)

GENDER_CHOICES = (
    ('M', 'Nam'),
    ('F', 'Nữ'),
    ('O', 'Khác')
)

MARITAL_STATUS_CHOICES = (
    ('S', 'Độc thân'),
    ('M', 'Đã kết hôn')
)

LANGUAGE_CHOICES = (
    (1, 'Việt Nam'),
    (2, 'Anh'),
    (3, 'Nhật Bản'),
    (4, 'Pháp'),
    (5, 'Trung Quốc'),
    (6, 'Nga'),
    (7, 'Hàn Quốc'),
    (8, 'Đức'),
    (9, 'Ý'),
    (10, 'Ả Rập'),
    (11, 'Khác'),
)

LANGUAGE_LEVEL_CHOICES = (
    (1, 'Level 1'),
    (2, 'Level 2'),
    (3, 'Level 3'),
    (4, 'Level 4'),
    (5, 'Level 5')
)

POSITION_CHOICES = (
    (1, 'Quản lý cấp cao'),
    (2, 'Quản lý cấp trung'),
    (3, 'Quản lý nhóm- giám sát'),
    (4, 'Chuyên gia'),
    (5, 'Chuyên viên- nhân viên'),
    (6, 'Cộng tác viên'),
)

TYPE_OF_WORKPLACE_CHOICES = (
    (1, 'Làm việc tại văn phòng'),
    (2, 'Làm việc kết hợp'),
    (3, 'Làm việc tại nhà')
)

JOB_TYPE_CHOICES = (
    (1, 'Toàn thời gian cố định'),
    (2, 'Toàn thời gian tạm thời'),
    (3, 'Bán thời gian cố định'),
    (4, 'Bán thời gian tạm thời'),
    (5, 'Theo hợp đồng tư vấn'),
    (6, 'Thực tập'),
    (7, 'Khác'),
)

EXPERIENCE_CHOICES = (
    (1, 'Chưa có kinh nghiệm'),
    (2, 'Dưới 1 năm kinh nghiệm '),
    (3, '1 năm kinh nghiệm'),
    (4, '2 năm kinh nghiệm'),
    (5, '3 năm kinh nghiệm'),
    (6, '4 năm kinh nghiệm'),
    (7, '5 năm kinh nghiệm'),
    (8, 'Trên 5 năm kinh nghiệm')
)

ACADEMIC_LEVEL = (
    (1, 'Trên Đại học'),
    (2, 'Đại học'),
    (3, 'Cao đẳng'),
    (4, 'Trung cấp'),
    (5, 'Trung học'),
    (6, 'Chứng chỉ')
)

EMPLOYEE_SIZE_CHOICES = (
    (1, 'Dưới 10 nhân viên'),
    (2, '10 - 150 nhân viên'),
    (3, '150 - 300 nhân viên'),
    (4, 'Trên 300 nhân viên'),
)

APPLICATION_STATUS = (
    (1, 'Chờ xác nhận'),
    (2, 'Đã liên hệ'),
    (3, 'Đã test'),
    (4, 'Đã phỏng vấn'),
    (5, 'Trúng tuyển'),
    (6, 'Không trúng tuyển')
)

FREQUENCY_NOTIFICATION = (
    (1, 'Mỗi ngày'),
    (2, '3 Ngày / lần'),
    (3, '1 Tuần / 1 lần'),
)

DESCRIPTION_LOCATION = (
    (1, 'TOP_LEFT'),
    (2, 'TOP_RIGHT'),
    (3, 'BOTTOM_LEFT'),
    (4, 'BOTTOM_RIGHT')
)

BANNER_TYPE = (
    (1, 'HOME'),
    (2, 'MAIN_JOB_RIGHT'),
)
