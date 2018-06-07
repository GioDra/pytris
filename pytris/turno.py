from grid import Grid

class Match(object):
    p1=""
    p2=""
    change = True

    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.g = Grid();

    def Turn(self):
        if(self.change == True):
            p = self.p1
            self.change = False
        else:
            p = self.p2
            self.change = True
        print(p, ' è il tuo turno')
        self.Move(p)

    def Move(self,p):
        done = False
        while not(done):
            x=-1
            y=-1
            self.g.PrintGrid();
            while not x in range(0,3) and not y in range(0,3):
                x = int(input("In quale colonna si vuole inserire la mossa? (1-3): "))-1
                y = int(input("In quale riga si vuole inserire la mossa? (1-3): "))-1
            if (self.change):
                done = self.g.InsertGrid(y,x,"X")
            else:
                done = self.g.InsertGrid(y,x,"O")

    def CheckEnd(self):
        #Controllo righe e colonne
        for x in range(0,3):
            y = 0
            if self.g.grid[x][y] != "*":
                if self.g.grid[x][y] == self.g.grid[x][y+1] and self.g.grid[x][y]==self.g.grid[x][y+2]:
                    print("Complimeti hai vinto")
                    return True
                if self.g.grid[y][x] == self.g.grid[y+1][x] and self.g.grid[y][x]==self.g.grid[y+2][x]:
                    print("Complimeti hai vinto")
                    return True

        #Controlle delle diagonali
        x=0
        y=0
        if self.g.grid[x][y] != "*":
            if self.g.grid[x][y] == self.g.grid[x+1][y+1] and self.g.grid[x][y] == self.g.grid[x+2][y+2]:
                print("Complimeti hai vinto")
                return True
        y=2
        if self.g.grid[x][y] != "*":
            if self.g.grid[x][y] == self.g.grid[x+1][y-1] and self.g.grid[x][y] == self.g.grid[x+2][y-2]:
                print("Complimenti hai vinto")
                return True
        return False
