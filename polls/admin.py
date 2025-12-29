from django.contrib import admin
from .models import Question  # Импортируем нашу модель Question

# Регистрируем модель Question в админ-панели
# Теперь вопросы будут отображаться в админке
admin.site.register(Question)