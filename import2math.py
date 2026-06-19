import math
class cilindro:
    def __init__(self,radio, altura):
        self.radio = radio
        self.altura = altura

    
    def volumen_cilindro(self):             
        return math.pi*(self.radio ** 2) * self.altura

    def area_cilindro(self):
        return 2*(math.pi*self.radio ) * (self.altura + self.radio)
    

    def describir(self):
        print(f"El vulumen del cilindro es {round(self.volumen_cilindro(),1)}")
        print(f"El area total de cilindro es {round(self.area_cilindro(),)}")
        
    
        
r = cilindro((float(input("Ingrese el valor de r :"))),(float(input("Ingrese el valor de altura: "))))
r.describir()