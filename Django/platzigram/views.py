from django.http import HttpResponse,JsonResponse
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi! Current server time is {now}'.format(now=str(now)))

def order_int(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to Platzigram'.format(name)
    return HttpResponse(message)
