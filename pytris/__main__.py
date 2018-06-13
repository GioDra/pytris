import sys
from turno import Match

'''
Gioco del tris
'''

'''
Nel main di questo programam vengono solo richiesti i nomi dei giocatori, il resto della partita sarà gestito da un oggetto
di classe Turno
'''

def main(args=None):
    print('Benvenuto nel gioco del Tris')
    p1= input('Inserire il nome del primo giocatore: ')
    p2= input('Inserire il nome del secondo giocatore: ')
    print('Nomi giocatori: ',p1 ,p2)
    terminata = False
    t = Match(p1,p2)

    while not (terminata):
       t.Turn()
       terminata = t.CheckEnd()

if __name__ == '__main__':
    main(sys.argv[1:])
