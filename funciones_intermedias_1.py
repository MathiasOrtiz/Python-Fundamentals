#Funciones intermedias (Core)
#Actualizar valores en diccionarios y listas
matriz = [[10, 15, 20], [3, 7, 14]]
constantes = [{"nombre": "Ricky Martin", "pais": "Puerto Rico"}, 
            {"nombre": "Chayanne", "pais": "Puerto Rico"}]

ciudades= {
    "Mexico": ["Ciudad de Mexico", "Guadalajara", "Cancun"],
    "Chile": ["Santiago", "Concepcion", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio 
# tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0]=6 
print(matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
constantes[0]["nombre"]="Enrique Martin Morales"
print(constantes)

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["Mexico"][2]="Monterrey"
print(ciudades) 

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"]=9.9355431
print(coordenadas)

#Iterar a través de una lista de diccionarios
#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios 
# y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. 
constantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
]
def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(llave, valor)
iterarDiccionario(constantes)

#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con 
# el nombre de una llave y una lista de diccionarios. La función debe imprimir 
# el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. 
def iterarDiccionario2(llave, lista):
    for i in lista:
        print(i[llave])
iterarDiccionario2("pais", constantes)

#Crea una función imprimirInformacion(diccionario) que reciba un diccionario 
# en donde los valores son listas. La función debe imprimir el nombre de cada 
# clave junto con el tamaño de su lista y seguido de esto los valores de la 
# lista para esa clave.
costa_rica = {
    "CIUDADES": ["San José", "Limón", "Cartago", "Puntarenas"],
    "COMIDAS": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
def imprimirInformacion(diccionario):
    for llave, valor in diccionario.items():
        print(len(valor), llave, valor)
imprimirInformacion(costa_rica)
