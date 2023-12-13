from django.shortcuts import render
from iommi import Page, html, Table, Action, Column
from .models import Intent, Bot, Response

class IndexPage(Page):
    title = html.h1('Data Management')
    welcome_text = 'Create intent, response, and stories'

    Intent = Table(
        auto__model=Intent, 
        actions__create_intent=Action(
    attrs__href='/intents/create/',
    include=lambda request, **_: request.user.is_staff,
),
columns__edit=Column.edit(
    after=0,
    include=lambda request, **_: request.user.is_staff,
),
columns__delete=Column.delete(
    include=lambda request, **_: request.user.is_staff,
),
)
    
