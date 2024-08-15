class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self._pi = 3.141521
    
    def __str__(self):
        return f"Un circulo con radio {self.radio}"

    def __add__(self, otro):
        suma = otro.cal_area() + self.cal_area()
        return f"La suma de los circulos es {suma}"

    def cal_perimetro(self):
        return 2 * self._pi * self.radio
    
    def cal_area(self):
        return self._pi * self.radio ** 2


circulo = Circulo(3.5)
circulo2 = Circulo(10)

print(circulo.cal_area())

print(f"{circulo._pi}")

print(circulo + circulo2)

# Publico: pi NO SEGURO
# Protegido: _pi MEDIO SEGURO
# Privado: __pi SEGURO
