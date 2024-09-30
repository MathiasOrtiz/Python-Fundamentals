
#crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde 
# el 0 hasta el número proporcionado como entrada. Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]
def num(num):
    return [i*2 for i in range(num+1)]
Resultado = num(24)
print(Resultado)

#Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
#Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
def suma_y_resta(a,b):
    suma = a+b
    resta = a-b
    print(suma)
    return resta
resultado = suma_y_resta(35,8)
print(resultado)

#Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
#Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
def sumatoria_menos_longitud(a):
    suma = sum(a)
    longitud = len(a)
    return suma - longitud
resultado = sumatoria_menos_longitud([1, 4, 6, 8, 19, 34, 56])
print(resultado)

#Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por 
# el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz 
# que la función regrese una lista vacía.
#Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
#Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]
def valores_multiplicados_segundo(a):
    if len(a) < 2:
        return []
    else:
        segundo_numero = a[1]
        return [i*segundo_numero for i in a]
resultado = valores_multiplicados_segundo([3,5,6,8,20,34,54])
print(resultado)

#Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar 
# una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
#Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]
def valor_multiplicado_longitud(a,b):
    return [a*b for i in range (b)] #Esta es una forma de hacerlo
print (valor_multiplicado_longitud(8,4))



