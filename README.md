# Actividad6_SSII_SantiagoAdan

Los parametros para el script son -i, -e, -d y -h.

-Con -i procedemos a instalar el programa, pediremos un nombre que usaremos para nombrar la carpeta, usuario y grupo.
Si el nombre ya existe saldra un mensaje que te lo dira y no haremos nada a menos que no tengas java instalado, si no lo tienes se instalara.
En caso de no existir tambien comprobaremos si tienes java y ademas crearemos el usuario junto a su grupo y directorio raiz, luego moveremos el ejecutable de pizarra a este directorio. Por ultimo daremos permisos al usuario sobre todo lo del directorio raiz, ademas le permitimos ejecutar comandos sudo.

-Con -e ejecutaremos el programa, tendras que en una linea primero poner sin espacios lo que quieres escribir en la pizarra y luego separado el color (R, G, Y). 
Este comando lo vamos a ejecutar como si fuesemos el usuario que se ha creado para el programa.

-Con -d borraremos el usuario, grupo y el directorio raiz, borrando asi todo lo relacionado con el programa realizado durante la instalacion.

-Finalmente con -h te saldra un mensaje de ayuda con toda la informacion necesaria para su empleo.
