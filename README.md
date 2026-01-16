# **AgendaTelefonica**
## DESCRIPCION
Se trata de un gestor de contactos, solo gestionará la entidad de contactos con los siguientes campos:
* Telefono
* Extension
* Nombre
* Apellidos
* Descripcion
* Correo
* Favorito
* Bloqueado

## FUNCIONES
Además de la operaciones CRUD(Crear contacto, Consultar contactos, Modificar contacto y eliminar contacto) hay funciones extras que son las siguientes:
* BUSQUEDA AVANZADA:
* * Permite realizar una busqueda a partir del un parametro dado que puede ser un numero de telefono o nombre de contacto ya que son campos obligatorios.
* LISTA FAVORITOS
  * Permite destacar contactos como favoritos teniendo las funciones de:
    *  mostrar favoritos
    *  añadir a favoritos
* LISTA BLOQUEADOS
  * Permite bloquear contactos no como no deseados teniendo las funciones de:
    * mostrar bloqueados
    * bloquear contacto   

## VALIDACIONES
### CREAR
  `def CrearNumTelefRepetido:`
* ### Entrada: 
  * Numero de telefono repetido
* ### Salida: 
  * Error
  -----------------------
  `def CrearNombreVacio:`
* ### Entrada: 
  * NombreVacio
* ### Salida: 
  * Error

### CONSULTAR

### MODIFICAR

### ELIMINAR