from django.shortcuts import render
from rest_framework import generics
from .models import Atividade
from .serializers import AtividadeSerializer

class AtividadeListCreate(generics.ListCreateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class AtividadeRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

def index(request):
    return render(request, "index.html")