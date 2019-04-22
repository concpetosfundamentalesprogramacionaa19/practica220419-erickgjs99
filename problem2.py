"""
Problema 2 Calcular un problema muy complejo basandose en x,y,z
"""
#Ingreso de datos
x = input("Ingrese el valor de x\n")
y = input("Ingrese el valor de y\n")
z = input("Ingrese el valor de z\n")
#calculo de datos
part1 = float(x) + (float(y)/float(z)) 
part2 = float(x) - (float(y)/float(z)) 
result = float(part1) / float(part2)
#resultado
print("El valor de m, en base a las variables:\n " + "\tx ="+str(x)+"\n\t y = "+str(y)+ "\n\t z = "+str(z)+"\nda como resultado: " "\n m = "+str(result))