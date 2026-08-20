import json

inventory = {
    "products": [
        {
            "nombre": "Lapiz",
            "cantidad": "5",
            "precio": 1500
        },
        {
            "nombre": "Calculadora",
            "cantidad": "5",
            "precio": 25000
          
        },
        {
            "nombre": "Cuaderno",
            "cantidad": "4",
            "precio": 8000
        }
    ]
}

# Carrito de compra
carrito = []


def comprar_products(nombre, cantidad):
    for products in inventory["products"]:

        if products["nombre"].lower() == nombre.lower():

            compra = {
                "nombre": products["nombre"],
                "cantidad": products["cantidad"],
                "precio": products["precio"],
                "cantidad": cantidad,
                "total": products["precio"] * cantidad
            }

            carrito.append(compra)

            print("Producto agregado al carrito")
            return

    print("El producto no existe")


# Realizar compras
comprar_products("Lapiz", 3)
comprar_products("Cuaderno", 2)


# Mostrar carrito
print("\n--- CARRITO DE COMPRA ---")

for producto in carrito:
    print(f"Producto: {producto['nombre']}")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Total: ${producto['total']}")
    print("------------------------")


# Calcular total de la compra
total_compra = sum(producto["total"] for producto in carrito)

print(f"TOTAL A PAGAR: ${total_compra}")