from django.shortcuts import render
from blog.models import Post
from .models import *
from django.template.loader import render_to_string
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django_ratelimit.decorators import ratelimit


def get_domain_specific_context(request):
    """
    Helper function to get domain-specific context.
    """
    domain = request.get_host()
    
    # Default values
    title = "Chat Gratis - español"
    chat_branding = "Chat Gratis"
    google_tag_manager_id = ""
    image_url = "images/chat.png"
    canonical_url = request.build_absolute_uri()

    # Domain-specific settings
    if domain == 'web.chateagratis.chat':
        title = "Bienvenidos a ChateaGratis"
        chat_branding = "ChateaGratis"
        google_tag_manager_id = "GTM-XXXXXXX1"
        canonical_url = f"https://web.chateagratis.chat{request.path}"
    elif domain == 'www.chateagratis.chat':
        title = "Bienvenidos a ChateaGratis - Chat Gratis en español"
        chat_branding = "ChateaGratis"
        google_tag_manager_id = "GTM-XXXXXXX2"
        canonical_url = f"https://www.chateagratis.chat{request.path}"
    elif domain == 'chateagratis.chat':
        title = "Bienvenidos a ChateaGratis - Chat Gratis en español"
        chat_branding = "Chatea Gratis"
        google_tag_manager_id = "GTM-PJ8GHV58"
        canonical_url = f"https://chateagratis.chat{request.path}"
    elif domain == 'www.vicio.chat':
        title = "ViciChat - Tu punto de encuentro en español"
        chat_branding = "ViCio.Chat"
        google_tag_manager_id = "GTM-XXXXXXX4"
        canonical_url = f"https://www.vicio.chat{request.path}"
    elif domain == 'vicio.chat':
        title = "ViCio.Chat - Tu punto de encuentro en la red"
        chat_branding = "ViCio.Chat"
        google_tag_manager_id = "GTM-XXXXXXX6"
        image_url = "images/vicio.chat.jpg"
        canonical_url = f"https://vicio.chat{request.path}"
    elif domain == 'www.redlatina.chat':
        title = "RedLatina - Chat Gratis"
        chat_branding = "RedLatina"
        google_tag_manager_id = "GTM-XXXXXXX7"
        canonical_url = f"https://www.redlatina.chat{request.path}"
    elif domain == 'web.redlatina.chat':
        title = "RedLatina - Chat Gratis"
        chat_branding = "Red-Latina"
        google_tag_manager_id = "GTM-XXXXXXX8"
        canonical_url = f"https://web.redlatina.chat{request.path}"
    elif domain == 'redlatina.chat':
        title = "RedLatina - Chat Gratis"
        chat_branding = "RedLatina"
        google_tag_manager_id = "GTM-XXXXXXX9"
        canonical_url = f"https://redlatina.chat{request.path}"

    return {
        'title': title,
        'chat_branding': chat_branding,
        'google_tag_manager_id': google_tag_manager_id,
        'canonical_url': canonical_url,
        'image_url': image_url
    }

