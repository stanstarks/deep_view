from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.core.cache import cache

from .models import Modification

# update database once starts
# list_dir = '/media/mi/data/pornographic/lists'

def get_client_ip(request):
    x_forwared_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwared_for:
        ip = x_forwared_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    return HttpResponse("Hello, world. You're at the annotations index.")

def modify(request, image):
    global labelmaps
    ip = get_client_ip(request)
    from_label = '0'
    to_label = request.POST['label']
    m = Modification(ip=ip,
                     date=timezone.now(),
                     from_label=from_label,
                     to_label=to_label,
                     image=image)
    m.save()
    # change labelmaps
    print cache.get(image)
    cache.set(image, to_label)
    return HttpResponse(status=204)
