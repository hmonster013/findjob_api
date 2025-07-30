from celery import shared_task
from firebase_admin import firestore, credentials
from helpers import helper
from configs import variable_system
from authentication.models import User
import firebase_admin
import os
import json


def initialize_firebase_if_needed():
    """
    Khởi tạo Firebase Admin SDK nếu chưa được khởi tạo
    """
    if not firebase_admin._apps:
        try:
            from django.conf import settings
            firebase_credentials_path = getattr(settings, 'FIREBASE_CREDENTIALS_PATH', '')
            firebase_database_url = getattr(settings, 'FIREBASE_DATABASE_URL', '')
            
            if firebase_credentials_path and os.path.exists(firebase_credentials_path):
                with open(firebase_credentials_path, 'r') as f:
                    firebase_config = json.load(f)
                
                cred = credentials.Certificate(firebase_config)
                firebase_admin.initialize_app(cred, {
                    'databaseURL': firebase_database_url
                })
                print("✅ Firebase Admin SDK initialized in Celery worker")
            else:
                raise RuntimeError("Firebase credentials file not found")
        except Exception as e:
            print(f"❌ Failed to initialize Firebase in Celery worker: {e}")
            raise e


@shared_task
def update_avatar(user_id, avatar_url):
    if not avatar_url:
        avatar_url = variable_system.AVATAR_DEFAULT["AVATAR"]
    
    try:
        initialize_firebase_if_needed()
        database = firestore.client()
        account_ref = database.collection("accounts").document(str(user_id))
        
        account_doc = account_ref.get()
        if account_doc.exists:
            account = account_doc.to_dict()
            update_data = {
                "avatarUrl": avatar_url
            }

            if account.get("company"):
                update_data.update({"company.imageUrl": avatar_url})
            account_ref.update(update_data)
    except Exception as e:
        helper.print_log_error("update_avatar", e)


@shared_task
def update_info(user_id, name):
    try:
        initialize_firebase_if_needed()
        database = firestore.client()
        account_ref = database.collection("accounts").document(str(user_id))

        account_doc = account_ref.get()
        if account_doc.exists:
            account = account_doc.to_dict()
            update_data = {
                "name": name
            }

            if account.get("company"):
                update_data.update({
                    "company.companyName": name,
                })
            account_ref.update(update_data)
    except Exception as e:
        helper.print_log_error("update_info", e)


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def sync_user_to_firebase_task(self, user_id, company_id=None):
    """
    Task bất đồng bộ để sync user data vào Firebase Firestore
    """
    try:
        # Khởi tạo Firebase nếu cần
        initialize_firebase_if_needed()
        
        user = User.objects.get(id=user_id)
        company = None
        
        if company_id:
            from info.models import Company
            company = Company.objects.get(id=company_id)
        
        # Lấy Firestore client
        db = firestore.client()
        doc_ref = db.collection('accounts').document(str(user.id))

        # Get avatar URL from user's avatar relationship
        avatar_url = None
        if user.avatar:
            try:
                avatar_url = user.avatar.get_full_url()
            except Exception:
                pass  # Ignore error if avatar method fails

        # Get company logo URL if company exists
        company_logo_url = None
        if company and hasattr(company, 'logo') and company.logo:
            try:
                company_logo_url = company.logo.get_full_url()
            except Exception:
                pass

        # Prepare user data for Firestore
        user_data = {
            'id': user.id,
            'name': user.full_name,
            'email': user.email,
            'avatarUrl': avatar_url,
            'roleName': user.role_name,
            'isActive': user.is_active,
            'isVerifyEmail': user.is_verify_email,
            'hasCompany': user.has_company,
            'company': {
                'id': company.id if company else None,
                'name': company.company_name if company else None,
                'imageUrl': company_logo_url,
                'slug': company.slug if company else None
            } if company else None
        }

        # Update or create document in Firestore
        doc_ref.set(user_data, merge=True)
        
        print(f"✅ [sync_user_to_firebase_task] Successfully synced user {user_id} to Firebase")
        
    except User.DoesNotExist:
        print(f"❌ [sync_user_to_firebase_task] User {user_id} not found")
    except RuntimeError as e:
        print(f"❌ [sync_user_to_firebase_task] Firebase not initialized: {e}")
        # Không retry nếu Firebase chưa được khởi tạo
    except Exception as e:
        helper.print_log_error("sync_user_to_firebase_task", e)
        # Retry task nếu có lỗi khác
        try:
            self.retry(countdown=60, max_retries=3)
        except self.MaxRetriesExceededError:
            print(f"❌ [sync_user_to_firebase_task] Max retries exceeded for user {user_id}")
            raise e


