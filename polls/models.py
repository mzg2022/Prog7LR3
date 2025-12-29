from django.db import models
import datetime
from django.utils import timezone

# Модель Вопрос (Question) - хранит вопросы для голосования
class Question(models.Model):
    # Поле для текста вопроса, максимум 200 символов
    question_text = models.CharField(max_length=200)
    
    # Поле для даты публикации с понятным названием 'date published'
    pub_date = models.DateTimeField('date published')
    
    # Метод для красивого отображения объекта
    def __str__(self):
        return self.question_text
    
    # Дополнительный метод: был ли вопрос опубликован недавно (за последние сутки)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# Модель Вариант ответа (Choice) - связана с Question
class Choice(models.Model):
    # Внешний ключ: каждый Choice относится к одному Question
    # on_delete=models.CASCADE - если удалить вопрос, удалятся все варианты ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    # Текст варианта ответа
    choice_text = models.CharField(max_length=200)
    
    # Количество голосов за этот вариант, по умолчанию 0
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text