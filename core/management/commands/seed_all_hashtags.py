from django.core.management.base import BaseCommand
from core.models import Category, SubCategory, Hashtag

class Command(BaseCommand):
    help = 'Seed all hashtags for all categories'

    def create_category_with_subs(self, cat_data):
        """ساخت دسته‌بندی با زیردسته‌هاش"""
        cat, created = Category.objects.get_or_create(
            name_fa=cat_data['name_fa'],
            name_en=cat_data['name_en'],
            slug=cat_data['slug']
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'✅ دسته‌بندی {cat_data["name_fa"]} ساخته شد'))
        
        sub_objects = {}
        for slug, names in cat_data['subcategories'].items():
            sub, _ = SubCategory.objects.get_or_create(
                category=cat,
                name_fa=names['fa'],
                name_en=names['en']
            )
            sub_objects[slug] = sub
        
        return cat, sub_objects

    def seed_hashtags(self, category, sub_objects, hashtags_data):
        """اضافه کردن هشتگ‌ها"""
        created_count = 0
        updated_count = 0
        
        for h_data in hashtags_data:
            sub = sub_objects.get(h_data.get('sub'))
            hashtag, created = Hashtag.objects.update_or_create(
                tag=h_data['tag'],
                language='fa',
                category=category,
                defaults={
                    'post_count': h_data['post_count'],
                    'subcategory': sub,
                    'is_active': True
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1
        
        return created_count, updated_count

    def handle(self, *args, **options):
        total_created = 0
        total_updated = 0

        # ==========================================
        # ۱. غذا و نوشیدنی
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: غذا و نوشیدنی')
        
        food_cat, food_subs = self.create_category_with_subs({
            'name_fa': 'غذا و نوشیدنی',
            'name_en': 'Food & Drinks',
            'slug': 'food',
            'subcategories': {
                'persian-food': {'fa': 'غذای ایرانی', 'en': 'Persian Food'},
                'fast-food': {'fa': 'فست فود', 'en': 'Fast Food'},
                'cooking': {'fa': 'آشپزی', 'en': 'Cooking'},
                'drinks': {'fa': 'نوشیدنی', 'en': 'Drinks'},
                'dessert': {'fa': 'دسر و شیرینی', 'en': 'Dessert & Sweets'},
                'diet-food': {'fa': 'غذای رژیمی', 'en': 'Diet Food'},
                'seafood': {'fa': 'غذای دریایی', 'en': 'Seafood'},
                'soup-salad': {'fa': 'سوپ و سالاد', 'en': 'Soup & Salad'},
                'restaurant-cafe': {'fa': 'رستوران و کافه', 'en': 'Restaurant & Cafe'},
                'general': {'fa': 'عمومی', 'en': 'General'},
            }
        })

        food_hashtags = [
            # ========== غذای ایرانی ==========
            {'tag': '#غذا', 'post_count': 5000000, 'sub': 'persian-food'},
            {'tag': '#غذای_ایرانی', 'post_count': 1900000, 'sub': 'persian-food'},
            {'tag': '#غذای_سنتی', 'post_count': 5500, 'sub': 'persian-food'},
            {'tag': '#غذای_محلی', 'post_count': 160000, 'sub': 'persian-food'},
            {'tag': '#غذای_خانگی', 'post_count': 1000000, 'sub': 'persian-food'},
            {'tag': '#غذای_خوشمزه', 'post_count': 292000, 'sub': 'persian-food'},
            {'tag': '#غذای_سالم', 'post_count': 1500000, 'sub': 'persian-food'},
            {'tag': '#غذای_جنوبی', 'post_count': 32800, 'sub': 'persian-food'},
            {'tag': '#غذای_شمالی', 'post_count': 128000, 'sub': 'persian-food'},
            {'tag': '#غذای_ترکی', 'post_count': 39000, 'sub': 'persian-food'},
            {'tag': '#غذای_عربی', 'post_count': 23700, 'sub': 'persian-food'},
            {'tag': '#غذای_ایتالیایی', 'post_count': 31600, 'sub': 'persian-food'},
            {'tag': '#غذای_آسیایی', 'post_count': 5000, 'sub': 'persian-food'},
            {'tag': '#غذای_فرنگی', 'post_count': 57400, 'sub': 'persian-food'},
            {'tag': '#غذای_بین_المللی', 'post_count': 1000, 'sub': 'persian-food'},
            {'tag': '#کباب', 'post_count': 1200000, 'sub': 'persian-food'},
            {'tag': '#چلوکباب', 'post_count': 114000, 'sub': 'persian-food'},
            {'tag': '#کباب_کوبیده', 'post_count': 282000, 'sub': 'persian-food'},
            {'tag': '#جوجه_کباب', 'post_count': 389000, 'sub': 'persian-food'},
            {'tag': '#کباب_برگ', 'post_count': 99200, 'sub': 'persian-food'},
            {'tag': '#شیشلیک', 'post_count': 115000, 'sub': 'persian-food'},
            {'tag': '#خورشت', 'post_count': 479000, 'sub': 'persian-food'},
            {'tag': '#قورمه_سبزی', 'post_count': 133000, 'sub': 'persian-food'},
            {'tag': '#قیمه', 'post_count': 175000, 'sub': 'persian-food'},
            {'tag': '#فسنجان', 'post_count': 40400, 'sub': 'persian-food'},
            {'tag': '#کرفس', 'post_count': 121000, 'sub': 'persian-food'},
            {'tag': '#بامیه', 'post_count': 124000, 'sub': 'persian-food'},
            {'tag': '#آلو_اسفناج', 'post_count': 1000, 'sub': 'persian-food'},
            {'tag': '#برنج', 'post_count': 929000, 'sub': 'persian-food'},
            {'tag': '#چلو', 'post_count': 82600, 'sub': 'persian-food'},
            {'tag': '#پلو', 'post_count': 275000, 'sub': 'persian-food'},
            {'tag': '#کته', 'post_count': 62900, 'sub': 'persian-food'},
            {'tag': '#مرغ', 'post_count': 1000000, 'sub': 'persian-food'},
            {'tag': '#مرغ_سوخاری', 'post_count': 154000, 'sub': 'persian-food'},
            {'tag': '#مرغ_شکم_پر', 'post_count': 82000, 'sub': 'persian-food'},
            {'tag': '#مرغ_گریل', 'post_count': 14100, 'sub': 'persian-food'},
            
            # ========== فست فود ==========
            {'tag': '#فست_فود', 'post_count': 1500000, 'sub': 'fast-food'},
            {'tag': '#پیتزا', 'post_count': 1500000, 'sub': 'fast-food'},
            {'tag': '#برگر', 'post_count': 651000, 'sub': 'fast-food'},
            {'tag': '#همبرگر', 'post_count': 434000, 'sub': 'fast-food'},
            {'tag': '#چیزبرگر', 'post_count': 81200, 'sub': 'fast-food'},
            {'tag': '#ساندویچ', 'post_count': 771000, 'sub': 'fast-food'},
            {'tag': '#هات_داگ', 'post_count': 107000, 'sub': 'fast-food'},
            {'tag': '#دونر', 'post_count': 39800, 'sub': 'fast-food'},
            {'tag': '#شاورما', 'post_count': 957000, 'sub': 'fast-food'},
            {'tag': '#فلافل', 'post_count': 463000, 'sub': 'fast-food'},
            {'tag': '#سمبوسه', 'post_count': 604000, 'sub': 'fast-food'},
            {'tag': '#غذای_سریع', 'post_count': 132000, 'sub': 'fast-food'},
            
            # ========== آشپزی ==========
            {'tag': '#آشپزی', 'post_count': 1300000, 'sub': 'cooking'},
            {'tag': '#آشپزی_ایرانی', 'post_count': 1400000, 'sub': 'cooking'},
            {'tag': '#آشپزی_خانگی', 'post_count': 143000, 'sub': 'cooking'},
            {'tag': '#آشپزی_سنتی', 'post_count': 87400, 'sub': 'cooking'},
            {'tag': '#آشپزی_حرفه_ای', 'post_count': 15400, 'sub': 'cooking'},
            {'tag': '#آشپزی_آسان', 'post_count': 958000, 'sub': 'cooking'},
            {'tag': '#آشپزی_سالم', 'post_count': 121000, 'sub': 'cooking'},
            {'tag': '#دستور_پخت', 'post_count': 82000, 'sub': 'cooking'},
            {'tag': '#دستور_غذا', 'post_count': 27900, 'sub': 'cooking'},
            {'tag': '#سرآشپز', 'post_count': 271000, 'sub': 'cooking'},
            {'tag': '#آشپز', 'post_count': 103000, 'sub': 'cooking'},
            {'tag': '#شف', 'post_count': 168000, 'sub': 'cooking'},
            
            # ========== نوشیدنی ==========
            {'tag': '#نوشیدنی', 'post_count': 903000, 'sub': 'drinks'},
            {'tag': '#نوشیدنی_سرد', 'post_count': 345000, 'sub': 'drinks'},
            {'tag': '#نوشیدنی_گرم', 'post_count': 176000, 'sub': 'drinks'},
            {'tag': '#قهوه', 'post_count': 455000, 'sub': 'drinks'},
            {'tag': '#اسپرسو', 'post_count': 927000, 'sub': 'drinks'},
            {'tag': '#کاپوچینو', 'post_count': 331000, 'sub': 'drinks'},
            {'tag': '#لاته', 'post_count': 370000, 'sub': 'drinks'},
            {'tag': '#چای', 'post_count': 1600000, 'sub': 'drinks'},
            {'tag': '#چای_ایرانی', 'post_count': 154000, 'sub': 'drinks'},
            {'tag': '#دمنوش', 'post_count': 1300000, 'sub': 'drinks'},
            {'tag': '#اسموتی', 'post_count': 216000, 'sub': 'drinks'},
            {'tag': '#آبمیوه', 'post_count': 71100, 'sub': 'drinks'},
            {'tag': '#آب_پرتقال', 'post_count': 24400, 'sub': 'drinks'},
            {'tag': '#لیموناد', 'post_count': 53500, 'sub': 'drinks'},
            
            # ========== دسر و شیرینی ==========
            {'tag': '#دسر', 'post_count': 2800000, 'sub': 'dessert'},
            {'tag': '#دسر_خانگی', 'post_count': 369000, 'sub': 'dessert'},
            {'tag': '#ژله', 'post_count': 1000000, 'sub': 'dessert'},
            {'tag': '#پودینگ', 'post_count': 52400, 'sub': 'dessert'},
            {'tag': '#بستنی', 'post_count': 854000, 'sub': 'dessert'},
            {'tag': '#فالوده', 'post_count': 55600, 'sub': 'dessert'},
            {'tag': '#کیک', 'post_count': 1700000, 'sub': 'dessert'},
            {'tag': '#کیک_خانگی', 'post_count': 3100000, 'sub': 'dessert'},
            {'tag': '#کیک_شکلاتی', 'post_count': 1900000, 'sub': 'dessert'},
            {'tag': '#کاپ_کیک', 'post_count': 687000, 'sub': 'dessert'},
            {'tag': '#چیزکیک', 'post_count': 323000, 'sub': 'dessert'},
            {'tag': '#شیرینی', 'post_count': 3100000, 'sub': 'dessert'},
            {'tag': '#شیرینی_خانگی', 'post_count': 570000, 'sub': 'dessert'},
            {'tag': '#شیرینی_خشک', 'post_count': 319000, 'sub': 'dessert'},
            {'tag': '#باقلوا', 'post_count': 326000, 'sub': 'dessert'},
            {'tag': '#حلوا', 'post_count': 579000, 'sub': 'dessert'},
            {'tag': '#شله_زرد', 'post_count': 131000, 'sub': 'dessert'},
            {'tag': '#فرنی', 'post_count': 67600, 'sub': 'dessert'},
            {'tag': '#شکلات', 'post_count': 2100000, 'sub': 'dessert'},
            
            # ========== غذای رژیمی ==========
            {'tag': '#غذای_رژیمی', 'post_count': 270000, 'sub': 'diet-food'},
            {'tag': '#غذای_گیاهی', 'post_count': 75800, 'sub': 'diet-food'},
            {'tag': '#رژیمی', 'post_count': 506000, 'sub': 'diet-food'},
            {'tag': '#رژیم', 'post_count': 1900000, 'sub': 'diet-food'},
            {'tag': '#تغذیه_سالم', 'post_count': 1200000, 'sub': 'diet-food'},
            {'tag': '#سلامتی', 'post_count': 1000, 'sub': 'diet-food'},
            {'tag': '#گیاهخواری', 'post_count': 284000, 'sub': 'diet-food'},
            {'tag': '#گیاهخوار', 'post_count': 39500, 'sub': 'diet-food'},
            {'tag': '#وگان', 'post_count': 257000, 'sub': 'diet-food'},
            {'tag': '#وگن', 'post_count': 139000, 'sub': 'diet-food'},
            {'tag': '#ارگانیک', 'post_count': 1000000, 'sub': 'diet-food'},
            {'tag': '#بدون_گلوتن', 'post_count': 25000, 'sub': 'diet-food'},
            {'tag': '#کم_کالری', 'post_count': 37200, 'sub': 'diet-food'},
            {'tag': '#پروتئین', 'post_count': 880000, 'sub': 'diet-food'},
            {'tag': '#ویتامین', 'post_count': 667000, 'sub': 'diet-food'},
            
            # ========== غذای دریایی ==========
            {'tag': '#غذای_دریایی', 'post_count': 107000, 'sub': 'seafood'},
            {'tag': '#ماهی', 'post_count': 1300000, 'sub': 'seafood'},
            {'tag': '#ماهی_شکم_پر', 'post_count': 61800, 'sub': 'seafood'},
            {'tag': '#ماهی_کبابی', 'post_count': 28800, 'sub': 'seafood'},
            {'tag': '#میگو', 'post_count': 232000, 'sub': 'seafood'},
            {'tag': '#میگو_سوخاری', 'post_count': 55600, 'sub': 'seafood'},
            {'tag': '#استیک', 'post_count': 284000, 'sub': 'seafood'},
            {'tag': '#استیک_گوشت', 'post_count': 31000, 'sub': 'seafood'},
            
            # ========== سوپ و سالاد ==========
            {'tag': '#سوپ', 'post_count': 343000, 'sub': 'soup-salad'},
            {'tag': '#سوپ_جو', 'post_count': 43300, 'sub': 'soup-salad'},
            {'tag': '#سوپ_قارچ', 'post_count': 15500, 'sub': 'soup-salad'},
            {'tag': '#سوپ_مرغ', 'post_count': 11200, 'sub': 'soup-salad'},
            {'tag': '#سالاد', 'post_count': 1100000, 'sub': 'soup-salad'},
            {'tag': '#سالاد_شیرازی', 'post_count': 65800, 'sub': 'soup-salad'},
            {'tag': '#سالاد_سزار', 'post_count': 122000, 'sub': 'soup-salad'},
            {'tag': '#سالاد_فصل', 'post_count': 104000, 'sub': 'soup-salad'},
            {'tag': '#پاستا', 'post_count': 452000, 'sub': 'soup-salad'},
            {'tag': '#اسپاگتی', 'post_count': 45700, 'sub': 'soup-salad'},
            {'tag': '#لازانیا', 'post_count': 162000, 'sub': 'soup-salad'},
            {'tag': '#ماکارونی', 'post_count': 21400, 'sub': 'soup-salad'},
            {'tag': '#راویولی', 'post_count': 1000, 'sub': 'soup-salad'},
            
            # ========== رستوران و کافه ==========
            {'tag': '#رستوران', 'post_count': 3700000, 'sub': 'restaurant-cafe'},
            {'tag': '#کافه', 'post_count': 4300000, 'sub': 'restaurant-cafe'},
            {'tag': '#کترینگ', 'post_count': 168000, 'sub': 'restaurant-cafe'},
            
            # ========== عمومی ==========
            {'tag': '#خوشمزه', 'post_count': 5300000, 'sub': 'general'},
            {'tag': '#لذیذ', 'post_count': 588000, 'sub': 'general'},
            {'tag': '#نوش_جان', 'post_count': 44600, 'sub': 'general'},
            {'tag': '#خوردنی', 'post_count': 217000, 'sub': 'general'},
            {'tag': '#خوراک', 'post_count': 263000, 'sub': 'general'},
            {'tag': '#خوراکی', 'post_count': 758000, 'sub': 'general'},
            {'tag': '#سفره', 'post_count': 930000, 'sub': 'general'},
            {'tag': '#مزه', 'post_count': 857000, 'sub': 'general'},
            {'tag': '#طعمدار', 'post_count': 1000, 'sub': 'general'},
            {'tag': '#خانگی', 'post_count': 844000, 'sub': 'general'},
            {'tag': '#صبحانه', 'post_count': 1800000, 'sub': 'general'},
            {'tag': '#املت', 'post_count': 224000, 'sub': 'general'},
            {'tag': '#نان_و_پنیر', 'post_count': 500, 'sub': 'general'},
            {'tag': '#ناهار', 'post_count': 1000000, 'sub': 'general'},
            {'tag': '#شام', 'post_count': 1800000, 'sub': 'general'},
            {'tag': '#میان_وعده', 'post_count': 225000, 'sub': 'general'},
            {'tag': '#اسنک', 'post_count': 180000, 'sub': 'general'},
        ]
        
        c, u = self.seed_hashtags(food_cat, food_subs, food_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 غذا: {c} جدید, {u} بروزرسانی')

        # ==========================================
        # ۲. سفر و گردشگری
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: سفر و گردشگری')
        
        travel_cat, travel_subs = self.create_category_with_subs({
            'name_fa': 'سفر و گردشگری',
            'name_en': 'Travel & Tourism',
            'slug': 'travel',
            'subcategories': {
                'general-travel': {'fa': 'عمومی سفر', 'en': 'General Travel'},
                'nature-adventure': {'fa': 'طبیعت و ماجراجویی', 'en': 'Nature & Adventure'},
                'accommodation': {'fa': 'اقامت و سفر راحت', 'en': 'Accommodation'},
                'road-trip': {'fa': 'مسیر و تجربه سفر', 'en': 'Road & Experience'},
            }
        })

        travel_hashtags = [
            # ========== عمومی سفر ==========
            {'tag': '#سفر', 'post_count': 930000, 'sub': 'general-travel'},
            {'tag': '#سفرنامه', 'post_count': 385000, 'sub': 'general-travel'},
            {'tag': '#گردشگری', 'post_count': 4900000, 'sub': 'general-travel'},
            {'tag': '#ایرانگردی', 'post_count': 3100000, 'sub': 'general-travel'},
            {'tag': '#جهانگردی', 'post_count': 823000, 'sub': 'general-travel'},
            {'tag': '#طبیعتگردی', 'post_count': 5200000, 'sub': 'general-travel'},
            {'tag': '#مسافرت', 'post_count': 2700000, 'sub': 'general-travel'},
            {'tag': '#توریست', 'post_count': 926000, 'sub': 'general-travel'},
            {'tag': '#سفر_خوب', 'post_count': 5000, 'sub': 'general-travel'},
            {'tag': '#سفر_ارزان', 'post_count': 87400, 'sub': 'general-travel'},
            {'tag': '#کوله_گردی', 'post_count': 138000, 'sub': 'general-travel'},
            {'tag': '#سفر_ماجراجویانه', 'post_count': 5000, 'sub': 'general-travel'},
            
            # ========== طبیعت و ماجراجویی ==========
            {'tag': '#طبیعت', 'post_count': 12700000, 'sub': 'nature-adventure'},
            {'tag': '#طبیعت_ایران', 'post_count': 927000, 'sub': 'nature-adventure'},
            {'tag': '#منظره', 'post_count': 888000, 'sub': 'nature-adventure'},
            {'tag': '#کوهنوردی', 'post_count': 3000000, 'sub': 'nature-adventure'},
            {'tag': '#کمپینگ', 'post_count': 932000, 'sub': 'nature-adventure'},
            {'tag': '#آفرود', 'post_count': 658000, 'sub': 'nature-adventure'},
            {'tag': '#ماجراجویی', 'post_count': 411000, 'sub': 'nature-adventure'},
            {'tag': '#طبیعت_بکر', 'post_count': 698000, 'sub': 'nature-adventure'},
            {'tag': '#حیات_وحش', 'post_count': 664000, 'sub': 'nature-adventure'},
            {'tag': '#جنگل', 'post_count': 3100000, 'sub': 'nature-adventure'},
            {'tag': '#دریا', 'post_count': 4200000, 'sub': 'nature-adventure'},
            {'tag': '#ساحل', 'post_count': 1600000, 'sub': 'nature-adventure'},
            {'tag': '#کویر', 'post_count': 824000, 'sub': 'nature-adventure'},
            {'tag': '#آبشار', 'post_count': 842000, 'sub': 'nature-adventure'},
            {'tag': '#غار', 'post_count': 147000, 'sub': 'nature-adventure'},
            {'tag': '#کوهستان', 'post_count': 950000, 'sub': 'nature-adventure'},
            
            # ========== اقامت و سفر راحت ==========
            {'tag': '#هتل', 'post_count': 1200000, 'sub': 'accommodation'},
            {'tag': '#اقامتگاه', 'post_count': 304000, 'sub': 'accommodation'},
            {'tag': '#ویلا', 'post_count': 3100000, 'sub': 'accommodation'},
            {'tag': '#رزرو_هتل', 'post_count': 91000, 'sub': 'accommodation'},
            {'tag': '#سفر_خانوادگی', 'post_count': 11100, 'sub': 'accommodation'},
            {'tag': '#سفر_لوکس', 'post_count': 14200, 'sub': 'accommodation'},
            {'tag': '#اقامت', 'post_count': 824000, 'sub': 'accommodation'},
            {'tag': '#ویلاگردی', 'post_count': 1000, 'sub': 'accommodation'},
            {'tag': '#سفر_داخلی', 'post_count': 5000, 'sub': 'accommodation'},
            {'tag': '#سفر_خارجی', 'post_count': 44000, 'sub': 'accommodation'},
            
            # ========== مسیر و تجربه سفر ==========
            {'tag': '#جاده', 'post_count': 888000, 'sub': 'road-trip'},
            {'tag': '#جاده_چالوس', 'post_count': 345000, 'sub': 'road-trip'},
            {'tag': '#سفر_جاده_ای', 'post_count': 1000, 'sub': 'road-trip'},
            {'tag': '#رانندگی', 'post_count': 466000, 'sub': 'road-trip'},
            {'tag': '#سفر_با_ماشین', 'post_count': 1000, 'sub': 'road-trip'},
        ]
        
        c, u = self.seed_hashtags(travel_cat, travel_subs, travel_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 سفر: {c} جدید, {u} بروزرسانی')



        # ==========================================
        # ۳. خودرو
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: خودرو')
        
        cars_cat, cars_subs = self.create_category_with_subs({
            'name_fa': 'خودرو',
            'name_en': 'Cars',
            'slug': 'cars',
            'subcategories': {
                'general-cars': {'fa': 'عمومی خودرو', 'en': 'General Cars'},
                'iranian-cars': {'fa': 'خودروهای ایرانی', 'en': 'Iranian Cars'},
                'foreign-cars': {'fa': 'خودروهای خارجی', 'en': 'Foreign Cars'},
                'luxury-cars': {'fa': 'خودروهای لوکس', 'en': 'Luxury Cars'},
                'tuning-sport': {'fa': 'تیونینگ و اسپرت', 'en': 'Tuning & Sport'},
                'motorcycle-racing': {'fa': 'موتور و مسابقات', 'en': 'Motorcycle & Racing'},
                'offroad': {'fa': 'آفرود', 'en': 'Offroad'},
                'repair-maintenance': {'fa': 'تعمیر و نگهداری', 'en': 'Repair & Maintenance'},
                'buy-sell': {'fa': 'خرید و فروش', 'en': 'Buy & Sell'},
                'classic-cars': {'fa': 'خودروهای کلاسیک', 'en': 'Classic Cars'},
            }
        })

        cars_hashtags = [
            # ========== عمومی خودرو ==========
            {'tag': '#خودرو', 'post_count': 4300000, 'sub': 'general-cars'},
            {'tag': '#ماشین', 'post_count': 7700000, 'sub': 'general-cars'},
            {'tag': '#اتومبیل', 'post_count': 650000, 'sub': 'general-cars'},
            {'tag': '#ماشین_باز', 'post_count': 2300000, 'sub': 'general-cars'},
            {'tag': '#خودروباز', 'post_count': 1000, 'sub': 'general-cars'},
            {'tag': '#عاشق_ماشین', 'post_count': 1000, 'sub': 'general-cars'},
            {'tag': '#دنیای_خودرو', 'post_count': 5000, 'sub': 'general-cars'},
            {'tag': '#اخبار_خودرو', 'post_count': 51200, 'sub': 'general-cars'},
            {'tag': '#خودرو_باز', 'post_count': 1000, 'sub': 'general-cars'},
            {'tag': '#ماشین_سواری', 'post_count': 26500, 'sub': 'general-cars'},
            
            # ========== خودروهای ایرانی ==========
            {'tag': '#خودرو_ایرانی', 'post_count': 36000, 'sub': 'iranian-cars'},
            {'tag': '#ماشین_ایرانی', 'post_count': 61000, 'sub': 'iranian-cars'},
            {'tag': '#ایران_خودرو', 'post_count': 447000, 'sub': 'iranian-cars'},
            {'tag': '#سایپا', 'post_count': 1300000, 'sub': 'iranian-cars'},
            {'tag': '#پژو', 'post_count': 2000000, 'sub': 'iranian-cars'},
            {'tag': '#سمند', 'post_count': 866000, 'sub': 'iranian-cars'},
            {'tag': '#دنا', 'post_count': 600000, 'sub': 'iranian-cars'},
            {'tag': '#تارا', 'post_count': 191000, 'sub': 'iranian-cars'},
            {'tag': '#شاهین', 'post_count': 431000, 'sub': 'iranian-cars'},
            {'tag': '#کوییک', 'post_count': 195000, 'sub': 'iranian-cars'},
            {'tag': '#رانا', 'post_count': 193000, 'sub': 'iranian-cars'},
            {'tag': '#پارس', 'post_count': 1900000, 'sub': 'iranian-cars'},
            
            # ========== خودروهای خارجی ==========
            {'tag': '#خودرو_خارجی', 'post_count': 62500, 'sub': 'foreign-cars'},
            {'tag': '#ماشین_خارجی', 'post_count': 142000, 'sub': 'foreign-cars'},
            {'tag': '#سوپراسپرت', 'post_count': 34000, 'sub': 'foreign-cars'},
            {'tag': '#سوپرخودرو', 'post_count': 100, 'sub': 'foreign-cars'},
            {'tag': '#خودرو_وارداتی', 'post_count': 238000, 'sub': 'foreign-cars'},
            
            # ========== خودروهای لوکس ==========
            {'tag': '#خودرو_لوکس', 'post_count': 377000, 'sub': 'luxury-cars'},
            {'tag': '#ماشین_لوکس', 'post_count': 738000, 'sub': 'luxury-cars'},
            {'tag': '#لاکچری', 'post_count': 52000, 'sub': 'luxury-cars'},
            {'tag': '#لوکس', 'post_count': 4100000, 'sub': 'luxury-cars'},
            {'tag': '#ابرخودرو', 'post_count': 1000, 'sub': 'luxury-cars'},
            
            # ========== تیونینگ و اسپرت ==========
            {'tag': '#تیونینگ', 'post_count': 696000, 'sub': 'tuning-sport'},
            {'tag': '#ماشین_اسپرت', 'post_count': 632000, 'sub': 'tuning-sport'},
            {'tag': '#اسپرت', 'post_count': 7100000, 'sub': 'tuning-sport'},
            {'tag': '#ریمپ', 'post_count': 172000, 'sub': 'tuning-sport'},
            {'tag': '#تقویت_موتور', 'post_count': 26100, 'sub': 'tuning-sport'},
            {'tag': '#اگزوز', 'post_count': 161000, 'sub': 'tuning-sport'},
            {'tag': '#رینگ_اسپرت', 'post_count': 284000, 'sub': 'tuning-sport'},
            {'tag': '#بدنه_اسپرت', 'post_count': 100, 'sub': 'tuning-sport'},
            
            # ========== موتور و مسابقات ==========
            {'tag': '#موتور', 'post_count': 3100000, 'sub': 'motorcycle-racing'},
            {'tag': '#موتورسیکلت', 'post_count': 581000, 'sub': 'motorcycle-racing'},
            {'tag': '#موتورسواری', 'post_count': 822000, 'sub': 'motorcycle-racing'},
            {'tag': '#مسابقات', 'post_count': 2500000, 'sub': 'motorcycle-racing'},
            {'tag': '#مسابقات_اتومبیلرانی', 'post_count': 1000, 'sub': 'motorcycle-racing'},
            {'tag': '#دریفت', 'post_count': 457000, 'sub': 'motorcycle-racing'},
            {'tag': '#شتاب', 'post_count': 153000, 'sub': 'motorcycle-racing'},
            {'tag': '#رالی', 'post_count': 80200, 'sub': 'motorcycle-racing'},
            {'tag': '#پیست', 'post_count': 199000, 'sub': 'motorcycle-racing'},
            
            # ========== آفرود ==========
            {'tag': '#آفرود', 'post_count': 658000, 'sub': 'offroad'},
            {'tag': '#بیراهه_نوردی', 'post_count': 31900, 'sub': 'offroad'},
            {'tag': '#سافاری', 'post_count': 151000, 'sub': 'offroad'},
            {'tag': '#کمپینگ', 'post_count': 932000, 'sub': 'offroad'},
            {'tag': '#طبیعتگردی', 'post_count': 5200000, 'sub': 'offroad'},
            
            # ========== تعمیر و نگهداری ==========
            {'tag': '#تعمیر_خودرو', 'post_count': 42700, 'sub': 'repair-maintenance'},
            {'tag': '#مکانیکی', 'post_count': 428000, 'sub': 'repair-maintenance'},
            {'tag': '#جلوبندی', 'post_count': 212000, 'sub': 'repair-maintenance'},
            {'tag': '#تعمیرگاه', 'post_count': 438000, 'sub': 'repair-maintenance'},
            {'tag': '#سرویس_دوره_ای', 'post_count': 17200, 'sub': 'repair-maintenance'},
            {'tag': '#تعویض_روغن', 'post_count': 131000, 'sub': 'repair-maintenance'},
            {'tag': '#لوازم_یدکی', 'post_count': 751000, 'sub': 'repair-maintenance'},
            
            # ========== خرید و فروش ==========
            {'tag': '#خرید_خودرو', 'post_count': 230000, 'sub': 'buy-sell'},
            {'tag': '#فروش_خودرو', 'post_count': 333000, 'sub': 'buy-sell'},
            {'tag': '#خرید_ماشین', 'post_count': 104000, 'sub': 'buy-sell'},
            {'tag': '#فروش_ماشین', 'post_count': 112000, 'sub': 'buy-sell'},
            {'tag': '#قیمت_خودرو', 'post_count': 595000, 'sub': 'buy-sell'},
            {'tag': '#کارکرده', 'post_count': 150000, 'sub': 'buy-sell'},
            {'tag': '#خودرو_دست_دوم', 'post_count': 14000, 'sub': 'buy-sell'},
            
            # ========== خودروهای کلاسیک ==========
            {'tag': '#خودرو_کلاسیک', 'post_count': 105000, 'sub': 'classic-cars'},
            {'tag': '#ماشین_کلاسیک', 'post_count': 187000, 'sub': 'classic-cars'},
            {'tag': '#کلاسیک', 'post_count': 3000000, 'sub': 'classic-cars'},
            {'tag': '#نوستالژی', 'post_count': 3800000, 'sub': 'classic-cars'},
            {'tag': '#ماشین_قدیمی', 'post_count': 39200, 'sub': 'classic-cars'},
        ]
        
        c, u = self.seed_hashtags(cars_cat, cars_subs, cars_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 خودرو: {c} جدید, {u} بروزرسانی')






                # ==========================================
        # ۴. تکنولوژی
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: تکنولوژی')
        
        tech_cat, tech_subs = self.create_category_with_subs({
            'name_fa': 'تکنولوژی',
            'name_en': 'Technology',
            'slug': 'technology',
            'subcategories': {
                'general-tech': {'fa': 'عمومی تکنولوژی', 'en': 'General Tech'},
                'mobile': {'fa': 'موبایل', 'en': 'Mobile'},
                'iphone': {'fa': 'آیفون', 'en': 'iPhone'},
                'android': {'fa': 'اندروید', 'en': 'Android'},
                'samsung': {'fa': 'سامسونگ', 'en': 'Samsung'},
                'laptop-pc': {'fa': 'لپتاپ و کامپیوتر', 'en': 'Laptop & PC'},
                'gadget': {'fa': 'گجت', 'en': 'Gadget'},
                'internet-security': {'fa': 'اینترنت و امنیت', 'en': 'Internet & Security'},
                'ai': {'fa': 'هوش مصنوعی', 'en': 'Artificial Intelligence'},
                'programming': {'fa': 'برنامه‌نویسی و وب', 'en': 'Programming & Web'},
                'application': {'fa': 'اپلیکیشن', 'en': 'Application'},
                'gaming': {'fa': 'بازی', 'en': 'Gaming'},
                'robotics': {'fa': 'رباتیک', 'en': 'Robotics'},
                'blockchain': {'fa': 'بلاکچین', 'en': 'Blockchain'},
            }
        })

        tech_hashtags = [
            # ========== عمومی تکنولوژی ==========
            {'tag': '#تکنولوژی', 'post_count': 1300000, 'sub': 'general-tech'},
            {'tag': '#فناوری', 'post_count': 557000, 'sub': 'general-tech'},
            {'tag': '#دنیای_تکنولوژی', 'post_count': 1000, 'sub': 'general-tech'},
            {'tag': '#اخبار_تکنولوژی', 'post_count': 36600, 'sub': 'general-tech'},
            {'tag': '#دیجیتال', 'post_count': 439000, 'sub': 'general-tech'},
            {'tag': '#نوآوری', 'post_count': 406000, 'sub': 'general-tech'},
            {'tag': '#تکنولوژی_روز', 'post_count': 134000, 'sub': 'general-tech'},
            
            # ========== موبایل ==========
            {'tag': '#موبایل', 'post_count': 2900000, 'sub': 'mobile'},
            {'tag': '#گوشی', 'post_count': 1400000, 'sub': 'mobile'},
            {'tag': '#گوشی_هوشمند', 'post_count': 126000, 'sub': 'mobile'},
            {'tag': '#بررسی_موبایل', 'post_count': 5000, 'sub': 'mobile'},
            {'tag': '#خرید_موبایل', 'post_count': 35600, 'sub': 'mobile'},
            {'tag': '#لوازم_جانبی_موبایل', 'post_count': 612000, 'sub': 'mobile'},
            
            # ========== آیفون ==========
            {'tag': '#آیفون', 'post_count': 773000, 'sub': 'iphone'},
            {'tag': '#اپل', 'post_count': 1400000, 'sub': 'iphone'},
            {'tag': '#آیفون_باز', 'post_count': 1000, 'sub': 'iphone'},
            {'tag': '#اپل_ایران', 'post_count': 1000, 'sub': 'iphone'},
            {'tag': '#آیفون_جدید', 'post_count': 5000, 'sub': 'iphone'},
            
            # ========== اندروید ==========
            {'tag': '#اندروید', 'post_count': 410000, 'sub': 'android'},
            {'tag': '#اندروید_باز', 'post_count': 100, 'sub': 'android'},
            {'tag': '#اندروید_جدید', 'post_count': 100, 'sub': 'android'},
            {'tag': '#اپلیکیشن_اندروید', 'post_count': 21800, 'sub': 'android'},
            
            # ========== سامسونگ ==========
            {'tag': '#سامسونگ', 'post_count': 2000000, 'sub': 'samsung'},
            {'tag': '#گوشی_سامسونگ', 'post_count': 223000, 'sub': 'samsung'},
            {'tag': '#سامسونگ_ایران', 'post_count': 1000, 'sub': 'samsung'},
            {'tag': '#گلکسی', 'post_count': 169000, 'sub': 'samsung'},
            
            # ========== لپتاپ و کامپیوتر ==========
            {'tag': '#لپتاپ', 'post_count': 467000, 'sub': 'laptop-pc'},
            {'tag': '#کامپیوتر', 'post_count': 765000, 'sub': 'laptop-pc'},
            {'tag': '#رایانه', 'post_count': 88300, 'sub': 'laptop-pc'},
            {'tag': '#سخت_افزار', 'post_count': 166000, 'sub': 'laptop-pc'},
            {'tag': '#قطعات_کامپیوتر', 'post_count': 19300, 'sub': 'laptop-pc'},
            {'tag': '#اسمبل_سیستم', 'post_count': 1000, 'sub': 'laptop-pc'},
            
            # ========== گجت ==========
            {'tag': '#گجت', 'post_count': 294000, 'sub': 'gadget'},
            {'tag': '#گجت_هوشمند', 'post_count': 72200, 'sub': 'gadget'},
            {'tag': '#ساعت_هوشمند', 'post_count': 361000, 'sub': 'gadget'},
            {'tag': '#لوازم_هوشمند', 'post_count': 1000, 'sub': 'gadget'},
            
            # ========== اینترنت و امنیت ==========
            {'tag': '#اینترنت', 'post_count': 747000, 'sub': 'internet-security'},
            {'tag': '#امنیت', 'post_count': 934000, 'sub': 'internet-security'},
            {'tag': '#امنیت_سایبری', 'post_count': 39700, 'sub': 'internet-security'},
            {'tag': '#شبکه', 'post_count': 436000, 'sub': 'internet-security'},
            {'tag': '#وایفای', 'post_count': 15100, 'sub': 'internet-security'},
            {'tag': '#حریم_خصوصی', 'post_count': 41100, 'sub': 'internet-security'},
            
            # ========== هوش مصنوعی ==========
            {'tag': '#هوش_مصنوعی', 'post_count': 1100000, 'sub': 'ai'},
            {'tag': '#یادگیری_ماشین', 'post_count': 30500, 'sub': 'ai'},
            {'tag': '#یادگیری_عمیق', 'post_count': 24900, 'sub': 'ai'},
            {'tag': '#پردازش_زبان_طبیعی', 'post_count': 1000, 'sub': 'ai'},
            {'tag': '#بینایی_ماشین', 'post_count': 5000, 'sub': 'ai'},
            
            # ========== برنامه‌نویسی و وب ==========
            {'tag': '#برنامه_نویسی', 'post_count': 502000, 'sub': 'programming'},
            {'tag': '#کدنویسی', 'post_count': 110000, 'sub': 'programming'},
            {'tag': '#توسعه_وب', 'post_count': 13400, 'sub': 'programming'},
            {'tag': '#طراحی_وب', 'post_count': 177000, 'sub': 'programming'},
            {'tag': '#فرانت_اند', 'post_count': 44400, 'sub': 'programming'},
            {'tag': '#بک_اند', 'post_count': 23100, 'sub': 'programming'},
            {'tag': '#جاوااسکریپت', 'post_count': 49800, 'sub': 'programming'},
            {'tag': '#پایتون', 'post_count': 136000, 'sub': 'programming'},
            {'tag': '#پی_اچ_پی', 'post_count': 14700, 'sub': 'programming'},
            {'tag': '#ریکت', 'post_count': 5000, 'sub': 'programming'},
            
            # ========== اپلیکیشن ==========
            {'tag': '#اپلیکیشن', 'post_count': 384000, 'sub': 'application'},
            {'tag': '#اپلیکیشن_موبایل', 'post_count': 52300, 'sub': 'application'},
            {'tag': '#توسعه_اپلیکیشن', 'post_count': 500, 'sub': 'application'},
            {'tag': '#نرم_افزار', 'post_count': 363000, 'sub': 'application'},
            
            # ========== بازی ==========
            {'tag': '#بازی', 'post_count': 4000000, 'sub': 'gaming'},
            {'tag': '#بازی_کامپیوتری', 'post_count': 83100, 'sub': 'gaming'},
            {'tag': '#بازی_موبایل', 'post_count': 66800, 'sub': 'gaming'},
            {'tag': '#گیمر', 'post_count': 902000, 'sub': 'gaming'},
            {'tag': '#گیمینگ', 'post_count': 665000, 'sub': 'gaming'},
            
            # ========== رباتیک ==========
            {'tag': '#رباتیک', 'post_count': 206000, 'sub': 'robotics'},
            {'tag': '#ربات', 'post_count': 300000, 'sub': 'robotics'},
            {'tag': '#اتوماسیون', 'post_count': 95600, 'sub': 'robotics'},
            {'tag': '#ربات_هوشمند', 'post_count': 19200, 'sub': 'robotics'},
            
            # ========== بلاکچین ==========
            {'tag': '#بلاکچین', 'post_count': 296000, 'sub': 'blockchain'},
            {'tag': '#رمزارز', 'post_count': 517000, 'sub': 'blockchain'},
            {'tag': '#ارز_دیجیتال', 'post_count': 639000, 'sub': 'blockchain'},
            {'tag': '#قرارداد_هوشمند', 'post_count': 5000, 'sub': 'blockchain'},
            {'tag': '#وب۳', 'post_count': 5000, 'sub': 'blockchain'},
        ]
        
        c, u = self.seed_hashtags(tech_cat, tech_subs, tech_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 تکنولوژی: {c} جدید, {u} بروزرسانی')








                # ==========================================
        # ۵. کسب‌وکار و مالی
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: کسب‌وکار و مالی')
        
        business_cat, business_subs = self.create_category_with_subs({
            'name_fa': 'کسب‌وکار و مالی',
            'name_en': 'Business & Finance',
            'slug': 'business',
            'subcategories': {
                'business-entrepreneurship': {'fa': 'کسب‌وکار و کارآفرینی', 'en': 'Business & Entrepreneurship'},
                'marketing-sales': {'fa': 'بازاریابی، فروش و برندینگ', 'en': 'Marketing, Sales & Branding'},
                'seo-content': {'fa': 'سئو و تولید محتوا', 'en': 'SEO & Content Creation'},
                'instagram-social': {'fa': 'اینستاگرام و شبکه‌های اجتماعی', 'en': 'Instagram & Social Media'},
                'telegram-messaging': {'fa': 'تلگرام و شبکه‌های پیام‌رسان', 'en': 'Telegram & Messaging'},
                'freelancing': {'fa': 'فریلنسری و کار آنلاین', 'en': 'Freelancing & Online Work'},
                'investment-crypto': {'fa': 'سرمایه‌گذاری، بورس و ارز دیجیتال', 'en': 'Investment, Stock & Crypto'},
            }
        })

        business_hashtags = [
            # ========== کسب‌وکار و کارآفرینی ==========
            {'tag': '#کسب_و_کار', 'post_count': 1900000, 'sub': 'business-entrepreneurship'},
            {'tag': '#کارآفرینی', 'post_count': 1300000, 'sub': 'business-entrepreneurship'},
            {'tag': '#استارتاپ', 'post_count': 433000, 'sub': 'business-entrepreneurship'},
            {'tag': '#استارتاپ_موفق', 'post_count': 13900, 'sub': 'business-entrepreneurship'},
            {'tag': '#تجارت', 'post_count': 698000, 'sub': 'business-entrepreneurship'},
            {'tag': '#کسب_درآمد', 'post_count': 1000000, 'sub': 'business-entrepreneurship'},
            {'tag': '#کسب_و_کار_آنلاین', 'post_count': 154000, 'sub': 'business-entrepreneurship'},
            {'tag': '#موفقیت_شغلی', 'post_count': 680000, 'sub': 'business-entrepreneurship'},
            {'tag': '#مدیریت_کسب_و_کار', 'post_count': 208000, 'sub': 'business-entrepreneurship'},
            {'tag': '#ایده_کسب_و_کار', 'post_count': 17000, 'sub': 'business-entrepreneurship'},
            
            # ========== بازاریابی، فروش و برندینگ ==========
            {'tag': '#بازاریابی', 'post_count': 1000000, 'sub': 'marketing-sales'},
            {'tag': '#بازاریابی_دیجیتال', 'post_count': 121000, 'sub': 'marketing-sales'},
            {'tag': '#دیجیتال_مارکتینگ', 'post_count': 901000, 'sub': 'marketing-sales'},
            {'tag': '#فروش', 'post_count': 5100000, 'sub': 'marketing-sales'},
            {'tag': '#افزایش_فروش', 'post_count': 123000, 'sub': 'marketing-sales'},
            {'tag': '#برندسازی', 'post_count': 297000, 'sub': 'marketing-sales'},
            {'tag': '#برندینگ', 'post_count': 777000, 'sub': 'marketing-sales'},
            {'tag': '#استراتژی_بازاریابی', 'post_count': 20000, 'sub': 'marketing-sales'},
            {'tag': '#تبلیغات', 'post_count': 4100000, 'sub': 'marketing-sales'},
            {'tag': '#تبلیغات_اینستاگرام', 'post_count': 619000, 'sub': 'marketing-sales'},
            
            # ========== سئو و تولید محتوا ==========
            {'tag': '#سئو', 'post_count': 314000, 'sub': 'seo-content'},
            {'tag': '#بهینه_سازی_سئو', 'post_count': 1000, 'sub': 'seo-content'},
            {'tag': '#سئو_سایت', 'post_count': 85600, 'sub': 'seo-content'},
            {'tag': '#تولید_محتوا', 'post_count': 1400000, 'sub': 'seo-content'},
            {'tag': '#محتوای_دیجیتال', 'post_count': 19100, 'sub': 'seo-content'},
            {'tag': '#استراتژی_محتوا', 'post_count': 29100, 'sub': 'seo-content'},
            {'tag': '#کپی_رایتینگ', 'post_count': 12800, 'sub': 'seo-content'},
            {'tag': '#محتوا_مارکتینگ', 'post_count': 500, 'sub': 'seo-content'},
            
            # ========== اینستاگرام و شبکه‌های اجتماعی ==========
            {'tag': '#اینستاگرام', 'post_count': 163000, 'sub': 'instagram-social'},
            {'tag': '#اینستاگرام_مارکتینگ', 'post_count': 696000, 'sub': 'instagram-social'},
            {'tag': '#رشد_اینستاگرام', 'post_count': 12500, 'sub': 'instagram-social'},
            {'tag': '#افزایش_فالوور', 'post_count': 179000, 'sub': 'instagram-social'},
            {'tag': '#الگوریتم_اینستاگرام', 'post_count': 149000, 'sub': 'instagram-social'},
            {'tag': '#ریلز', 'post_count': 6600000, 'sub': 'instagram-social'},
            {'tag': '#پست_اینستاگرام', 'post_count': 53500, 'sub': 'instagram-social'},
            {'tag': '#ادمین_اینستاگرام', 'post_count': 697000, 'sub': 'instagram-social'},
            {'tag': '#رشد_پیج', 'post_count': 141000, 'sub': 'instagram-social'},
            {'tag': '#بازاریابی_اینستاگرام', 'post_count': 63300, 'sub': 'instagram-social'},
            
            # ========== تلگرام و شبکه‌های پیام‌رسان ==========
            {'tag': '#تلگرام', 'post_count': 1000000, 'sub': 'telegram-messaging'},
            {'tag': '#کانال_تلگرام', 'post_count': 116000, 'sub': 'telegram-messaging'},
            {'tag': '#مدیریت_کانال', 'post_count': 100, 'sub': 'telegram-messaging'},
            {'tag': '#بازاریابی_تلگرامی', 'post_count': 100, 'sub': 'telegram-messaging'},
            {'tag': '#رشد_کانال', 'post_count': 100, 'sub': 'telegram-messaging'},
            {'tag': '#فروش_تلگرامی', 'post_count': 100, 'sub': 'telegram-messaging'},
            
            # ========== فریلنسری و کار آنلاین ==========
            {'tag': '#فریلنسری', 'post_count': 52600, 'sub': 'freelancing'},
            {'tag': '#فریلنسر', 'post_count': 106000, 'sub': 'freelancing'},
            {'tag': '#کار_در_خانه', 'post_count': 78100, 'sub': 'freelancing'},
            {'tag': '#درآمد_دلاری', 'post_count': 747000, 'sub': 'freelancing'},
            {'tag': '#کار_آنلاین', 'post_count': 71200, 'sub': 'freelancing'},
            {'tag': '#دورکاری', 'post_count': 92000, 'sub': 'freelancing'},
            {'tag': '#درآمد_آنلاین', 'post_count': 18600, 'sub': 'freelancing'},
            {'tag': '#شغل_آزاد', 'post_count': 5000, 'sub': 'freelancing'},
            
            # ========== سرمایه‌گذاری، بورس و ارز دیجیتال ==========
            {'tag': '#سرمایه_گذاری', 'post_count': 2200000, 'sub': 'investment-crypto'},
            {'tag': '#بورس', 'post_count': 2700000, 'sub': 'investment-crypto'},
            {'tag': '#بازار_بورس', 'post_count': 118000, 'sub': 'investment-crypto'},
            {'tag': '#ارز_دیجیتال', 'post_count': 639000, 'sub': 'investment-crypto'},
            {'tag': '#کریپتو', 'post_count': 736000, 'sub': 'investment-crypto'},
            {'tag': '#بیت_کوین', 'post_count': 764000, 'sub': 'investment-crypto'},
            {'tag': '#ترید', 'post_count': 1000000, 'sub': 'investment-crypto'},
            {'tag': '#معامله_گری', 'post_count': 87800, 'sub': 'investment-crypto'},
            {'tag': '#درآمد_غیرفعال', 'post_count': 5000, 'sub': 'investment-crypto'},
            {'tag': '#ثروت', 'post_count': 2600000, 'sub': 'investment-crypto'},
        ]
        
        c, u = self.seed_hashtags(business_cat, business_subs, business_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 کسب‌وکار و مالی: {c} جدید, {u} بروزرسانی')







                # ==========================================
        # ۶. مد و فشن
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: مد و فشن')
        
        fashion_cat, fashion_subs = self.create_category_with_subs({
            'name_fa': 'مد و فشن',
            'name_en': 'Fashion',
            'slug': 'fashion',
            'subcategories': {
                'general-fashion': {'fa': 'مد و فشن (عمومی)', 'en': 'General Fashion'},
                'women-fashion': {'fa': 'لباس زنانه و استایل زنانه', 'en': 'Women Fashion'},
                'men-fashion': {'fa': 'لباس مردانه و استایل مردانه', 'en': 'Men Fashion'},
                'kids-fashion': {'fa': 'لباس بچگانه', 'en': 'Kids Fashion'},
                'shoes-bags': {'fa': 'کفش و کیف', 'en': 'Shoes & Bags'},
                'watch-accessories': {'fa': 'ساعت و اکسسوری', 'en': 'Watches & Accessories'},
                'manto-hijab': {'fa': 'مانتو، روسری و حجاب استایل', 'en': 'Manto & Hijab Style'},
                'sport-formal': {'fa': 'لباس اسپرت و مجلسی', 'en': 'Sport & Formal Wear'},
            }
        })

        fashion_hashtags = [
            # ========== مد و فشن (عمومی) ==========
            {'tag': '#مد', 'post_count': 4800000, 'sub': 'general-fashion'},
            {'tag': '#فشن', 'post_count': 1400000, 'sub': 'general-fashion'},
            {'tag': '#استایل', 'post_count': 1700000, 'sub': 'general-fashion'},
            {'tag': '#استایل_شخصی', 'post_count': 28200, 'sub': 'general-fashion'},
            {'tag': '#مد_و_پوشاک', 'post_count': 14400, 'sub': 'general-fashion'},
            {'tag': '#استایل_خاص', 'post_count': 1900000, 'sub': 'general-fashion'},
            {'tag': '#ترند_مد', 'post_count': 5000, 'sub': 'general-fashion'},
            {'tag': '#مد_روز', 'post_count': 1100000, 'sub': 'general-fashion'},
            {'tag': '#زیبایی', 'post_count': 1200000, 'sub': 'general-fashion'},
            {'tag': '#شیک_پوشی', 'post_count': 139000, 'sub': 'general-fashion'},
            
            # ========== لباس زنانه و استایل زنانه ==========
            {'tag': '#لباس_زنانه', 'post_count': 3900000, 'sub': 'women-fashion'},
            {'tag': '#مد_زنانه', 'post_count': 204000, 'sub': 'women-fashion'},
            {'tag': '#استایل_زنانه', 'post_count': 519000, 'sub': 'women-fashion'},
            {'tag': '#شیک_پوشی_زنانه', 'post_count': 100, 'sub': 'women-fashion'},
            {'tag': '#مد_ایرانی', 'post_count': 79600, 'sub': 'women-fashion'},
            {'tag': '#استایل_خاص_زنانه', 'post_count': 1000, 'sub': 'women-fashion'},
            {'tag': '#لباس_شیک', 'post_count': 2600000, 'sub': 'women-fashion'},
            {'tag': '#لباس_مجلسی_زنانه', 'post_count': 387000, 'sub': 'women-fashion'},
            {'tag': '#استایل_روزمره', 'post_count': 188000, 'sub': 'women-fashion'},
            {'tag': '#مد_مدرن', 'post_count': 1000, 'sub': 'women-fashion'},
            
            # ========== لباس مردانه و استایل مردانه ==========
            {'tag': '#لباس_مردانه', 'post_count': 1000000, 'sub': 'men-fashion'},
            {'tag': '#مد_مردانه', 'post_count': 72700, 'sub': 'men-fashion'},
            {'tag': '#استایل_مردانه', 'post_count': 386000, 'sub': 'men-fashion'},
            {'tag': '#استایل_خاص_مردانه', 'post_count': 1000, 'sub': 'men-fashion'},
            {'tag': '#شیک_پوشی_مردانه', 'post_count': 100, 'sub': 'men-fashion'},
            {'tag': '#لباس_اسپرت_مردانه', 'post_count': 5000, 'sub': 'men-fashion'},
            {'tag': '#مد_روزمره', 'post_count': 1000, 'sub': 'men-fashion'},
            {'tag': '#استایل_کلاسیک', 'post_count': 104000, 'sub': 'men-fashion'},
            {'tag': '#تیپ_مردانه', 'post_count': 73000, 'sub': 'men-fashion'},
            {'tag': '#فشن_مردانه', 'post_count': 32800, 'sub': 'men-fashion'},
            
            # ========== لباس بچگانه ==========
            {'tag': '#لباس_بچگانه', 'post_count': 2600000, 'sub': 'kids-fashion'},
            {'tag': '#مد_بچگانه', 'post_count': 17800, 'sub': 'kids-fashion'},
            {'tag': '#استایل_بچگانه', 'post_count': 66500, 'sub': 'kids-fashion'},
            {'tag': '#لباس_کودک', 'post_count': 2800000, 'sub': 'kids-fashion'},
            {'tag': '#فشن_کودک', 'post_count': 22500, 'sub': 'kids-fashion'},
            {'tag': '#لباس_نوزاد', 'post_count': 445000, 'sub': 'kids-fashion'},
            {'tag': '#لباس_شیک_بچگانه', 'post_count': 108000, 'sub': 'kids-fashion'},
            {'tag': '#کودک_استایل', 'post_count': 5000, 'sub': 'kids-fashion'},
            {'tag': '#مد_کودکان', 'post_count': 1000, 'sub': 'kids-fashion'},
            
            # ========== کفش و کیف ==========
            {'tag': '#کفش', 'post_count': 1600000, 'sub': 'shoes-bags'},
            {'tag': '#کفش_زنانه', 'post_count': 2200000, 'sub': 'shoes-bags'},
            {'tag': '#کفش_مردانه', 'post_count': 959000, 'sub': 'shoes-bags'},
            {'tag': '#کفش_اسپرت', 'post_count': 3300000, 'sub': 'shoes-bags'},
            {'tag': '#کیف', 'post_count': 1400000, 'sub': 'shoes-bags'},
            {'tag': '#کیف_زنانه', 'post_count': 4000000, 'sub': 'shoes-bags'},
            {'tag': '#کیف_دستی', 'post_count': 1000000, 'sub': 'shoes-bags'},
            {'tag': '#کیف_شیک', 'post_count': 1300000, 'sub': 'shoes-bags'},
            {'tag': '#استایل_کیف_و_کفش', 'post_count': 100, 'sub': 'shoes-bags'},
            {'tag': '#مد_اکسسوری', 'post_count': 500, 'sub': 'shoes-bags'},
            
            # ========== ساعت و اکسسوری ==========
            {'tag': '#ساعت', 'post_count': 4900000, 'sub': 'watch-accessories'},
            {'tag': '#ساعت_مچی', 'post_count': 1200000, 'sub': 'watch-accessories'},
            {'tag': '#اکسسوری', 'post_count': 2800000, 'sub': 'watch-accessories'},
            {'tag': '#اکسسوری_زنانه', 'post_count': 810000, 'sub': 'watch-accessories'},
            {'tag': '#اکسسوری_مردانه', 'post_count': 125000, 'sub': 'watch-accessories'},
            {'tag': '#زیورآلات', 'post_count': 1100000, 'sub': 'watch-accessories'},
            {'tag': '#جواهرات', 'post_count': 1800000, 'sub': 'watch-accessories'},
            {'tag': '#استایل_اکسسوری', 'post_count': 1000, 'sub': 'watch-accessories'},
            
            # ========== مانتو، روسری و حجاب استایل ==========
            {'tag': '#مانتو', 'post_count': 1700000, 'sub': 'manto-hijab'},
            {'tag': '#مانتو_شیک', 'post_count': 3800000, 'sub': 'manto-hijab'},
            {'tag': '#مد_مانتو', 'post_count': 5000, 'sub': 'manto-hijab'},
            {'tag': '#روسری', 'post_count': 1700000, 'sub': 'manto-hijab'},
            {'tag': '#شال', 'post_count': 1800000, 'sub': 'manto-hijab'},
            {'tag': '#حجاب_استایل', 'post_count': 796000, 'sub': 'manto-hijab'},
            {'tag': '#استایل_محجبه', 'post_count': 5000, 'sub': 'manto-hijab'},
            {'tag': '#لباس_ایرانی', 'post_count': 67300, 'sub': 'manto-hijab'},
            {'tag': '#مد_محجبه', 'post_count': 1000, 'sub': 'manto-hijab'},
            
            # ========== لباس اسپرت و مجلسی ==========
            {'tag': '#لباس_اسپرت', 'post_count': 617000, 'sub': 'sport-formal'},
            {'tag': '#استایل_اسپرت', 'post_count': 151000, 'sub': 'sport-formal'},
            {'tag': '#لباس_راحتی', 'post_count': 1300000, 'sub': 'sport-formal'},
            {'tag': '#لباس_مجلسی', 'post_count': 6400000, 'sub': 'sport-formal'},
            {'tag': '#لباس_مجلسی_شیک', 'post_count': 268000, 'sub': 'sport-formal'},
            {'tag': '#استایل_مجلسی', 'post_count': 86400, 'sub': 'sport-formal'},
            {'tag': '#مد_مجلسی', 'post_count': 1000, 'sub': 'sport-formal'},
            {'tag': '#تیپ_اسپرت', 'post_count': 206000, 'sub': 'sport-formal'},
            {'tag': '#فشن_اسپرت', 'post_count': 1000, 'sub': 'sport-formal'},
        ]
        
        c, u = self.seed_hashtags(fashion_cat, fashion_subs, fashion_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 مد و فشن: {c} جدید, {u} بروزرسانی')







                # ==========================================
        # ۷. آرایش و زیبایی
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: آرایش و زیبایی')
        
        beauty_cat, beauty_subs = self.create_category_with_subs({
            'name_fa': 'آرایش و زیبایی',
            'name_en': 'Beauty',
            'slug': 'beauty',
            'subcategories': {
                'general-beauty': {'fa': 'زیبایی (عمومی)', 'en': 'General Beauty'},
                'makeup': {'fa': 'آرایش و میکاپ', 'en': 'Makeup'},
                'skincare': {'fa': 'مراقبت پوست', 'en': 'Skincare'},
                'haircare': {'fa': 'مراقبت و زیبایی مو', 'en': 'Hair Care'},
                'haircolor': {'fa': 'رنگ مو و کراتین', 'en': 'Hair Color & Keratin'},
                'nails': {'fa': 'ناخن و طراحی ناخن', 'en': 'Nails & Nail Art'},
                'eyelash-eyebrow': {'fa': 'مژه و ابرو', 'en': 'Eyelash & Eyebrow'},
                'perfume': {'fa': 'عطر و رایحه', 'en': 'Perfume & Fragrance'},
                'facial-clinic': {'fa': 'فیشیال و کلینیک زیبایی', 'en': 'Facial & Beauty Clinic'},
            }
        })

        beauty_hashtags = [
            # ========== زیبایی (عمومی) ==========
            {'tag': '#زیبایی', 'post_count': 1200000, 'sub': 'general-beauty'},
            {'tag': '#زیبایی_زنانه', 'post_count': 43500, 'sub': 'general-beauty'},
            {'tag': '#زیبایی_طبیعی', 'post_count': 597000, 'sub': 'general-beauty'},
            {'tag': '#زیبایی_مدرن', 'post_count': 1000, 'sub': 'general-beauty'},
            {'tag': '#آراستگی', 'post_count': 18200, 'sub': 'general-beauty'},
            {'tag': '#زیبایی_و_سلامت', 'post_count': 1000, 'sub': 'general-beauty'},
            {'tag': '#استایل_زیبایی', 'post_count': 500, 'sub': 'general-beauty'},
            {'tag': '#خدمات_زیبایی', 'post_count': 312000, 'sub': 'general-beauty'},
            {'tag': '#زیبایی_روز', 'post_count': 500, 'sub': 'general-beauty'},
            {'tag': '#زیبایی_ایرانی', 'post_count': 5000, 'sub': 'general-beauty'},
            
            # ========== آرایش و میکاپ ==========
            {'tag': '#آرایش', 'post_count': 1500000, 'sub': 'makeup'},
            {'tag': '#میکاپ', 'post_count': 1400000, 'sub': 'makeup'},
            {'tag': '#میکاپ_آرتیست', 'post_count': 1700000, 'sub': 'makeup'},
            {'tag': '#آرایش_صورت', 'post_count': 634000, 'sub': 'makeup'},
            {'tag': '#آرایش_عروس', 'post_count': 508000, 'sub': 'makeup'},
            {'tag': '#میکاپ_عروس', 'post_count': 2100000, 'sub': 'makeup'},
            {'tag': '#آرایش_حرفه_ای', 'post_count': 18600, 'sub': 'makeup'},
            {'tag': '#میکاپ_خاص', 'post_count': 447000, 'sub': 'makeup'},
            {'tag': '#آرایش_روزانه', 'post_count': 70000, 'sub': 'makeup'},
            {'tag': '#میکاپ_ایرانی', 'post_count': 11400, 'sub': 'makeup'},
            
            # ========== مراقبت پوست ==========
            {'tag': '#مراقبت_پوست', 'post_count': 2600000, 'sub': 'skincare'},
            {'tag': '#پوست_سالم', 'post_count': 2400000, 'sub': 'skincare'},
            {'tag': '#زیبایی_پوست', 'post_count': 2600000, 'sub': 'skincare'},
            {'tag': '#اسکین_کر', 'post_count': 533000, 'sub': 'skincare'},
            {'tag': '#روتین_پوستی', 'post_count': 1300000, 'sub': 'skincare'},
            {'tag': '#آبرسانی_پوست', 'post_count': 1100000, 'sub': 'skincare'},
            {'tag': '#جوانسازی_پوست', 'post_count': 1600000, 'sub': 'skincare'},
            {'tag': '#پوست_شفاف', 'post_count': 871000, 'sub': 'skincare'},
            {'tag': '#درمان_پوست', 'post_count': 162000, 'sub': 'skincare'},
            {'tag': '#کلینیک_پوست', 'post_count': 298000, 'sub': 'skincare'},
            
            # ========== مراقبت و زیبایی مو ==========
            {'tag': '#مراقبت_مو', 'post_count': 903000, 'sub': 'haircare'},
            {'tag': '#مو_سالم', 'post_count': 151000, 'sub': 'haircare'},
            {'tag': '#زیبایی_مو', 'post_count': 1000000, 'sub': 'haircare'},
            {'tag': '#روتین_مو', 'post_count': 96200, 'sub': 'haircare'},
            {'tag': '#تقویت_مو', 'post_count': 629000, 'sub': 'haircare'},
            {'tag': '#موی_زیبا', 'post_count': 121000, 'sub': 'haircare'},
            {'tag': '#درمان_ریزش_مو', 'post_count': 527000, 'sub': 'haircare'},
            {'tag': '#مو_درخشان', 'post_count': 5000, 'sub': 'haircare'},
            
            # ========== رنگ مو و کراتین ==========
            {'tag': '#رنگ_مو', 'post_count': 2900000, 'sub': 'haircolor'},
            {'tag': '#رنگ_مو_جدید', 'post_count': 54400, 'sub': 'haircolor'},
            {'tag': '#هایلایت', 'post_count': 1100000, 'sub': 'haircolor'},
            {'tag': '#آمبره', 'post_count': 840000, 'sub': 'haircolor'},
            {'tag': '#بالیاژ', 'post_count': 1800000, 'sub': 'haircolor'},
            {'tag': '#کراتین', 'post_count': 3200000, 'sub': 'haircolor'},
            {'tag': '#کراتین_مو', 'post_count': 597000, 'sub': 'haircolor'},
            {'tag': '#صاف_کردن_مو', 'post_count': 18200, 'sub': 'haircolor'},
            {'tag': '#مو_ابریشمی', 'post_count': 15500, 'sub': 'haircolor'},
            {'tag': '#رنگ_مو_فانتزی', 'post_count': 216000, 'sub': 'haircolor'},
            
            # ========== ناخن و طراحی ناخن ==========
            {'tag': '#ناخن', 'post_count': 1400000, 'sub': 'nails'},
            {'tag': '#کاشت_ناخن', 'post_count': 745000, 'sub': 'nails'},
            {'tag': '#طراحی_ناخن', 'post_count': 4400000, 'sub': 'nails'},
            {'tag': '#ناخن_شیک', 'post_count': 3400000, 'sub': 'nails'},
            {'tag': '#ژلیش', 'post_count': 3200000, 'sub': 'nails'},
            {'tag': '#مانیکور', 'post_count': 3200000, 'sub': 'nails'},
            {'tag': '#پدیکور', 'post_count': 2100000, 'sub': 'nails'},
            {'tag': '#ناخن_کار', 'post_count': 425000, 'sub': 'nails'},
            {'tag': '#زیبایی_ناخن', 'post_count': 198000, 'sub': 'nails'},
            
            # ========== مژه و ابرو ==========
            {'tag': '#مژه', 'post_count': 3400000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#اکستنشن_مژه', 'post_count': 3200000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#لیفت_مژه', 'post_count': 1700000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#ابرو', 'post_count': 2500000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#فیبروز_ابرو', 'post_count': 562000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#میکروبلیدینگ', 'post_count': 3300000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#قرینه_سازی_ابرو', 'post_count': 168000, 'sub': 'eyelash-eyebrow'},
            {'tag': '#ابرو_زیبا', 'post_count': 23900, 'sub': 'eyelash-eyebrow'},
            {'tag': '#مژه_حجیم', 'post_count': 1000, 'sub': 'eyelash-eyebrow'},
            
            # ========== عطر و رایحه ==========
            {'tag': '#عطر', 'post_count': 551000, 'sub': 'perfume'},
            {'tag': '#عطر_زنانه', 'post_count': 602000, 'sub': 'perfume'},
            {'tag': '#عطر_مردانه', 'post_count': 362000, 'sub': 'perfume'},
            {'tag': '#ادکلن', 'post_count': 2100000, 'sub': 'perfume'},
            {'tag': '#رایحه_خاص', 'post_count': 47200, 'sub': 'perfume'},
            {'tag': '#عطر_لوکس', 'post_count': 32600, 'sub': 'perfume'},
            {'tag': '#عطر_شیک', 'post_count': 21300, 'sub': 'perfume'},
            {'tag': '#عطر_ایرانی', 'post_count': 1000, 'sub': 'perfume'},
            {'tag': '#بوی_خوب', 'post_count': 30100, 'sub': 'perfume'},
            
            # ========== فیشیال و کلینیک زیبایی ==========
            {'tag': '#فیشیال', 'post_count': 873000, 'sub': 'facial-clinic'},
            {'tag': '#فیشیال_پوست', 'post_count': 121000, 'sub': 'facial-clinic'},
            {'tag': '#کلینیک_زیبایی', 'post_count': 1200000, 'sub': 'facial-clinic'},
            {'tag': '#خدمات_پوستی', 'post_count': 16300, 'sub': 'facial-clinic'},
            {'tag': '#پاکسازی_پوست', 'post_count': 2200000, 'sub': 'facial-clinic'},
            {'tag': '#جوانسازی', 'post_count': 1600000, 'sub': 'facial-clinic'},
            {'tag': '#کلینیک_پوست', 'post_count': 298000, 'sub': 'facial-clinic'},
            {'tag': '#لیزر_پوست', 'post_count': 55700, 'sub': 'facial-clinic'},
            {'tag': '#زیبایی_کلینیکی', 'post_count': 100, 'sub': 'facial-clinic'},
            {'tag': '#درمان_پوست', 'post_count': 162000, 'sub': 'facial-clinic'},
        ]
        
        c, u = self.seed_hashtags(beauty_cat, beauty_subs, beauty_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 آرایش و زیبایی: {c} جدید, {u} بروزرسانی')







                # ==========================================
        # ۸. ورزش
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: ورزش')
        
        sports_cat, sports_subs = self.create_category_with_subs({
            'name_fa': 'ورزش',
            'name_en': 'Sports',
            'slug': 'sports',
            'subcategories': {
                'general-sports': {'fa': 'ورزش (عمومی)', 'en': 'General Sports'},
                'bodybuilding': {'fa': 'بدنسازی و فیتنس', 'en': 'Bodybuilding & Fitness'},
                'crossfit': {'fa': 'کراس فیت', 'en': 'CrossFit'},
                'yoga-pilates': {'fa': 'یوگا و پیلاتس', 'en': 'Yoga & Pilates'},
                'football': {'fa': 'فوتبال', 'en': 'Football'},
                'volleyball': {'fa': 'والیبال', 'en': 'Volleyball'},
                'basketball': {'fa': 'بسکتبال', 'en': 'Basketball'},
                'swimming': {'fa': 'شنا', 'en': 'Swimming'},
                'running-cycling': {'fa': 'دویدن و دوچرخه‌سواری', 'en': 'Running & Cycling'},
                'martial-arts': {'fa': 'ورزش‌های رزمی', 'en': 'Martial Arts'},
                'wrestling': {'fa': 'کشتی', 'en': 'Wrestling'},
                'boxing': {'fa': 'بوکس', 'en': 'Boxing'},
            }
        })

        sports_hashtags = [
            # ========== ورزش (عمومی) ==========
            {'tag': '#ورزش', 'post_count': 1100000, 'sub': 'general-sports'},
            {'tag': '#ورزشکار', 'post_count': 1100000, 'sub': 'general-sports'},
            {'tag': '#سلامتی', 'post_count': 1000, 'sub': 'general-sports'},
            {'tag': '#تناسب_اندام', 'post_count': 3100000, 'sub': 'general-sports'},
            {'tag': '#فعالیت_بدنی', 'post_count': 63000, 'sub': 'general-sports'},
            {'tag': '#سبک_زندگی_سالم', 'post_count': 398000, 'sub': 'general-sports'},
            {'tag': '#ورزش_روزانه', 'post_count': 29900, 'sub': 'general-sports'},
            {'tag': '#انگیزه_ورزشی', 'post_count': 10900, 'sub': 'general-sports'},
            {'tag': '#تمرین', 'post_count': 1300000, 'sub': 'general-sports'},
            {'tag': '#سلامت_بدن', 'post_count': 220000, 'sub': 'general-sports'},
            
            # ========== بدنسازی و فیتنس ==========
            {'tag': '#بدنسازی', 'post_count': 3900000, 'sub': 'bodybuilding'},
            {'tag': '#فیتنس', 'post_count': 3400000, 'sub': 'bodybuilding'},
            {'tag': '#بدن_سازی', 'post_count': 51400, 'sub': 'bodybuilding'},
            {'tag': '#عضله_سازی', 'post_count': 358000, 'sub': 'bodybuilding'},
            {'tag': '#تمرین_بدنسازی', 'post_count': 24100, 'sub': 'bodybuilding'},
            {'tag': '#باشگاه', 'post_count': 2900000, 'sub': 'bodybuilding'},
            {'tag': '#بدن_ایده_آل', 'post_count': 5000, 'sub': 'bodybuilding'},
            {'tag': '#تناسب_اندام', 'post_count': 3100000, 'sub': 'bodybuilding'},
            {'tag': '#فیتنس_بانوان', 'post_count': 804000, 'sub': 'bodybuilding'},
            {'tag': '#فیتنس_آقایان', 'post_count': 277000, 'sub': 'bodybuilding'},
            
            # ========== کراس فیت ==========
            {'tag': '#کراس_فیت', 'post_count': 73600, 'sub': 'crossfit'},
            {'tag': '#تمرین_کراس_فیت', 'post_count': 100, 'sub': 'crossfit'},
            {'tag': '#کراسفیت_ایران', 'post_count': 28000, 'sub': 'crossfit'},
            {'tag': '#تمرین_قدرتی', 'post_count': 16000, 'sub': 'crossfit'},
            {'tag': '#استقامت', 'post_count': 163000, 'sub': 'crossfit'},
            {'tag': '#ورزش_عملکردی', 'post_count': 100, 'sub': 'crossfit'},
            {'tag': '#آمادگی_جسمانی', 'post_count': 41000, 'sub': 'crossfit'},
            {'tag': '#تمرین_شدید', 'post_count': 500, 'sub': 'crossfit'},
            {'tag': '#فیتنس_حرفه_ای', 'post_count': 100, 'sub': 'crossfit'},
            
            # ========== یوگا و پیلاتس ==========
            {'tag': '#یوگا', 'post_count': 1100000, 'sub': 'yoga-pilates'},
            {'tag': '#پیلاتس', 'post_count': 301000, 'sub': 'yoga-pilates'},
            {'tag': '#تمرین_یوگا', 'post_count': 5000, 'sub': 'yoga-pilates'},
            {'tag': '#آرامش', 'post_count': 1200000, 'sub': 'yoga-pilates'},
            {'tag': '#مدیتیشن', 'post_count': 1200000, 'sub': 'yoga-pilates'},
            {'tag': '#انعطاف_بدن', 'post_count': 5000, 'sub': 'yoga-pilates'},
            {'tag': '#سلامت_ذهن', 'post_count': 273000, 'sub': 'yoga-pilates'},
            {'tag': '#ورزش_بانوان', 'post_count': 443000, 'sub': 'yoga-pilates'},
            {'tag': '#تمرین_خانگی', 'post_count': 5000, 'sub': 'yoga-pilates'},
            {'tag': '#یوگا_ایران', 'post_count': 5000, 'sub': 'yoga-pilates'},
            
            # ========== فوتبال ==========
            {'tag': '#فوتبال', 'post_count': 760000, 'sub': 'football'},
            {'tag': '#فوتبالی', 'post_count': 699000, 'sub': 'football'},
            {'tag': '#فوتبال_ایران', 'post_count': 760000, 'sub': 'football'},
            {'tag': '#لیگ_برتر', 'post_count': 1500000, 'sub': 'football'},
            {'tag': '#گل', 'post_count': 581000, 'sub': 'football'},
            {'tag': '#تمرین_فوتبال', 'post_count': 23600, 'sub': 'football'},
            {'tag': '#بازیکن_فوتبال', 'post_count': 36700, 'sub': 'football'},
            {'tag': '#هوادار_فوتبال', 'post_count': 1000, 'sub': 'football'},
            {'tag': '#عشق_فوتبال', 'post_count': 12900, 'sub': 'football'},
            
            # ========== والیبال ==========
            {'tag': '#والیبال', 'post_count': 859000, 'sub': 'volleyball'},
            {'tag': '#والیبال_ایران', 'post_count': 149000, 'sub': 'volleyball'},
            {'tag': '#بازیکن_والیبال', 'post_count': 1000, 'sub': 'volleyball'},
            {'tag': '#تمرین_والیبال', 'post_count': 1000, 'sub': 'volleyball'},
            {'tag': '#توپ_والیبال', 'post_count': 17200, 'sub': 'volleyball'},
            {'tag': '#ورزش_تیمی', 'post_count': 500, 'sub': 'volleyball'},
            {'tag': '#والیبالیست', 'post_count': 125000, 'sub': 'volleyball'},
            {'tag': '#مسابقه_والیبال', 'post_count': 1000, 'sub': 'volleyball'},
            
            # ========== بسکتبال ==========
            {'tag': '#بسکتبال', 'post_count': 529000, 'sub': 'basketball'},
            {'tag': '#بسکتبال_ایران', 'post_count': 53400, 'sub': 'basketball'},
            {'tag': '#بازیکن_بسکتبال', 'post_count': 1000, 'sub': 'basketball'},
            {'tag': '#تمرین_بسکتبال', 'post_count': 1000, 'sub': 'basketball'},
            {'tag': '#توپ_بسکتبال', 'post_count': 5000, 'sub': 'basketball'},
            {'tag': '#بسکتبالیست', 'post_count': 65400, 'sub': 'basketball'},
            {'tag': '#مسابقه_بسکتبال', 'post_count': 500, 'sub': 'basketball'},
            
            # ========== شنا ==========
            {'tag': '#شنا', 'post_count': 711000, 'sub': 'swimming'},
            {'tag': '#شناگر', 'post_count': 115000, 'sub': 'swimming'},
            {'tag': '#آموزش_شنا', 'post_count': 15700, 'sub': 'swimming'},
            {'tag': '#استخر', 'post_count': 1100000, 'sub': 'swimming'},
            {'tag': '#ورزش_آبی', 'post_count': 14500, 'sub': 'swimming'},
            {'tag': '#تمرین_شنا', 'post_count': 1000, 'sub': 'swimming'},
            {'tag': '#شنا_حرفه_ای', 'post_count': 1000, 'sub': 'swimming'},
            {'tag': '#سلامت_بدن', 'post_count': 220000, 'sub': 'swimming'},
            {'tag': '#ورزش_تابستانی', 'post_count': 500, 'sub': 'swimming'},
            
            # ========== دویدن و دوچرخه‌سواری ==========
            {'tag': '#دویدن', 'post_count': 143000, 'sub': 'running-cycling'},
            {'tag': '#دوندگی', 'post_count': 1000, 'sub': 'running-cycling'},
            {'tag': '#رانینگ', 'post_count': 395000, 'sub': 'running-cycling'},
            {'tag': '#دوچرخه_سواری', 'post_count': 556000, 'sub': 'running-cycling'},
            {'tag': '#دوچرخه', 'post_count': 742000, 'sub': 'running-cycling'},
            {'tag': '#تمرین_هوازی', 'post_count': 12800, 'sub': 'running-cycling'},
            {'tag': '#استقامت', 'post_count': 163000, 'sub': 'running-cycling'},
            {'tag': '#ورزش_صبحگاهی', 'post_count': 45600, 'sub': 'running-cycling'},
            {'tag': '#زندگی_سالم', 'post_count': 1500000, 'sub': 'running-cycling'},
            {'tag': '#کالری_سوزی', 'post_count': 108000, 'sub': 'running-cycling'},
            
            # ========== ورزش‌های رزمی ==========
            {'tag': '#ورزش_رزمی', 'post_count': 43600, 'sub': 'martial-arts'},
            {'tag': '#رزمی', 'post_count': 718000, 'sub': 'martial-arts'},
            {'tag': '#هنرهای_رزمی', 'post_count': 101000, 'sub': 'martial-arts'},
            {'tag': '#دفاع_شخصی', 'post_count': 269000, 'sub': 'martial-arts'},
            {'tag': '#تمرین_رزمی', 'post_count': 1000, 'sub': 'martial-arts'},
            {'tag': '#رزمی_کار', 'post_count': 35200, 'sub': 'martial-arts'},
            {'tag': '#قدرت', 'post_count': 1400000, 'sub': 'martial-arts'},
            {'tag': '#انضباط', 'post_count': 59700, 'sub': 'martial-arts'},
            {'tag': '#ورزشکار_رزمی', 'post_count': 100, 'sub': 'martial-arts'},
            
            # ========== کشتی ==========
            {'tag': '#کشتی', 'post_count': 1000000, 'sub': 'wrestling'},
            {'tag': '#کشتی_ایران', 'post_count': 37800, 'sub': 'wrestling'},
            {'tag': '#کشتی_گیر', 'post_count': 65600, 'sub': 'wrestling'},
            {'tag': '#تمرین_کشتی', 'post_count': 1000, 'sub': 'wrestling'},
            {'tag': '#قهرمان_کشتی', 'post_count': 1000, 'sub': 'wrestling'},
            {'tag': '#ورزش_ملی', 'post_count': 1000, 'sub': 'wrestling'},
            {'tag': '#مسابقات_کشتی', 'post_count': 1000, 'sub': 'wrestling'},
            {'tag': '#آمادگی_بدنی', 'post_count': 1000, 'sub': 'wrestling'},
            
            # ========== بوکس ==========
            {'tag': '#بوکس', 'post_count': 766000, 'sub': 'boxing'},
            {'tag': '#بوکسور', 'post_count': 232000, 'sub': 'boxing'},
            {'tag': '#تمرین_بوکس', 'post_count': 1000, 'sub': 'boxing'},
            {'tag': '#بوکس_ایران', 'post_count': 35200, 'sub': 'boxing'},
            {'tag': '#ورزش_رزمی', 'post_count': 43600, 'sub': 'boxing'},
            {'tag': '#مبارزه', 'post_count': 441000, 'sub': 'boxing'},
            {'tag': '#قدرت_بدنی', 'post_count': 24700, 'sub': 'boxing'},
            {'tag': '#باشگاه_بوکس', 'post_count': 1000, 'sub': 'boxing'},
            {'tag': '#فیتنس_رزمی', 'post_count': 100, 'sub': 'boxing'},
        ]
        
        c, u = self.seed_hashtags(sports_cat, sports_subs, sports_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 ورزش: {c} جدید, {u} بروزرسانی')





                # ==========================================
        # ۹. هنر
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: هنر')
        
        art_cat, art_subs = self.create_category_with_subs({
            'name_fa': 'هنر',
            'name_en': 'Art',
            'slug': 'art',
            'subcategories': {
                'general-art': {'fa': 'هنر (عمومی)', 'en': 'General Art'},
                'painting': {'fa': 'نقاشی', 'en': 'Painting'},
                'drawing': {'fa': 'طراحی', 'en': 'Drawing'},
                'digital-art': {'fa': 'دیجیتال آرت', 'en': 'Digital Art'},
                'graphic-logo': {'fa': 'گرافیک و طراحی لوگو', 'en': 'Graphic & Logo Design'},
                'calligraphy': {'fa': 'خوشنویسی', 'en': 'Calligraphy'},
                'sculpture': {'fa': 'مجسمه‌سازی', 'en': 'Sculpture'},
                'pottery': {'fa': 'سفالگری', 'en': 'Pottery'},
            }
        })

        art_hashtags = [
            # ========== هنر (عمومی) ==========
            {'tag': '#هنر', 'post_count': 1200000, 'sub': 'general-art'},
            {'tag': '#هنرمند', 'post_count': 7800000, 'sub': 'general-art'},
            {'tag': '#هنر_ایرانی', 'post_count': 474000, 'sub': 'general-art'},
            {'tag': '#آثار_هنری', 'post_count': 42900, 'sub': 'general-art'},
            {'tag': '#خلاقیت', 'post_count': 4900, 'sub': 'general-art'},
            {'tag': '#هنر_دست', 'post_count': 1200000, 'sub': 'general-art'},
            {'tag': '#هنر_معاصر', 'post_count': 120000, 'sub': 'general-art'},
            {'tag': '#سبک_هنری', 'post_count': 5000, 'sub': 'general-art'},
            {'tag': '#گالری_هنری', 'post_count': 483000, 'sub': 'general-art'},
            {'tag': '#هنر_زیبا', 'post_count': 16500, 'sub': 'general-art'},
            
            # ========== نقاشی ==========
            {'tag': '#نقاشی', 'post_count': 1200000, 'sub': 'painting'},
            {'tag': '#نقاشی_هنری', 'post_count': 17000, 'sub': 'painting'},
            {'tag': '#نقاشی_روی_بوم', 'post_count': 54500, 'sub': 'painting'},
            {'tag': '#نقاشی_مدرن', 'post_count': 1100000, 'sub': 'painting'},
            {'tag': '#رنگ_روغن', 'post_count': 921000, 'sub': 'painting'},
            {'tag': '#آبرنگ', 'post_count': 286000, 'sub': 'painting'},
            {'tag': '#اکرلیک', 'post_count': 290000, 'sub': 'painting'},
            {'tag': '#اثر_هنری', 'post_count': 65300, 'sub': 'painting'},
            {'tag': '#هنر_نقاشی', 'post_count': 143000, 'sub': 'painting'},
            {'tag': '#نقاش_ایرانی', 'post_count': 5000, 'sub': 'painting'},
            
            # ========== طراحی ==========
            {'tag': '#طراحی', 'post_count': 925000, 'sub': 'drawing'},
            {'tag': '#طراحی_دستی', 'post_count': 15700, 'sub': 'drawing'},
            {'tag': '#طراحی_چهره', 'post_count': 823000, 'sub': 'drawing'},
            {'tag': '#اسکچ', 'post_count': 122000, 'sub': 'drawing'},
            {'tag': '#طراحی_مداد', 'post_count': 42900, 'sub': 'drawing'},
            {'tag': '#طراحی_خلاقانه', 'post_count': 29500, 'sub': 'drawing'},
            {'tag': '#طراحی_هنری', 'post_count': 5000, 'sub': 'drawing'},
            {'tag': '#آموزش_طراحی', 'post_count': 31400, 'sub': 'drawing'},
            {'tag': '#هنر_طراحی', 'post_count': 100, 'sub': 'drawing'},
            
            # ========== دیجیتال آرت ==========
            {'tag': '#دیجیتال_آرت', 'post_count': 10800, 'sub': 'digital-art'},
            {'tag': '#هنر_دیجیتال', 'post_count': 48400, 'sub': 'digital-art'},
            {'tag': '#نقاشی_دیجیتال', 'post_count': 259000, 'sub': 'digital-art'},
            {'tag': '#طراحی_دیجیتال', 'post_count': 58400, 'sub': 'digital-art'},
            {'tag': '#دیجیتال_پینتینگ', 'post_count': 19300, 'sub': 'digital-art'},
            {'tag': '#کانسپت_آرت', 'post_count': 5000, 'sub': 'digital-art'},
            {'tag': '#ایلاستریشن', 'post_count': 5000, 'sub': 'digital-art'},
            {'tag': '#آرت_دیجیتال', 'post_count': 1000, 'sub': 'digital-art'},
            {'tag': '#هنرمند_دیجیتال', 'post_count': 500, 'sub': 'digital-art'},
            
            # ========== گرافیک و طراحی لوگو ==========
            {'tag': '#گرافیک', 'post_count': 2100000, 'sub': 'graphic-logo'},
            {'tag': '#طراحی_گرافیک', 'post_count': 504000, 'sub': 'graphic-logo'},
            {'tag': '#گرافیست', 'post_count': 585000, 'sub': 'graphic-logo'},
            {'tag': '#طراحی_لوگو', 'post_count': 734000, 'sub': 'graphic-logo'},
            {'tag': '#لوگو', 'post_count': 1600000, 'sub': 'graphic-logo'},
            {'tag': '#برندینگ', 'post_count': 777000, 'sub': 'graphic-logo'},
            {'tag': '#هویت_بصری', 'post_count': 171000, 'sub': 'graphic-logo'},
            {'tag': '#طراحی_هویت_بصری', 'post_count': 16300, 'sub': 'graphic-logo'},
            {'tag': '#لوگو_تایپ', 'post_count': 153000, 'sub': 'graphic-logo'},
            {'tag': '#طراح_گرافیک', 'post_count': 205000, 'sub': 'graphic-logo'},
            
            # ========== خوشنویسی ==========
            {'tag': '#خوشنویسی', 'post_count': 1200000, 'sub': 'calligraphy'},
            {'tag': '#خطاطی', 'post_count': 780000, 'sub': 'calligraphy'},
            {'tag': '#خط_فارسی', 'post_count': 5000, 'sub': 'calligraphy'},
            {'tag': '#نستعلیق', 'post_count': 604000, 'sub': 'calligraphy'},
            {'tag': '#شکسته_نستعلیق', 'post_count': 205000, 'sub': 'calligraphy'},
            {'tag': '#هنر_خوشنویسی', 'post_count': 30300, 'sub': 'calligraphy'},
            {'tag': '#قلم_نی', 'post_count': 22400, 'sub': 'calligraphy'},
            {'tag': '#خط_زیبا', 'post_count': 24800, 'sub': 'calligraphy'},
            {'tag': '#هنر_ایرانی', 'post_count': 474000, 'sub': 'calligraphy'},
            
            # ========== مجسمه‌سازی ==========
            {'tag': '#مجسمه_سازی', 'post_count': 304000, 'sub': 'sculpture'},
            {'tag': '#مجسمه', 'post_count': 1400000, 'sub': 'sculpture'},
            {'tag': '#هنر_حجمی', 'post_count': 100, 'sub': 'sculpture'},
            {'tag': '#پیکرتراشی', 'post_count': 287000, 'sub': 'sculpture'},
            {'tag': '#هنرمند_مجسمه_ساز', 'post_count': 100, 'sub': 'sculpture'},
            {'tag': '#آثار_حجمی', 'post_count': 100, 'sub': 'sculpture'},
            {'tag': '#مجسمه_هنری', 'post_count': 1000, 'sub': 'sculpture'},
            {'tag': '#هنر_سه_بعدی', 'post_count': 500, 'sub': 'sculpture'},
            {'tag': '#مجسمه_دستی', 'post_count': 100, 'sub': 'sculpture'},
            
            # ========== سفالگری ==========
            {'tag': '#سفالگری', 'post_count': 415000, 'sub': 'pottery'},
            {'tag': '#سفال', 'post_count': 1200000, 'sub': 'pottery'},
            {'tag': '#سرامیک', 'post_count': 1700000, 'sub': 'pottery'},
            {'tag': '#هنر_سفال', 'post_count': 5000, 'sub': 'pottery'},
            {'tag': '#ظروف_سفالی', 'post_count': 44300, 'sub': 'pottery'},
            {'tag': '#سفال_دستی', 'post_count': 1000, 'sub': 'pottery'},
            {'tag': '#هنر_دستی', 'post_count': 186000, 'sub': 'pottery'},
            {'tag': '#سرامیک_دست_ساز', 'post_count': 22900, 'sub': 'pottery'},
            {'tag': '#صنایع_دستی', 'post_count': 2900000, 'sub': 'pottery'},
            {'tag': '#هنر_سنتی', 'post_count': 31800, 'sub': 'pottery'},
        ]
        
        c, u = self.seed_hashtags(art_cat, art_subs, art_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 هنر: {c} جدید, {u} بروزرسانی')








                # ==========================================
        # ۱۰. عکاسی
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: عکاسی')
        
        photo_cat, photo_subs = self.create_category_with_subs({
            'name_fa': 'عکاسی',
            'name_en': 'Photography',
            'slug': 'photography',
            'subcategories': {
                'general-photo': {'fa': 'عکاسی (عمومی)', 'en': 'General Photography'},
                'portrait': {'fa': 'عکاسی پرتره', 'en': 'Portrait Photography'},
                'nature-photo': {'fa': 'عکاسی طبیعت', 'en': 'Nature Photography'},
                'street-photo': {'fa': 'عکاسی خیابانی', 'en': 'Street Photography'},
                'architecture': {'fa': 'عکاسی معماری', 'en': 'Architecture Photography'},
                'mobilegraphy': {'fa': 'موبایل‌گرافی', 'en': 'Mobile Photography'},
                'photo-edit': {'fa': 'ادیت عکس', 'en': 'Photo Editing'},
                'lighting': {'fa': 'نورپردازی', 'en': 'Lighting'},
            }
        })

        photo_hashtags = [
            # ========== عکاسی (عمومی) ==========
            {'tag': '#عکاسی', 'post_count': 15000000, 'sub': 'general-photo'},
            {'tag': '#عکاس', 'post_count': 1500000, 'sub': 'general-photo'},
            {'tag': '#عکس', 'post_count': 2600000, 'sub': 'general-photo'},
            {'tag': '#هنر_عکاسی', 'post_count': 151000, 'sub': 'general-photo'},
            {'tag': '#ثبت_لحظه', 'post_count': 11700, 'sub': 'general-photo'},
            {'tag': '#قاب_زیبا', 'post_count': 5000, 'sub': 'general-photo'},
            {'tag': '#عکاسی_حرفه_ای', 'post_count': 552000, 'sub': 'general-photo'},
            {'tag': '#خلاقیت_در_عکاسی', 'post_count': 5000, 'sub': 'general-photo'},
            {'tag': '#تصویر_زیبا', 'post_count': 5000, 'sub': 'general-photo'},
            {'tag': '#عکاسی_ایرانی', 'post_count': 5000, 'sub': 'general-photo'},
            
            # ========== عکاسی پرتره ==========
            {'tag': '#پرتره', 'post_count': 1700000, 'sub': 'portrait'},
            {'tag': '#عکاسی_پرتره', 'post_count': 1500000, 'sub': 'portrait'},
            {'tag': '#پرتره_هنری', 'post_count': 236000, 'sub': 'portrait'},
            {'tag': '#پرتره_طبیعی', 'post_count': 100, 'sub': 'portrait'},
            {'tag': '#پرتره_استودیویی', 'post_count': 500, 'sub': 'portrait'},
            {'tag': '#چهره_نگاری', 'post_count': 5000, 'sub': 'portrait'},
            {'tag': '#مدلینگ', 'post_count': 6500000, 'sub': 'portrait'},
            {'tag': '#عکاسی_مدل', 'post_count': 15900, 'sub': 'portrait'},
            {'tag': '#پرتره_خاص', 'post_count': 15100, 'sub': 'portrait'},
            
            # ========== عکاسی طبیعت ==========
            {'tag': '#عکاسی_طبیعت', 'post_count': 1300000, 'sub': 'nature-photo'},
            {'tag': '#طبیعت', 'post_count': 5200000, 'sub': 'nature-photo'},
            {'tag': '#منظره', 'post_count': 889000, 'sub': 'nature-photo'},
            {'tag': '#مناظر_طبیعی', 'post_count': 5000, 'sub': 'nature-photo'},
            {'tag': '#عکاسی_منظره', 'post_count': 99600, 'sub': 'nature-photo'},
            {'tag': '#غروب', 'post_count': 2400000, 'sub': 'nature-photo'},
            {'tag': '#طلوع', 'post_count': 349000, 'sub': 'nature-photo'},
            {'tag': '#جنگل', 'post_count': 3100000, 'sub': 'nature-photo'},
            {'tag': '#کوهستان', 'post_count': 950000, 'sub': 'nature-photo'},
            {'tag': '#طبیعت_گردی', 'post_count': 1800000, 'sub': 'nature-photo'},
            
            # ========== عکاسی خیابانی ==========
            {'tag': '#عکاسی_خیابانی', 'post_count': 463000, 'sub': 'street-photo'},
            {'tag': '#استریت_فتوگرافی', 'post_count': 500, 'sub': 'street-photo'},
            {'tag': '#خیابان', 'post_count': 431000, 'sub': 'street-photo'},
            {'tag': '#زندگی_شهری', 'post_count': 11300, 'sub': 'street-photo'},
            {'tag': '#لحظه_نگاری', 'post_count': 1000, 'sub': 'street-photo'},
            {'tag': '#عکاسی_شهری', 'post_count': 113000, 'sub': 'street-photo'},
            {'tag': '#عکس_مستند', 'post_count': 5000, 'sub': 'street-photo'},
            {'tag': '#عکاسی_مستند', 'post_count': 100000, 'sub': 'street-photo'},
            {'tag': '#زندگی_روزمره', 'post_count': 23600, 'sub': 'street-photo'},
            
            # ========== عکاسی معماری ==========
            {'tag': '#عکاسی_معماری', 'post_count': 85200, 'sub': 'architecture'},
            {'tag': '#معماری', 'post_count': 5500000, 'sub': 'architecture'},
            {'tag': '#ساختمان', 'post_count': 3000000, 'sub': 'architecture'},
            {'tag': '#طراحی_معماری', 'post_count': 707000, 'sub': 'architecture'},
            {'tag': '#نمای_ساختمان', 'post_count': 204000, 'sub': 'architecture'},
            {'tag': '#عکاسی_ساختمان', 'post_count': 1000, 'sub': 'architecture'},
            {'tag': '#فضای_شهری', 'post_count': 11200, 'sub': 'architecture'},
            {'tag': '#معماری_مدرن', 'post_count': 940000, 'sub': 'architecture'},
            {'tag': '#جزئیات_معماری', 'post_count': 1000, 'sub': 'architecture'},
            
            # ========== موبایل‌گرافی ==========
            {'tag': '#موبایل_گرافی', 'post_count': 440000, 'sub': 'mobilegraphy'},
            {'tag': '#عکاسی_با_موبایل', 'post_count': 728000, 'sub': 'mobilegraphy'},
            {'tag': '#موبایل_فتوگرافی', 'post_count': 5000, 'sub': 'mobilegraphy'},
            {'tag': '#عکس_با_موبایل', 'post_count': 13000, 'sub': 'mobilegraphy'},
            {'tag': '#موبایل_شات', 'post_count': 100, 'sub': 'mobilegraphy'},
            {'tag': '#موبایل_آرت', 'post_count': 100, 'sub': 'mobilegraphy'},
            {'tag': '#تکنیک_عکاسی', 'post_count': 10300, 'sub': 'mobilegraphy'},
            {'tag': '#عکاسی_خلاقانه', 'post_count': 95700, 'sub': 'mobilegraphy'},
            {'tag': '#موبایل_پروگرافی', 'post_count': 100, 'sub': 'mobilegraphy'},
            
            # ========== ادیت عکس ==========
            {'tag': '#ادیت_عکس', 'post_count': 897000, 'sub': 'photo-edit'},
            {'tag': '#ویرایش_عکس', 'post_count': 32100, 'sub': 'photo-edit'},
            {'tag': '#فتوشاپ', 'post_count': 1200000, 'sub': 'photo-edit'},
            {'tag': '#لایت_روم', 'post_count': 19900, 'sub': 'photo-edit'},
            {'tag': '#پریست', 'post_count': 19500, 'sub': 'photo-edit'},
            {'tag': '#رتوش', 'post_count': 56900, 'sub': 'photo-edit'},
            {'tag': '#ادیت_حرفه_ای', 'post_count': 41500, 'sub': 'photo-edit'},
            {'tag': '#اصلاح_رنگ', 'post_count': 16000, 'sub': 'photo-edit'},
            {'tag': '#ویرایش_تصویر', 'post_count': 1000, 'sub': 'photo-edit'},
            
            # ========== نورپردازی ==========
            {'tag': '#نورپردازی', 'post_count': 836000, 'sub': 'lighting'},
            {'tag': '#نور_طبیعی', 'post_count': 13200, 'sub': 'lighting'},
            {'tag': '#نور_استودیویی', 'post_count': 100, 'sub': 'lighting'},
            {'tag': '#نور_عکاسی', 'post_count': 1000, 'sub': 'lighting'},
            {'tag': '#تکنیک_نورپردازی', 'post_count': 100, 'sub': 'lighting'},
            {'tag': '#نور_خلاقانه', 'post_count': 100, 'sub': 'lighting'},
            {'tag': '#عکاسی_استودیویی', 'post_count': 11400, 'sub': 'lighting'},
            {'tag': '#نور_پرتره', 'post_count': 100, 'sub': 'lighting'},
            {'tag': '#نور_سینمایی', 'post_count': 500, 'sub': 'lighting'},
        ]
        
        c, u = self.seed_hashtags(photo_cat, photo_subs, photo_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 عکاسی: {c} جدید, {u} بروزرسانی')







                # ==========================================
        # ۱۱. موسیقی
        # ==========================================
        self.stdout.write('\n📦 شروع دسته‌بندی: موسیقی')
        
        music_cat, music_subs = self.create_category_with_subs({
            'name_fa': 'موسیقی',
            'name_en': 'Music',
            'slug': 'music',
            'subcategories': {
                'general-music': {'fa': 'موسیقی (عمومی)', 'en': 'General Music'},
                'pop': {'fa': 'موسیقی پاپ', 'en': 'Pop Music'},
                'traditional': {'fa': 'موسیقی سنتی', 'en': 'Traditional Music'},
                'rap': {'fa': 'رپ', 'en': 'Rap'},
                'rock': {'fa': 'راک', 'en': 'Rock'},
                'classical': {'fa': 'موسیقی کلاسیک', 'en': 'Classical Music'},
                'concert': {'fa': 'کنسرت', 'en': 'Concert'},
                'singer-song': {'fa': 'خواننده و آهنگ', 'en': 'Singer & Song'},
                'opera': {'fa': 'اپرا', 'en': 'Opera'},
            }
        })

        music_hashtags = [
            # ========== موسیقی (عمومی) ==========
            {'tag': '#موسیقی', 'post_count': 1700000, 'sub': 'general-music'},
            {'tag': '#موزیک', 'post_count': 228000, 'sub': 'general-music'},
            {'tag': '#آهنگ', 'post_count': 3000000, 'sub': 'general-music'},
            {'tag': '#خواننده', 'post_count': 5600000, 'sub': 'general-music'},
            {'tag': '#هنر_موسیقی', 'post_count': 20800, 'sub': 'general-music'},
            {'tag': '#موسیقی_ایرانی', 'post_count': 1300000, 'sub': 'general-music'},
            {'tag': '#موسیقی_جهانی', 'post_count': 5000, 'sub': 'general-music'},
            {'tag': '#ملودی', 'post_count': 406000, 'sub': 'general-music'},
            {'tag': '#ترانه', 'post_count': 2500000, 'sub': 'general-music'},
            {'tag': '#عاشقان_موسیقی', 'post_count': 1000, 'sub': 'general-music'},
            
            # ========== موسیقی پاپ ==========
            {'tag': '#پاپ', 'post_count': 1700000, 'sub': 'pop'},
            {'tag': '#موسیقی_پاپ', 'post_count': 842000, 'sub': 'pop'},
            {'tag': '#پاپ_ایرانی', 'post_count': 5000, 'sub': 'pop'},
            {'tag': '#پاپ_فارسی', 'post_count': 1000, 'sub': 'pop'},
            {'tag': '#آهنگ_پاپ', 'post_count': 84200, 'sub': 'pop'},
            {'tag': '#خواننده_پاپ', 'post_count': 408000, 'sub': 'pop'},
            {'tag': '#ترانه_پاپ', 'post_count': 5000, 'sub': 'pop'},
            {'tag': '#موزیک_پاپ', 'post_count': 502000, 'sub': 'pop'},
            {'tag': '#پاپ_جدید', 'post_count': 500, 'sub': 'pop'},
            
            # ========== موسیقی سنتی ==========
            {'tag': '#سنتی', 'post_count': 2000000, 'sub': 'traditional'},
            {'tag': '#موسیقی_سنتی', 'post_count': 1700000, 'sub': 'traditional'},
            {'tag': '#موسیقی_اصیل', 'post_count': 704000, 'sub': 'traditional'},
            {'tag': '#موسیقی_ایرانی', 'post_count': 1300000, 'sub': 'traditional'},
            {'tag': '#آواز_سنتی', 'post_count': 206000, 'sub': 'traditional'},
            {'tag': '#ساز_ایرانی', 'post_count': 40500, 'sub': 'traditional'},
            {'tag': '#ردیف_موسیقی', 'post_count': 5000, 'sub': 'traditional'},
            {'tag': '#موسیقی_کلاسیک_ایرانی', 'post_count': 22300, 'sub': 'traditional'},
            {'tag': '#نوای_ایرانی', 'post_count': 1000, 'sub': 'traditional'},
            
            # ========== رپ ==========
            {'tag': '#رپ', 'post_count': 2700000, 'sub': 'rap'},
            {'tag': '#رپ_فارسی', 'post_count': 1000000, 'sub': 'rap'},
            {'tag': '#هیپ_هاپ', 'post_count': 502000, 'sub': 'rap'},
            {'tag': '#رپر', 'post_count': 305000, 'sub': 'rap'},
            {'tag': '#موسیقی_رپ', 'post_count': 5000, 'sub': 'rap'},
            {'tag': '#رپ_جدید', 'post_count': 1000, 'sub': 'rap'},
            {'tag': '#هیپ_هاپ_فارسی', 'post_count': 10000, 'sub': 'rap'},
            {'tag': '#آهنگ_رپ', 'post_count': 12000, 'sub': 'rap'},
            {'tag': '#بیت', 'post_count': 350000, 'sub': 'rap'},
            
            # ========== راک ==========
            {'tag': '#راک', 'post_count': 363000, 'sub': 'rock'},
            {'tag': '#موسیقی_راک', 'post_count': 48600, 'sub': 'rock'},
            {'tag': '#راک_فارسی', 'post_count': 26400, 'sub': 'rock'},
            {'tag': '#راک_کلاسیک', 'post_count': 100, 'sub': 'rock'},
            {'tag': '#راک_مدرن', 'post_count': 100, 'sub': 'rock'},
            {'tag': '#گیتار_الکتریک', 'post_count': 77800, 'sub': 'rock'},
            {'tag': '#بند_راک', 'post_count': 100, 'sub': 'rock'},
            {'tag': '#آهنگ_راک', 'post_count': 1000, 'sub': 'rock'},
            {'tag': '#راک_اند_رول', 'post_count': 5000, 'sub': 'rock'},
            
            # ========== موسیقی کلاسیک ==========
            {'tag': '#کلاسیک', 'post_count': 3000000, 'sub': 'classical'},
            {'tag': '#موسیقی_کلاسیک', 'post_count': 293000, 'sub': 'classical'},
            {'tag': '#ارکستر', 'post_count': 129000, 'sub': 'classical'},
            {'tag': '#سمفونی', 'post_count': 21900, 'sub': 'classical'},
            {'tag': '#پیانو', 'post_count': 1100000, 'sub': 'classical'},
            {'tag': '#ویولن', 'post_count': 427000, 'sub': 'classical'},
            {'tag': '#آثار_کلاسیک', 'post_count': 500, 'sub': 'classical'},
            {'tag': '#آهنگساز', 'post_count': 545000, 'sub': 'classical'},
            {'tag': '#موسیقی_بی_کلام', 'post_count': 17100, 'sub': 'classical'},
            
            # ========== کنسرت ==========
            {'tag': '#کنسرت', 'post_count': 3500000, 'sub': 'concert'},
            {'tag': '#اجرای_زنده', 'post_count': 527000, 'sub': 'concert'},
            {'tag': '#موسیقی_زنده', 'post_count': 117000, 'sub': 'concert'},
            {'tag': '#کنسرت_ایران', 'post_count': 5000, 'sub': 'concert'},
            {'tag': '#استیج', 'post_count': 269000, 'sub': 'concert'},
            {'tag': '#اجرای_موسیقی', 'post_count': 5000, 'sub': 'concert'},
            {'tag': '#فستیوال_موسیقی', 'post_count': 5000, 'sub': 'concert'},
            {'tag': '#شب_کنسرت', 'post_count': 100, 'sub': 'concert'},
            {'tag': '#هواداران_موسیقی', 'post_count': 100, 'sub': 'concert'},
            
            # ========== خواننده و آهنگ ==========
            {'tag': '#خواننده', 'post_count': 5600000, 'sub': 'singer-song'},
            {'tag': '#خواننده_ایرانی', 'post_count': 303000, 'sub': 'singer-song'},
            {'tag': '#آهنگ', 'post_count': 3000000, 'sub': 'singer-song'},
            {'tag': '#آهنگ_جدید', 'post_count': 1200000, 'sub': 'singer-song'},
            {'tag': '#ترانه', 'post_count': 2500000, 'sub': 'singer-song'},
            {'tag': '#تک_آهنگ', 'post_count': 14000, 'sub': 'singer-song'},
            {'tag': '#آلبوم', 'post_count': 217000, 'sub': 'singer-song'},
            {'tag': '#موزیک_جدید', 'post_count': 2200000, 'sub': 'singer-song'},
            {'tag': '#پخش_موسیقی', 'post_count': 1000, 'sub': 'singer-song'},
            
            # ========== اپرا ==========
            {'tag': '#اپرا', 'post_count': 39500, 'sub': 'opera'},
            {'tag': '#موسیقی_اپرا', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#خوانندگی_اپرا', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#اپرای_کلاسیک', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#نمایش_موسیقی', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#آواز_اپرا', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#هنر_اپرا', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#اجرای_اپرا', 'post_count': 100, 'sub': 'opera'},
            {'tag': '#موسیقی_نمایشی', 'post_count': 100, 'sub': 'opera'},
        ]
        
        c, u = self.seed_hashtags(music_cat, music_subs, music_hashtags)
        total_created += c
        total_updated += u
        self.stdout.write(f'  📊 موسیقی: {c} جدید, {u} بروزرسانی')


        # ==========================================
        # گزارش نهایی
        # ==========================================
        self.stdout.write(self.style.SUCCESS(
            f'\n🎉 عملیات با موفقیت انجام شد!'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'📊 مجموع: {total_created} هشتگ جدید + {total_updated} بروزرسانی'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'📦 تعداد کل هشتگ‌ها: {Hashtag.objects.count()} عدد'
        ))