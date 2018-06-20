from unittest import TestCase
from pytris.grid import Grid
from pytris.turno import Match


class SampleTestCase(TestCase):
    def test_pass(self):
        self.assertTrue("dummy sample test")

    def test_grid_building(self):
        g = Grid()
        g.BuildGrid()
        self.assertEqual(len(g.grid[0]),3)
        self.assertEqual(len(g.grid[1]),3)
        self.assertEqual(len(g.grid[2]),3)
        self.assertListEqual(g.grid[0],['*','*','*'])
        self.assertListEqual(g.grid[1],['*','*','*'])
        self.assertListEqual(g.grid[2],['*','*','*'])

    def test_inputGrid(self):
        f = Grid()
        f.BuildGrid()
        self.assertTrue(f.InsertGrid(1,2,"X"))
        self.assertFalse(f.InsertGrid(1,2,"S"))

    def test_checkWinCombination(self):
        d=Match("p1","p2")

        #Test colonna
        d.g.grid[0][0] ="x"
        d.g.grid[0][1] ="x"
        d.g.grid[0][2] ="x"
        self.assertEqual(d.CheckEnd(),True)
        d.g.grid[0][0] ="*"
        d.g.grid[0][1] ="*"
        d.g.grid[0][2] ="*"

        #Test riga
        d.g.grid[0][0] ="x"
        d.g.grid[1][0] ="x"
        d.g.grid[2][0] ="x"
        self.assertEqual(d.CheckEnd(),True)
        d.g.grid[0][0] ="*"
        d.g.grid[1][0] ="*"
        d.g.grid[2][0] ="*"

        #Test diagonale
        d.g.grid[0][0] ="x"
        d.g.grid[1][1] ="x"
        d.g.grid[2][2] ="x"
        self.assertEqual(d.CheckEnd(),True)
        d.g.grid[0][0] ="*"
        d.g.grid[1][1] ="*"
        d.g.grid[2][2] ="*"

        #Test tabella piena senza vicinta
        d.g.grid[0][0] ="x"
        d.g.grid[0][1] ="y"
        d.g.grid[0][2] ="x"
        d.g.grid[1][0] ="x"
        d.g.grid[1][1] ="x"
        d.g.grid[1][2] ="y"
        d.g.grid[2][0] ="y"
        d.g.grid[2][1] ="x"
        d.g.grid[2][2] ="y"
        self.assertEqual(d.CheckEnd(),True)
        d.g.grid[0][0] ="*"
        d.g.grid[0][1] ="*"
        d.g.grid[0][2] ="*"
        d.g.grid[1][0] ="*"
        d.g.grid[1][1] ="*"
        d.g.grid[1][2] ="*"
        d.g.grid[2][0] ="*"
        d.g.grid[2][1] ="*"
        d.g.grid[2][2] ="*"

        #Test controllo griglia senza vicincita e partita ancora in corso
        d.g.grid[0][0] ="x"
        d.g.grid[0][1] ="y"
        d.g.grid[0][2] ="x"
        self.assertEqual(d.CheckEnd(),False)
        d.g.grid[0][0] ="*"
        d.g.grid[0][1] ="*"
        d.g.grid[0][2] ="*"












