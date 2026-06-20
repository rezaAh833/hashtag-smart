"""
Django settings for hashtag_smart project.
"""
import dj_database_url
from pathlib import Path
import os

# ============================================================
# ۱. مسیرهای پایه
# ============================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# ۲. امنیت - کلیدها و حالت اجرا
# ============================================================
# کلید رمزنگاری - در production حتماً از متغیر محیطی خونده بشه
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-^&f8m+20j$rt3%%bugj8887@(aan&vs4npal@%%)73u0mraco4')

# DEBUG = True یعنی خطاها با جزئیات نمایش داده بشن (فقط توی توسعه)
# در production حتماً False باشه تا اطلاعات سرور لو نره
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# لیست هاست‌های مجاز - * یعنی همه (فقط برای تست)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# ============================================================
# ۳. امنیت - محافظت از کوکی‌ها و ارتباطات
# ============================================================
# جلوگیری از MIME-type sniffing (حمله‌کننده نتونه نوع فایل رو حدس بزنه)
SECURE_CONTENT_TYPE_NOSNIFF = True

# جلوگیری از XSS در مرورگرهای قدیمی
SECURE_BROWSER_XSS_FILTER = True

# جلوگیری از نمایش سایت در iframe (جلوگیری از Clickjacking)
X_FRAME_OPTIONS = 'DENY'

# کوکی‌های CSRF و Session فقط از طریق HTTPS ارسال بشن
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG

# ============================================================
# ۴. اپلیکیشن‌ها
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',     # اجازه دسترسی از دامنه‌های دیگه (فرانت جدا شده)
    'core',             # اپ اصلی ما
]

# ============================================================
# ۵. میان‌افزارها (Middleware)
# ============================================================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',           # باید اول باشه - مدیریت CORS
    'django.middleware.security.SecurityMiddleware',   # امنیت پایه (HSTS و...)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',       # محافظت CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hashtag_smart.urls'


# ============================================================
# ۶. قالب‌ها - دیگه استفاده نمی‌کنیم (فرانت جداست)
# ============================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hashtag_smart.wsgi.application'

# ============================================================
# ۷. پایگاه داده PostgreSQL
# ============================================================
DATABASES = {
    'default': dj_database_url.config(
        default="postgres://postgres:rezaAH83@localhost:5432/hashtag_db",
        conn_max_age=600
    )
}

# ============================================================
# ۸. اعتبارسنجی رمز عبور
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================
# ۹. بین‌المللی‌سازی
# ============================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ============================================================
# ۱۰. فایل‌های استاتیک
# ============================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ============================================================
# ۱۱. تنظیمات CORS - دسترسی فرانت‌اند
# ============================================================
# در production فقط دامنه‌های مشخص مجاز باشن
CORS_ALLOWED_ORIGINS = os.environ.get(
    'CORS_ORIGINS',
    'http://127.0.0.1:5500,http://localhost:5500'
).split(',')

# فقط متدهای GET و OPTIONS رو قبول کن (نیاز به POST/PUT/DELETE نداریم)
CORS_ALLOW_METHODS = ['GET', 'OPTIONS']

# ============================================================
# ۱۲. نوع فیلد پیش‌فرض
# ============================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================
# ۱۳. لاگ‌گیری - ثبت خطاها و رویدادها
# ============================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {module}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}