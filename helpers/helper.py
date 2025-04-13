import time

from datetime import datetime
from django.conf import settings
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from configs import variable_system
from console.jobs import queue_notification

def print_log_error(func_name, error, now=datetime.now()):
    print(f"ERROR [{now}][{func_name}] >> {error}")

def get_full_client_url(func):
    app_env = settings.APP_ENVIRONMENT
    
    return settings.DOMAIN_CLIENT[app_env] + func

def check_expiration_time(expiration_time):
    return expiration_time - int(time.time()) > 0

def urlsafe_base64_decode_with_encoded_data(encoded_data):
    try:
        encoded_data_split = str(encoded_data).split("|")
        data = force_str(urlsafe_base64_decode(encoded_data_split[0]))
        expiration_time = force_str(urlsafe_base64_decode(encoded_data_split[1]))
        
        return data, int(expiration_time)
    except:
        return None, None

def add_system_notifications(title, content, user_id_list):
    try:
        type_name = variable_system.NOTIFICATION_TYPE["SYSTEM"]
        queue_notification.add_notification_to_user.delay(title=title, content=content,
                                                          type_name=type_name, user_id_list=user_id_list)
    except Exception as ex:
        print_log_error("add_system_notifications", ex)