import math
class esfera:
    def __init__(self,radio):
        self.radio = radio

    
    def area(self):             
        return math.pi*(self.radio ** 2)

    def perimetro(self):
        return 2*(math.pi*self.radio)
    
    def volumen(self):
        return (4/3)*(math.pi*self.radio ** 3)
    
    def volumen_cilindro(self):
        return 
    def describir(self):
        print(f"El area es {round(self.area(),2)}")
        
    

        print(f"El perimetro es {round(self.perimetro(),2)}")
        print(f"El volumen es {round(self.volumen(),2)}")
    
        
r = esfera (float(input("Ingrese el valor de r :")))

r.describir()
    




    
    

    
    
    