from django.http import HttpResponse

def index(request):
    # Эта функция обрабатывает запрос и возвращает ответ
    return HttpResponse("Hello, world. You're at the polls index.")