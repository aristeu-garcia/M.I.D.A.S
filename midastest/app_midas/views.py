from django.http import JsonResponse

def HealthCheck(request):
    return JsonResponse({'message': 'ok'})
