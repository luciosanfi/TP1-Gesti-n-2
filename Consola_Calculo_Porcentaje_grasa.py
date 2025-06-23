from calculadora_calculos import calcular_porcentaje_grasa

def menu():
    print("Cálculo del Porcentaje de Grasa Corporal")

    try:
        peso = float(input("Ingresá tu peso en kg: "))
        altura = float(input("Ingresá tu altura en metros: "))
        edad = int(input("Ingresá tu edad en años: "))

        valor_genero = float(input("Ingresá el valor del género (10.8 para hombre, 0 para mujer): "))
        if valor_genero == 10.8:
            genero_texto = "hombre"
        elif valor_genero == 0:
            genero_texto = "mujer"
        else:
            print("Valor de género no válido. Usá 10.8 o 0.")
            return

        porcentaje = calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
        print(f"Tu porcentaje estimado de grasa corporal ({genero_texto}) es: {porcentaje:.2f}%")

    except ValueError:
        print("Error: ingresá valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: la altura no puede ser cero.")

respuesta = input("¿Querés ejecutar el programa? (S/N): ").strip().upper()
if respuesta == "S":
    menu()
else:
    print("Programa finalizado.")
