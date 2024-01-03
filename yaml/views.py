from django.shortcuts import render
from iommi import Page, html, Table, Action, Column
from .models import Intent, Bot, Response


class IndexPage(Page):
    title = html.h1("Chatbot Management")
    welcome_text = 'Create intent, response, and stories'

    Intent = Table(
        auto__model=Intent, 
        columns__name__filter__include=True,
        actions__create_intent=Action(
            attrs__href='/io-intent/'
),
columns__edit=Column.edit(
    after=0,
    include=lambda request, **_: request.user.is_staff,
),
columns__delete=Column.delete(
    include=lambda request, **_: request.user.is_staff,
),
)
    
