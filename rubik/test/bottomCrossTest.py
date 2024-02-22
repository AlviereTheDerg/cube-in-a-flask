'''
Created on Feb 12, 2023

@author: Alviere
'''
import unittest
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomCross import _raiseBottomFaces
from rubik.controller.bottomCross import _raisePetal
from rubik.controller.bottomCross import _findPetalAndSlot
from rubik.controller.bottomCross import _findPetalToDrop
from rubik.controller.bottomCross import _dropBottomFaces
import re

class Test(unittest.TestCase):
    
    def setUp(self):
        self.solvedCross = re.compile(r".{7}b.{8}o.{8}g.{8}r.{11}y.y{3}.y.")
        self.raisedPetals = re.compile(r".{36}.y.ywy.y..{9}")
        self.colours = "bogrwy"
    
    
    def test_100_bottomCross_solvedCube(self):
        cubeString = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        theCube = Cube(cubeString)
        result = solveBottomCross(theCube)
        self.assertTrue(re.match(self.solvedCross,theCube.get()))
        self.assertEqual('',result)
        self.assertEqual(cubeString, theCube.get())
        
    def test_110_bottomCross_solvedCross(self):
        cubeString = 'rbybbgrboggwoorworrwbggbbgbowyrroorwwobrwwgwogygyyyyyy'
        theCube = Cube(cubeString)
        result = solveBottomCross(theCube)
        self.assertTrue(re.match(self.solvedCross,theCube.get()))
        self.assertEqual('',result)
        self.assertEqual(cubeString, theCube.get())
        
    def test_120_bottomCross_slightlyUnsolvedCross(self):
        cubeString = 'bbrbbbbbrwowoorygrrgygggbwogroorrwwooybywyyygwwgrywgoy'
        theCube = Cube(cubeString)
        result = solveBottomCross(theCube)
        self.assertTrue(re.match(self.solvedCross,theCube.get()))
        theOtherCube = Cube(cubeString)
        theOtherCube.rotate(result)
        self.assertEqual(theCube.get(),theOtherCube.get())
        
    def test_130_bottomCross_mildlyUnsolvedCross(self):
        cubeString = 'brybbwgoybwwoooorybgryggbgggrroryobrywoywrwgrwbgwybwyo'
        theCube = Cube(cubeString)
        result = solveBottomCross(theCube)
        self.assertTrue(re.match(self.solvedCross,theCube.get()))
        theOtherCube = Cube(cubeString)
        theOtherCube.rotate(result)
        self.assertEqual(theCube.get(),theOtherCube.get())
    
    
    def test_200_raisePetal_topRing(self):
        self.assertEqual('fUl',_raisePetal(FTM,UBM))
        self.assertEqual('rUf',_raisePetal(RTM,UMR))
        self.assertEqual('bUr',_raisePetal(BTM,UTM))
        self.assertEqual('lUb',_raisePetal(LTM,UML))
    
    def test_201_raisePetal_bottomRing(self):
        self.assertEqual('fuR',_raisePetal(FBM,UBM))
        self.assertEqual('ruB',_raisePetal(RBM,UMR))
        self.assertEqual('buL',_raisePetal(BBM,UTM))
        self.assertEqual('luF',_raisePetal(LBM,UML))
    
    def test_202_raisePetal_frontRing(self):
        self.assertEqual('F', _raisePetal(LMR,UBM))
        self.assertEqual('FF',_raisePetal(DTM,UBM))
        self.assertEqual('f', _raisePetal(RML,UBM))
        self.assertEqual('',  _raisePetal(UBM,UBM))
    
    def test_203_raisePetal_rightRing(self):
        self.assertEqual('R', _raisePetal(FMR,UMR))
        self.assertEqual('RR',_raisePetal(DMR,UMR))
        self.assertEqual('r', _raisePetal(BML,UMR))
        self.assertEqual('',  _raisePetal(UMR,UMR))
    
    def test_204_raisePetal_backRing(self):
        self.assertEqual('B', _raisePetal(RMR,UTM))
        self.assertEqual('BB',_raisePetal(DBM,UTM))
        self.assertEqual('b', _raisePetal(LML,UTM))
        self.assertEqual('',  _raisePetal(UTM,UTM))
    
    def test_205_raisePetal_leftRing(self):
        self.assertEqual('L', _raisePetal(BMR,UML))
        self.assertEqual('LL',_raisePetal(DML,UML))
        self.assertEqual('l', _raisePetal(FML,UML))
        self.assertEqual('',  _raisePetal(UML,UML))
        
    
    def test_210_raiseBottomFaces(self):
        theCube = Cube('brybbwgoybwwoooorybgryggbgggrroryobrywoywrwgrwbgwybwyo')
        _raiseBottomFaces(theCube, self.colours)
        self.assertTrue(re.match(self.raisedPetals,theCube.get()))
        
    def test_211_raiseBottomFaces(self):
        theCube = Cube('bogybrywororbogyoybwwrgwgyooyyrrrbbgggwowbrwwobbyygwgr')
        _raiseBottomFaces(theCube, self.colours)
        self.assertTrue(re.match(self.raisedPetals,theCube.get()))
        
    def test_212_raiseBottomFaces(self):
        theCube = Cube('goyybwoggbgogorrbrgrbbgygorobygrrwwbwwwowooyryrybyybww')
        _raiseBottomFaces(theCube, self.colours)
        self.assertTrue(re.match(self.raisedPetals,theCube.get()))
        
    def test_213_raiseBottomFaces(self):
        theCube = Cube('byyobgwwbgggrogwryryyogwrbbrgrbrborogbwywwwoogooyywyrb')
        _raiseBottomFaces(theCube, self.colours)
        self.assertTrue(re.match(self.raisedPetals,theCube.get()))
    
    
    def test_220_findPetalAndSlot_flippedFront(self):
        theCube = Cube.makeCube('oyybbgbwrbbgoooyrgwgbbggwbwyrgwrrbwooyoywyyorwogrygrwr')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [FTM,UBM]
        self.assertEqual(expected, result)
    
    def test_221_findPetalAndSlot_flippedRight(self):
        theCube = Cube.makeCube('oyybbgbwrbbgoooyrgwgbbggwbwyrgwrrbwooyoywyyorwogrygrwr')
        theCube.rotate('u')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [RTM,UMR]
        self.assertEqual(expected, result)
    
    def test_222_findPetalAndSlot_flippedBack(self):
        theCube = Cube.makeCube('oyybbgbwrbbgoooyrgwgbbggwbwyrgwrrbwooyoywyyorwogrygrwr')
        theCube.rotate('uu')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [BTM,UTM]
        self.assertEqual(expected, result)
    
    def test_223_findPetalAndSlot_flippedLeft(self):
        theCube = Cube.makeCube('oyybbgbwrbbgoooyrgwgbbggwbwyrgwrrbwooyoywyyorwogrygrwr')
        theCube.rotate('uuu')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [LTM,UML]
        self.assertEqual(expected, result)
    
        
    def test_230_findPetalAndSlot_bottomFront(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('rUF')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [FBM,UBM]
        self.assertEqual(expected, result)
        
    def test_231_findPetalAndSlot_bottomRight(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('bUR')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [RBM,UMR]
        self.assertEqual(expected, result)
        
    def test_232_findPetalAndSlot_bottomBack(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('lUB')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [BBM,UTM]
        self.assertEqual(expected, result)
        
    def test_233_findPetalAndSlot_bottomLeft(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('fUL')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [LBM,UML]
        self.assertEqual(expected, result)
    
    
    def test_240_findPetalAndSlot_frontRing(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('f')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [LMR,UBM]
        self.assertEqual(expected, result)
        theCube.rotate('f')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DTM,UBM]
        self.assertEqual(expected, result)
        theCube.rotate('f')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [RML,UBM]
        self.assertEqual(expected, result)
    
    def test_241_findPetalAndSlot_rightRing(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('r')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [FMR,UMR]
        self.assertEqual(expected, result)
        theCube.rotate('r')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DMR,UMR]
        self.assertEqual(expected, result)
        theCube.rotate('r')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [BML,UMR]
        self.assertEqual(expected, result)
    
    def test_242_findPetalAndSlot_backRing(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('b')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [RMR,UTM]
        self.assertEqual(expected, result)
        theCube.rotate('b')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DBM,UTM]
        self.assertEqual(expected, result)
        theCube.rotate('b')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [LML,UTM]
        self.assertEqual(expected, result)
    
    def test_243_findPetalAndSlot_leftRing(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('l')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [BMR,UML]
        self.assertEqual(expected, result)
        theCube.rotate('l')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DML,UML]
        self.assertEqual(expected, result)
        theCube.rotate('l')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [FML,UML]
        self.assertEqual(expected, result)
    
    
    def test_250_findPetalAndSlot_Misaligned(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('FFu')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DTM,UMR]
        self.assertEqual(expected, result)
        theCube.rotate('u')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DTM,UTM]
        self.assertEqual(expected, result)
        theCube.rotate('u')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DTM,UML]
        self.assertEqual(expected, result)
    
    def test_251_findPetalAndSlot_Optimization(self):
        theCube = Cube.makeCube('yobrbowbgwrggogobwogyrgbrobrbbwrwygbgyyywyoyrorwwyorwg')
        theCube.rotate('FFRRu')
        result = _findPetalAndSlot(theCube, self.colours)
        expected = [DMR,UMR]
        self.assertEqual(expected, result)
    
    
    def test_300_findPetalToDrop_SinglePetal(self):
        theCube = Cube.makeCube('wrwrboybwborworgorywybgoggbrgbgrgorggbbwwbrwooyoyyyyyw')
        theCube.rotate('FF')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UBM,'f']
        self.assertEqual(expected, result)
        theCube.rotate('FFRR')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UMR,'r']
        self.assertEqual(expected, result)
        theCube.rotate('RRBB')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UTM,'b']
        self.assertEqual(expected, result)
        theCube.rotate('BBLL')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UML,'l']
        self.assertEqual(expected, result)
    
    def test_301_findPetalToDrop_OffsetPetal(self):
        theCube = Cube.makeCube('wrwrboybwborworgorywybgoggbrgbgrgorggbbwwbrwooyoyyyyyw')
        theCube.rotate('FFu')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UMR,'f']
        self.assertEqual(expected, result)
        theCube.rotate('u')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UTM,'f']
        self.assertEqual(expected, result)
        theCube.rotate('u')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UML,'f']
        self.assertEqual(expected, result)
    
    def test_302_findPetalToDrop_Optimization(self):
        theCube = Cube.makeCube('wrwrboybwborworgorywybgoggbrgbgrgorggbbwwbrwooyoyyyyyw')
        theCube.rotate('FFBBUURR')
        result = _findPetalToDrop(theCube, self.colours)
        expected = [UMR,'r']
        self.assertEqual(expected, result)
    
    
    def test_310_dropBottomFaces(self):
        theCube = Cube.makeCube('wrggbwbrwobybobrgbbowogwowgrggrrorrobyrywyoyywbggywyoy')
        _dropBottomFaces(theCube, self.colours)
        self.assertTrue(re.fullmatch(self.solvedCross, theCube.get()))
    
    def test_311_dropBottomFaces(self):
        theCube = Cube.makeCube('brwbbrywrboowobyggggyogbwrbobywrrrwgbywywyryoooggyowgr')
        _dropBottomFaces(theCube, self.colours)
        self.assertTrue(re.fullmatch(self.solvedCross, theCube.get()))
    
    def test_312_dropBottomFaces_Optimization(self):
        theCube = Cube.makeCube('bwybbrybbrgyworwoborwbgorgggwybrworgrgboworggoyoyyywyw')
        result = _dropBottomFaces(theCube, self.colours)
        self.assertEqual('', result)
        
if __name__ == '__main__':
    unittest.main()