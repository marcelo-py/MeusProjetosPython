from django.shortcuts import render
from .func_cpf_gerador import gerar_cpf

def index(request):
    if request.method == 'POST':
        gera_quant = request.POST.get('quant_cpfs')
        gerados = gerar_cpf(quant=gera_quant)

        return render(request, 'index.html', {
            'gerados': gerados
        })
    return render(request, 'index.html',)

