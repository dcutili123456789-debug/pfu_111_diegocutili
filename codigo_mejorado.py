print("=== REGISTRO DE PEDIDOS ===")

producto = input("Nombre del producto: ")
while producto == "":
    print("Error: el nombre no puede estar vacío.")
    producto = input("Nombre del producto: ")

cantidad = int(input("Cantidad solicitada: "))
while cantidad <= 0:
    print("Error: la cantidad debe ser mayor que cero.")
    cantidad = int(input("Cantidad solicitada: "))

precio = float(input("Precio unitario: "))
while precio <= 0:
    print("Error: el precio debe ser mayor que cero.")
    precio = float(input("Precio unitario: "))

descuento = float(input("Porcentaje de descuento (0-100): "))
while descuento < 0 or descuento > 100:
    print("Error: el descuento debe estar entre 0 y 100.")
    descuento = float(input("Porcentaje de descuento (0-100): "))

total = cantidad * precio
total = total - (total * descuento / 100)

print("Producto:", producto)
print("Cantidad:", cantidad)
print("Total a pagar:", total)

print("¿Desea confirmar el pedido?")
print("1. Sí")
print("2. No")
opcion = int(input("Opción: "))
while opcion != 1 and opcion != 2:
    print("Error: opción no válida. Ingrese 1 o 2.")
    opcion = int(input("Opción: "))

if opcion == 1:
    print("Pedido confirmado.")
else:
    print("Pedido cancelado.")

print("Proceso finalizado.")
