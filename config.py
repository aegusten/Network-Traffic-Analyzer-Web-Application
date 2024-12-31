# config.py
import os

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "/app/uploads/")
FILE_FOLDER = os.getenv("FILE_FOLDER", "/app/files/")
PDF_FOLDER = os.getenv("PDF_FOLDER", "/app/files/pdf/")
