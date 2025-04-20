from decouple import config
import os

print("EMAIL_HOST_PASSWORD:", repr(config("EMAIL_HOST_PASSWORD")))
print("Current working directory:", os.getcwd())
print("All files in cwd:", os.listdir())
