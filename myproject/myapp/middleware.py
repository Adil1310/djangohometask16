from django.shortcuts import redirect
import logging

class RedirectIfNotLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        response = self.get_response(request)
        return response

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('request_logger')

    def __call__(self, request):
        self.logger.info(f"Method: {request.method}, Path: {request.path}, User: {request.user}")
        response = self.get_response(request)
        return response