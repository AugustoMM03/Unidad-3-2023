from claseCarrera import Carrera

class Facultad:
    def __init__(self, cod = '', nom = '', direccion = '', localidad = '', telefono = ''):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono
    
    def addCarrera(self, carre):
        self.__carreras.append(carre)

    def mostrarCarreras(self):
        carreras_str = ''
        for carrera in self.__carreras:
            carreras_str += str(carrera) + "\n"
        return carreras_str

    def __str__(self):
        return self.__codigo + ' ' + self.__nombre + ' ' + self.__direccion + ' ' + self.__localidad + ' ' + self.__telefono + '\n' + self.mostrarCarreras()
    
    def FacultadDuraciones(self):
        for carrera in self.__carreras:
            print("Nombre de carrera: {}".format(carrera.getNomCarrera()))
            print("Duracion de la carrera: {}".format(carrera.getDuracion()))

    def buscarCarrera(self, nomcarrera):
        for carrera in self.__carreras:
            if nomcarrera == carrera.getNomCarrera():
                print("Facultad: "+ self.__nombre + ' ' + self.__direccion + ' ' + self.__localidad + ' ' + self.__telefono)

