from django.http import JsonResponse


def json404(request):
    """Return a JSON 404 instead of Django's default HTML 404.
    """
    error = {'detail': 'Not found.'}
    return JsonResponse(error)
