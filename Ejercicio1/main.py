from manejadorFacultades import controlFacultades
from menu import menuOpciones


listaFacultades = controlFacultades()
listaFacultades.cargarLista()
#listaFacultades.mostrarFacultades()
menu = menuOpciones() 
menu.opciones(listaFacultades)

