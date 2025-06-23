def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    imc = calcular_imc(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    altura_cm = altura * 100
    return (10 * peso) + (6.25 * altura_cm) - (5 * edad) + valor_genero

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.8
    rango_superior = tmb * 0.85
    return f"Para adelgazar se recomienda consumir entre {rango_inferior:.1f} y {rango_superior:.1f} calorías al día."
