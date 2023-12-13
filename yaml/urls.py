from django.urls import path
from iommi import Form, Table
from .views import IndexPage
from .models import Bot, Intent, Response, Story

urlpatterns = [
    path('', IndexPage().as_view()),
    path('io-bot/', Form.create(auto__model=Bot).as_view()),
    path('io-form/', Form.create(auto__model=Intent).as_view()),
    path('io-resp/', Form.create(auto__model=Response).as_view()),
    path('io-table/',Table(auto__model=Intent).as_view()),
]