from models.Guarderia import Guarderia

nombre_de_la_boa = 'Filomena'

guarderia = Guarderia()

try:
    for boa in range(0,22):
        print(guarderia.alimentar_boa(nombre_de_la_boa))
except ValueError as error:
    print(error)
