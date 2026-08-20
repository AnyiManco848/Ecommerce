import json

# Inventory inicial
inventory = {
    "products": []
}

# Función para agregar products
def add_product(nombre, cantidad, precio):
    product = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventory["products"].append(product)

# Adds products
add_product("Lapiz", "5", 1500)
add_product("Calculadora", "5", 25000)
add_product("Cuaderno", "5", 8000)


# Mostrar el JSON
print(json.dumps(inventory, indent=4, ensure_ascii=False))