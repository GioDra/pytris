from grid import Grid

class Match(object):
    p1=""
    p2=""
    change = True

    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

        #Viene istanziato un oggetto di classe Grid per la gestione del 'campo' di gioco
        self.g = Grid();


    #Questo metodo permette di capire a chi tocca prima di iniziare la fase del turno vera e propria
    def Turn(self):
        if(self.change == True):
            p = self.p1
            self.change = False
        else:
            p = self.p2
            self.change = True
        print(p, ' è il tuo turno')
        self.Move(p)

    #Viene richiesto all'utente quale casella vuole riempire (griglia3x3)
    def Move(self,p):
        done = False
        while not(done):
            x=-1
            y=-1
            self.g.PrintGrid();
            while not x in range(0,3) or not y in range(0,3):
                try:
                    x = int(input("In quale colonna si vuole inserire la mossa? (1-3): "))-1
                except ValueError:
                    print("Input non valido")
                    x=-1
                try:
                    y = int(input("In quale riga si vuole inserire la mossa? (1-3): "))-1
                except ValueError:
                    print("Input non valido")
                    y=-1
            if (self.change):
                done = self.g.InsertGrid(y,x,"X")
            else:
                done = self.g.InsertGrid(y,x,"O")


    #Controllo delle clausole di conclusione del gioco
    def CheckEnd(self):
        #Controllo righe e colonne
        for x in range(0,3):
            y = 0
            if self.g.grid[x][y] != "*":
                if self.g.grid[x][y] == self.g.grid[x][y+1] and self.g.grid[x][y]==self.g.grid[x][y+2]:
                    print("Complimeti hai vinto (orizzontale)")
                    return True
            if self.g.grid[y][x] != "*":
                if self.g.grid[y][x] == self.g.grid[y+1][x] and self.g.grid[y][x]==self.g.grid[y+2][x]:
                    print("Complimeti hai vinto (verticale)")
                    return True


        #Controlle delle diagonali
        x=0
        y=0
        if self.g.grid[x][y] != "*":
            if self.g.grid[x][y] == self.g.grid[x+1][y+1] and self.g.grid[x][y] == self.g.grid[x+2][y+2]:
                print("Complimeti hai vinto (diagonale_1)")
                return True
        y=2
        if self.g.grid[x][y] != "*":
            if self.g.grid[x][y] == self.g.grid[x+1][y-1] and self.g.grid[x][y] == self.g.grid[x+2][y-2]:
                print("Complimenti hai vinto (diagonale_2)")
                return True
        y=0
        full= True
        while x < 3 and (full):
            for y in range(0,2):
                if self.g.grid[x][y]=="*":
                    full= False
            x+=1
        if(full):
            print("Pareggio")
            return True
        return False
