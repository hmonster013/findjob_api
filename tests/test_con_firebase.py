from pathlib import Path
import firebase_admin
from firebase_admin import credentials

BASE_DIR = Path(__file__).resolve().parent.parent

FIREBASE_CREDENTIALS_PATH = BASE_DIR / "firebase_cred.json"

if FIREBASE_CREDENTIALS_PATH.exists():
    cred = credentials.Certificate(str(FIREBASE_CREDENTIALS_PATH))
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
        print("✅ Firebase initialized successfully!")
else:
    print("❌ firebase_cred.json not found!")
