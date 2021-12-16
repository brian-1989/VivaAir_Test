from django.core.cache import cache
from django.http import JsonResponse
from stories_app.help_functions import history_api, id_api
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api(request):
    """ This function analyzes the API request in three ways: 1. Analyzes
    if the information is cached, 2. it analyzes if the parameters come in
    the body of the URL or 3. it analyzes if the parameters come in Json type.
    If the information is correct, it queries the hacker-news APIs and the
    information is cached for 10 seconds.

    Return: A list of stories, each story is in dictionary format, with id
    and title fields. Otherwise, a 400 error

    """
    # Condition to check if the information is save in cache
    if cache.get('main_id') and cache.get('stories'):
        return JsonResponse(cache.get('stories'), safe=False)
    else:
        # Condition to check if the information is in JSON type
        data_json = request.data
        if not data_json:
            # Conditions to check if the information is in the body of the URL
            if not request.GET.get('i'):
                error_text = 'Missing i'
                return Response(error_text, status=status.HTTP_400_BAD_REQUEST)
            elif not request.GET.get('n'):
                error_text = 'Missing n'
                return Response(error_text, status=status.HTTP_400_BAD_REQUEST)
            else:
                ids = id_api(request.GET.get('i'), request.GET.get('n'))
        else:
            ids = id_api(data_json['i'], data_json['n'])
        # Stores ID information
        cache.set('main_id', ids, 10)
        stories = history_api(ids)
        # Stores stories with ID and title fields
        cache.set('stories', stories, 10)
        return JsonResponse(stories, safe=False)

