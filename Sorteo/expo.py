import random
import os

# Lista de alumnos con sus nombres
alumnos = {
    '01': 'Carlos Alonso',
    '02': 'Samuel Barahoma',
    '03': 'Eduardo Corpa',
    '04': 'Hugo de Argila',
    '05': 'Alvaro Díez',
    '06': 'Sergio Ferreras',
    '07': 'Marta Fraile',
    '08': 'Roberto García',
    '09': 'Daniel García',
    '10': 'Pablo A Herrera',
    '11': 'Victor Hervás',
    '12': 'Andy (Tsuen Kit Lui)',
    '13': 'Miguel Marañón',
    '14': 'Mario Martín',
    '15': 'Daniel Mellado',
    '16': 'Hugo Moreno',
    '17': 'Leonardo David',
    '18': 'Javier Pérez',
    '19': 'Sergio Pulido',
    '20': 'Alejandro Rodriguez',
    '21': 'David Rubio',
    '22': 'Mario Santana',
    '23': 'Daniel Serrano',
    '24': 'Sergio Simón',
    '25': 'Christian Teruel'
}

# Preguntar por la fecha de hoy
fecha_hoy = input("Introduce la fecha de hoy (dd-mm-yyyy): ")

# Leer los expositores anteriores desde el archivo (si existe)
expositores_anteriores = set()

if os.path.exists("expositores.txt"):
    with open("expositores.txt", "r") as f:
        for linea in f:
            if " - " in linea:  # Buscar líneas que contienen expositores anteriores
                nombre = linea.strip().split(" - ")[1]  # Extraer el nombre del expositor
                expositores_anteriores.add(nombre)

# Filtrar los alumnos que no han sido expositores anteriormente
alumnos_disponibles = {numero: nombre for numero, nombre in alumnos.items() if nombre not in expositores_anteriores}

# Verificar si hay suficientes alumnos disponibles
if len(alumnos_disponibles) < 5:
    print("No hay suficientes alumnos disponibles que no hayan sido expositores anteriormente.")
else:
    # Seleccionar aleatoriamente cinco alumnos
    expositores_de_hoy = random.sample(list(alumnos_disponibles.values()), 5)

    # Imprimir los expositores seleccionados
    print(f"Los expositores del día de hoy {fecha_hoy} son: {', '.join(expositores_de_hoy)}")

    # Guardar los expositores de hoy en el archivo expositores.txt
    with open("expositores.txt", "a") as f:
        f.write(f"\nExpositores del día {fecha_hoy}:\n")
        for expositor in expositores_de_hoy:
            numero = next(num for num, nombre in alumnos.items() if nombre == expositor)
            f.write(f"{numero} - {expositor}\n")

    print("Expositores guardados en expositores.txt.")
