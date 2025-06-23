from calculadora_calculos import calcular_calorias_en_actividad

def menu():
    print("Cálculo de calorías según actividad física")

    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        edad = int(input("Ingrese su edad en años: "))

        valor_genero = float(input("Ingresá el valor del género (5 para hombre, -161 para mujer): "))
        if valor_genero == 5:
            genero_texto = "hombre"
        elif valor_genero == -161:
            genero_texto = "mujer"
        else:
            print("Valor de género no válido. Usá 5 o -161.")
            return

        print("Ingresá el valor numérico que representa tu nivel de actividad física:")
        print("1.2 → poco o ningún ejercicio")
        print("1.375 → ejercicio ligero (1 a 3 días por semana)")
        print("1.55 → ejercicio moderado (3 a 5 días por semana)")
        print("1.72 o 1.725 → deportista (6 - 7 días por semana)")
        print("1.9 → atleta (entrena mañana y tarde)")

        valor_actividad = float(input("Ingresá el valor de tu nivel de actividad física: "))

        valores_validos = {1.2, 1.375, 1.55, 1.72, 1.725, 1.9}
        if valor_actividad not in valores_validos:
            print("Valor de actividad física no válido.")
            return

        calorias = calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
        print(f"Tu gasto calórico estimado con actividad física ({genero_texto}) es de: {calorias:.2f} calorías por día.")

    except ValueError:
        print("Error: ingresá valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: la altura no puede ser cero.")

respuesta = input("¿Querés ejecutar el programa? (S/N): ").strip().upper()
if respuesta == "S":
    menu()
else:
    print("Programa finalizado.")