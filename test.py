anio_actual = 2024
anio_nac= int(input('Ingrese su año de nacimiento: '))
calculo = anio_actual - anio_nac
if calculo >= 18:
    print('Usted es mayor de edad.')
else:
    print('Usted es menor de edad.')