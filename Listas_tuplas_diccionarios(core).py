#1. Carga de Datos
#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
#«producto»: una cadena de texto que represente el nombre del producto vendido.
#«cantidad»: un número entero que represente la cantidad de productos vendidos.
#«precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {"fecha": "2024-03-06", "producto": "Libro", "cantidad": 5, "precio": 8.54},
    {"fecha": "2023-05-03", "producto": "Notebook", "cantidad": 10, "precio": 125.64}, 
    {"fecha": "2023-09-10", "producto": "Televisor", "cantidad": 32, "precio": 800.34},
    {"fecha": "2024-10-12", "producto": "Monitor", "cantidad": 7, "precio": 547.23}
]
print(ventas)

#Cálculo de Ingresos Totales:
#Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. 
# Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.
Ingresos_totales = 0
for i in ventas:
    Ingresos = (i["cantidad"] * i["precio"])
    Ingresos_totales += Ingresos
print(Ingresos_totales)

#Análisis del Producto Más Vendido:
#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
ventas_por_producto = {}
for i in ventas:
    if i["producto"] in ventas_por_producto:
        ventas_por_producto[i["producto"]] += i["cantidad"]
    else:
        ventas_por_producto[i["producto"]] = i["cantidad"]
print(ventas_por_producto)

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get) #la funcion ,max() con key=.get() permite seleccionar el producto que tiene la mayor cantidad de ventas.
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]
print("El producto más vendido es: \n", producto_mas_vendido, "con", cantidad_mas_vendida, "unidades")

#Promedio de Precio por Producto:
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener
# dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
ventas = [
    {"fecha": "2024-03-06", "producto": "Libro", "cantidad": 5, "precio": 8.54},
    {"fecha": "2023-05-03", "producto": "Notebook", "cantidad": 10, "precio": 125.64}, 
    {"fecha": "2023-09-10", "producto": "Televisor", "cantidad": 32, "precio": 800.34},
    {"fecha": "2024-10-12", "producto": "Monitor", "cantidad": 7, "precio": 547.23}
]
precios_por_producto = {}
for i in ventas:
    producto = i["producto"]
    cantidad = i["cantidad"]
    precio_total_venta = i["cantidad"] * i["precio"] 
    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + precio_total_venta,
            precios_por_producto[producto][1] + cantidad
        )
    else:
        precios_por_producto[producto] = (precio_total_venta, cantidad)
print(precios_por_producto)
#precio promedio de venta para cada producto
for i in precios_por_producto:
    print(i, ":", precios_por_producto[i][0] / precios_por_producto[i][1])

#Ventas por Día:
#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
ventas = [
    {"fecha": "2024-03-06", "producto": "Libro", "cantidad": 5, "precio": 8.54},
    {"fecha": "2023-05-03", "producto": "Notebook", "cantidad": 10, "precio": 125.64}, 
    {"fecha": "2023-09-10", "producto": "Televisor", "cantidad": 32, "precio": 800.34},
    {"fecha": "2024-10-12", "producto": "Monitor", "cantidad": 7, "precio": 547.23}
]
ingresos_por_dia = {}
for i in ventas:
    fechas = i["fecha"]
    cantidad = i["cantidad"]
    precio = i["precio"]
    if fechas in ingresos_por_dia:
        ingresos_por_dia[fechas] += cantidad * precio
    else:
        ingresos_por_dia[fechas] = cantidad * precio
print(ingresos_por_dia)

#Representación de Datos:
#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean 
# diccionarios anidados. Cada diccionario anidado debe contener:
#«cantidad_total»: la cantidad total vendida del producto.
#«ingresos_totales»: los ingresos totales generados por la venta del producto.
#«precio_promedio»: el precio promedio de venta del producto.
resumen_ventas = {}
for i in ventas:
    nombres = i["producto"]
    cantidad = i["cantidad"]
    precio_total_venta = i["cantidad"] * i["precio"]
    precio_promedio = precio_total_venta / cantidad
    if nombres in resumen_ventas:
        resumen_ventas[nombres]["Cantidad total"] + cantidad
        resumen_ventas[nombres]["Ingresos totales"] + precio_total_venta
        resumen_ventas[nombres]["Precio promedio"] + precio_promedio
    else:
        resumen_ventas[nombres] = (cantidad, precio_total_venta, precio_promedio)
print(resumen_ventas)

