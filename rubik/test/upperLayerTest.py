'''
Created on Apr 14, 2023

@author: Alviere
'''
import unittest
from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.controller.upperLayer import solveUpperLayer
from rubik.controller.upperLayer import _solveCorners
from rubik.controller.upperLayer import _findCornersToSwap
from rubik.controller.upperLayer import _solveEdges
from rubik.controller.upperLayer import _findSolvedEdge
import re


class Test(unittest.TestCase):

# Tests for overall solving
    def test_100_solveUpperLayer_donothing_alreadySolved(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveUpperLayer(theCube)
        expected = ''
        self.assertEqual(expected, result)
    
    def test_101_solveUpperLayer_donothing_unmetPrereqs(self):
        theCube = Cube('ogyobwbrbgryroyrgwboobgwrggwwwbrbrrybyrowygyoobwgyoywg')
        result = solveUpperLayer(theCube)
        expected = ''
        self.assertEqual(expected, result)
    
    def test_110_solveUpperLayer_dosomething_topsurface(self):
        theCube = Cube('bbbbbbbbborgoooooorgogggggggorrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveUpperLayer(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
    
    def test_111_solveUpperLayer_dosomething_topcorners(self):
        theCube = Cube('bgbbbbbbborooooooogbgggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveUpperLayer(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
    
    def test_120_solveUpperLayer_solvethings_topsurface(self):
        theCube = Cube('bbbbbbbbborgoooooorgogggggggorrrrrrrwwwwwwwwwyyyyyyyyy')
        solveUpperLayer(theCube)
        self.assertTrue(theCube.status('solved'))
    
    def test_121_solveUpperLayer_solvethings_topcorners(self):
        theCube = Cube('bbbbbbbbborgoooooorgogggggggorrrrrrrwwwwwwwwwyyyyyyyyy')
        solveUpperLayer(theCube)
        self.assertTrue(theCube.status('solved'))


# Tests for solving the corners
    def test_200_solveCorners_donothing_alreadySolved(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = _solveCorners(theCube)
        expected = ''
        self.assertEqual(expected, result)
    
    def test_201_solveCorners_donothing_unmetPrereqs(self):
        theCube = Cube('ogyobwbrbgryroyrgwboobgwrggwwwbrbrrybyrowygyoobwgyoywg')
        result = _solveCorners(theCube)
        expected = ''
        self.assertEqual(expected, result)
    
    def test_210_solveCorners_swap1pair(self):
        theCube = Cube('bbobbbbbbgrboooooooggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topsurface'))
        result = _solveCorners(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('topcorners'))
    
    def test_211_solveCorners_swap1pair_androtate(self):
        theCube = Cube('grbbbbbbboggoooooororggggggbborrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topsurface'))
        result = _solveCorners(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('topcorners'))
    
    def test_220_solveCorners_swap2pair_androtate(self):
        theCube = Cube('bggbbbbbbroooooooogbbggggggorrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topsurface'))
        result = _solveCorners(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('topcorners'))
    

    def test_300_findCornersToSwap_twoInPlace(self):
        result = _findCornersToSwap('bbobbbbbbgrboooooooggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        expected = {'r'}
        self.assertIn(result, expected)
    
    def test_301_findCornersToSwap_twoOutOfPlace(self):
        result = _findCornersToSwap('grbbbbbbboggoooooororggggggbborrrrrrwwwwwwwwwyyyyyyyyy')
        expected = {'f'}
        self.assertIn(result, expected)
    
    def test_302_findCornersToSwap_twoOutOfPlace(self):
        result = _findCornersToSwap('oggbbbbbbroroooooobbogggggggrbrrrrrrwwwwwwwwwyyyyyyyyy')
        expected = {'l'}
        self.assertIn(result, expected)
    
    def test_303_findCornersToSwap_twoOutOfPlace(self):
        result = _findCornersToSwap('rorbbbbbbbbooooooogrbggggggoggrrrrrrwwwwwwwwwyyyyyyyyy')
        expected = {'b'}
        self.assertIn(result, expected)
    
    def test_310_findCornersToSwap_oneInPlace_diagonals(self):
        result = _findCornersToSwap('oggbbbbbbroroooooobbogggggggrbrrrrrrwwwwwwwwwyyyyyyyyy')
        expected = {'l','r','f','b'}
        self.assertIn(result, expected)
    
    def test_311_findCornersToSwap_oneOutOfPlace_diagonals(self):
        result = _findCornersToSwap('oggbbbbbbroroooooobbogggggggrbrrrrrrwwwwwwwwwyyyyyyyyy')
        expected = {'l','r','f','b'}
        self.assertIn(result, expected)
        
    def test_320_findCornersToSwap_cornersSolved_inPlace(self):
        result = _findCornersToSwap('bgbbbbbbborooooooogbgggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertFalse(result)
        
    def test_321_findCornersToSwap_cornersSolved_offset1(self):
        result = _findCornersToSwap('orobbbbbbgbgoooooororggggggbgbrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertFalse(result)
        
    def test_322_findCornersToSwap_cornersSolved_offset2(self):
        result = _findCornersToSwap('gbgbbbbbbroroooooobgbggggggororrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertFalse(result)
        
    def test_323_findCornersToSwap_cornersSolved_offset3(self):
        result = _findCornersToSwap('rorbbbbbbbgbooooooorogggggggbgrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertFalse(result)


# Tests for solving the edges
    def test_400_solveEdges_donothing_alreadySolved(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = _solveEdges(theCube)
        expected = ''
        self.assertEqual(expected, result)
    
    def test_401_solveEdges_donothing_unmetPrereqs(self):
        theCube = Cube('ogyobwbrbgryroyrgwboobgwrggwwwbrbrrybyrowygyoobwgyoywg')
        result = _solveEdges(theCube)
        expected = ''
        self.assertEqual(expected, result)
    
    def test_410_solveEdges_frontsolved_CWoffset(self):
        theCube = Cube('bbbbbbbbbogooooooogrgggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_411_solveEdges_frontsolved_CCWoffset(self):
        theCube = Cube('bbbbbbbbborooooooogogggggggrgrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_412_solveEdges_rightsolved_CWoffset(self):
        theCube = Cube('bgbbbbbbbooooooooogrgggggggrbrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_413_solveEdges_rightsolved_CCWoffset(self):
        theCube = Cube('brbbbbbbbooooooooogbgggggggrgrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_414_solveEdges_backsolved_CWoffset(self):
        theCube = Cube('bobbbbbbborooooooogggggggggrbrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_415_solveEdges_backsolved_CCWoffset(self):
        theCube = Cube('brbbbbbbbobooooooogggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_416_solveEdges_leftsolved_CWoffset(self):
        theCube = Cube('bobbbbbbbogooooooogbgggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_417_solveEdges_leftsolved_CCWoffset(self):
        theCube = Cube('bgbbbbbbbobooooooogogggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_420_solveEdges_crossed_pairs(self):
        theCube = Cube('bgbbbbbbborooooooogbgggggggrorrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_421_solveEdges_neighbours1(self):
        theCube = Cube('brbbbbbbbogooooooogogggggggrbrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    def test_422_solveEdges_neighbours2(self):
        theCube = Cube('bobbbbbbbobooooooogrgggggggrgrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(theCube.status('topcorners'))
        result = _solveEdges(theCube)
        self.assertTrue(re.fullmatch(VALID_ROTATE_SYMBOLS, result))
        self.assertTrue(theCube.status('toplayer'))
    
    
    def test_500_findSolvedEdge_fullsolved(self):
        result = _findSolvedEdge(Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertFalse(result)
    
    def test_510_findSolvedEdge_1solved_front(self):
        result = _findSolvedEdge(Cube.makeCube('bbbbbbbbbogooooooogrgggggggrorrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertEqual('f', result)
    
    def test_511_findSolvedEdge_1solved_right(self):
        result = _findSolvedEdge(Cube.makeCube('bgbbbbbbbooooooooogrgggggggrbrrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertEqual('r', result)
    
    def test_512_findSolvedEdge_1solved_back(self):
        result = _findSolvedEdge(Cube.makeCube('bobbbbbbborooooooogggggggggrbrrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertEqual('b', result)
    
    def test_513_findSolvedEdge_1solved_left(self):
        result = _findSolvedEdge(Cube.makeCube('bobbbbbbbogooooooogbgggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertEqual('l', result)
    
    def test_520_findSolvedEdge_0solved_crossed(self):
        result = _findSolvedEdge(Cube.makeCube('bgbbbbbbborooooooogbgggggggrorrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertIn(result, {'f','r','b','l'})
    
    def test_521_findSolvedEdge_0solved_neighbours1(self):
        result = _findSolvedEdge(Cube.makeCube('brbbbbbbbogooooooogogggggggrbrrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertIn(result, {'f','r','b','l'})
    
    def test_521_findSolvedEdge_0solved_neighbours2(self):
        result = _findSolvedEdge(Cube.makeCube('bobbbbbbbobooooooogrgggggggrgrrrrrrrwwwwwwwwwyyyyyyyyy'))
        self.assertIn(result, {'f','r','b','l'})
        
if __name__ == '__main__':
    unittest.main()