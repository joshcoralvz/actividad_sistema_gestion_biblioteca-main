# Importa tus módulos aquí
# Importa tus módulos aquí
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria
)

from data.biblioteca import libros, categorias

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Llama a mostrar_disponibles()
        mostrar_disponibles(libros)

    elif opcion == "2":
        # Llama a buscar_por_paginas()
        buscar_por_paginas(libros, 400)

    elif opcion == "3":
        # Llama contar_libros()
        print("Cantidad de libros:", contar_libros(libros))

        # Llama promedio_paginas()
        print("Promedio de páginas:", promedio_paginas(libros))

    elif opcion == "4":
        nueva_categoria = input("Ingrese la nueva categoría: ")
        agregar_categoria(categorias, nueva_categoria)

        print("Categorías disponibles:")
        print(categorias)

    elif opcion == "5":
        print("¡Hasta luego!")
        continuar = "n"

    else:
        print("Opción inválida. Intente nuevamente.")
