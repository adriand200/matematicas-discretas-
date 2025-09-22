#Calculadora de lógica de proposiciones con tabla de verdad
# El usuario puede usar entre 2 y 5 variables (p, q, r, s, t)
# Operadores: Negación, Conjunción, Disyunción, Condicional y Bicondicional

from itertools import product   # Para generar combinaciones de 0 y 1

# --- Paso 1: Número de variables ---
n = int(input("¿Cuántas variables quieres usar (2 a 5)? "))

# --- Paso 2: Menú de operadores ---
print("\nElige el operador lógico:")
print("1. Negación (¬)")          # Operador unario (se aplica sobre una sola variable)
print("2. Conjunción (∧)")        # AND lógico
print("3. Disyunción (∨)")        # OR lógico
print("4. Condicional (→)")       # Si p entonces q
print("5. Bicondicional (↔)")     # p si y solo si q

op = int(input("Opción: "))

# --- Paso 3: Elección de variables ---
variables = ["p", "q", "r", "s", "t"]   # Nombres de variables disponibles

if op == 1:   # Si es negación solo se pide una variable
    var1 = input(f"¿Qué variable quieres negar? {variables[:n]}: ")
else:         # Para el resto se piden dos variables
    var1 = input(f"Primera variable {variables[:n]}: ")
    var2 = input(f"Segunda variable {variables[:n]}: ")

print("\nTabla de verdad:\n")

# --- Paso 4: Generar combinaciones ---
# Generamos todas las posibles combinaciones de 0 y 1
# Ejemplo: con 2 variables → (0,0), (0,1), (1,0), (1,1)
combinaciones = list(product([0,1], repeat=n))

# Imprimimos el encabezado de la tabla
print("\t".join(variables[:n]) + "\tResultado")

# --- Paso 5: Calcular y mostrar resultados ---
for fila in combinaciones:
    valores = dict(zip(variables, fila))  # Asignamos cada valor a su variable, ej: {"p":0,"q":1}

    # Negación
    if op == 1:
        res = int(not valores[var1])  # Se aplica "not" y se convierte a entero (0 o 1)
        print("\t".join(str(v) for v in fila) + f"\t¬{var1} = {res}")

    # Conjunción
    elif op == 2:
        res = valores[var1] and valores[var2]  # AND entre las dos variables
        print("\t".join(str(v) for v in fila) + f"\t{var1} ∧ {var2} = {res}")

    # Disyunción
    elif op == 3:
        res = valores[var1] or valores[var2]  # OR entre las dos variables
        print("\t".join(str(v) for v in fila) + f"\t{var1} ∨ {var2} = {res}")

    # Condicional
    elif op == 4:
        res = int((not valores[var1]) or valores[var2])  # (¬p) ∨ q
        print("\t".join(str(v) for v in fila) + f"\t{var1} → {var2} = {res}")

    # Bicondicional
    elif op == 5:
        res = int(valores[var1] == valores[var2])  # Verdadero si son iguales
        print("\t".join(str(v) for v in fila) + f"\t{var1} ↔ {var2} = {res}")
#var1 y var2 → son las letras (variables) que el usuario eligió. .join(...) → sirve para imprimir la fila de forma ordenada como tabla.
#res → es el resultado lógico de la operación en esa fila.
