from util import Buscar

personas = [
    "Ana", "Bruno", "Carla", "Diego", "Elena",
    "Fabio", "Gabriela", "Hugo", "Ines", "Juan",
    "Laura", "Marcos", "Natalia", "Oscar", "Paula",
    "Ricardo", "Sofia", "Tomas", "Valeria", "Walter"
]

buscado = input("Ingresa el nombre a buscar: ")

resultado = Buscar(personas, buscado)

if resultado:
    print("Encontrado")
else:
    print("No encontrado")
