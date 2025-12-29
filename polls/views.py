from django.utils import timezone
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Общее представление для главной страницы (список вопросов)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'  # Используем наш шаблон
    context_object_name = 'latest_question_list'  # Имя переменной в шаблоне
    
    def get_queryset(self):
        """
        Возвращает последние 5 опубликованных вопросов (исключая будущие).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()  # lte = less than or equal (меньше или равно)
        ).order_by('-pub_date')[:5]

# Общее представление для деталей вопроса
class DetailView(generic.DetailView):
    model = Question  # Указываем модель
    template_name = 'polls/detail.html'  # Используем наш шаблон

    def get_queryset(self):
        """
        Исключает вопросы, которые еще не опубликованы (будущие даты).
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# Общее представление для результатов
class ResultsView(generic.DetailView):
    model = Question  # Та же модель
    template_name = 'polls/results.html'  # Другой шаблон

    def get_queryset(self):
        """
        Исключает вопросы, которые еще не опубликованы (будущие даты).
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# Функция для обработки голосования
def vote(request, question_id):
    """
    Обрабатывает голосование за конкретный вариант ответа.
    Увеличивает счетчик голосов и перенаправляет на страницу результатов.
    """
    # Получаем вопрос или 404
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        # Получаем выбранный вариант из POST-данных
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Если вариант не выбран или не существует, показываем форму с ошибкой
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Вы не выбрали вариант ответа.",
        })
    else:
        # Используем F() для атомарного увеличения счетчика в базе данных
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Обновляем объект из базы, чтобы получить актуальное значение
        selected_choice.refresh_from_db()
        
        # Всегда возвращаем HttpResponseRedirect после успешной обработки POST
        # Это предотвращает повторную отправку формы при нажатии кнопки "Назад"
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
        )