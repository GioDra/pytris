import sys



def main(args=None):
    print('Benvenuto nel gioco del Tris')
    p1= input('Inserire il nome del primo giocatore: ')
    p2= input('Inserire il nome del secondo giocatore: ')
    print('Nomi giocatori: ',p1 ,p2)


if __name__ == '__main__':
    main(sys.argv[1:])