def get_meta_information(context_type, chat_branding):
    """
    Helper function to get meta information based on the context type and dynamically insert chat branding.
    """
    meta_info = {
        'meta_title': f"Chat Gratis - español",
        'meta_description': f"Únete a {chat_branding}, la mejor plataforma de chat gratis en español donde puedes conocer gente nueva, hacer amigos y disfrutar de conversaciones en tiempo real.",
        'meta_keywords': "chat gratis, chat en español, conocer gente, amigos, chat online",
        'meta_author': "ChateaGratis",
        'meta_image': "/static/images/chateagratis.chat.svg",
    }

    if context_type == "españa":
        meta_info.update({
            'meta_title': "Chat de España - Chats de España sin registro",
            'meta_description': f"Únete al chat de España en {chat_branding}, la mejor plataforma para conocer gente, hacer amigos y disfrutar de conversaciones en tiempo real en España.",
            'meta_keywords': "chat gratis, chat de españa, chat español, amigos españa, chatear en españa, chicas madrid, chat madrid, chat en español españa",
            'meta_author': "ChateaGratis España",
            'meta_image': "/static/images/chateagratis.chat.svg",
        })
    elif context_type == "latinoamerica":
        meta_info.update({
            'meta_title': "Chats de Latinoamérica para latinos de Latinchat",
            'meta_description': f"Únete al chat de Latinoamérica en {chat_branding}, la mejor plataforma para conocer gente, hacer amigos y disfrutar de conversaciones en tiempo real en Latinoamérica.",
            'meta_keywords': "chat gratis, chat de latinoamérica, chat latino, amigos latinoamérica, chatear en latinoamérica, chicas latinoamérica, chat en español latinoamérica",
            'meta_author': "ChateaGratis Latinoamérica",
            'meta_image': "/media/home_category_images/latinoamerica-1.jpg",
        })
    elif context_type == "paraguay":
        meta_info.update({
            'meta_title': "Chat de Paraguay - Yaguachat - Chat paraguayo",
            'meta_description': f"Únete al chat de Paraguay en {chat_branding}, la mejor plataforma para conocer gente, hacer amigos y disfrutar de conversaciones en tiempo real en Paraguay.",
            'meta_keywords': "chat gratis, chat de paraguay, chat paraguayo, amigos paraguay, chatear en paraguay, chicas asuncion, chat asuncion, chat en español paraguay",
            'meta_author': "Paraguay de Paraguay",
            'meta_image': "/media/chatroomslatam/Paraguay.jpg",
        })
    elif context_type == "argentina":
        meta_info.update({
            'meta_title': "Chats del pais de Argentina - Argentinos y Argentinas chat gratis",
            'meta_description': f"Únete al chat de Argentina en {chat_branding}, la mejor plataforma para conocer gente, hacer amigos y disfrutar de conversaciones en tiempo real en Argentina.",
            'meta_keywords': "chat gratis, chat de argentina, chat argentino, amigos argentina, chatear en argentina, chicas buenos aires, chat buenos aires, chat en español argentina",
            'meta_author': "ChateaGratis Argentina",
            'meta_image': "/media/chatroomslatam/Arg.jpg",
        })
    elif context_type == "home":
        meta_info.update({
            'meta_title': f"{chat_branding} - Chats gratis en español",
            'meta_description': f"Únete a {chat_branding}, la mejor plataforma para conocer gente, hacer amigos y disfrutar de conversaciones en tiempo real.",
            'meta_keywords': "chat gratis, chat de argentina, chat argentino, amigos argentina, chatear en argentina, chicas buenos aires, chat buenos aires, chat en español argentina",
            'meta_author': "ChateaGratis",
            'meta_image': "/static/images/chateagratis.chat.svg",
        })
    
    return meta_info

