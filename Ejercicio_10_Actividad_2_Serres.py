nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

# Inciso A
def generar_estructura(nombres, notas_1, notas_2):
    """ Esta función genera una estructura que asocia a múltiples alumnos con sus notas. 
        Recibe 3 parámetros, una cadena de strings, y dos listas con notas.
        Retorna un diccionario."""
    
    nombres_de_alumnos = nombres.replace(" ", "").replace("'", "").replace("\n", "").split(",")  
    alumnos = {nombre:[nota_1, nota_2] for nombre, nota_1, nota_2 in zip (nombres_de_alumnos, notas_1, notas_2)}
    return alumnos

# Inciso B
def calcular_promedio_por_estudiante (alumnos):
    """ Esta función devuelve un diccionario que contiene el promedio de notas de cada alumno a partir de un diccionario que relaciona a un alumno con sus notas"""

    promedio = {}
    for elem in alumnos:
        promedio[elem] = sum(alumnos[elem])/len(alumnos[elem]) if (len(alumnos[elem]) > 0) else -1
    return promedio

# Inciso C
def calcular_promedio_del_curso (promedio_por_estudiante):
    """ A partir de la estructura que contiene el promedio de cada alumno, devuelve el promedio de notas de todo el curso (numero real)"""

    promedio = sum(promedio_por_estudiante.values()) / len(promedio_por_estudiante) if (len(promedio_por_estudiante) > 0) else -1
    return promedio

# Inciso D
def calcular_mayor_promedio (promedio_por_estudiante):
    """ A partir de la estructura que contiene el promedio de cada estudiante, devuelve el nombre del alumno con el mayor promedio"""

    mayor = max(promedio_por_estudiante.items(), key=lambda x: x[1])[0]
    return mayor

# Inciso E
def calcular_menor_nota (alumnos):
    """ A partir de un diccionario cuyas claves son los nombres de los alumnos y sus valores son listas con las notas, devuelve el nombre del alumno con menor nota"""

    minimo = min(alumnos.items(), key = lambda x: min(x[1]))[0]
    return minimo


alumnos = generar_estructura(nombres, notas_1, notas_2)
promedio_por_estudiante = calcular_promedio_por_estudiante(alumnos)
promedio_del_curso = calcular_promedio_del_curso(promedio_por_estudiante)
mayor_promedio = calcular_mayor_promedio(promedio_por_estudiante)
menor_nota = calcular_menor_nota(alumnos)

print(f"La estructura generada es : {alumnos}")
print(f"La estructura que relaciona cada estudiante con su promedio es: {promedio_por_estudiante}")
print(f"La nota promedio del curso es: {promedio_del_curso}")
print(f"El alumno con mayor promedio es: {mayor_promedio}")
print(f"Y el alumno con la nota mas baja es: {menor_nota}")

