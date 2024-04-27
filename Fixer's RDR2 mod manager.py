import os
import shutil

fart='D:\Rockstar Games\Red Dead Redemption 2'
fart2='D:\RDR2Mods'

def listar_archivos(directorio):
    for raiz, dirs, archivos in os.walk(directorio):
        for archivo in archivos:
            yield os.path.join(raiz, archivo)

def escribir_lista():
        with open('list.txt', 'w') as f:
            for archivo in listar_archivos('D:\Rockstar Games\Red Dead Redemption 2'):
                f.write(archivo + '\n')
        f.close()
        print("All vanilla files listed in list.txt")

def load_mods():
    for archivo in listar_archivos(fart2):
        destino = os.path.join(fart, os.path.relpath(archivo, fart2))
        if os.path.isdir(archivo):
            os.makedirs(destino, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            shutil.copy2(archivo, destino)
    print("Mods loaded successfully")

def unload_mods():
    for archivo in listar_archivos(fart):
        if archivo not in leer_lista():
            os.remove(archivo)
    print("Mods unloaded successfully")

def leer_lista():
    with open('list.txt', 'r') as f:
        return [linea.strip() for linea in f]


def load_locations():
            fart = leer_linea_especifica('locations.txt', 1)
            fart2 = leer_linea_especifica('locations.txt', 2)

def leer_linea_especifica(nombre_archivo, numero_linea):
    with open(nombre_archivo, 'r') as f:
        for i, linea in enumerate(f):
            if i == numero_linea - 1:
                return linea.strip()



if __name__ == '__main__':
    load_locations()
    print('Welcome to Fixer\'s RDR2 mod manager\n Press 1 to make a list of al the vanilla files in the game directory\n Press 2 to load all the mods\n Press 3 to unload the mods\n Press 4 to exit')
    while True:
        opcion = input('Enter an option: ')
        if opcion == '1':
            escribir_lista()
        elif opcion == '2':
            load_mods()
        elif opcion == '3':
            unload_mods()
        elif opcion == '4':
            break
        else:
            print('Invalid option')