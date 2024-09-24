from django.contrib.sitemaps import Sitemap
from .models import ChatRoom, SubCategory, ChatRoomLatam, SubCategoryLatam, ChatRoomOcio, SubCategoryOcio, HomeCategory
from django.utils.html import strip_tags
from urllib.parse import urljoin
from django.utils.html import strip_tags
from urllib.parse import urljoin

BASE_URL = "/"

class BaseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def location(self, obj):
        # Clean up the URL and construct a full URL
        clean_url = strip_tags(obj.url)  # Ensures there are no HTML tags
        return urljoin(BASE_URL, clean_url)

class ChatRoomSitemap(BaseSitemap):
    priority = 0.8

    def items(self):
        return ChatRoom.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

class SubCategorySitemap(BaseSitemap):
    def items(self):
        return SubCategory.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

class ChatRoomLatamSitemap(BaseSitemap):
    priority = 0.8

    def items(self):
        return ChatRoomLatam.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

class SubCategoryLatamSitemap(BaseSitemap):
    def items(self):
        return SubCategoryLatam.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

class ChatRoomOcioSitemap(BaseSitemap):
    priority = 0.8

    def items(self):
        return ChatRoomOcio.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

class SubCategoryOcioSitemap(BaseSitemap):
    def items(self):
        return SubCategoryOcio.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

class HomeCategorySitemap(BaseSitemap):
    def items(self):
        return HomeCategory.objects.all().order_by('name')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        clean_url = strip_tags(obj.link)  # Ensures there are no HTML tags
        return urljoin(BASE_URL, clean_url)
