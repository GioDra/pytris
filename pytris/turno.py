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

