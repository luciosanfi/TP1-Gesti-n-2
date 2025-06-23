from calculadora_calculos import calcular_calorias_en_reposo as reposo

def menu():
    print("Cálculo de calorías en reposo (Tasa Metabólica Basal)")

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

        resultado = reposo(peso, altura, edad, valor_genero)
        print(f"Tu tasa metabólica basal en reposo ({genero_texto}) es de: {resultado:.2f} calorías por día.")

    except ValueError:
        print("Error: ingresá valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: la altura no puede ser cero.")

respuesta = input("¿Querés ejecutar el programa? (S/N): ").strip().upper()
if respuesta == "S":
    menu()
else:
    print("Programa finalizado.")