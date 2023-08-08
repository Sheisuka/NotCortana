from django.views import View
from django.http import JsonResponse


def index(request):
    return JsonResponse({"error": "hi"})