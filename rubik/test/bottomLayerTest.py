'''
Created on Feb 28, 2023

@author: Alviere
'''
import unittest
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomLayer import _findPiecesToMove
from rubik.controller.bottomLayer import _movePieceToUp
from rubik.controller.bottomLayer import _dropPieceIntoSlot
import re


class Test(unittest.TestCase):


    def test_100_bottomLayer_solvedCube(self):
        theCube = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = solveBottomLayer(theCube)
        self.assertEqual('', result) #Should not change anything, this bit is already solved
        
    def test_110_bottomLayer_scrambledCube(self):
        theCube = Cube.makeCube('wwogbyobwbowooggoybyrrgrgrbwgbyrwyoygboywwrbygrogybrwr')
        result = solveBottomLayer(theCube)
        self.assertEqual('', result) #Should not change anything, prerequisites not met
        
    def test_120_bottomLayer_bottomCrossSolved(self):
        theCube = Cube.makeCube('bbygbrobwowyborbobgorggwwgrgwyrrogrgywobwgrobwyryyywyo')
        self.assertTrue(theCube.status('bottomcross'))
        result = solveBottomLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_130_bottomLayer_cornersRotatedInPlace(self):
        theCube = Cube.makeCube('wowwbbrbyrggworbogrrbwgoygrobgbrgyrywgwrwoowbbyoyyygyo')
        self.assertTrue(theCube.status('bottomcross'))
        result = solveBottomLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_140_bottomLayer_cornersMismatched(self):
        theCube = Cube.makeCube('owgrborborboborgorwgrwgobgbbgwwrborgwrbowwggwyyyyyyyyy')
        self.assertTrue(theCube.status('bottomcross'))
        result = solveBottomLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_150_bottomLayer_oneOutOfPlace(self):
        theCube = Cube.makeCube('wowbbobbbbrwgooooworgbgrbggowrbrwrrrygggwwgwoyyyyyyyyr')
        self.assertTrue(theCube.status('bottomcross'))
        result = solveBottomLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_160_bottomLayer_oneRotatedInPlace(self):
        theCube = Cube.makeCube('orrbbobbbbbogowoogwwrogryggwrwbrwrrrggbwwoggwyyyyyyyyo')
        self.assertTrue(theCube.status('bottomcross'))
        result = solveBottomLayer(theCube)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result))
        self.assertTrue(theCube.status('bottomlayer'))
    
    def test_200_findPiecesToMove_solvedCube(self):
        theCube = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        result = _findPiecesToMove(theCube)
        self.assertEqual(None, result) #No piece and slot to move
        
    def test_210_findPiecesToMove_onePairLeft(self):
        theCube = Cube.makeCube('wrbbbwbbowgrborboowoowgrgggbwgbrorrryggowwogryywyyyyyy')
        expected = {UTL:DTR}
        result = _findPiecesToMove(theCube)
        self.assertTrue(result[0] in expected.keys())
        self.assertTrue(result[1] in expected.values())
    
    def test_220_findPiecesToMove_bottomCrossSolved(self):
        theCube = Cube.makeCube('bwbgbwwborggbobboborgogwrggyoorrrorgrbygwwyoyrywyyywyw')
        expected = {UBL:DTR, UBR:DTL, UTR:DBR, LTL:DBL}
        result = _findPiecesToMove(theCube)
        self.assertTrue(result[0] in expected.keys())
        self.assertTrue(result[1] in expected.values())
    
    def test_230_findPiecesToMove_cornersRotatedInPlace(self):
        theCube = Cube.makeCube('wrgobwybywwgbogboyrboogbogrwrbrrwyrbbowgwgrworyoyyygyg')
        expected = {FBL:DTL, FBR:DTR, RBR:DBR, LBL:DBL}
        result = _findPiecesToMove(theCube)
        self.assertTrue(result[0] in expected.keys())
        self.assertTrue(result[1] in expected.values())
    
    def test_240_findPiecesToMove_cornersMismatched(self):
        theCube = Cube.makeCube('owrwbbobowrrrowgogbowogwrgroobbrgbrbgbwgwgwrgyyyyyyyyy')
        expected = {DTL:DTR, DTR:DBR, DBR:DBL, DBL:DTL}
        result = _findPiecesToMove(theCube)
        self.assertTrue(result[0] in expected.keys())
        self.assertTrue(result[1] in expected.values())
        
    def test_300_movePieceToUp_piecesInUp(self):
        pieces = {FTL,FTR,RTL,RTR,BTL,BTR,LTL,LTR,UTL,UTR,UBL,UBR}
        for piece in pieces:
            self.assertEqual('', _movePieceToUp(piece))
            
    def test_310_movePieceToUp_dflCorner(self):
        pieces = {LBR,FBL,DTL}
        for piece in pieces:
            self.assertEqual('Fuf', _movePieceToUp(piece))
            
    def test_320_movePieceToUp_dfrCorner(self):
        pieces = {FBR,RBL,DTR}
        for piece in pieces:
            self.assertEqual('Rur', _movePieceToUp(piece))
            
    def test_330_movePieceToUp_drbCorner(self):
        pieces = {RBR,BBL,DBR}
        for piece in pieces:
            self.assertEqual('Bub', _movePieceToUp(piece))
            
    def test_340_movePieceToUp_dblCorner(self):
        pieces = {BBR,LBL,DBL}
        for piece in pieces:
            self.assertEqual('Lul', _movePieceToUp(piece))
    
    def test_400_dropPieceIntoSlot_faceCheck(self):
        pieces = CORNERS - set(DOWN[0]) - set(DOWN[2]) - set(DOWN[4])
        for piece in pieces:
            result = _dropPieceIntoSlot(piece)
            self.assertEqual('d', Cube.faceOf(Cube.whereWillXBe(result, piece)))
        
    def test_410_dropPieceIntoSlot_UFL(self):
        pieces = {FTL,UBL,LTR}
        for piece in pieces:
            result = _dropPieceIntoSlot(piece)
            self.assertEqual(DTL, Cube.whereWillXBe(result, piece))
        
    def test_420_dropPieceIntoSlot_UFR(self):
        pieces = {RTL,UBR,FTR}
        for piece in pieces:
            result = _dropPieceIntoSlot(piece)
            self.assertEqual(DTR, Cube.whereWillXBe(result, piece))
        
    def test_430_dropPieceIntoSlot_URB(self):
        pieces = {BTL,UTR,RTR}
        for piece in pieces:
            result = _dropPieceIntoSlot(piece)
            self.assertEqual(DBR, Cube.whereWillXBe(result, piece))
        
    def test_440_dropPieceIntoSlot_UBL(self):
        pieces = {LTL,UTL,BTR}
        for piece in pieces:
            result = _dropPieceIntoSlot(piece)
            self.assertEqual(DBL, Cube.whereWillXBe(result, piece))
    
if __name__ == '__main__':
    unittest.main()