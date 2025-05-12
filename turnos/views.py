import json
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def listar_turnos(request):
    ruta_json = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'turnos.jason'))
    
# Cargar turnos existentes
    try:
        with open(ruta_json, 'r') as f:
            turnos = json.load(f)
    except FileNotFoundError:
        turnos = []
        
# Procesar formulario si se envió
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            hora_a_eliminar = request.POST.get('eliminar')
            turnos = [t for t in turnos if t['hora'] != hora_a_eliminar]
        else:
            hora = request.POST.get('hora')
            disponibles = request.POST.get('disponibles')
            if hora and disponibles:
                try:
                    nuevo = {
                        "hora": hora,
                        "disponibles": int(disponibles)
                    }
                    turnos.append(nuevo)
                except ValueError:
                    pass
            
        with open(ruta_json, 'w') as f:
            json.dump(turnos, f, indent=2)
        
        return redirect('/')
                             
    return render(request, 'turnos/index.html', {'turnos': turnos})