import random
import requests

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def home(request):
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:4]
    home_categories = HomeCategory.objects.all()
    recommended_chat_rooms = RecommendedChatRoom.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)

    # Get news articles from API
    news_url = f"https://api.currentsapi.services/v1/latest-news?language=es&apiKey=_yoXuUAc50lyd-oydhdaH_PyUowjpliAWQ6u2PWkfDPZJEJ4"
    response = requests.get(news_url)
    news_data = response.json().get('news', [])
    
    # Randomize news articles
    if news_data:
        random.shuffle(news_data)
        news_articles = news_data[:4]  # Limit to 4 articles for display
    else:
        news_articles = []

    # Add data to context
    context.update({
        'latest_posts': latest_posts,
        'home_categories': home_categories,
        'recommended_chat_rooms': recommended_chat_rooms,
        'news_articles': news_articles,
        'canonical_url': request.build_absolute_uri(),
    })

    return render(request, 'main/home.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def opciones(request):
    context = get_domain_specific_context(request)
    if request.method == "POST":
        nick = request.POST.get('nick', '')
        join = request.POST.get('join', '')
        show_password = request.POST.get('show_password', '')
        show_password = 'true' if show_password else 'false'
        context.update({'nick': nick, 'join': join, 'show_password': show_password})
    
    return render(request, 'main/opciones.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def webchat(request):
    context = get_domain_specific_context(request)
    if request.method == "POST":
        nick = request.POST.get('nick', '')
        join = request.POST.get('join', '')
        show_password = request.POST.get('show_password', '')
        show_password = 'true' if show_password else 'false'
        context.update({'nick': nick, 'join': join, 'show_password': show_password})
    
    return render(request, 'main/webchat.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def salas_amistad(request):
    context = get_domain_specific_context(request)
    return render(request, 'main/salas/amistad.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def salas_ligar(request):
    context = get_domain_specific_context(request)
    return render(request, 'main/salas/ligar.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def salas_masde40(request):
    context = get_domain_specific_context(request)
    return render(request, 'main/salas/mas-de-40.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def salas_amor(request):
    context = get_domain_specific_context(request)
    return render(request, 'main/salas/amor.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def cookie_policy(request):
    context = get_domain_specific_context(request)
    return render(request, 'main/cookie_policy.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def terms_of_use(request):
    context = get_domain_specific_context(request)
    return render(request, 'main/terms_of_use.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def paises_españa(request):
    chat_rooms = ChatRoom.objects.all()
    subcategories = SubCategory.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)

    # Get meta information for España (Spain)
    meta_info = get_meta_information("españa", context['chat_branding'])
    context.update(meta_info)

    # Add additional view-specific context
    context.update({
        'chat_rooms': chat_rooms,
        'subcategories': subcategories,
        'canonical_url': request.build_absolute_uri(),
    })

    return render(request, 'main/salas/paises/españa.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def paises_latinoamerica(request):
    chat_roomsLatam = ChatRoomLatam.objects.all()
    subcategoriesLatam = SubCategoryLatam.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)

    # Get meta information for Latinoamérica
    meta_info = get_meta_information("latinoamerica", context['chat_branding'])
    context.update(meta_info)

    # Add additional view-specific context
    context.update({
        'chat_roomsLatam': chat_roomsLatam,
        'subcategoriesLatam': subcategoriesLatam,
        'canonical_url': request.build_absolute_uri(),
    })

    return render(request, 'main/salas/paises/latinoamerica.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt   
def salas_ocio(request):
    chat_roomsOcio = ChatRoomOcio.objects.all()
    subcategoriesOcio = SubCategoryOcio.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)
    context.update({
        'chat_roomsOcio': chat_roomsOcio,
        'subcategoriesOcio': subcategoriesOcio,
    })

    return render(request, 'main/salas/ocio.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def paises_paraguay(request):
    chat_roomsLatam = ChatRoomLatam.objects.all()
    subcategoriesParaguay = SubCategoryParaguay.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)

    # Get meta information for Paraguay
    meta_info = get_meta_information("paraguay", context['chat_branding'])
    context.update(meta_info)

    # Add additional view-specific context
    context.update({
        'chat_roomsLatam': chat_roomsLatam,
        'subcategoriesParaguay': subcategoriesParaguay,
        'canonical_url': request.build_absolute_uri(),
    })

    return render(request, 'main/salas/paises/paraguay.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def paises_argentina(request):
    chat_roomsLatam = ChatRoomLatam.objects.all()
    subcategoriesArgentina = SubCategoryArgentina.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)

    # Get meta information for Argentina
    meta_info = get_meta_information("argentina", context['chat_branding'])
    context.update(meta_info)

    # Add additional view-specific context
    context.update({
        'chat_roomsLatam': chat_roomsLatam,
        'subcategoriesArgentina': subcategoriesArgentina,
        'canonical_url': request.build_absolute_uri(),
    })

    return render(request, 'main/salas/paises/argentina.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def salas_dev(request):
    chat_roomsDev = ChatRoomDev.objects.all()
    subcategoriesDev = SubCategoryDev.objects.all()

    # Get domain-specific context
    context = get_domain_specific_context(request)
    context.update({
        'chat_roomsDev': chat_roomsDev,
        'subcategoriesDev': subcategoriesDev,
    })

    return render(request, 'main/salas/dev.html', context)

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
@csrf_exempt
def robots_txt(request):
    content = render_to_string('robots.txt')
    return HttpResponse(content, content_type='text/plain')
