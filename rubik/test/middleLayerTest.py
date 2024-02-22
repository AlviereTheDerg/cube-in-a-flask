'''
Created on Mar 24, 2023

@author: Alviere
'''
import unittest
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.middleLayer import _findMiddleEdges
import re


class Test(unittest.TestCase):


    def test_100_middleLayer_solvedCube(self):
        theCube = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveMiddleLayer(theCube)
        self.assertEqual('', result) #Should not change anything, this bit is already solved
        
    def test_110_middleLayer_scrambledCube(self):
        theCube = Cube.makeCube('wwogbyobwbowooggoybyrrgrgrbwgbyrwyoygboywwrbygrogybrwr')
        result = solveMiddleLayer(theCube)
        self.assertEqual('', result) #Should not change anything, prerequisites not met
        
    def test_120_middleLayer_bottomLayerSolved(self):
        theCube = Cube.makeCube('obrwbbbbbwgwwogooooorwgrgggbrbwrorrrwbggwowrgyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = solveMiddleLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_130_middleLayer_edgesRotatedInPlace(self):
        theCube = Cube.makeCube('obrrbobbbbrbbogooooorogrgggwgwgrbrrrgwwwwwgwwyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = solveMiddleLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_140_middleLayer_edgesMismatched(self):
        theCube = Cube.makeCube('owrobgbbbwwwoogoooogrrgbgggbobrrbrrrwwgwwrwbgyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = solveMiddleLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_150_middleLayer_oneOutOfPlace(self):
        theCube = Cube.makeCube('oorbbbbbbwgwoorooooorwgggggbbbrrrrrrwggwwwwwgyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = solveMiddleLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_160_middleLayer_oneRotatedInPlace(self):
        theCube = Cube.makeCube('bbbbbbbbbooroogooowwwogggggogrrrrrrrgrgwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = solveMiddleLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('middlelayer'))
    
    


    def test_200_findMiddleEdges_solvedCube(self):
        theCube = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = _findMiddleEdges(theCube)
        expected = {}
        self.assertTrue(result.issubset(expected))
        self.assertEqual(0, len(result))
        
    def test_220_findMiddleEdges_bottomLayerSolved(self):
        theCube = Cube.makeCube('obrwbbbbbwgwwogooooorwgrgggbrbwrorrrwbggwowrgyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = _findMiddleEdges(theCube)
        expected = {FTM, RTM, BTM, LTM}
        self.assertTrue(result.issubset(expected))
        self.assertEqual(4, len(result))
        
    def test_230_findMiddleEdges_edgesRotatedInPlace(self):
        theCube = Cube.makeCube('obrrbobbbbrbbogooooorogrgggwgwgrbrrrgwwwwwgwwyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = _findMiddleEdges(theCube)
        expected = {FML, FMR, RML, RMR, BML, BMR, LML, LMR}
        self.assertTrue(result.issubset(expected))
        self.assertEqual(4, len(result))
        
    def test_240_findMiddleEdges_edgesMismatched(self):
        theCube = Cube.makeCube('owrobgbbbwwwoogoooogrrgbgggbobrrbrrrwwgwwrwbgyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = _findMiddleEdges(theCube)
        expected = {FML, FMR, RML, RMR, BML, BMR, LML, LMR}
        self.assertTrue(result.issubset(expected))
        self.assertEqual(4, len(result))
        
    def test_250_findMiddleEdges_oneOutOfPlace(self):
        theCube = Cube.makeCube('oorbbbbbbwgwoorooooorwgggggbbbrrrrrrwggwwwwwgyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = _findMiddleEdges(theCube)
        expected = {BTM}
        self.assertTrue(result.issubset(expected))
        self.assertEqual(1, len(result))
        
    def test_260_findMiddleEdges_oneRotatedInPlace(self):
        theCube = Cube.makeCube('bbbbbbbbbooroogooowwwogggggogrrrrrrrgrgwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('bottomlayer'))
        result = _findMiddleEdges(theCube)
        expected = {RMR, BML}
        self.assertTrue(result.issubset(expected))
        self.assertEqual(1, len(result))
        
if __name__ == '__main__':
    unittest.main()