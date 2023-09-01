from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva
from .form import ReservaForm

# Create your views here.
def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
        form = ReservaForm()

    return render(request, 'core/form.html', {'form': form})

def reserva_listar(request):
    reservas = Reserva.objects.all()
    context ={
        'reservas':reservas
    }
    return render(request, 'core/reservas.html',context)

def reserva_detalhar(request,id):
    reserva = Reserva.objects.get(id=id)
    return render(request,'core/detalhes.html', {'reserva': reserva})

def reserva_remover(request, id):
    aluno = get_object_or_404(Reserva, id=id)
    aluno.delete()
    return redirect('reserva_listar')

def index(request):
    return render(request, 'core/index.html')

# Create your views here.
def fazer_reserva(request):
    return render(request, 'core/form.html')