import random

def get_page_size(followers):
    """تشخیص سایز پیج"""
    if followers <= 5_000:
        return 'small'
    elif followers <= 50_000:
        return 'medium'
    elif followers <= 500_000:
        return 'large'
    else:
        return 'very_large'

def get_optimal_count(followers):
    """تعداد بهینه هشتگ"""
    if followers <= 5_000:
        return 5
    elif followers <= 50_000:
        return 5
    elif followers <= 500_000:
        return 4
    else:
        return 2

def get_distribution(followers):
    """توزیع درصدی سطوح رقابت"""
    if followers <= 5_000:
        return {'low': 3, 'medium': 3, 'high': 2}
    elif followers <= 50_000:
        return {'low': 2, 'medium': 2, 'high': 2}
    elif followers <= 500_000:
        return {'low': 1, 'medium': 2, 'high': 1}
    else:
        return {'low': 1, 'medium': 0, 'high': 1}

def get_recommendation_message(followers):
    """پیام پیشنهادی بر اساس سایز پیج"""
    if followers <= 5_000:
        return "پیج شما تازه‌کار است. از هشتگ‌های کم‌رقابت و متوسط استفاده کنید تا دیده شوید."
    elif followers <= 50_000:
        return "پیج شما در حال رشد است. ترکیب هشتگ‌های کم‌رقابت و متوسط و پررقابت مناسب شماست."
    elif followers <= 500_000:
        return "پیج شما بزرگ است. تمرکز روی کیفیت محتوا و هشتگ‌های تخصصی."
    else:
        return "پیج شما بسیار بزرگ است. هشتگ صرفاً برای کلاس‌بندی محتوا استفاده شود."

def get_specialized_hashtags(queryset, followers):
    """
    انتخاب هوشمند هشتگ‌ها برای بخش تخصصی
    
    Args:
        queryset: QuerySet از هشتگ‌های فیلترشده
        followers: تعداد فالوئر
    
    Returns:
        لیست هشتگ‌های انتخاب‌شده
    """
    dist = get_distribution(followers)
    total_needed = get_optimal_count(followers)
    
    # جدا کردن هشتگ‌ها بر اساس competition_level
    low_tags = list(queryset.filter(post_count__lt=50_000))
    medium_tags = list(queryset.filter(post_count__gte=50_000, post_count__lt=300_000))
    high_tags = list(queryset.filter(post_count__gte=300_000))
    
    selected = []
    
    def pick_random(tag_list, count):
        """انتخاب تصادفی از یک لیست"""
        available = [t for t in tag_list if t not in selected]
        return random.sample(available, min(count, len(available)))
    
    # انتخاب به ترتیب اولویت
    selected.extend(pick_random(low_tags, dist['low']))
    selected.extend(pick_random(medium_tags, dist['medium']))
    selected.extend(pick_random(high_tags, dist['high']))
    
    # اگه کم آوردیم، از بقیه پر کن
    if len(selected) < total_needed:
        remaining = total_needed - len(selected)
        all_remaining = [t for t in queryset if t not in selected]
        if all_remaining:
            selected.extend(random.sample(all_remaining, min(remaining, len(all_remaining))))
    
    # برگردوندن تگ‌ها
    return [h.tag for h in selected[:total_needed]]