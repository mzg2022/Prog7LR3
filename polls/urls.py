from django.urls import path
from . import views  # импортируем наши views из текущей папки

# Пространство имен приложения - важно для избежания конфликтов URL
app_name = 'polls'

# urlpatterns - список маршрутов (URL-адресов)
urlpatterns = [
    # path("", ...) - главная страница приложения polls
    path("", views.index, name="index"),
    # "" - означает "polls/" (будет подключено к основному проекту)
    # views.index - функция, которая обработает запрос
    # name="index" - имя маршрута для удобства

    # Детали вопроса: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    
    # Результаты: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    
    # Голосование: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]