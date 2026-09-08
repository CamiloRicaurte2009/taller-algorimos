# ==========================================================
# EJERCICIO 1 - TABLERO DE PRECIOS
# Bubble Sort tradicional y optimizado
# ==========================================================


# ----------------------------------------------------------
# PARTE A - BUBBLE SORT TRADICIONAL
# ----------------------------------------------------------

def bubble_sort(arreglo):

    n = len(arreglo)

    comparaciones = 0
    intercambios = 0

    print("\n" + "=" * 50)
    print("BUBBLE SORT TRADICIONAL")
    print("=" * 50)

    print("Arreglo inicial:", arreglo)

    # Recorremos el arreglo varias veces
    for i in range(n - 1):

        # Comparamos los elementos que están juntos
        for j in range(n - 1 - i):

            comparaciones += 1

            # Si el de la izquierda es mayor,
            # los cambiamos de posición
            if arreglo[j] > arreglo[j + 1]:

                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

                intercambios += 1

        # Mostramos cómo va quedando el arreglo
        print(f"Pasada {i + 1}: {arreglo}")

    print("\n--- RESULTADOS ---")
    print("Arreglo ordenado:", arreglo)
    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)

    return arreglo, comparaciones, intercambios


# ----------------------------------------------------------
# PARTE B - BUBBLE SORT OPTIMIZADO
# ----------------------------------------------------------

def bubble_sort_optimizado(arreglo):

    n = len(arreglo)

    comparaciones = 0
    intercambios = 0
    pasadas = 0

    print("\n" + "=" * 50)
    print("BUBBLE SORT OPTIMIZADO")
    print("=" * 50)

    print("Arreglo inicial:", arreglo)

    for i in range(n - 1):

        # Empezamos suponiendo que no habrá cambios
        hubo_intercambio = False

        for j in range(n - 1 - i):

            comparaciones += 1

            if arreglo[j] > arreglo[j + 1]:

                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

                intercambios += 1
                hubo_intercambio = True

        pasadas += 1

        print(f"Pasada {pasadas}: {arreglo}")

        # Si no hubo ningún cambio, ya está ordenado
        if hubo_intercambio == False:

            print("\nNo hubo intercambios.")
            print("El arreglo ya estaba ordenado.")
            print("Se detiene el algoritmo.")

            break

    print("\n--- RESULTADOS ---")
    print("Arreglo ordenado:", arreglo)
    print("Pasadas realizadas:", pasadas)
    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)

    return arreglo, pasadas, comparaciones, intercambios


# ----------------------------------------------------------
# TABLERO ORIGINAL
# ----------------------------------------------------------

productos = [8, 3, 9, 1, 6, 4]

resultado, comparaciones, intercambios = bubble_sort(
    productos.copy()
)


# ----------------------------------------------------------
# CASO CASI ORDENADO
# ----------------------------------------------------------

# Aquí solamente el 6 y el 4 están desordenados
casi_ordenado = [8, 3, 9, 1, 6, 4]

resultado2, pasadas, comparaciones2, intercambios2 = (
    bubble_sort_optimizado(casi_ordenado.copy())
)


# ----------------------------------------------------------
# COMPARACIÓN DE PASADAS
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("COMPARACIÓN")
print("=" * 50)

# Para 6 elementos, el peor caso necesita 5 pasadas
peor_caso = len(productos) - 1

print("Peor caso:", peor_caso, "pasadas")
print("Caso casi ordenado:", pasadas, "pasadas")

print("\nLa bandera permite detener el algoritmo")
print("cuando una pasada no necesita hacer intercambios.")


# ----------------------------------------------------------
# ¿QUÉ PASA CON 200.000 REGISTROS?
# ----------------------------------------------------------

n = 200_000

# En el peor caso, Bubble Sort hace:
# n * (n - 1) / 2 comparaciones

comparaciones_peor_caso = n * (n - 1) // 2

print("\n" + "=" * 50)
print("ESCALABILIDAD CON 200.000 REGISTROS")
print("=" * 50)

print("Cantidad de registros:", n)
print("Complejidad: O(n²)")
print("Comparaciones en el peor caso:",
      comparaciones_peor_caso)

print("\n--- CONCLUSIÓN ---")

print(
    "Para 6 productos, Bubble Sort funciona bien "
    "porque hay pocos datos."
)

print(
    "Pero con 200.000 registros tendría que hacer "
    "casi 20 mil millones de comparaciones en el peor caso."
)

print(
    "Por eso Bubble Sort no es una buena opción para "
    "una cantidad tan grande de datos."
)