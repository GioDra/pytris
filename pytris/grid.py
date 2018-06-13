class Grid(object):

    #Griglia di gioco 3x3
    grid = []


    def __init__(self):
        self.BuildGrid()

    #Costruzione della griglia
    def BuildGrid(self):
        for x in range (0,3):
            new = []
            for y in range (0,3):
                new.append("*")
            self.grid.append(new)

    #Stampa griglia
    def PrintGrid(self):
        for x in range (0,3):
            msg=""
            for y in range (0,3):
                msg+=""+str(self.grid[x][y])+"\t"
            print(msg+"\n")

    #Controlla ed esegue inserimenti nella griglia
    def InsertGrid(self,y,x,mark):
        if self.grid[y][x]!="*":
            print("Input non valido")
            return False
        else:
            self.grid[y][x]=mark
            return True