import os

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


if __name__ == '__main__':
    print('Welcome to Fixer\'s RDR2 mod manager\n Press 1 to list all files in the game directory\n Press 2 to load all the mods\n Press 3 to unload the mods\n Press 4 to exit')
    while True:
        opcion = input('Enter an option: ')
        if opcion == '1':
            escribir_lista()
        elif opcion == '2':
            print('Loading mods')
        elif opcion == '3':
            print('Unloading mods')
        elif opcion == '4':
            break
        else:
            print('Invalid option')