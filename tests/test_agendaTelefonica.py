from agendaTelefonica import crearContacto, consultarContacto, consultarFavoritos, consultarBloqueados, modificarContacto, añadirFavorito, bloquearContacto, eliminarContacto, buscarContacto
import pytest
#las validaciones seran correspondientes a la escala de la capa, desde la capa de controlador se validarán las reglas de negocio y desde el modelo se validarán cosas primarias como los tipos de datos, por ejemplo.

#CREAR-CONTACTO|||

#   tests ||EXITO||
def crearExitosoEstandar():
    #Entrada:campos de contacto correctos telefono=645645645
    #Salida:OK
    pass
def crearSinOpcionales():
    #Entrada:campos correo,apellidos y descripcion=""
    #Salida:OK
    pass

#       ||NOMBRE|| 
def crearNombre25Carac():
    #Entrada:campos de contacto correctos, nombre= 25 caracteres de longuitud
    #Salida:OK
    pass

#       ||APELLIDOS|| 
def crearSinApellidos():
    #Entrada:campos de contacto correctos apellidos=""
    #Salida:OK
    pass
def crearApellido25Carac():
    #Entrada:campos de contacto correctos, apellido= 25 caracteres de longuitud
    #Salida:OK
    pass

#       ||DESCRIPCION|| 
def crearSinDescripcion():
    #Entrada:campos de contacto correctos apellidos=""
    #Salida:OK
    pass
def crearDescripcion50Carac():
    #Entrada:campos de contacto correctos, Descripcion= 50 caracteres de longuitud
    #Salida:OK
    pass

#       ||CORREO||
def crearSinCorreo():
    #Entrada:campos de contacto correctos apellidos=""
    #Salida:OK
    pass

def crearVariosCorreos():
    #Entrada:campo correo=correo@gmail.com
    #Salida:OK
    pass

#   tests ||ERROR||
def crearDuplicado():
    #Entrada:Numero de telefono de otro contacto ya registrado.
    #Salida:Error
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
#       ||NOMBRE||
def crearSinNombre():
    #Entrada:campos de contacto completos menos el nombre, estando vacio
    #Salida:Error
    pass

def crearNombre26Carac():
    #Entrada:campos de contacto correctos, nombre= 26 caracteres de longuitud
    #Salida:Error
    pass
#       ||APELLIDOS||
def crearApellido26Carac():
    #Entrada:campos de contacto correctos, apellido= 26 caracteres de longuitud
    #Salida:Error
    pass

def crearSinApellido():
    #Entrada:campos de contacto correctos, apellido=VACIO
    #Salida:OK
    pass
#       ||DESCRIPCION||
def crearDescripcion51Carac():
    #Entrada:campos de contacto correctos, Descripcion= 51 caracteres de longuitud
    #Salida:Error
    pass
#       ||CORREO||
def crearCorreoInvalido():
    #Entrada:campos de contacto correctos menos correo=correo@gemail.coma
    #Salida:Error
    pass

def crearVariosCorreosAmbosInvalidos():
    #Entrada:campos de contacto correctos menos correo=[correo@gemail.coma, migmail@gimailpuntocom]
    #Salida:error
    pass
def crearVariosCorreosUnoInvalido():
    #Entrada:campos de contacto correctos menos correo=[correo@gmail.com, migmail@gimailpuntocom]
    #Salida:error
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