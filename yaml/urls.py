from django.urls import path
from iommi import Form, Table

from .models import Bot, Intent, Response, Story

urlpatterns = [
    path('io-bot/', Form.create(auto__model=Bot).as_view()),
    path('io-form/', Form.create(auto__model=Intent).as_view()),
    path('io-table/',Table(auto__model=Intent).as_view()),
]