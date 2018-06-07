class Grid(object):

    grid = []


    def __init__(self):
        self.BuildGrid()

    def BuildGrid(self):
        for x in range (0,3):
            new = []
            for y in range (0,3):
                new.append("*")
            self.grid.append(new)
        #self.PrintGrid()

    def PrintGrid(self):
        for x in range (0,3):
            msg=""
            for y in range (0,3):
                msg+=""+str(self.grid[x][y])+"\t"
            print(msg+"\n")

    def InsertGrid(self,y,x,mark):
        if self.grid[y][x]!="*":
            print("Input non valido")
            return False
        else:
            self.grid[y][x]=mark
            return True