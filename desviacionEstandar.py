
from traceback import print_tb


cantidadLista = int(input("Ingrese la cantidad de listas a crear"))
longitudLista = int(input("ingrese la cantidad de datos para cada lista"))
crearLista = []
llenarLista = []

def crear(cantidadLista, longitudLista, crearLista, llenarLista):

    for i in range(0,cantidadLista):

        for j in range(0,longitudLista):
            texto = "Coloca un numero en la lista " + str(i) + " en la posicion " + str(j)
            numero = int(input(texto))

            llenarLista.append(numero)

        crearLista.append(llenarLista)
        llenarLista=[]
    print(crearLista)    
    return crearLista

def sumar(datosLista, longitudLista):

    contador = 0
    indices = 0
    suma = 0
    sumaListas = []

    for i in range(longitudLista):
        for datos in datosLista[i]:
            suma+=datos
            contador+=1
        sumaListas.append(suma/longitudLista)
        suma = 0
    
    return sumaListas

def restar(listaDatos, listaSumatorias):
    dato = []
    sumaDatos = []
    da = 0
    i= 0
    while(i < listaSumatorias.size()):
        sumatoria = listaSumatorias[i]
        for nuevosDatos in listaDatos:
            dato.append(sumatoria - nuevosDatos)
        for nuevo in sumaDatos:
            da += nuevo
        sumaDatos.append(da)
        i+=1

    return sumaDatos



sumar(crear(cantidadLista, longitudLista, crearLista, llenarLista), longitudLista)
print(restar(crearLista, sumar(crearLista, longitudLista)))

