#!/usr/bin/env python3

import os

def instalar():
    carpeta = input("Dime el nombre del directorio para la instalacion: ")
    if os.path.isdir("/home/" + carpeta):
        print("La carpeta ya existe.")

        if os.path.exists("/usr/bin/java") or os.path.exists("/usr/sbin/java"):
            print("La carpeta ya esta preparada, no se ha instalado java porque tambien lo tienes instalado.")
        else:
            os.system("sudo apt install default-jdk")
            print("Tienes la carpeta preparada pero no tenias java, asi que la hemos instalado.")
    else:
        os.system("sudo groupadd " + carpeta)
        os.system("sudo useradd -m -g " + carpeta + " -s /bin/bash " + carpeta)
        os.system("sudo cp pizarra.class /home/" + carpeta)
        os.system("sudo chown -R " + carpeta + ":" + carpeta + " /home/" + carpeta)
        os.system("sudo usermod -aG sudo " + carpeta)
        if os.path.exists("/usr/bin/java") or os.path.exists("/usr/sbin/java"):
            print("Ya tienes java instalado.")
        else:
            os.system("sudo apt install default-jdk")
            print("No tenias java y lo hemos instalado.")
        print("Hemos añadido un nuevo usuario, grupo y creado un directorio raiz de ese usuario, hemos copiado el programa dentro del directorio raiz de ese usuario y le hemos dado permisos a ese usuario. Tambien le hemos dado permisos para ejecutar el comando sudo.")

def ejecutar():
    carpeta = input("Dime el nombre de la carpeta para la ejecucion: ")

    if os.path.isdir("/home/" + carpeta):
        palabras, color = input("¿Que quieres escribir en la pizarra (sin espacios) y que color le quieres dar(R, G, Y)? ").split()
        os.chdir("/home/" + carpeta)
        with open("Texto.txt", "w") as f:
            f.write(palabras)
        os.system("java pizarra Texto.txt " + color)
    else:
        print("La carpeta no existe.")

def desinstalar():
    print("Dime el nombre del directorio a desinstalar.")
    carpeta = input()
    if os.path.isdir("/home/{}".format(carpeta)):
        os.system("sudo userdel -r {}".format(carpeta))
        print("Se ha borrado el usuario, el grupo y el directorio raiz de {}.".format(carpeta))
    else:
        print("La carpeta no existe.")

def ayuda():
    print("Bienvenido al programa de ejecucion de nuestra pizarra.")
    print("Los parametros son -i, -e, -d y -h.")
    print("Con -i procedemos a instalar el programa, pediremos un nombre que usaremos para nombrar la carpeta, usuario y grupo.")
    print("Si el nombre ya existe saldra un mensaje que te lo dira y no haremos nada a menos que no tengas java instalado, si no lo tienes se instalara.")
    print("En caso de no existir crearemos el usuario junto a su grupo y directorio raiz, luego moveremos el ejecutable de pizarra a este directorio. Por ultimo daremos permisos al usuario sobre todo lo del directorio raiz, ademas le permitimos ejecutar comandos sudo.")
    print("Antes de terminar la instalacion comprobaremos si tienes java instalado para instalarlo si no lo tienes.")
    print("Con -e ejecutaremos el programa, tendras que en una linea primero poner sin espacios lo que quieres escribir en la pizarra y luego el color (R, G, Y) que quieres. Este comando lo vamos a ejecutar como si fuesemos el usuario que se ha creado para el programa.")
    print("Con -d desinstalaremos el programa, pediremos el nombre del directorio y se borrara el usuario, el grupo y el directorio raiz.")
    print("Con -h te mostraremos esta ayuda.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py [-i|-e|-d|-h]")
        sys.exit()

    if sys.argv[1] == "-i":
        instalar()
    elif sys.argv[1] == "-e":
        ejecutar()
    elif sys.argv[1] == "-d":
        desinstalar()
    elif sys.argv[1] == "-h":
        ayuda()
    else:
        print("Invalid option.")