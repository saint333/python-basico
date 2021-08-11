#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas=int(input("¿Cuantas horas trabajas?: "))
coste_horas=int(input("¿Cuanto te pagan por hora?: "))
pago=horas_trabajadas*coste_horas
print(f"tu pago sera: {pago}")