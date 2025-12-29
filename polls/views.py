from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    """
    Главная страница приложения polls.
    Показывает 5 последних вопросов, отсортированных по дате публикации (новые сначала).
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Передаем список вопросов в шаблон
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    Страница с деталями конкретного вопроса.
    Показывает текст вопроса и все варианты ответов.
    Если вопрос не существует - возвращает ошибку 404.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Страница с результатами голосования для конкретного вопроса.
    Показывает количество голосов за каждый вариант.
    """
    return HttpResponse(f"Вы смотрите результаты вопроса {question_id}.")

def vote(request, question_id):
    """
    Обрабатывает голосование за конкретный вариант ответа.
    Принимает POST-запрос с выбранным вариантом.
    """
    return HttpResponse(f"Вы голосуете за вопрос {question_id}.")