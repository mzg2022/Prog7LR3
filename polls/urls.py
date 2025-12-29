from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # Главная страница: /polls/
    path('', views.IndexView.as_view(), name='index'),
    
    # Детали вопроса: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    # Результаты: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    
    # Голосование: /polls/5/vote/ (остается функцией, не классом)
    path('<int:question_id>/vote/', views.vote, name='vote'),
]