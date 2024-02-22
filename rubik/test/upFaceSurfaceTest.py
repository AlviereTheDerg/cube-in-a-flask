'''
Created on Apr 7, 2023

@author: Alviere
'''
import unittest
from rubik.model.constants import UTL,UTR,UBR,UBL
from rubik.model.cube import Cube
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upFaceSurface import _getSolveFromFish
import re


class Test(unittest.TestCase):


    def test_100_upCorners_solvedCube(self):
        theCube = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveUpSurface(theCube)
        self.assertEqual('', result) #Should not change anything, this bit is already solved
        
    def test_110_upCorners_scrambledCube(self):
        theCube = Cube.makeCube('wwogbyobwbowooggoybyrrgrgrbwgbyrwyoygboywwrbygrogybrwr')
        result = solveUpSurface(theCube)
        self.assertEqual('', result) #Should not change anything, prerequisites not met
        
    def test_120_upCorners_cornersSolved(self):
        theCube = Cube.makeCube('gobbbbbbbobgoooooorrrggggggbgorrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveUpSurface(theCube)
        self.assertEqual('', result) #Should not change anything, this bit is already solved
        
    def test_130_upCorners_diagonalCornersSolved(self):
        theCube = Cube.makeCube('grobbbbbbwbgoooooorgwggggggroorrrrrrbwwwwwwwbyyyyyyyyy')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_131_upCorners_diagonalCornersSolved(self):
        theCube = Cube.makeCube('grobbbbbbwbgoooooorgwggggggroorrrrrrbwwwwwwwbyyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_140_upCorners_adjacentCornersSolved(self):
        theCube = Cube.makeCube('rorbbbbbbbrgoooooowgwggggggbbgrrrrrrowowwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_141_upCorners_adjacentCornersSolved(self):
        theCube = Cube.makeCube('rorbbbbbbbrgoooooowgwggggggbbgrrrrrrowowwwwwwyyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_142_upCorners_adjacentCornersSolved(self):
        theCube = Cube.makeCube('rorbbbbbbbrgoooooowgwggggggbbgrrrrrrowowwwwwwyyyyyyyyy')
        theCube.rotate('uu')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_143_upCorners_adjacentCornersSolved(self):
        theCube = Cube.makeCube('rorbbbbbbbrgoooooowgwggggggbbgrrrrrrowowwwwwwyyyyyyyyy')
        theCube.rotate('U')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_150_upCorners_oneCornerSolved_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_151_upCorners_oneCornerSolved_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_152_upCorners_oneCornerSolved_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        theCube.rotate('uu')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_153_upCorners_oneCornerSolved_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        theCube.rotate('U')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_160_upCorners_oneCornerSolved_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_161_upCorners_oneCornerSolved_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_162_upCorners_oneCornerSolved_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        theCube.rotate('uu')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))
        
    def test_163_upCorners_oneCornerSolved_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        theCube.rotate('U')
        self.assertTrue(theCube.status('topcross'))
        result = solveUpSurface(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topsurface'))



    def test_200_getSolveFromFish_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UBL)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_201_getSolveFromFish_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UBR)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_202_getSolveFromFish_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        theCube.rotate('uu')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UTR)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_203_getSolveFromFish_clockwiseOffset(self):
        theCube = Cube.makeCube('robbbbbbbwrgoooooowgoggggggwbgrrrrrrbwowwwwwryyyyyyyyy')
        theCube.rotate('U')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UTL)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_210_getSolveFromFish_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UBL)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_211_getSolveFromFish_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UBR)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_212_getSolveFromFish_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        theCube.rotate('uu')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UTR)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
    def test_213_getSolveFromFish_counterClockwiseOffset(self):
        theCube = Cube.makeCube('rowbbbbbbrrwooooooogwggggggbbgrrrrrrowgwwwwwbyyyyyyyyy')
        theCube.rotate('U')
        self.assertTrue(theCube.status('topcross'))
        result = _getSolveFromFish(theCube, UTL)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        theCube.rotate(result)
        self.assertTrue(theCube.status('topsurface'))
        
if __name__ == '__main__':
    unittest.main()