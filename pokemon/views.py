from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Pokemon
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def get_pokemon(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user = User.objects.get(username=username)
        pokemon = Pokemon.objects.filter(user=user)
        return HttpResponse(serializers.serialize("json", pokemon), content_type="application/json")
    else:
        return JsonResponse({'status': 'failed', 'message': 'Method not allowed'})
   
@csrf_exempt
def create_pokemon(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        if user is None:
            return JsonResponse({'status': 'failed', 'message': 'User not found'})
        name = request.POST.get('name')
        level = request.POST.get('level')
        if level is None:
            return JsonResponse({'status': 'failed', 'message': 'Level is required'})
        element_type = request.POST.get('element_type')
        Pokemon.objects.create(name=name, level=level, element_type=element_type, user=user)
        return JsonResponse({'status': 'success', 'message': 'Pokemon created successfully'})
    else:
        return JsonResponse({'status': 'failed', 'message': 'Method not allowed'})
