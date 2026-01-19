from agendaTelefonica import crearContacto, consultarContacto, consultarFavoritos, consultarBloqueados, modificarContacto, añadirFavorito, bloquearContacto, eliminarContacto, buscarContacto
import pytest
#las validaciones seran correspondientes a la escala de la capa, desde la capa de controlador se validarán las reglas de negocio y desde el modelo se validarán cosas primarias como los tipos de datos, por ejemplo.

#CREAR-CONTACTO|||
#   tests ERROR
def crearDuplicado():
    #Entrada:Numero de telefono de otro contacto ya registrado.
    #Salida:Error
    pass

def crearSinNombre():
    #Entrada:campos de contacto completos menos el nombre, estando vacio
    #Salida:Error
    pass

def crearCorreoInvalido():
    #Entrada:campos de contacto correctos menos correo=correo@gemail.coma
    #Salida:Error
    pass

def crearVariosCorreos():
    #Entrada:campo correo=correo@gmail.com
    #Salida:OK
    pass

def crearVariosCorreosAmbosInvalidos():
    #Entrada:campos de contacto correctos menos correo=[correo@gemail.coma, migmail@gimailpuntocom]
    #Salida:error
    pass
def crearVariosCorreosUnoInvalido():
    #Entrada:campos de contacto correctos menos correo=[correo@gmail.com, migmail@gimailpuntocom]
    #Salida:error
    pass

def crearTelefInvalido():
    #Entrada:campos de contacto correctos menos telefono=1212121212122212 |validar num telefono por españa
    #Salida:Error
    pass
def crearTelefTexto():
    #Entrada:campos de contacto correctos menos telefono="miNumerode telefono"
    #Salida:Error
    pass
def crearTelefFloat():
    #Entrada:campos de contacto correctos menos telefono=333.5 |validar num telefono por españa
    #Salida:Error
    pass
def crearVariosTelef():
    #Entrada:campos de contacto correctos menos telefono=Coleccion o lista de telefonos.
    #Salida:Error
    pass

def crearTelefVacio():
    #Entrada:campos de contacto correctos menos telefono=""
    #Salida:Error
    pass

#|||consultarContacto|||
#   tests
def 
#|||consultarFavoritos|||
#   tests
def
#|||consultarBloqueados|||
#   tests
def
#|||modificarContacto|||
#   tests
def
#|||añadirFavorito|||
#   tests
def
#|||bloquearContacto|||
#   tests
def
#|||eliminarContacto|||
#   tests
def
#|||buscarContacto|||
#   tests
def