from django.shortcuts import render, get_object_or_404, redirect
from .models import Eventos
from .forms import EventosForm

''' 
from  django.views.generic import ListView
from .models import Eventos

class EventoListView(ListView):
    model = Eventos
'''
# Create your views here.

def home(request):
    #onde vai ficar a lista de eventos
    eventos = Eventos.objects.all()
    return render(request, r'.\home.html', {'eventos': eventos})

def detalhes(request, evento_id):
    evento = get_object_or_404(Eventos, id=evento_id)
    print(evento)
    return render(request, r'.\detalhes.html', {'evento': evento})



def cadastro_evento(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventosForm()
    return render(request, r'.\cadastro_evento.html', {'form': form})
