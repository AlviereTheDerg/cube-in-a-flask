'''
Created on Apr 7, 2023

@author: Alviere
'''
import unittest
from rubik.model.cube import Cube
from rubik.controller.upFaceCross import solveUpCross
import re


class Test(unittest.TestCase):

    def test_100_topCross_solvedCube(self):
        theCube = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveUpCross(theCube)
        self.assertEqual('', result) #Should not change anything, this bit is already solved
        
    def test_110_topCross_scrambledCube(self):
        theCube = Cube.makeCube('wwogbyobwbowooggoybyrrgrgrbwgbyrwyoygboywwrbygrogybrwr')
        result = solveUpCross(theCube)
        self.assertEqual('', result) #Should not change anything, prerequisites not met
        
    def test_120_topCross_dotShapeTop(self):
        theCube = Cube.makeCube('gwbbbbbbbowwoooooogwbggggggwworrrrrrrbrowrwgwyyyyyyyyy')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
    def test_130_topCross_horizontallineShapeTop(self):
        theCube = Cube.makeCube('gwbbbbbbbogwoooooogwbggggggwrorrrrrrrbrwwwwowyyyyyyyyy')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
    def test_140_topCross_verticallineShapeTop(self):
        theCube = Cube.makeCube('ogwbbbbbbgwboooooowrogggggggwbrrrrrrwwrowbwwryyyyyyyyy')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
    def test_150_topCross_downleftShapeTop(self):
        theCube = Cube.makeCube('rrrbbbbbbbwwooooooowoggggggwbgrrrrrrbogwwgwwwyyyyyyyyy')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
    def test_160_topCross_downrightShapeTop(self):
        theCube = Cube.makeCube('rrrbbbbbbbwwooooooowoggggggwbgrrrrrrbogwwgwwwyyyyyyyyy')
        theCube.rotate('u')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
    def test_170_topCross_uprightShapeTop(self):
        theCube = Cube.makeCube('rrrbbbbbbbwwooooooowoggggggwbgrrrrrrbogwwgwwwyyyyyyyyy')
        theCube.rotate('uu')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
    def test_180_topCross_upleftShapeTop(self):
        theCube = Cube.makeCube('rrrbbbbbbbwwooooooowoggggggwbgrrrrrrbogwwgwwwyyyyyyyyy')
        theCube.rotate('U')
        self.assertTrue(theCube.status('middlelayer'))
        result = solveUpCross(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('topcross'))
        
if __name__ == '__main__':
    unittest.main()