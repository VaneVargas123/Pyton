"""
    De La Cruz Vargas Vanessa
    2022640604
    Practica 2 
    24/septiembre/2023
    Programacion Avanzada 
    
    Practica 2 Clases y objetos  
        a) Crear una lista de personas
"""

class persona: 
    def __init__(self, nombre: str ='Ninguno', edad: int = 0, estatura: float = 0.0, ntelefono: int = 0000000000) -> None:
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.ntelefono = ntelefono
    
    def to_string(self): 
        print(f'¡Hola!, Mi nombre es {self.nombre}, tengo {self.edad} años, naci el {2023 - self.edad}, mido {self.estatura} metros y mi numero de contacto es {self.ntelefono} ¡Saludos!')
        
print('\tPograma 1: Lista de Registro de 3 personas (Nombre, Edad, Estatura y Contacto) \n')

Gente = persona()
Persona = []
for i in range(3):
    Nombre = input(f'\n Escribe el nombre de la persona {i+1}:  ')
    Edad = int(input(f'Escribe la edad de la persona {i+1}:  '))
    Estatura = float(input(f'Escribe la estatura de la persona {i+1} (en metros):  '))
    NTelefono = int(input(f'Escribe el numero de contato de la persona {i+1}:  '))
    
    for metodo, variable in [('nombre', Nombre), 
                             ('edad', Edad), 
                             ('estatura', Estatura), 
                             ('ntelefono', NTelefono)]:
        setattr(Gente, metodo, variable)
        
    Persona.append(Gente)
    

for i, Gente in enumerate(Persona):       
    print(f'\nPersona {i+1}')
    Gente.to_string()