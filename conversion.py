#Conversión entre sistemas numéricos


# Pide datos al usuario

def pedir_numero():
    """
    Esta función muestra un menú al usuario para que elija
    en qué sistema está escrito el número que va a ingresar.
    Luego pide el número como texto (string).
    Devuelve: el número (string) y la opción elegida (int).
    """
    print("Seleccione el sistema del número ingresado:")
    print("1. Decimal")
    print("2. Binario")
    print("3. Octal")
    print("4. Hexadecimal")
    
    opcion = int(input("Opción: "))
    
    # Pedimos número
    numero = input("Ingrese el número: ")

    return numero, opcion

# FUNCIÓN: Convertir a decimal

def convertir_a_decimal(numero, opcion):
    """
    Convierte el número ingresado en cualquier sistema
    (decimal, binario, octal o hexadecimal) a decimal.
    """

    if opcion == 1:  # Decimal
        return int(numero) 
    
    elif opcion == 2:  # Binario
        return int(numero, 2)  
    
    elif opcion == 3:  # Octal
        return int(numero, 8) 
    
    elif opcion == 4:  # Hexadecimal
        return int(numero, 16)
    
    else:
        print("Opción no válida.")
        return None


# FUNCIÓN: Convertir desde decimal a otros sistemas

def convertir_desde_decimal(decimal):
    """
    Convierte un número decimal a:
      - Binario
      - Octal
      - Hexadecimal
    Devuelve un diccionario con los resultados.
    """
    return {
        "Decimal": decimal,
        "Binario": bin(decimal)[2:],        # bin() agrega "0b", lo quitamos con [2:]
        "Octal": oct(decimal)[2:],          
        "Hexadecimal": hex(decimal)[2:].upper()  
    }



# Complemento a 2

def complemento_a2(numero, bits=8):
    """
    Calcula el complemento a 2 de un número con cierta cantidad de bits.
    Si el número es positivo, solo lo representa en binario normal.
    Si es negativo, aplica la fórmula (1 << bits) + numero.
    """
    if numero >= 0:
        # Convierte el número positivo a binario con el formato de n bits
        return format(numero, f"0{bits}b")
    else:
        # Para números negativos: suma el número a 2^bits
        return format((1 << bits) + numero, f"0{bits}b")

# Ejecuta todo el programa

def main():
    # Paso 1: Pedir número y sistema
    numero, opcion = pedir_numero()
    
    # Paso 2: Convertir a decimal
    decimal = convertir_a_decimal(numero, opcion)

    if decimal is not None:  # Si la conversión fue válida
        # Paso 3: Convertir desde decimal a los otros sistemas
        resultados = convertir_desde_decimal(decimal)

        # Mostrar resultados
        print("\n Conversiones ")
        for sistema, valor in resultados.items():
            print(f"{sistema}: {valor}")

        # Paso 4: Mostrar complemento a 2 en 8 bits
        print("\n Complemento a 2 (8 bits)")
        print(complemento_a2(decimal, 8))
main()
