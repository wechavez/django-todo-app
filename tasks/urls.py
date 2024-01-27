from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='index'),
    path('complete/<int:id>', views.complete),
    path('delete/<int:id>', views.delete),
]
