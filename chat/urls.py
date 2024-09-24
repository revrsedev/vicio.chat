from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import (
    ChatRoomSitemap,
    SubCategorySitemap,
    ChatRoomLatamSitemap,
    SubCategoryLatamSitemap,
    ChatRoomOcioSitemap,
    SubCategoryOcioSitemap,
    HomeCategorySitemap,
)
sitemaps = {
    'chatrooms': ChatRoomSitemap,
    'subcategories': SubCategorySitemap,
    'chatroomslatam': ChatRoomLatamSitemap,
    'subcategorieslatam': SubCategoryLatamSitemap,
    'chatroomocio': ChatRoomOcioSitemap,
    'subcategoriesocio': SubCategoryOcioSitemap,
    'homecategories': HomeCategorySitemap,  # Add this line
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('authapp.urls')),  # Include the authapp URLs
    path('blog/', include('blog.urls', namespace='blog')),  # Include the blog URLs
    #path('unrealircd/', include('unrealircd_rpc.urls')),  # Include your app's URLs
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
