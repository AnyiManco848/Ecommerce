import numpy as  np
import json

#Vector de products
products = np.array(['Lapiz', 'Libro', 'Calculadora', 'Cuaderno', 'Mochila', 'Regla', 'Borrador', 'Marcador', 'Tijeras', 'Pegamento'])    

inventory = {
    "products": products.tolist()
}

print(json.dumps(inventory, indent=4))


with open("inventory.json", "r", encoding="utf-8") as archivo:
    inventory = json.load(archivo)

print(json.dumps(inventory, indent=4))