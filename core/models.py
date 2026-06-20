from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name_fa = models.CharField(max_length=100, verbose_name="نام فارسی")
    name_en = models.CharField(max_length=100, verbose_name="نام انگلیسی")
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['name_fa']
    
    def __str__(self):
        return f"{self.name_fa} / {self.name_en}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name_fa = models.CharField(max_length=100, verbose_name="نام فارسی")
    name_en = models.CharField(max_length=100, verbose_name="نام انگلیسی")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "زیردسته"
        verbose_name_plural = "زیردسته‌ها"
        ordering = ['category', 'name_fa']
    
    def __str__(self):
        return f"{self.category.name_fa} > {self.name_fa}"


class Hashtag(models.Model):
    LANGUAGE_CHOICES = [
        ('fa', 'فارسی'),
        ('en', 'انگلیسی'),
    ]
    
    tag = models.CharField(max_length=200, verbose_name="هشتگ")
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='fa')
    post_count = models.BigIntegerField(default=0, verbose_name="تعداد پست")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='hashtags')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='hashtags')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "هشتگ"
        verbose_name_plural = "هشتگ‌ها"
        ordering = ['-post_count']
        indexes = [
            models.Index(fields=['language', 'category']),
            models.Index(fields=['post_count']),
        ]
    
    def __str__(self):
        return f"{self.tag} ({self.post_count:,} پست)"
    
    @property
    def competition_level(self):
        """سطح رقابت بر اساس تعداد پست"""
        if self.post_count < 50_000:
            return 'low'
        elif self.post_count < 300_000:
            return 'medium'
        elif self.post_count < 2_000_000:
            return 'high'
        else:
            return 'very_high'
    
    def save(self, *args, **kwargs):
        if self.tag and not self.tag.startswith('#'):
            self.tag = f"#{self.tag}"
        super().save(*args, **kwargs)


class SiteVisit(models.Model):
    """مدل ثبت بازدید روزانه"""
    date = models.DateField(auto_now_add=True, verbose_name="تاریخ")
    ip_address = models.GenericIPAddressField(verbose_name="آدرس IP")
    endpoint = models.CharField(max_length=100, verbose_name="مسیر درخواست")
    user_agent = models.TextField(blank=True, verbose_name="مرورگر کاربر")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = "بازدیدها"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.ip_address} - {self.date} - {self.endpoint}"