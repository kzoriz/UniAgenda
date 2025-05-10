from django.contrib import admin
from .models import Atividade

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'hora', 'status')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data', 'status')
