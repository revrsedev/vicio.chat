# main/admin.py

from django.contrib import admin
from .models import *

admin.site.register(HomeCategory)
admin.site.register(RecommendedChatRoom)
admin.site.register(ChatRoom)
admin.site.register(SubCategory)
admin.site.register(ChatRoomLatam)
admin.site.register(SubCategoryLatam)
admin.site.register(ChatRoomOcio)
admin.site.register(SubCategoryOcio)
admin.site.register(SubCategoryParaguay)
admin.site.register(SubCategoryArgentina)

admin.site.site_header = "chateagratis.chat"
admin.site.site_title = "chateagratis.chat"
admin.site.index_title = "chateagratis.chat"