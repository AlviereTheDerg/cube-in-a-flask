'''
Created on Jan 31, 2023

@author: Alviere
'''
from unittest import TestCase
from rubik.model.cube import Cube
from rubik.model.constants import *


class Test(TestCase):
    
    def setUp(self):
        self.scrambledCube = Cube('ogyobwbrbgryroyrgwboobgwrggwwwbrbrrybyrowygyoobwgyoywg')
        # Gotten from scrambling my cube, used to test the individual face turns
        # If faces were homogeneous, then the corners/edges of the rotated face would be ambiguous in a rotation
        
        self.solvedCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        # Used to test multi-face rotations, once it is known that single-face turns work
    
#    Individual face turns
    def test_100_turnFrontClock(self):
        self.scrambledCube._turn('F')
        self.assertEqual('boorbgbwygryyoyogwboobgwrggwwobrbrrwbyrowyybwrrggyoywg', self.scrambledCube.get())
    
    def test_101_turnRightClock(self):
        self.scrambledCube._turn('R')
        self.assertEqual('ogwobobrgrrggorwyyoooygwrggwwwbrbrrybyyowwgybobrgybywb', self.scrambledCube.get())
    
    def test_102_turnBackClock(self):
        self.scrambledCube._turn('B')
        self.assertEqual('ogyobwbrbgrgrowrgyrbbggogworwwyrbbryyywowygyoobwgyowbr', self.scrambledCube.get())
    
    def test_103_turnLeftClock(self):
        self.scrambledCube._turn('L')
        self.assertEqual('bgyobwgrbgryroyrgwboybggrgorbwrrwybwgyrwwyoyoobwoyobwg', self.scrambledCube.get())
    
    def test_104_turnUpClock(self):
        self.scrambledCube._turn('U')
        self.assertEqual('gryobwbrbbooroyrgwwwwbgwrggogybrbrrygobywyoyrobwgyoywg', self.scrambledCube.get())
    
    def test_105_turnFrontCounter(self):
        self.scrambledCube._turn('f')
        self.assertEqual('ywbgbroobwryboyogwboobgwrggwwobryrrgbyrowygrrwbygyoywg', self.scrambledCube.get())
    
    def test_106_turnRightCounter(self):
        self.scrambledCube._turn('r')
        self.assertEqual('ogrobybroyywroggrrgooogwwggwwwbrbrrybyrowbgybobygywywb', self.scrambledCube.get())
    
    def test_107_turnBackCounter(self):
        self.scrambledCube._turn('b')
        self.assertEqual('ogyobwbrbgrbroyrgrowgoggbbrywwwrbgryrbwowygyoobwgyowyy', self.scrambledCube.get())
    
    def test_108_turnLeftCounter(self):
        self.scrambledCube._turn('l')
        self.assertEqual('ogygbwyrbgryroyrgwbogbgorgbwbywrrwbroyrowybyogbwwyoowg', self.scrambledCube.get())
    
    def test_109_turnUpCounter(self):
        self.scrambledCube._turn('u')
        self.assertEqual('wwwobwbrbogyroyrgwgrybgwrggboobrbrryryoywybogobwgyoywg', self.scrambledCube.get())
    
    def test_110_rotateSingle(self):
        self.solvedCube.rotate('F')
        self.assertEqual('bbbbbbbbbwoowoowoogggggggggrryrryrrywwwwwwrrroooyyyyyy', self.solvedCube.get())
    
    def test_120_twoTurns(self):
        self.solvedCube.rotate('Fr')
        self.assertEqual('bbwbbwbbroooooowwwyggyggoggrryrryrrywwgwwgrrgoobyybyyb', self.solvedCube.get())
    
    def test_130_tenTurns(self):
        self.solvedCube.rotate('FrBlUfRbLu')
        self.assertEqual('yryrbboyrgwwwobyyrgobyggwowywrwrbggwobrrwobgobrgoygoyb', self.solvedCube.get())
        
    def test_140_makeCube(self):
        result = Cube.makeCube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        self.assertTrue(isinstance(result, Cube))
        self.assertEqual('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy', result.get())
        
    def test_160_faceOf_front(self):
        self.assertEqual('f',Cube.faceOf(FMR))
    
    def test_161_faceOf_right(self):
        self.assertEqual('r',Cube.faceOf(RBL))
        
    def test_162_faceOf_back(self):
        self.assertEqual('b',Cube.faceOf(BTR))
        
    def test_163_faceOf_left(self):
        self.assertEqual('l',Cube.faceOf(LBM))
    
    def test_164_faceOf_top(self):
        self.assertEqual('u',Cube.faceOf(UMM))
    
    def test_165_faceOf_bottom(self):
        self.assertEqual('d',Cube.faceOf(DML))
    
    def test_180_facesTouching_Front(self):
        self.assertEqual('r',Cube.facesTouching(FMR))
        self.assertEqual('u',Cube.facesTouching(FTM))
        self.assertEqual('l',Cube.facesTouching(FML))
        self.assertEqual('d',Cube.facesTouching(FBM))
    
    def test_181_facesTouching_Right(self):
        self.assertEqual('b',Cube.facesTouching(RMR))
        self.assertEqual('u',Cube.facesTouching(RTM))
        self.assertEqual('f',Cube.facesTouching(RML))
        self.assertEqual('d',Cube.facesTouching(RBM))
    
    def test_182_facesTouching_Back(self):
        self.assertEqual('l',Cube.facesTouching(BMR))
        self.assertEqual('u',Cube.facesTouching(BTM))
        self.assertEqual('r',Cube.facesTouching(BML))
        self.assertEqual('d',Cube.facesTouching(BBM))
    
    def test_183_facesTouching_Left(self):
        self.assertEqual('f',Cube.facesTouching(LMR))
        self.assertEqual('u',Cube.facesTouching(LTM))
        self.assertEqual('b',Cube.facesTouching(LML))
        self.assertEqual('d',Cube.facesTouching(LBM))
    
    def test_184_facesTouching_Up(self):
        self.assertEqual('r',Cube.facesTouching(UMR))
        self.assertEqual('b',Cube.facesTouching(UTM))
        self.assertEqual('l',Cube.facesTouching(UML))
        self.assertEqual('f',Cube.facesTouching(UBM))
    
    def test_185_facesTouching_Down(self):
        self.assertEqual('r',Cube.facesTouching(DMR))
        self.assertEqual('f',Cube.facesTouching(DTM))
        self.assertEqual('l',Cube.facesTouching(DML))
        self.assertEqual('b',Cube.facesTouching(DBM))
    
    def test_1860_facesTouching_FrontCorners(self):
        self.assertEqual('lu',Cube.facesTouching(FTL))
        self.assertEqual('ur',Cube.facesTouching(FTR))
        self.assertEqual('rd',Cube.facesTouching(FBR))
        self.assertEqual('dl',Cube.facesTouching(FBL))
    
    def test_1861_facesTouching_RightCorners(self):
        self.assertEqual('fu',Cube.facesTouching(RTL))
        self.assertEqual('ub',Cube.facesTouching(RTR))
        self.assertEqual('bd',Cube.facesTouching(RBR))
        self.assertEqual('df',Cube.facesTouching(RBL))
    
    def test_1862_facesTouching_BackCorners(self):
        self.assertEqual('ru',Cube.facesTouching(BTL))
        self.assertEqual('ul',Cube.facesTouching(BTR))
        self.assertEqual('ld',Cube.facesTouching(BBR))
        self.assertEqual('dr',Cube.facesTouching(BBL))
    
    def test_1863_facesTouching_LeftCorners(self):
        self.assertEqual('bu',Cube.facesTouching(LTL))
        self.assertEqual('uf',Cube.facesTouching(LTR))
        self.assertEqual('fd',Cube.facesTouching(LBR))
        self.assertEqual('db',Cube.facesTouching(LBL))
    
    def test_1864_facesTouching_TopCorners(self):
        self.assertEqual('lb',Cube.facesTouching(UTL))
        self.assertEqual('br',Cube.facesTouching(UTR))
        self.assertEqual('rf',Cube.facesTouching(UBR))
        self.assertEqual('fl',Cube.facesTouching(UBL))
    
    def test_1865_facesTouching_BottomCorners(self):
        self.assertEqual('lf',Cube.facesTouching(DTL))
        self.assertEqual('fr',Cube.facesTouching(DTR))
        self.assertEqual('rb',Cube.facesTouching(DBR))
        self.assertEqual('bl',Cube.facesTouching(DBL))
        
    def test_190_alignPiece_Front(self):
        self.assertEqual('F', Cube.alignPiece(FTM,'r'))
        self.assertEqual('FF',Cube.alignPiece(FMR,'l'))
        self.assertEqual('f', Cube.alignPiece(FBM,'r'))
        self.assertEqual('',  Cube.alignPiece(FML,'l'))
        
    def test_191_alignPiece_Right(self):
        self.assertEqual('R', Cube.alignPiece(RTM,'b'))
        self.assertEqual('RR',Cube.alignPiece(RMR,'f'))
        self.assertEqual('r', Cube.alignPiece(RBM,'b'))
        self.assertEqual('',  Cube.alignPiece(RML,'f'))
        
    def test_192_alignPiece_Back(self):
        self.assertEqual('BB',Cube.alignPiece(BTM,'d'))
        self.assertEqual('B', Cube.alignPiece(BMR,'d'))
        self.assertEqual('',  Cube.alignPiece(BBM,'d'))
        self.assertEqual('b', Cube.alignPiece(BML,'d'))
        
    def test_193_alignPiece_Left(self):
        self.assertEqual('l', Cube.alignPiece(LTM,'b'))
        self.assertEqual('',  Cube.alignPiece(LMR,'f'))
        self.assertEqual('L', Cube.alignPiece(LBM,'b'))
        self.assertEqual('LL',Cube.alignPiece(LML,'f'))
        
    def test_194_alignPiece_Up(self):
        self.assertEqual('U', Cube.alignPiece(UTM,'r'))
        self.assertEqual('UU',Cube.alignPiece(UMR,'l'))
        self.assertEqual('u', Cube.alignPiece(UBM,'r'))
        self.assertEqual('',  Cube.alignPiece(UML,'l'))
        
    def test_195_alignPiece_Down(self):
        self.assertEqual('D', Cube.alignPiece(DTM,'r'))
        self.assertEqual('DD',Cube.alignPiece(DMR,'l'))
        self.assertEqual('d', Cube.alignPiece(DBM,'r'))
        self.assertEqual('',  Cube.alignPiece(DML,'l'))
        
    def test_190_alignPiece_1_Front(self):
        self.assertEqual('u', Cube.alignPiece(FTM,'r',1))
        self.assertEqual('RR',Cube.alignPiece(FMR,'b',1))
        self.assertEqual('d', Cube.alignPiece(FBM,'l',1))
        self.assertEqual('',  Cube.alignPiece(FML,'f',1))
        
    def test_191_alignPiece_1_Right(self):
        self.assertEqual('u', Cube.alignPiece(RTM,'b',1))
        self.assertEqual('BB',Cube.alignPiece(RMR,'l',1))
        self.assertEqual('d', Cube.alignPiece(RBM,'f',1))
        self.assertEqual('',  Cube.alignPiece(RML,'r',1))
        
    def test_192_alignPiece_1_Back(self):
        self.assertEqual('u', Cube.alignPiece(BTM,'l',1))
        self.assertEqual('LL',Cube.alignPiece(BMR,'f',1))
        self.assertEqual('d', Cube.alignPiece(BBM,'r',1))
        self.assertEqual('',  Cube.alignPiece(BML,'b',1))
        
    def test_193_alignPiece_1_Left(self):
        self.assertEqual('u', Cube.alignPiece(LTM,'f',1))
        self.assertEqual('FF',Cube.alignPiece(LMR,'r',1))
        self.assertEqual('d', Cube.alignPiece(LBM,'b',1))
        self.assertEqual('',  Cube.alignPiece(LML,'l',1))
        
    def test_194_alignPiece_1_Up(self):
        self.assertEqual('b', Cube.alignPiece(UTM,'r',1))
        self.assertEqual('RR',Cube.alignPiece(UMR,'d',1))
        self.assertEqual('f', Cube.alignPiece(UBM,'l',1))
        self.assertEqual('',  Cube.alignPiece(UML,'u',1))
        
    def test_195_alignPiece_1_Down(self):
        self.assertEqual('f', Cube.alignPiece(DTM,'r',1))
        self.assertEqual('RR',Cube.alignPiece(DMR,'u',1))
        self.assertEqual('b', Cube.alignPiece(DBM,'l',1))
        self.assertEqual('',  Cube.alignPiece(DML,'d',1))
    
    def test_200cycleOf_Front(self):
        self.assertEqual(FRONT,Cube.cycleOf('f'))
    
    def test_201cycleOf_Right(self):
        self.assertEqual(RIGHT,Cube.cycleOf('r'))
    
    def test_202cycleOf_Back(self):
        self.assertEqual(BACK,Cube.cycleOf('b'))
    
    def test_203cycleOf_Left(self):
        self.assertEqual(LEFT,Cube.cycleOf('l'))
    
    def test_204cycleOf_Up(self):
        self.assertEqual(UP,Cube.cycleOf('u'))
    
    def test_205cycleOf_Down(self):
        self.assertEqual(DOWN,Cube.cycleOf('d'))
    
    def test_210_otherPieceOf_FrontEdges(self):
        self.assertEqual(UBM,Cube.otherPieceOf(FTM))
        self.assertEqual(RML,Cube.otherPieceOf(FMR))
        self.assertEqual(DTM,Cube.otherPieceOf(FBM))
        self.assertEqual(LMR,Cube.otherPieceOf(FML))
    
    def test_211_otherPieceOf_RightEdges(self):
        self.assertEqual(UMR,Cube.otherPieceOf(RTM))
        self.assertEqual(BML,Cube.otherPieceOf(RMR))
        self.assertEqual(DMR,Cube.otherPieceOf(RBM))
        self.assertEqual(FMR,Cube.otherPieceOf(RML))
    
    def test_212_otherPieceOf_BackEdges(self):
        self.assertEqual(UTM,Cube.otherPieceOf(BTM))
        self.assertEqual(LML,Cube.otherPieceOf(BMR))
        self.assertEqual(DBM,Cube.otherPieceOf(BBM))
        self.assertEqual(RMR,Cube.otherPieceOf(BML))
    
    def test_213_otherPieceOf_LeftEdges(self):
        self.assertEqual(UML,Cube.otherPieceOf(LTM))
        self.assertEqual(FML,Cube.otherPieceOf(LMR))
        self.assertEqual(DML,Cube.otherPieceOf(LBM))
        self.assertEqual(BMR,Cube.otherPieceOf(LML))
    
    def test_214_otherPieceOf_TopEdges(self):
        self.assertEqual(BTM,Cube.otherPieceOf(UTM))
        self.assertEqual(RTM,Cube.otherPieceOf(UMR))
        self.assertEqual(FTM,Cube.otherPieceOf(UBM))
        self.assertEqual(LTM,Cube.otherPieceOf(UML))
    
    def test_215_otherPieceOf_BottomEdges(self):
        self.assertEqual(FBM,Cube.otherPieceOf(DTM))
        self.assertEqual(RBM,Cube.otherPieceOf(DMR))
        self.assertEqual(BBM,Cube.otherPieceOf(DBM))
        self.assertEqual(LBM,Cube.otherPieceOf(DML))
    
    def test_2160_otherPieceOf_FrontCorners0(self):
        self.assertEqual(LTR,Cube.otherPieceOf(FTL,0))
        self.assertEqual(UBR,Cube.otherPieceOf(FTR,0))
        self.assertEqual(RBL,Cube.otherPieceOf(FBR,0))
        self.assertEqual(DTL,Cube.otherPieceOf(FBL,0))
        
    def test_2160_otherPieceOf_FrontCorners1(self):
        self.assertEqual(UBL,Cube.otherPieceOf(FTL,1))
        self.assertEqual(RTL,Cube.otherPieceOf(FTR,1))
        self.assertEqual(DTR,Cube.otherPieceOf(FBR,1))
        self.assertEqual(LBR,Cube.otherPieceOf(FBL,1))
    
    def test_2161_otherPieceOf_RightCorners0(self):
        self.assertEqual(FTR,Cube.otherPieceOf(RTL,0))
        self.assertEqual(UTR,Cube.otherPieceOf(RTR,0))
        self.assertEqual(BBL,Cube.otherPieceOf(RBR,0))
        self.assertEqual(DTR,Cube.otherPieceOf(RBL,0))
    
    def test_2161_otherPieceOf_RightCorners1(self):
        self.assertEqual(UBR,Cube.otherPieceOf(RTL,1))
        self.assertEqual(BTL,Cube.otherPieceOf(RTR,1))
        self.assertEqual(DBR,Cube.otherPieceOf(RBR,1))
        self.assertEqual(FBR,Cube.otherPieceOf(RBL,1))
    
    def test_2162_otherPieceOf_BackCorners0(self):
        self.assertEqual(RTR,Cube.otherPieceOf(BTL,0))
        self.assertEqual(UTL,Cube.otherPieceOf(BTR,0))
        self.assertEqual(LBL,Cube.otherPieceOf(BBR,0))
        self.assertEqual(DBR,Cube.otherPieceOf(BBL,0))
    
    def test_2162_otherPieceOf_BackCorners1(self):
        self.assertEqual(UTR,Cube.otherPieceOf(BTL,1))
        self.assertEqual(LTL,Cube.otherPieceOf(BTR,1))
        self.assertEqual(DBL,Cube.otherPieceOf(BBR,1))
        self.assertEqual(RBR,Cube.otherPieceOf(BBL,1))
    
    def test_2163_otherPieceOf_LeftCorners0(self):
        self.assertEqual(BTR,Cube.otherPieceOf(LTL,0))
        self.assertEqual(UBL,Cube.otherPieceOf(LTR,0))
        self.assertEqual(FBL,Cube.otherPieceOf(LBR,0))
        self.assertEqual(DBL,Cube.otherPieceOf(LBL,0))
    
    def test_2163_otherPieceOf_LeftCorners1(self):
        self.assertEqual(UTL,Cube.otherPieceOf(LTL,1))
        self.assertEqual(FTL,Cube.otherPieceOf(LTR,1))
        self.assertEqual(DTL,Cube.otherPieceOf(LBR,1))
        self.assertEqual(BBR,Cube.otherPieceOf(LBL,1))
    
    def test_2164_otherPieceOf_TopCorners0(self):
        self.assertEqual(LTL,Cube.otherPieceOf(UTL,0))
        self.assertEqual(BTL,Cube.otherPieceOf(UTR,0))
        self.assertEqual(RTL,Cube.otherPieceOf(UBR,0))
        self.assertEqual(FTL,Cube.otherPieceOf(UBL,0))
    
    def test_2164_otherPieceOf_TopCorners1(self):
        self.assertEqual(BTR,Cube.otherPieceOf(UTL,1))
        self.assertEqual(RTR,Cube.otherPieceOf(UTR,1))
        self.assertEqual(FTR,Cube.otherPieceOf(UBR,1))
        self.assertEqual(LTR,Cube.otherPieceOf(UBL,1))
    
    def test_2165_otherPieceOf_BottomCorners0(self):
        self.assertEqual(LBR,Cube.otherPieceOf(DTL,0))
        self.assertEqual(FBR,Cube.otherPieceOf(DTR,0))
        self.assertEqual(RBR,Cube.otherPieceOf(DBR,0))
        self.assertEqual(BBR,Cube.otherPieceOf(DBL,0))
    
    def test_2165_otherPieceOf_BottomCorners1(self):
        self.assertEqual(FBL,Cube.otherPieceOf(DTL,1))
        self.assertEqual(RBL,Cube.otherPieceOf(DTR,1))
        self.assertEqual(BBL,Cube.otherPieceOf(DBR,1))
        self.assertEqual(LBL,Cube.otherPieceOf(DBL,1))
    
    def test_220_getColours(self):
        actual = self.solvedCube.getColours()
        expected = "bogrwy"
        self.assertEqual(expected, actual)
    
    def test_221_getColours(self):
        testCube = Cube.makeCube(9*"2" + 9*"8" + 9*"1" + 9*"7" + 9*"3" + 9*"6")
        actual = testCube.getColours()
        expected = "281736"
        self.assertEqual(expected, actual)
    
    def test_230_centerOf(self):
        self.assertEqual(FMM, Cube.centerOf('f'))
        self.assertEqual(RMM, Cube.centerOf('r'))
        self.assertEqual(BMM, Cube.centerOf('b'))
        self.assertEqual(LMM, Cube.centerOf('l'))
        self.assertEqual(UMM, Cube.centerOf('u'))
        self.assertEqual(DMM, Cube.centerOf('d'))
    
    def test_240_findFaceOf(self):
        self.assertEqual('f', self.solvedCube.findFaceOf('b'))
        self.assertEqual('r', self.solvedCube.findFaceOf('o'))
        self.assertEqual('b', self.solvedCube.findFaceOf('g'))
        self.assertEqual('l', self.solvedCube.findFaceOf('r'))
        self.assertEqual('u', self.solvedCube.findFaceOf('w'))
        self.assertEqual('d', self.solvedCube.findFaceOf('y'))
    
    def test_241_findFaceOf_invalidColour(self):
        self.assertEqual(None, self.solvedCube.findFaceOf('3'))
    
    def test_250_findPieces_defaultFind(self):
        result = self.solvedCube.findPieces(EDGES, 'w')
        result2 = self.solvedCube.findPieces(EDGES, 'w', True)
        expected = {UTM,UMR,UBM,UML}
        self.assertEqual(expected,result)
        self.assertEqual(result,result2)
    
    def test_251_findPieces_alternateFind(self):
        result = self.solvedCube.findPieces(EDGES, 'b', False)
        expected = EDGES - set(FRONT[1])
        self.assertEqual(expected, result)
    
    def test_260_status_solvedCube(self):
        self.assertFalse(self.solvedCube.status("scrambled"))
        self.assertTrue(self.solvedCube.status("bottomcross"))
        self.assertTrue(self.solvedCube.status("bottomlayer"))
        self.assertTrue(self.solvedCube.status("middlelayer"))
        self.assertTrue(self.solvedCube.status("topcross"))
        self.assertTrue(self.solvedCube.status("topsurface"))
        self.assertTrue(self.solvedCube.status("topcorners"))
        self.assertTrue(self.solvedCube.status("toplayer"))
        self.assertTrue(self.solvedCube.status("solved"))
        
    def test_261_status_scrambledCube(self):
        self.assertTrue(self.scrambledCube.status("scrambled"))
        self.assertFalse(self.scrambledCube.status("bottomcross"))
        self.assertFalse(self.scrambledCube.status("bottomlayer"))
        self.assertFalse(self.scrambledCube.status("middlelayer"))
        self.assertFalse(self.scrambledCube.status("topcross"))
        self.assertFalse(self.scrambledCube.status("topsurface"))
        self.assertFalse(self.scrambledCube.status("topcorners"))
        self.assertFalse(self.scrambledCube.status("toplayer"))
        self.assertFalse(self.scrambledCube.status("solved"))
    
    def test_262_status_raisedPetals(self):
        theCube = Cube.makeCube("bgrrbwrwowbyroogggrrbbggowroooorbwgywygywyyygboywyrbbw")
        self.assertFalse(theCube.status("scrambled"))
        self.assertTrue(theCube.status("raisedpetals"))
        self.assertFalse(theCube.status("bottomcross"))
        self.assertFalse(theCube.status("bottomlayer"))
        self.assertFalse(theCube.status("middlelayer"))
        self.assertFalse(theCube.status("topcross"))
        self.assertFalse(theCube.status("topsurface"))
        
    def test_263_status_bottomCross(self):
        theCube = Cube.makeCube("bgrbbgrbrwwooobwoogwyrgwbgorgorrogrygowwwbyrgbybyyyyyw")
        self.assertFalse(theCube.status("scrambled"))
        self.assertFalse(theCube.status("raisedpetals"))
        self.assertTrue(theCube.status("bottomcross"))
        self.assertFalse(theCube.status("bottomlayer"))
        self.assertFalse(theCube.status("middlelayer"))
        self.assertFalse(theCube.status("topcross"))
        self.assertFalse(theCube.status("topsurface"))
        
    def test_264_status_bottomLayer(self):
        theCube = Cube.makeCube("rworbbbbbgrbooooooobrggwgggbggrrbrrrwwwwwgwowyyyyyyyyy")
        self.assertFalse(theCube.status("scrambled"))
        self.assertFalse(theCube.status("raisedpetals"))
        self.assertTrue(theCube.status("bottomcross"))
        self.assertTrue(theCube.status("bottomlayer"))
        self.assertFalse(theCube.status("middlelayer"))
        self.assertFalse(theCube.status("topcross"))
        self.assertFalse(theCube.status("topsurface"))
        
    def test_265_status_middleLayer(self):
        theCube = Cube.makeCube("gwbbbbbbbowroooooobogggggggrgorrrrrrwwwwwbwrwyyyyyyyyy")
        self.assertFalse(theCube.status("scrambled"))
        self.assertFalse(theCube.status("raisedpetals"))
        self.assertTrue(theCube.status("bottomcross"))
        self.assertTrue(theCube.status("bottomlayer"))
        self.assertTrue(theCube.status("middlelayer"))
        self.assertFalse(theCube.status("topcross"))
        self.assertFalse(theCube.status("topsurface"))
        
    def test_266_status_topCross(self):
        theCube = Cube.makeCube("wbwbbbbbbrrbooooooogogggggggorrrrrrrwwwwwwgwbyyyyyyyyy")
        self.assertFalse(theCube.status("scrambled"))
        self.assertFalse(theCube.status("raisedpetals"))
        self.assertTrue(theCube.status("bottomcross"))
        self.assertTrue(theCube.status("bottomlayer"))
        self.assertTrue(theCube.status("middlelayer"))
        self.assertTrue(theCube.status("topcross"))
        self.assertFalse(theCube.status("topsurface"))
        
    def test_267_status_topSurface(self):
        theCube = Cube.makeCube("rbrbbbbbbbrbooooooogogggggggogrrrrrrwwwwwwwwwyyyyyyyyy")
        self.assertFalse(theCube.status("scrambled"))
        self.assertFalse(theCube.status("raisedpetals"))
        self.assertTrue(theCube.status("bottomcross"))
        self.assertTrue(theCube.status("bottomlayer"))
        self.assertTrue(theCube.status("middlelayer"))
        self.assertTrue(theCube.status("topcross"))
        self.assertTrue(theCube.status("topsurface"))
    
    def test_270_whereDoesXGo_inPlaceTests(self):
        for piece in (EDGES.union(CORNERS)):
            self.assertEqual(piece, self.solvedCube.whereDoesXGo(piece))
        
    def test_271_whereDoesXGo_slightOffsets(self):
        theCube = Cube(self.solvedCube.get())
        theCube.rotate("RflUb")
        
        #Edges
        self.assertEqual(DTM, theCube.whereDoesXGo(RML))
        self.assertEqual(FML, theCube.whereDoesXGo(FBM))
        self.assertEqual(UML, theCube.whereDoesXGo(BTM))
        self.assertEqual(BBM, theCube.whereDoesXGo(BMR))
        
        #Corners
        self.assertEqual(UBR, theCube.whereDoesXGo(RTL))
        self.assertEqual(BTL, theCube.whereDoesXGo(LBL))
        self.assertEqual(LTR, theCube.whereDoesXGo(UTR))
        self.assertEqual(DTR, theCube.whereDoesXGo(RBR))
        
    def test_280_alignCorner(self):
        self.assertEqual('F', Cube.alignCorner(FTL, 'ufr', 'f'))
        self.assertEqual('FF', Cube.alignCorner(FTL, 'dfr', 'f'))
        self.assertEqual('u', Cube.alignCorner(FTL, 'ufr', 'u'))
        
    def test_281_alignCorner(self):
        self.assertEqual('R', Cube.alignCorner(RTL, 'urb', 'r'))
        self.assertEqual('r', Cube.alignCorner(RTL, 'dfr', 'r'))
        self.assertEqual('u', Cube.alignCorner(RTL, 'urb', 'u'))
        
    def test_290_moveAlgorithm(self):
        self.assertEqual('FrbLu', Cube.moveAlgorithm('FrbLu', 'f'))
        self.assertEqual('RblFu', Cube.moveAlgorithm('FrbLu', 'r'))
        self.assertEqual('BlfRu', Cube.moveAlgorithm('FrbLu', 'b'))
        self.assertEqual('LfrBu', Cube.moveAlgorithm('FrbLu', 'l'))
        
    def test_291_moveAlgorithm(self):
        self.assertEqual('fRBlU', Cube.moveAlgorithm('fRBlU', 'f'))
        self.assertEqual('rBLfU', Cube.moveAlgorithm('fRBlU', 'r'))
        self.assertEqual('bLFrU', Cube.moveAlgorithm('fRBlU', 'b'))
        self.assertEqual('lFRbU', Cube.moveAlgorithm('fRBlU', 'l'))
        
    def test_300_whereWillXBe(self):
        self.assertEqual(FTL, Cube.whereWillXBe(''  , FTL))
        self.assertEqual(FTR, Cube.whereWillXBe('F' , FTL))
        self.assertEqual(FBR, Cube.whereWillXBe('FF', FTL))
        self.assertEqual(FBL, Cube.whereWillXBe('f' , FTL))
        self.assertEqual(FTM, Cube.whereWillXBe(''  , FTM))
        self.assertEqual(FMR, Cube.whereWillXBe('F' , FTM))
        self.assertEqual(FBM, Cube.whereWillXBe('FF', FTM))
        self.assertEqual(FML, Cube.whereWillXBe('f' , FTM))
        
    def test_301_whereWillXBe(self):
        self.assertEqual(BTL, Cube.whereWillXBe('FRUlb', FTR))
        self.assertEqual(LTM, Cube.whereWillXBe('RUrurFRRuruRUrf', RTM))
        self.assertEqual(RTR, Cube.whereWillXBe('RUrurFRRuruRUrf', FTR))
        self.assertEqual(FBM, Cube.whereWillXBe('RUrurFRRuruRUrf', FBM))
        
    
        
