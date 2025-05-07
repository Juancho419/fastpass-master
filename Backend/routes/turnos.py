import json
import os

from flask import Blueprint, jsonify, request

# Se crea el blueprint
turnos_bp = Blueprint('turnos', __name__)

# Ruta del archivo de datos
archivo_turnos = os.path.join(os.path.dirname(__file__), '..', 'turnos.json')

# Cargar turnos desde el archivo
with open(archivo_turnos, 'r') as f:
    turnos_disponibles = json.load(f)
    

# Ruta GET: Ver turnos disponibles
@turnos_bp.route('/turnos', methods=['GET'])
def listar_turnos():
    return jsonify(turnos_disponibles)

# Ruta POST: Agregar un nuevo turno
@turnos_bp.route('/turnos', methods=['POST'])
def crear_turno():
    nuevo_turno = request.get_json()
    
    if not nuevo_turno or 'hora' not in nuevo_turno or 'disponibles' not in nuevo_turno:
        return jsonify({"error": "Datos inválidos. Se requiere 'hora' y 'disponibles'."}), 400
    
    if not isinstance(nuevo_turno['hora'], str) or not isinstance(nuevo_turno['disponibles'], int):
        return jsonify({"error": "Tipos incorrectos. 'hora' debe ser texto y 'disponibles' un número"}), 400

# Nuevos turnos a la lista
    turnos_disponibles.append(nuevo_turno)
        
    with open(archivo_turnos, 'w') as f:
        json.dump(turnos_disponibles, f, indent=2)
        
    return jsonify({"mensaje": "Turno agregado correctamente"}), 201

# Borrar turnos
@turnos_bp.route('/turnos/<hora>', methods=['DELETE'])
def cancelar_turno(hora):
    global turnos_disponibles
    
# Buscar si hay turno a esa hora
    turnos_filtrados = [t for t in turnos_disponibles if t['hora'] != hora]
    
    if len(turnos_filtrados) == len(turnos_disponibles):
        return jsonify({"error": f"No existe un turno a las {hora}."}), 404
    
# Actualizar la lista y se guardar el archivo
    turnos_disponibles = turnos_filtrados
    with open(archivo_turnos, 'w') as f:
        json.dump(turnos_disponibles, f, indent=2)
        
    return jsonify({"mensaje": f"Turno a las {hora} cancelado correctamente"}), 200