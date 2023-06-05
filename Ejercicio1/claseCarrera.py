class Carrera:
    def __init__(self, cod = '', nom = '', fecha = '', duracion = '', titulo = ''):
        self.__codigo = cod
        self.__nombre = nom
        self.__fechain = fecha
        self.__duracion = duracion
        self.__titulo = titulo

    def getCodigo(self):
        return self.__codigo
    
    def getNomCarrera(self):
        return self.__nombre
    
    def getFecha(self):
        return self.__fechain
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo
    
    def __str__(self):
        return self.__codigo + ' ' + self.__nombre + ' ' + self.__fechain + ' ' + self.__duracion + ' ' + self.__titulo