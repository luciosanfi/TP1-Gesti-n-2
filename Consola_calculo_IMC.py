from calculadora_calculos import calcular_imc

def menu():
    print("Cálculo del Índice de Masa Corporal (IMC)")
    try:
        peso = float(input("Ingresá tu peso en kg: "))
        altura = float(input("Ingresá tu altura en metros: "))
        imc = calcular_imc(peso, altura)
        print(f"Tu índice de masa corporal es: {imc:.2f}")
    except ValueError:
        print("Error: ingresá valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: la altura no puede ser cero.")

respuesta = input("¿Querés ejecutar el programa? (S/N): ").strip().upper()
if respuesta == "S":
    menu()
else:
    print("Programa finalizado.")
