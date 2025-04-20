import os
import sys
import django

# === Thêm thư mục cha vào sys.path để import đúng ===
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# === Setup Django ===
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'findjob_api.settings')
django.setup()

# === Import celery app ===
from findjob_api.celery import app
from celery.result import AsyncResult

# === Task test ===
@app.task(bind=True)
def test_celery_redis(self, x, y):
    print(f"[CELERY] Processing {x} + {y}")
    return x + y


if __name__ == '__main__':
    print("📤 Sending test task to Celery...")
    result = test_celery_redis.delay(7, 3)

    print(f"Task ID: {result.id}")
    print("⌛ Waiting for result...")
    output = result.get(timeout=10)

    print(f"✅ Result from Celery: {output}")
