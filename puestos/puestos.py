import random
from datetime import datetime

# Lista de alumnos del 01 al 25
alumnos = [f'{i:02}' for i in range(1, 26)]

# Lista de ordenadores T07-01 al T07-25
ordenadores = [f'T07-{i:02}' for i in range(1, 26)]

# Preguntar por la fecha de hoy
fecha_hoy = input("Introduce la fecha de hoy (dd-mm-yyyy): ")

# Asignar aleatoriamente un ordenador a cada alumno
random.shuffle(ordenadores)

# Crear las asignaciones
asignaciones = {}
for i, alumno in enumerate(alumnos):
    asignaciones[alumno] = ordenadores[i]

# Imprimir las asignaciones
print(f"Asignaciones para el día {fecha_hoy}:")
for alumno, ordenador in asignaciones.items():
    print(f"Alumno {alumno}: {ordenador}")

# Guardar las asignaciones en un fichero asignados.txt
with open("asignados.txt", "a") as f:
    f.write(f"\nAsignaciones del día {fecha_hoy}:\n")
    for alumno, ordenador in asignaciones.items():
        f.write(f"Alumno {alumno}: {ordenador}\n")

print("Asignaciones guardadas en asignados.txt.")