# Sad path
#    Test for missing cube
    def test_900_makeCube_missingCube(self):
        result = Cube.makeCube()
        expected = 'missing cube'
        self.assertTrue(isinstance(result, str))
        self.assertEqual(expected, result)
        
#    Test for cube length
    def test_910_makeCube_invalidCubeLength(self):
        result = Cube.makeCube('grbyow')
        expected = 'invalid cube length'
        self.assertTrue(isinstance(result, str))
        self.assertEqual(expected, result)
        
#    Test for unique face centers
    def test_920_makeCube_invalidFaceCenters(self):
        result = Cube.makeCube('gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyoooowoooowwowwwwww')
        expected = 'invalid face centers'
        self.assertTrue(isinstance(result, str))
        self.assertEqual(expected, result)

#    Test for 9 of each character, this + cube length check => 54 faces
    def test_930_makeCube_invalidColourCounts(self):
        result = Cube.makeCube('gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyoooooooowwwwwwwwww')
        expected = 'invalid colour amounts'
        self.assertTrue(isinstance(result, str))
        self.assertEqual(expected, result)

#    Test for invalid symbols in cube
    def test_940_makeCube_invalidCubeCharacters(self):
        result = Cube.makeCube('gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy.........wwwwwwwww')
        expected = 'invalid symbols used'
        self.assertTrue(isinstance(result, str))
        self.assertEqual(expected, result)
        
#    Test for a character appearing that doesn't match any face centers
    def test_950_makeCube_characterMatchesNoFace(self):
        result = Cube.makeCube('ggTggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww')
        expected = 'symbol matches no face'
        self.assertTrue(isinstance(result, str))
        self.assertEqual(expected, result)
        
#    Test for invalid symbols in rotation
    def test_960_rotate_invalidRotateCharacters(self):
        result = self.solvedCube.rotate('RbfUd')
        expected = 'invalid rotation'
        self.assertEqual(expected, result)
        
if __name__ == '__main__':
    unittest.main()