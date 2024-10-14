import random

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
    '26': 'Ana Cristina Borja'
}

# Lista de ordenadores T07-01 al T07-25
ordenadores = [f'T07-{i:02}' for i in range(1, 26)]

# Preguntar por la fecha de hoy
fecha_hoy = input("Introduce la fecha de hoy (dd-mm-yyyy): ")

# Asignar aleatoriamente un ordenador a cada alumno
random.shuffle(ordenadores)

# Crear las asignaciones
asignaciones = {}
for i, (numero, nombre) in enumerate(alumnos.items()):
    asignaciones[f'{numero} - {nombre}'] = ordenadores[i]

# Imprimir las asignaciones
print(f"Asignaciones para el día {fecha_hoy}:")
for alumno, ordenador in asignaciones.items():
    print(f"{alumno}: {ordenador}")

# Guardar las asignaciones en un fichero asignados.txt
with open("asignados.txt", "a") as f:
    f.write(f"\nAsignaciones del día {fecha_hoy}:\n")
    for alumno, ordenador in asignaciones.items():
        f.write(f"{alumno}: {ordenador}\n")

print("Asignaciones guardadas en asignados.txt.")
