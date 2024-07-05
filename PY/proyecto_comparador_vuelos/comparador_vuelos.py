from random import randint
# aquí se crean los paises, los precios se almacenan en diccionarios y se generan aleatoriamente
argentina = {1: randint(600, 1150), 2: randint(600, 1150), 3: randint(600, 1150)}
brasil = {1: randint(750, 1375), 2: randint(750, 1375), 3: randint(750, 1375)}
bolivia = {1: randint(500, 980), 2: randint(500, 980), 3: randint(500, 980)}
canada = {1: randint(700, 1300), 2: randint(700, 1300), 3: randint(700, 1300)}
chile = {1: randint(700, 1100), 2: randint(700, 1100), 3: randint(700, 1100)}
colombia = {1: randint(600, 900), 2: randint(600, 900), 3: randint(600, 900)}
ecuador = {1: randint(500, 820), 2: randint(500, 820), 3: randint(500, 820)}
usa = {1: randint(850, 1300), 2: randint(850, 1300), 3: randint(850, 1300)}
guatemala = {1: randint(300, 500), 2: randint(300, 500), 3: randint(300, 500)}
honduras = {1: randint(320, 550), 2: randint(320, 550), 3: randint(320, 550)}
mexico = {1: randint(450, 890), 2: randint(450, 890), 3: randint(450, 890)}
nicaragua = {1: randint(450, 600), 2: randint(450, 600), 3: randint(450, 600)}
panama = {1: randint(490, 760), 2: randint(490, 760), 3: randint(490, 760)}
uruguay = {1: randint(815, 1225), 2: randint(815, 1225), 3: randint(815, 1225)}
# aquí se guardan las variables de los paises
lista_precio_pais = [argentina, brasil, bolivia, canada, chile, colombia, ecuador, usa, guatemala, honduras, mexico,
                     nicaragua, panama, uruguay]
# aquí se crea una lista con los nombres de los países
lista_paises = ["Argentina", "Brasil", "Bolivia", "Canada", "Chile", "Colombia", "Ecuador", "Estados Unidos",
                "Guatemala", "Honduras", "México", "Nicaragua", "Panamá", "Uruguay"]

def nombre_usuario(usuario):
    print(f"Saludos {usuario}, mucho gusto.\n")

def mostrar_paises():
    print("Los países con vuelos disponibles son: ")
    # se abre el archivo con los nombres de los países y los lee
    with open("TXT/paises.txt", "r") as paises:
        print(paises.read())

def comparacion_precios(opcion, lista_paises, lista_precio_pais):
    # Aquí se almacenará el nombre del país elegido
    pais = ""
    # Aquí se almacenarán los precios del país elegido
    precio_pais = ""
    for x in range(0, opcion):
        pais = lista_paises[x]
        precio_pais = lista_precio_pais[x]
    # aquí se imprimirá el nombre del país elegido
    print(f"\nEl país elegido es: {pais}")
    # aquí se imprimirán los precios del país elegido
    #print(f"Los precios del país elegido son: {precio_pais.values()}")
    print("Hay 3 aerolíneas con vuelos disponibles:")
    print(f"1. Horizontes Altos ${precio_pais[1]} USD\n"
          f"2. Vuelos Especiales ${precio_pais[2]} USD\n"
          f"3. Vuelos Meridiano ${precio_pais[3]} USD")

    if precio_pais[1] < precio_pais[2] and precio_pais[1] < precio_pais[3]:
        print(f"\nEl precio más bajo es el de Horizontes Altos con ${precio_pais[1]} USD")
    elif precio_pais[2] < precio_pais[1] and precio_pais[2] < precio_pais[3]:
        print(f"\nEl precio más bajo es el de Vuelos Especiales con ${precio_pais[2]} USD")
    elif precio_pais[3] < precio_pais[1] and precio_pais[3] < precio_pais[2]:
        print(f"\nEl precio más bajo es el de Vuelos Meridiano con ${precio_pais[3]} USD")
    else:
        print(f"\nHay más de un precio menor {usuario}!")

while True:
    respuesta = input("\n¿Te gustaría viajar?: ").title()

    if respuesta == "Si":

        usuario = input("Hola ¿Cuál es tu nombre?: ").title()
        nombre_usuario(usuario)

        mostrar_paises()

        print("Ingresa el número del país al que te interese viajar")
        print("#NOTA SI INGRESAS UN DECIMAL SE TOMARA SOLO EL VALOR ENTERO")

        while True:
            try:
                opcion = int(float(input()))

                if opcion < 1 or opcion > len(lista_paises):
                    print(f"\nEl número ingresado {usuario} no es válido, intenta de nuevo: ")
                else:
                    break

            except ValueError:
                print(f"\nHa habido un problema {usuario}!, solo puedes ingresar números\nIntenta de nuevo: \n")

        comparacion_precios(opcion, lista_paises, lista_precio_pais)

    elif respuesta == "No":
        print("\nMuchas Gracias, regresa cuando puedas")
        break
    else:
        print("\nOpción no valida\n")
