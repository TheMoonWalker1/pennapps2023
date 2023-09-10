from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .realtime import get_data

# Create your views here.
@api_view(('POST',))
def ajax(request):
    if request.method == 'POST':
        # Assuming the latitude and longitude are sent in the request's POST data
        try:
            data = json.loads(request.body.decode('utf-8'))
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            # Perform your processing with latitude and longitude here
            # For example, you can save them to a model or perform some calculations

            response_data = {
                'message': 'Location data received and processed successfully.',
                'latitude': latitude,
                'longitude': longitude,
                'swe': str(abs(float(get_data(longitude, latitude))))
            }
            print(response_data)
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})