from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django_ratelimit.decorators import ratelimit
from .models import Category, SubCategory, Hashtag, SiteVisit
from .utils import get_specialized_hashtags, get_recommendation_message


def track_visit(request):
    """ثبت بازدید"""
    SiteVisit.objects.create(
        ip_address=request.META.get('REMOTE_ADDR', '0.0.0.0'),
        endpoint=request.path,
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500]
    )


def index(request):
    """
    ریشه API - اطلاعات پایه
    بدون محدودیت نرخ چون فقط یه JSON ساده‌ست
    """
    return JsonResponse({
        'name': 'هشتگ یار API',
        'version': '1.0',
        'status': 'running',
        'endpoints': {
            'categories': '/api/categories/?language=fa',
            'search': '/api/search-categories/?q=...&language=fa',
            'hashtags': '/api/hashtags/?language=fa&category=...&followers=...',
        }
    })


@require_GET
@ratelimit(key='ip', rate='30/m', block=True)
def get_categories(request):
    track_visit(request)
    language = request.GET.get('language', 'fa')
    
    categories = Category.objects.prefetch_related('subcategories').only(
        'slug', 'name_fa', 'name_en'
    )
    
    data = []
    for cat in categories:
        subs = []
        for sub in cat.subcategories.all():
            subs.append({
                'id': sub.id,
                'name': sub.name_fa if language == 'fa' else sub.name_en
            })
        
        data.append({
            'slug': cat.slug,
            'name': cat.name_fa if language == 'fa' else cat.name_en,
            'subcategories': subs
        })
    
    return JsonResponse({'categories': data})


@require_GET
@ratelimit(key='ip', rate='20/m', block=True)
def search_categories(request):
    track_visit(request)
    query = request.GET.get('q', '').strip()
    language = request.GET.get('language', 'fa')
    
    if not query or len(query) < 2:
        return JsonResponse({'results': []})
    
    results = []
    
    if language == 'fa':
        categories = Category.objects.filter(
            name_fa__icontains=query
        ).only('slug', 'name_fa', 'name_en')[:10]
    else:
        categories = Category.objects.filter(
            name_en__icontains=query
        ).only('slug', 'name_fa', 'name_en')[:10]
    
    for cat in categories:
        results.append({
            'type': 'category',
            'slug': cat.slug,
            'name': cat.name_fa if language == 'fa' else cat.name_en,
            'subcategory_id': None,
            'category_name': cat.name_fa if language == 'fa' else cat.name_en
        })
    
    if language == 'fa':
        subcategories = SubCategory.objects.filter(
            name_fa__icontains=query
        ).select_related('category').only(
            'id', 'name_fa', 'name_en', 'category__slug', 'category__name_fa', 'category__name_en'
        )[:10]
    else:
        subcategories = SubCategory.objects.filter(
            name_en__icontains=query
        ).select_related('category').only(
            'id', 'name_fa', 'name_en', 'category__slug', 'category__name_fa', 'category__name_en'
        )[:10]
    
    for sub in subcategories:
        results.append({
            'type': 'subcategory',
            'slug': sub.category.slug,
            'name': sub.name_fa if language == 'fa' else sub.name_en,
            'subcategory_id': sub.id,
            'category_name': sub.category.name_fa if language == 'fa' else sub.category.name_en
        })
    
    return JsonResponse({'results': results[:20]})


@require_GET
@ratelimit(key='ip', rate='10/m', block=True)
def get_hashtags(request):
    track_visit(request)
    language = request.GET.get('language', 'fa')
    lang_code = 'fa' if language in ['fa', 'persian'] else 'en'
    followers = int(request.GET.get('followers', 0))
    category_slug = request.GET.get('category', '')
    subcategory_id = request.GET.get('subcategory', '')
    
    hashtags = Hashtag.objects.filter(
        language=lang_code,
        is_active=True
    ).select_related('category', 'subcategory')
    
    if category_slug:
        hashtags = hashtags.filter(category__slug=category_slug)
    
    if subcategory_id and subcategory_id != '':
        hashtags = hashtags.filter(subcategory_id=int(subcategory_id))
    
    competitive_qs = hashtags.filter(
        post_count__gte=300_000
    ).order_by('-post_count')[:12]
    competitive_tags = [h.tag for h in competitive_qs]
    
    low_medium_qs = hashtags.filter(
        post_count__lt=300_000
    ).order_by('post_count')[:12]
    low_medium_tags = [h.tag for h in low_medium_qs]
    
    specialized_tags = get_specialized_hashtags(hashtags, followers)
    
    message = get_recommendation_message(followers)
    
    return JsonResponse({
        'competitive': competitive_tags,
        'low_medium': low_medium_tags,
        'specialized': specialized_tags,
        'recommendation': {
            'message': message,
            'special_group': 'specialized'
        }
    })