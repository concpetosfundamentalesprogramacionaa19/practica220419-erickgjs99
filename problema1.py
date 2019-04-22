"""
        Problema 1 ---- Calculo de salario mensual
"""
#ingreso de datos
htraba = input("Ingrese las horas trabajadas\n")
hsueld = input("Ingrese  cuanto gana por hora\n")
#calculo de sueldo
sueld = int(htraba) * int(hsueld)
desc = int(sueld) * 0.1
result = float(sueld) - float(desc)
#resultado final
print("Su Salario final a pagarse es de: \n"+str(result))