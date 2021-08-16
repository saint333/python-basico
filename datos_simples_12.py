#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
pan=3.49
descuento=3.49-(0.60*3.49)
pan_novendido=int(input("Barras de pan vendidas que no son del día: "))
coste_final=pan_novendido*descuento
print(f"El precio habitual del pan es {pan}, el descuento por pan es del 60%, y el coste final es {round(coste_final,2)}")