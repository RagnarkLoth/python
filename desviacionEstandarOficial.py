import os 

listaDatos = []
nombresListas = []


#ESTA FUNCION NOS SERVIRA PARA DECLARAR LA CANTIDAD DE LISTAS A UTILIZAR EN EL PROGRAMA, EL TAMAÑO DE CADA UNA
#Y SETTEAR LOS DATOS EN CADA LISTA
def llenarLista():
    cantidadListas = int(input("Cantidad de listas a procesar o evaluar:"))
    longitudListas = int(input("Cantidad de datos de cada lista:"))
    listaIndividual = []

    for longitud in range(0, cantidadListas):
        nombresListas.append(input("Nombre de la lista " + str(longitud+1) + ":"))
    for lista in range(0,cantidadListas):
        print("============================================================")
        for longitud in range(0, longitudListas):
            dato = input("Ingrese el valor " + str(longitud+1) + " de la lista " + str(lista+1) + "-" + nombresListas[lista] + ":")
            if(dato.count('.') == 1):
                listaIndividual.append(float(dato))
            else:
                listaIndividual.append(int(dato))
        listaDatos.append(listaIndividual)

        #ESTO SIRVE PARA VACIAR LA LISTA PARA QUE LOS ELEMENTOS ANTERIORMENTE AÑADIDOS NO SE JUNTEN CON LOS NUEVOS
        listaIndividual = [] 

def promedio(listaDatos, cantidadListas):

    promedios = []
    sumatoria = 0
    for repeticiones in range(0, cantidadListas):
        for datos in listaDatos[repeticiones]:
            sumatoria += datos
        promedios.append(sumatoria/len(listaDatos[repeticiones]))
        sumatoria = 0
    
    return promedios

def desviacion(promedio, listaDatos):
    
    desviacion = []
    distanciaMedia = []
    sumatoria = 0
    for repeticiones in range(0, len(listaDatos)):
        for datos in listaDatos[repeticiones]:
            if((promedio[repeticiones]-datos) < 0):
                distanciaMedia.append((promedio[repeticiones]-datos)*-1)            
                print((promedio[repeticiones]-datos)*-1)
            else:
                distanciaMedia.append(promedio[repeticiones]-datos)
                print((promedio[repeticiones]-datos))
        for datos in distanciaMedia:
            sumatoria+=datos
        desviacion.append(sumatoria/len(distanciaMedia))
        sumatoria = 0
        distanciaMedia = []

    return desviacion

#ESTA CLASE NOS SIRVE PARA MOSTRAR LOS DATOS AL FINALIZAR
def mostrarDatos(listaDatos, nombreDatos, promedio, desviacion):
    print("============================================================")
    print("Resultados:")
    for indice in range(0, len(listaDatos)):
        print("Lista " + str(nombreDatos[desviacion.index(sorted(desviacion)[indice])]) + " presenta una media de " + str(promedio[desviacion.index(sorted(desviacion)[indice])]) + " y una desviacion con respecto a la media de " + str(desviacion[desviacion.index(sorted(desviacion)[indice])]))
        print("Esto es producto de los siguientes datos: ")
        for datos in listaDatos[desviacion.index(sorted(desviacion)[indice])]:
            print(datos, end=", ")
        print(" ") 

    pregunta = input("¿Quieres continuar Sí/No?")
    return pregunta.lower()

def informacion():
    print("Programa para clasificar listas de datos mediante desviaciones con respecto a la media, ingrese los siguientes datos:")
    print("==========================================================")
    print("OPCIONES: ")
    print("NUMERO 1: Ingresar al sistema")
    print("NUMERO 2: Limpiar pantalla")
    print("NUMERO 3: Salir del sistema")
    opcion = int(input("Por favor, escoge solo el numero: "))

    return opcion

def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def despedida():
    print("Gracias por utilizarme, vuelva pronto. :)")


while True:
    resultado = informacion()
    if resultado == 3:
        despedida()
        break
    elif resultado == 2:
        limpiarConsola()
    elif resultado == 1:
        llenarLista()
        if mostrarDatos(listaDatos, nombresListas, promedio(listaDatos, len(listaDatos)),desviacion(promedio(listaDatos, len(listaDatos)), listaDatos)) == "si":
            pass
        else:
            despedida()
            break


