from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

index = never_cache(TemplateView.as_view(template_name='index.html'))
@api_view(['GET'])
def send_some_data(request):
    return Response({
        "data": "nandanigeitpl@gmail.com"
    })