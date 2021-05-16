from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Automato, Maquina, Expressao
from .forms import SequenciaForm, AutomatoForm, MaquinaForm, ExpressaoForm


def index(request):
    return render(request, 'computacao/index.html')





def automato(request, automato_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Automato.objects.get(id=automato_id).valida_sequencia(sequencia)

    context = {
        'automato': Automato.objects.get(id=automato_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/automato.html', context)


def automatos(request):

    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)


def novo_automato(request):

    form = AutomatoForm(request.POST or None)
    if form.is_valid():
        new_automata = form.save()
        new_automata.desenha_diagrama()
        new_automata.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    context = {'form': form}

    return render(request, 'computacao/novo_automato.html', context)


def edita_automato(request, automato_id):


    instance = Automato.objects.get(id=automato_id)
    form = AutomatoForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))


    context = {'form': form, 'automato_id':automato_id}
    return render(request, 'computacao/edita_automato.html', context)

def apaga_automato(request, automato_id):
    Automato.objects.filter(id=automato_id).delete()
    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)






def MaquinaTuring(request):
    context = {'MaquinaTuring': Maquina.objects.all()}
    return render(request, 'computacao/MaquinaTuring.html', context)




def DetalhesMaquina(request, maquina_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Maquina.objects.get(id=maquina_id).valida_sequencia(sequencia)

    context = {
        'maquina': Maquina.objects.get(id=maquina_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/DetalhesMaquina.html', context)



def NovaMaquina(request):

    form = MaquinaForm(request.POST or None)
    if form.is_valid():
        new_maquina = form.save()
        new_maquina.desenha_diagrama()
        new_maquina.save()
        return HttpResponseRedirect(reverse('computacao:MaquinaTuring'))

    context = {'form': form}

    return render(request, 'computacao/NovaMaquina.html', context)



def EditarMaquina(request, maquina_id):

    instance = Maquina.objects.get(id=maquina_id)
    form = MaquinaForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:MaquinaTuring'))

   
    context = {'form': form, 'maquina_id':maquina_id}
    return render(request, 'computacao/EditarMaquina.html', context)


def ApagaMaquina(request, maquina_id):
    Maquina.objects.filter(id=maquina_id).delete()
    context = {'MaquinaTuring': Maquina.objects.all()}
    return render(request, 'computacao/MaquinaTuring.html', context)





def ExpressoesRegulares(request):
    context = {'ExpressoesRegulares': Expressao.objects.all()}
    return render(request, 'computacao/ExpressoesRegulares.html', context)

def NovaExpressao(request):
    form = ExpressaoForm(request.POST or None)
    if form.is_valid():
        NovaExpressao = form.save()
        NovaExpressao.save()
        return HttpResponseRedirect(reverse('computacao:ExpressoesRegulares'))
    context = {'form': form} 
    return render(request, 'computacao/NovaExpressao.html', context)

def EditarExpressao(request, expressao_id):
    instance = Expressao.objects.get(id-expressao_id)
    form = ExpressaoForm(request.POST or None, instance-instance)
    if form.is_valid():
        e = form.save()
        e.save()
        return HttpResponseRedirect(reverse('computacao:ExpressoesRegulares'))
    context = {'form': form, 'expressao.id':expressao_id}
    return render(request, 'computacao/EditarExpressao.html', context)

def ApagaExpressao(request, expressao_id):
    Expressao.objects.filter(id=expressao_id).delete()
    context = {'ExpressoesRegulares': Expressao.objects.all()}
    return render(request, 'computacao/ExpressoesRegulares.html', context)

def DetalhesExpressao(request, expressao_id):
    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Expressao.objects.get(id=expressao_id).valida_sequencia(sequencia)

    context = {
        'expressao': Expressao.objects.get(id=expressao_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/DetalhesExpressao.html', context)