from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Turno

@login_required
def listar_turnos(request):
    turnos = Turno.objects.all()
    
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            hora = request.POST.get('eliminar')
            Turno.objects.filter(hora=hora).delete()
        else:
            hora = request.POST.get('hora')
            disponibles = request.POST.get('disponibles')
            
            if hora and disponibles:
                Turno.objects.create(
                    hora=hora,
                    disponibles=int(disponibles)
                )
                
        return redirect('/')
    
    return render(request, 'turnos/index.html',{'turnos': turnos})
