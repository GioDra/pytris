import sys
from turno import Match
#from grid import Grid

def main(args=None):
    print('Benvenuto nel gioco del Tris')
    p1= input('Inserire il nome del primo giocatore: ')
    p2= input('Inserire il nome del secondo giocatore: ')
    print('Nomi giocatori: ',p1 ,p2)
    terminata = False
    t = Match(p1,p2)
    #g = Grid()
    #print(g.grid[1][2])

    while terminata != True:
       t.Turn()

if __name__ == '__main__':
    main(sys.argv[1:])
