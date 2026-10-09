print("=== REGISTRO DE PEDIDOS ===")

producto = input("Nombre del producto: ")
cantidad = int(input("Cantidad solicitada: "))
precio = float(input("Precio unitario: "))
descuento = float(input("Porcentaje de descuento: "))

total = cantidad * precio
total = total - (total * descuento / 100)

print("Producto:", producto)
print("Cantidad:", cantidad)
print("Total a pagar:", total)

print("¿Desea confirmar el pedido?")
print("1. Sí")
print("2. No")
opcion = int(input("Opción: "))

if opcion == 1:
    print("Pedido confirmado.")
else:
    print("Pedido cancelado.")

print("Proceso finalizado.")
