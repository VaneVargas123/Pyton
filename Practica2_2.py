"""
    De La Cruz Vargas Vanessa
    2022640604
    Practica 2 
    24/septiembre/2023
    Programacion Avanzada 
    
    Practica 2 Clases y objetos  
        b) Crear una lista de alumnos por el profesor
"""

class Profesor: 
    def __init__(self, nombre: str = 'Chuchito', nempleado: int = 0) -> None:
        self.nombre = nombre
        self.nempleado = nempleado
       
class Alumno: 
    def __init__(self, nombre: str = 'Panfilo', apellidopat: str = '', apellidomat: str = '', boleta: int = 0, carrera: str = '', grupo: int = 0, correo: str ='', dia: int = 0, mes: int = 0, anio: int = 0) -> None:
        self.nombre = nombre
        self.apellidopat = apellidopat
        self.apellidomat = apellidomat
        self.boleta = boleta
        self.carrera = carrera
        self.grupo = grupo
        self.correo = correo
        self.dia = dia
        self.mes = mes
        self.anio = anio
                     
class listas: 
    def __init__(self) -> None:
        self.__profesor = None
        self.__num_empleado = None
        self.__listas_alumno = []
        
    def registro_profesor(self, nombre: str, nempleado: int):
        self.__profesor = Profesor(nombre)
        self.__num_empleado = Profesor(nempleado)
        print(f'Num:  {self.__num_empleado.nempleado}')
        
    def registro_alumno(self,alumno: Alumno = None, nombre: str = None, apellidopat: str = None, apellidomat: str = None, boleta: int = None, carrera: str = None, grupo: str = None, correo: str = None, dia: int = None, mes: int = None, anio: int = None):
        if (alumno is not None):
            self.__listas_alumno.append(alumno)
        else:
            alumno = Alumno(nombre, apellidopat, apellidomat, boleta, carrera, grupo, correo, dia, mes, anio)
            self.__listas_alumno.append(alumno)
            
    def imprimir_registro(self) -> None:
        print(f'Profesor: {self.__profesor.nombre} \n No. Empleado: {self.__num_empleado.nempleado}')
        print('================================================================================')
        i = 1
        for alumno in self.__listas_alumno:
            print(f'{i}. {alumno.apellidopat} {alumno.apellidomat} {alumno.nombre} - {alumno.boleta} - {alumno.dia}/{alumno.mes}/{alumno.anio} - Ing. {alumno.carrera} - {alumno.grupo} - {alumno.correo}')
            i += 1
        print('=========================================================================')
        print(f'Total de alumnos = {len(self.__listas_alumno)}')
        
        
print('\t Programa 2: Lista de registro de alumnos \n')

listaEst = listas()
print('Registro de profesor: ')
NomProf = input(f'Escriba su nombre:  ')
NumEmp = input(f'Escriba el numero de empleado:  ')
listaEst.registro_profesor(NomProf, NumEmp)
cantidad = int(input(f'\n Bienvenido Profesor {NomProf} \n   Por favor ingrese el numero de estudiantes a registrar:   '))

for i in range(cantidad):
    Nombre = input(f'\n\nEscriba el nombre del alumno {i+1}:  ')
    Nombre = Nombre.title()
    ApePat = input(f'Escriba el apellido paterno del alumno {i+1}:  ')
    ApePat = ApePat.title()
    ApeMat = input(f'Escriba el apellido materno del alumno {i+1}:  ')
    ApeMat = ApeMat.title()
    Boleta = int(input(f'Escriba la boleta del alumno {i+1}:  '))
    Carrera = input(f'Escriba la carrera del alumno {i+1}:  ')
    Carrera = Carrera.title()
    Grupo = input(f'Escriba el grupo del alumno {i+1}:  ')
    Correo = input(f'Escriba el correo del alumno {i+1}:  ')
    print(f'\nEscribe en NUMERO la fecha de nacimiento del alumno {i+1}')
    Dia = int(input(f'Escriba el dia de nacimiento:  '))
    Mes = int(input(f'Escriba el mes de nacimiento:  '))
    Anio = int(input(f'Escriba el año de nacimiento:  '))
    
    listaEst.registro_alumno(alumno = Alumno(Nombre, ApePat, ApeMat, Boleta, Carrera, Grupo, Correo, Dia, Mes, Anio))
    
listaEst.imprimir_registro()
    
    


        