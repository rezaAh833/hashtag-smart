from django.contrib import admin
from .models import Category, SubCategory, Hashtag, SiteVisit


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    fields = ['name_fa', 'name_en']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_fa', 'name_en', 'slug', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name_fa', 'name_en', 'slug']
    prepopulated_fields = {'slug': ('name_en',)}
    inlines = [SubCategoryInline]
    readonly_fields = ['created_at']


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'language', 'post_count', 'category', 'subcategory', 'is_active', 'updated_at']
    list_filter = ['language', 'category', 'subcategory', 'is_active']
    search_fields = ['tag', 'category__name_fa', 'subcategory__name_fa']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 50
    
    actions = ['activate_all', 'deactivate_all']
    
    @admin.action(description='فعال کردن')
    def activate_all(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} هشتگ فعال شد.')
    
    @admin.action(description='غیرفعال کردن')
    def deactivate_all(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} هشتگ غیرفعال شد.')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_fa', 'name_en', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['name_fa', 'name_en']


@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ['date', 'ip_address', 'endpoint', 'created_at']
    list_filter = ['date', 'endpoint']
    search_fields = ['ip_address']
    readonly_fields = ['date', 'ip_address', 'endpoint', 'user_agent', 'created_at']
    date_hierarchy = 'date'
    list_per_page = 30
    
    def has_add_permission(self, request):
        return False


admin.site.site_header = 'پنل مدیریت هشتگ یار'
admin.site.site_title = 'هشتگ یار'
admin.site.index_title = 'مدیریت هشتگ‌ها'