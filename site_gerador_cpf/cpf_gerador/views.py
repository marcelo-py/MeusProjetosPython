from django.shortcuts import render, redirect
from .func_cpf_gerador import gerar_cpf

def index(request):
    if request.method != 'POST':
        return render(request, 'index.html', {
            'gerados': [],
        })


    gera_quant = request.POST.get('quant_cpfs')
    postar_no_arq = bool(request.POST.get('criar_arq'))
    postar = False
    print(postar_no_arq, '<<<<<<<<<<<<<<<')
    gerados = gerar_cpf(quant=gera_quant)

    return render(request, 'index.html', {
        'gerados': gerados
    })
    

