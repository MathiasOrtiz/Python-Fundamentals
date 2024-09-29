#Imprime todos los números enteros del 0 al 100
num = int
for num in range (101):
    print(num)

#Imprime todos los numeros múltiplos de 2 entre 2 y 500
num = int
for num in range (2, 501, 2):
    print(num)
    
#Imprime los números enteros del 1 al 100. Si es divisible por 5 imprime "ice ice" en vez del número. Si es divisible por 10, imprime "baby"
num = int
for num in range (1, 101):
    if num % 5 == 0 and num % 10 == 0:
        print("baby")
    elif num % 5 == 0:
        print("ice ice")
    else:
        print(num)

#Suma los números pares del 0 al 500000 e imprime la suma total
num = int
sum = 0
for num in range (0, 500001, 2):
    sum = sum + num
print(sum)

#Imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
num = int
for num in range(2024, 0, -3):
    print(num)
    
#Establece tres variables:numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los numeros enteros
# que sean multiplos de multiplo. Por ejemplo: si si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 
# 4, 6, 8, 10 (en líneas sucesivas).
numInicial = 5
numFinal = 97
multiplo = 4
for num in range (numInicial, numFinal +1):
    if num % multiplo == 0:
        print(num)
