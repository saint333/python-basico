#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.
cantidad=float(input("Cantidad a invertir: "))
interes=float(input("Interés porcentual anual: "))
año=int(input("Cantidad de años: "))
capital=cantidad*(interes/100+1)**año
print(f"Capital final es: {round(capital,2)}")