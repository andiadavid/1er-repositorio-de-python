import string
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
#funciones 
def generar_estructura(nombres,notas_1,notas_2):
    """genero un diccionario relacionando el estudiante con sus notas .
        Primero hago un zip de las tres listas y despues genero un diccionario
        que tenga como clave el nombre del estudiante,(los nombres y las notas 
        ya estan ordenados como corresponden, ademas los nombres no se repiten)"""
    nombres=nombres.strip().replace("'","").replace(" ","").replace("\n","").split(',')
    tupla_para_dict=zip(nombres,notas_1,notas_2)
    estudiantes={nombre: (nota_1,nota_2) for nombre, nota_1, nota_2 in tupla_para_dict}
    return estudiantes

def calcular_prom(estudiantes):
    """calcula el promedio de cada estudiante sumando las notas de cada uno y 
        dividiendolas por la cantidasd de notas, para esto utilizo en -map- que 
        aplica la funcion lambda a cada elemento de la estructura"""
    prom_estudiantes=dict(map(lambda estu: (estu[0], (sum(estu[1]))/2), estudiantes.items()) )
    return prom_estudiantes

def calcular_prom_general(promedio):
    """calculo el promedio general de todos los estudiantes sumando los values(nota_promedio x estudiante)
        y lo divido por la vantidad de estudiantes """
    return sum(promedio.values())/len(promedio.values())

def calcular_prom_alto(promedio_est):
    """calculo el maximo de los promedios de los estudiantes(campo[1])del diccionario y
        de ese maximo me quedo con la key(campp[0]) que es el nombre del estudiante con la nota mas alta"""
    return max(promedio_est.items(),key=lambda x: x[1])[0]

def calcular_nota_bajo(estudiantes):
    """calculo y retorno al estudiante con la nota mas baja ,logica igual a la funcion -prom_alto- pero 
    se recibe como parametro la estrucctura que contiene las notas y no los promedio"""
    return min(promedio_est.items(),key=lambda x: x[1])[0]

#programa principal 
estudiantes = generar_estructura(nombres,notas_1,notas_2)
promedio_est = calcular_prom(estudiantes)
promedio_general = calcular_prom_general(promedio_est)
estudiante_prom_alto = calcular_prom_alto(promedio_est)
estudiante_nota_bajo = calcular_nota_bajo(estudiantes)
print(estudiantes)
print(promedio_est)
print(promedio_general)
print(estudiante_prom_alto)
print(estudiante_nota_bajo)
