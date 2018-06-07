import sys
from turno import Partita


def main(args=None):
    print('Benvenuto nel gioco del Tris')
    p1= input('Inserire il nome del primo giocatore: ')
    p2= input('Inserire il nome del secondo giocatore: ')
    print('Nomi giocatori: ',p1 ,p2)
    terminata = False
    t = Partita(p1,p2)

    while terminata != True:
        t.Turno()

if __name__ == '__main__':
    main(sys.argv[1:])
