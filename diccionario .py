perro = {}
print("lista vacia",perro)
perro2={ "nombre": "firulais",
        "color": "blanco",
        "raza": "criollo",
        "patas": 4,
        "edad": 8
}
print("datos del perro", perro2)
estudiante = {
    "nombre": "geampierre",
    "apellido": "deuloufeut hoyos",
    "sexo": 'Masculino',
    "edad": 18,
    "estado civil": 'Soltero',
    "habilidades": ["correr rapido", "mucha fuerza","bueno en las matematicas"],
    "país": "colombia",
    "ciudad": "cartagena de indias",
    "dirección": "villas de la candelaria mz39 lt23"}
print("datos estudiante",estudiante)

estudiantes1 = len(estudiante)
print("Longitud del diccionario del estudiante:",estudiantes1)
habilidades = estudiante["habilidades"]
print("Habilidades del estudiante:", habilidades)
print("Tipo de datos de habilidades:", type(habilidades))

estudiante["habilidades"].extend(["Comunicación", "friba optica","bueno en el futbol"])
claves = list(estudiante.keys())
print("Claves del diccionario del estudiante:", claves)

valor = list(estudiante.values())
print("Valores del diccionario del estudiante:", valor)

lt = list(estudiante.items())
print("Diccionario del estudiante como lista de tuplas:", lt)

del estudiante['edad']
print("Diccionario del estudiante después de eliminar 'edad':", estudiante)

lista1 = []
lista1.append(estudiante)
print("Lista de diccionarios:", lista1)
