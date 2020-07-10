from django.urls import path
from .views import index, update_task

urlpatterns = [
    path('', index, name='list'),
    path('update_task/<str:pk>/', update_task, name='update_task')
]
