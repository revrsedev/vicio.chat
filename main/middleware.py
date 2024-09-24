from django.utils.deprecation import MiddlewareMixin
import json

class CookieConsentMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        cookies_consent = request.COOKIES.get('cookies_consent')
        
        # If the user has not consented to cookies, remove any cookies except the consent cookie itself
        if cookies_consent != 'true':
            for cookie in request.COOKIES:
                if cookie != 'cookies_consent':
                    response.delete_cookie(cookie)
        
        return response