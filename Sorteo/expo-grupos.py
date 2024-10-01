import random

# Listas de estudiantes por tema
digital_maturity = ['Edu', 'David', 'Roberto', 'Daniel G']
data_driven_maturity = ['Sergio P', 'Sergio F', 'Leo', 'Daniel S', 'Sergio S']
data_science_maturity = ['Christian', 'Daniel M', 'Mario S', 'Pablo', 'Mario M']
big_data_maturity = ['Andy', 'Alvaro', 'Javier P', 'Alejandro R', 'Marta']
genai_maturity = ['Hugo de Arguila', 'Miguel', 'Carlos', 'Samuel', 'Victor']

# Selección aleatoria de un estudiante de cada lista
selected_students = {
    "Digital Maturity": random.choice(digital_maturity),
    "Data Driven Maturity": random.choice(data_driven_maturity),
    "Data Science Maturity": random.choice(data_science_maturity),
    "Big Data Maturity": random.choice(big_data_maturity),
    "GenAI Maturity": random.choice(genai_maturity)
}

# Imprimir los resultados
for topic, student in selected_students.items():
    print(f"{topic}: {student}")
