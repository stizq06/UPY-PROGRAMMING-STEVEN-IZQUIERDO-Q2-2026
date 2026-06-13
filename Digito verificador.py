# INPUT
rol = input("Ingresa el rol sin guión: ")

# PROCESS
rol_invertido = rol[::-1]

suma = 0
multiplicador = 2

for digito in rol_invertido:
    suma += int(digito) * multiplicador
    multiplicador += 1
    
    if multiplicador > 7:
        multiplicador = 2  # Reinicia la secuencia según la regla

resultado_resta = 11 - (suma % 11)

# Casos especiales estándar del algoritmo Módulo 11
if resultado_resta == 11:
    digito_verificador = "0"
elif resultado_resta == 10:
    digito_verificador = "K"
else:
    digito_verificador = str(resultado_resta)

# OUTPUT
print(f"Finalmente, el dígito verificador será el obtenido en la resta: {rol}-{digito_verificador}")