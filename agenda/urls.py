from django.urls import path
from .views import AtividadeListCreate, AtividadeRetrieveDestroy, index

urlpatterns = [
    path('atividades/', AtividadeListCreate.as_view(), name='atividade-list-create'),
    path('atividades/<int:pk>/', AtividadeRetrieveDestroy.as_view(), name='atividade-detail-delete'),
    path('', index, name='index'),
]