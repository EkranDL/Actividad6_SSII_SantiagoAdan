#!/bin/bash
#Actividad UD6

instalar() {
    echo "Dime el nombre del directorio para la instalacion."
    read carpeta
    if [ -d "/home/$carpeta" ]
    then
        echo "La carpeta ya existe."

        if [ -x /usr/bin/java ] || [ -x /usr/sbin/java ] 
        then
            echo "La carpeta ya esta preparada, no se ha instalado java porque tambien lo tienes instalado."
        else
            sudo apt install default-jdk
            echo "Tienes la carpeta preparada pero no tenias java, asi que la hemos instalado."
        fi
    else
        sudo groupadd $carpeta
        sudo useradd -m -g $carpeta -s /bin/bash $carpeta
        sudo cp pizarra.class /home/$carpeta
        sudo chown -R $carpeta:$carpeta /home/$carpeta
        sudo usermod -aG sudo $carpeta
        if [ -x /usr/bin/java ] || [ -x /usr/sbin/java ] 
        then
            echo "Ya tienes java instalado."
        else
            sudo apt install default-jdk
            echo "No tenias java y lo hemos instalado."
        fi
        echo "Hemos añadido un nuevo usuario, grupo y creado un directorio raiz de ese usuario, hemos copiado el programa dentro del directorio raiz de ese usuario y le hemos dado permisos a ese usuario. Tambien le hemos dado permisos para ejecutar el comando sudo."
    fi
}

ejecutar(){
    echo "Dime el nombre de la carpeta para la ejecucion."
    read carpeta

    if [ -d "/home/$carpeta" ]
    then
        echo "¿Que quieres escribir en la pizarra (sin espacios) y que color le quieres dar(R, G, Y)?"
        read palabras color
        cd /home/$carpeta/
        echo "$palabras" > Texto.txt
        java pizarra Texto.txt $color
    else
        echo "La carpeta no existe."
    fi
}

desinstalar() {
    echo "Dime el nombre del directorio a desinstalar."
    read carpeta

    if [ -d "/home/$carpeta" ]
    then
        sudo userdel -r $carpeta
        echo "Se ha borrado el usuario, el grupo y el directorio raiz de $carpeta."
    else
        echo "La carpeta no existe."
    fi
}

ayuda() {
    echo "Bienvenido al programa de ejecucion de nuestra pizarra."
    echo "Los parametros son -i, -e, -d y -h."
    echo "Con -i procedemos a instalar el programa, pediremos un nombre que usaremos para nombrar la carpeta, usuario y grupo."
    echo "Si el nombre ya existe saldra un mensaje que te lo dira y no haremos nada a menos que no tengas java instalado, si no lo tienes se instalara."
    echo "En caso de no existir crearemos el usuario junto a su grupo y directorio raiz, luego moveremos el ejecutable de pizarra a este directorio. Por ultimo daremos permisos al usuario sobre todo lo del directorio raiz, ademas le permitimos ejecutar comandos sudo."
    echo "Antes de terminar la instalacion comprobaremos si tienes java instalado para instalarlo si no lo tienes."
    echo "Con -e ejecutaremos el programa, tendras que en una linea primero poner sin espacios lo que quieres escribir en la pizarra y luego separado el color (R, G, Y). Este comando lo vamos a ejecutar como si fuesemos el usuario que se ha creado para el programa."
    echo "Con -d borraremos el usuario, grupo y el directorio raiz, borrando asi todo lo relacionado con el programa realizado durante la instalacion."
    echo "Finalmente con -h te saldra este esta ayuda."
}

comando=$1

if [ $comando = -i ]
then
    instalar
elif [ $comando = -e ]
then
    ejecutar
elif [ $comando = -d ]
then
    desinstalar
elif [ $comando = -h ]
then
    ayuda
fi