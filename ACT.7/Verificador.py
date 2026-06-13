import math

# Input
a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")

# Manejo de 'pi' con replace y eval para soportar fracciones como 'pi/2'
if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)

if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)

f_x = input("Write the function to integrate (use math. prefixes for sin, cos, etc): ")
method = input("Select integration Method (LRM/RRM/MPM/TRAP): ")

# Process
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1
elif method == "MPM":
    constant = h / 2
# LRM usa shift=0 y constant=0 por defecto

for i in range(0 + shift, n + shift):
    if method == "TRAP":
        # Para el trapecio, calculamos la altura en ambos bordes del subintervalo y la promediamos
        xi_left = a + i * h
        xi_right = a + (i + 1) * h
        
        # Envolvemos xi en paréntesis f"({xi})" para evitar errores de signos con potencias
        height_left = eval(f_x.replace("x", f"({xi_left})"))
        height_right = eval(f_x.replace("x", f"({xi_right})"))
        
        height = (height_left + height_right) / 2
    else:
        # Lógica original intacta para LRM, RRM y MPM
        xi = a + i * h + constant
        height = eval(f_x.replace("x", f"({xi})"))
        
    area += height * h
    
# Output
print(f"The integration of {f_x} is {area:.2f}")
# Preparado para entrega final