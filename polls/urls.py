from django.urls import path
from . import views  # импортируем наши views из текущей папки

# urlpatterns - список маршрутов (URL-адресов)
urlpatterns = [
    # path("", ...) - главная страница приложения polls
    path("", views.index, name="index"),
    # "" - означает "polls/" (будет подключено к основному проекту)
    # views.index - функция, которая обработает запрос
    # name="index" - имя маршрута для удобства
]