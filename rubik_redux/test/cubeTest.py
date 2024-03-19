"""
Created on Feb 24 2024

@author: Alviere
"""
import unittest
from rubik_redux.model.cube import Cube
import rubik_redux.model.constants as constants
from rubik_redux.model.constants import *

class CubeTest(unittest.TestCase):
    # Initializer tests
    def test_invalid_input_type_int(self):
        with self.assertRaises(TypeError) as result:
            Cube(3241)
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(1)}", str(result.exception))

    def test_invalid_input_type_none(self):
        with self.assertRaises(TypeError) as result:
            Cube(None)
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(None)}", str(result.exception))

    def test_invalid_character_count_low(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffff")
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 53', str(result.exception))

    def test_invalid_character_count_high(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffff")
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 55', str(result.exception))

    def test_invalid_characters_present(self):
        with self.assertRaises(ValueError) as result:
            Cube("=========---------!!!!!!!!!;;;;;;;;;/////////?????????")
        self.assertEqual('Error: Cube string contents: Please only use alphanumeric characters a-z, A-Z, 0-9', str(result.exception))

    def test_invalid_unique_centerpoints(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeefeeeffffeffff")
        self.assertEqual('Error: Cube string contents: Centerpoints contain duplicates', str(result.exception))

    def test_invalid_piece_match_centers(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffg")
        self.assertEqual('Error: Cube string contents: Non-center pieces need to match present centerpieces', str(result.exception))

    def test_invalid_piece_counts(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffa")
        self.assertEqual('Error: Cube string contents: Require 9 pieces of each symbol', str(result.exception))

    def valid_cube_test(self, cube_string):
        cube = Cube(cube_string)
        self.assertTrue(isinstance(cube, Cube))
        self.assertEqual(cube_string, str(cube))
        self.assertEqual({'f':cube_string[constants.FMM], 'r':cube_string[constants.RMM], 
                          'b':cube_string[constants.BMM], 'l':cube_string[constants.LMM], 
                          'u':cube_string[constants.UMM], 'd':cube_string[constants.DMM]}, 
                          cube.colours)

    # TODO: add more valid cube creation tests
    def test_valid_cube_creation_1(self):
        self.valid_cube_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_valid_cube_creation_2(self):
        self.valid_cube_test("wyrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    def test_valid_cube_creation_3(self):
        self.valid_cube_test("owoybbbgrgboyoygbowoyrgygowrgyorgbwrggbwwwbrwyrwoyrrby")
    def test_valid_cube_creation_4(self):
        self.valid_cube_test("ogroboogrwbbwowbbyowwrgrgrorbwyryggbbbwowrgwgyoyyyyygr")

    
    # Tests for unsolvable cubes
    def unsolvable_impossible_piece_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Impossible pieces', str(result.exception))
    
    def test_unsolvable_impossible_piece_1(self): # edges with same colour on both sides
        self.unsolvable_impossible_piece_test("bwbbbbbbbooooooooogggggggggrrrrrbrrrwwwrwwwwwyyyyyyyyy")
    def test_unsolvable_impossible_piece_2(self): # edges with colours of opposite cube sides
        self.unsolvable_impossible_piece_test("bbbobbbbbooogooooogggrgggggrrrbrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_impossible_piece_3(self): # corner with improper colour amounts
        self.unsolvable_impossible_piece_test("bbwbbbrbbooooooooogggggggggrrbrrrrrrwwwwwwbwwyyyyyyyyy")
    def test_unsolvable_impossible_piece_4(self): # corners with colours of opposite cube sides
        self.unsolvable_impossible_piece_test("obbbbbbbbgoooooooorggggggggbrrrrrrrrwwwwwwwwwyyyyyyyyy")


    def unsolvable_edge_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Edge parity', str(result.exception))

    def test_unsolvable_edge_parity_1(self):
        self.unsolvable_edge_parity_test("bwbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwbwyyyyyyyyy")
    def test_unsolvable_edge_parity_2(self):
        self.unsolvable_edge_parity_test("wbrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwboyyogowygwbg")
    def test_unsolvable_edge_parity_3(self):
        self.unsolvable_edge_parity_test("wyrybybwggoyrooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    
    def unsolvable_corner_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Corner parity', str(result.exception))

    def test_unsolvable_corner_parity_1(self):
        self.unsolvable_corner_parity_test("bbobbbbbbwoooooooogggggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy")
    def test_unsolvable_corner_parity_2(self):
        self.unsolvable_corner_parity_test("bbwbbbbbbboooooooogggggggggrrrrrrrrrwwwwwwwwoyyyyyyyyy")
    def test_unsolvable_corner_parity_3(self):
        self.unsolvable_corner_parity_test("wbobbbbbbwoooooooogggggggggrrbrrrrrrwwwwwwrwbyyyyyyyyy")
    def test_unsolvable_corner_parity_4(self):
        self.unsolvable_corner_parity_test("rbwbbbbbbboooooooogggggggggrrwrrrrrrwwwwwwbwoyyyyyyyyy")
    def test_unsolvable_corner_parity_5(self):
        self.unsolvable_corner_parity_test("owgybbbgrwboyoygbowoyrgygowrgyorgbwrggbwwwbroyrwoyrrby")
    def test_unsolvable_corner_parity_6(self):
        self.unsolvable_corner_parity_test("owwybbbgroboyoygbowoyrgygowrgyorgbwrggbwwwbrgyrwoyrrby")
    def test_unsolvable_corner_parity_7(self):
        self.unsolvable_corner_parity_test("bwgybbbgrwboyoygbowoyrgygowrgoorgbwrggbwwwyroyrwoyrrby")
    def test_unsolvable_corner_parity_8(self):
        self.unsolvable_corner_parity_test("ywwybbbgroboyoygbowoyrgygowrgborgbwrggbwwworgyrwoyrrby")
    

    def unsolvable_permutation_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Permutation parity', str(result.exception))
    
    def test_unsolvable_permutation_parity_1(self): # swap edges 1x
        self.unsolvable_permutation_parity_test("bgbbbbbbbooooooooogbgggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_2(self): # swap corners 1x
        self.unsolvable_permutation_parity_test("obrbbbbbbboooooooogggggggggrrbrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_3(self): # swap 3x edges
        self.unsolvable_permutation_parity_test("brbbbbbbbobooooooogogggggggrgrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_4(self): # swap 2x edges 1x corners
        self.unsolvable_permutation_parity_test("oorbbbbbbbgooooooogbgggggggrrbrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_5(self): # swap edges 1x
        self.unsolvable_permutation_parity_test("obroboogrwbbwowbbyowwrgrgrorbwyryggbbgwowrgwgyoyyyyygr")
    def test_unsolvable_permutation_parity_6(self): # swap corners 1x
        self.unsolvable_permutation_parity_test("wgwoboogrobbwowbbyowwrgrgrorbryryggbbbwowrgwgyoyyyyygr")
    def test_unsolvable_permutation_parity_7(self): # swap 3x edges
        self.unsolvable_permutation_parity_test("obroboogrwgbwowbbyobwrgrgrorwwyryggbbrwbwwgogyoyyyyygr")
    def test_unsolvable_permutation_parity_8(self): # swap 2x edges 1x corners
        self.unsolvable_permutation_parity_test("wbwoboogrobbwowbbyowwrgrgrorbryryggbbgwrwogwgyoyyyyygr")


    # Test 'where does [piece] go'
    def test_where_does_piece_go_solved(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        for piece in constants.CENTERS | constants.EDGES | constants.CORNERS:
            self.assertEqual(piece, cube.where_does_piece_go(piece))
    
    def test_where_does_piece_go_scrambled(self):
        cube = Cube("bwgrbyggbwbbrogyybywgygowggrgrbrbywywoowwywrororbyooro")
        expected = {FTL:FTL, FTM:UML, FTR:BTL, FML:LMR, FMM:FMM, FMR:DML, FBL:BBR, FBM:BML, FBR:FBL,
                    RTL:UTR, RTM:FBM, RTR:FBR, RML:LBM, RMM:RMM, RMR:BBM, RBL:DTL, RBM:DMR, RBR:FTR,
                    BTL:DTR, BTM:UMR, BTR:BTR, BML:DBM, BMM:BMM, BMR:RML, BBL:UBR, BBM:BMR, BBR:BBL,
                    LTL:LTL, LTM:BTM, LTR:LTR, LML:FMR, LMM:LMM, LMR:FML, LBL:DBR, LBM:UBM, LBR:DBL,
                    UTL:UTL, UTM:RTM, UTR:RBL, UML:UTM, UMM:UMM, UMR:DTM, UBL:UBL, UBM:LTM, UBR:RTR,
                    DTL:LBL, DTM:RMR, DTR:LBR, DML:FTM, DMM:DMM, DMR:RBM, DBL:RBR, DBM:LML, DBR:RTL}
        self.assertEqual(expected, {piece:cube.where_does_piece_go(piece) for piece in constants.CENTERS | constants.EDGES | constants.CORNERS})
        
    
    # Test finding face from colour
    def test_find_face_from_colour_solved(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        expected_map = {'b':'f', 'o':'r', 'g':'b', 'r':'l', 'w':'u', 'y':'d'}
        self.assertEqual("".join(expected_map[piece] for piece in cube.cube_data), "".join(cube.find_face_from_colour(piece) for piece in cube.cube_data))
    
    def test_find_face_from_colour_scrambled(self):
        cube = Cube("bwgrbyggbwbbrogyybywgygowggrgrbrbywywoowwywrororbyooro")
        expected_map = {'b':'f', 'o':'r', 'g':'b', 'r':'l', 'w':'u', 'y':'d'}
        self.assertEqual("".join(expected_map[piece] for piece in cube.cube_data), "".join(cube.find_face_from_colour(piece) for piece in cube.cube_data))


    
    def test_rotate_invalid_characters(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        for char in r"aceghijkmnopqstvwxyzACEGHIJKMNOPQSTVWXYZ1234567890!@#$%^&*()`-=~_+[]\{}|":
            # checking that an error happened
            with self.assertRaises(ValueError) as result:
                cube.rotate(char)
            self.assertEqual(f"Error: Invalid Cube turn: Expected char in \"FfRrBbLlUuDd\", recieved \"{char}\"", str(result.exception))

            # checking that cube doesn't get corrupted
            self.assertEqual("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", str(cube))
    
    def rotate_changes_correctly_test(self, input_cube_string: str, turn_input: str, expected_cube_string_changes: dict[int, int]):
        cube = Cube(input_cube_string)
        cube.rotate(turn_input)
        expected_cube_string = "".join(input_cube_string[expected_cube_string_changes.get(piece, piece)] for piece in range(len(input_cube_string)))
        self.assertEqual(expected_cube_string, str(cube))

    def rotate_test_all_turns_of_cube(self, base_cube):
        fronts = {FTL:FBL, FTR:FTL, FBR:FTR, FBL:FBR, FTM:FML, FMR:FTM, FBM:FMR, FML:FBM, 
                  UBL:LBR, UBM:LMR, UBR:LTR, RTL:UBL, RML:UBM, RBL:UBR, DTR:RTL, DTM:RML, DTL:RBL, LBR:DTR, LMR:DTM, LTR:DTL}
        self.rotate_changes_correctly_test(base_cube, 'F', fronts)
        self.rotate_changes_correctly_test(base_cube, 'f', {v:k for k,v in fronts.items()})

        rights = {RTL:RBL, RTR:RTL, RBR:RTR, RBL:RBR, RTM:RML, RMR:RTM, RBM:RMR, RML:RBM,
                  UBR:FBR, UMR:FMR, UTR:FTR, BTL:UBR, BML:UMR, BBL:UTR, DBR:BTL, DMR:BML, DTR:BBL, FBR:DBR, FMR:DMR, FTR:DTR}
        self.rotate_changes_correctly_test(base_cube, 'R', rights)
        self.rotate_changes_correctly_test(base_cube, 'r', {v:k for k,v in rights.items()})

        backs =  {BTL:BBL, BTR:BTL, BBR:BTR, BBL:BBR, BTM:BML, BMR:BTM, BBM:BMR, BML:BBM,
                  UTR:RBR, UTM:RMR, UTL:RTR, LTL:UTR, LML:UTM, LBL:UTL, DBL:LTL, DBM:LML, DBR:LBL, RBR:DBL, RMR:DBM, RTR:DBR}
        self.rotate_changes_correctly_test(base_cube, 'B', backs)
        self.rotate_changes_correctly_test(base_cube, 'b', {v:k for k,v in backs.items()})

        lefts =  {LTL:LBL, LTR:LTL, LBR:LTR, LBL:LBR, LTM:LML, LMR:LTM, LBM:LMR, LML:LBM,
                  UTL: BBR, UML:BMR, UBL:BTR, FTL:UTL, FML:UML, FBL:UBL, DTL:FTL, DML:FML, DBL:FBL, BBR:DTL, BMR:DML, BTR:DBL}
        self.rotate_changes_correctly_test(base_cube, 'L', lefts)
        self.rotate_changes_correctly_test(base_cube, 'l', {v:k for k,v in lefts.items()})

        ups =    {UTL:UBL, UTR:UTL, UBR:UTR, UBL:UBR, UTM:UML, UMR:UTM, UBM:UMR, UML:UBM,
                  BTR:LTR, BTM:LTM, BTL:LTL, RTR:BTR, RTM:BTM, RTL:BTL, FTR:RTR, FTM:RTM, FTL:RTL, LTR:FTR, LTM:FTM, LTL:FTL}
        self.rotate_changes_correctly_test(base_cube, 'U', ups)
        self.rotate_changes_correctly_test(base_cube, 'u', {v:k for k,v in ups.items()})

        downs =  {DTL:DBL, DTR:DTL, DBR:DTR, DBL:DBR, DTM:DML, DMR:DTM, DBM:DMR, DML:DBM,
                  FBL:LBL, FBM:LBM, FBR:LBR, RBL:FBL, RBM:FBM, RBR:FBR, BBL:RBL, BBM:RBM, BBR:RBR, LBL:BBL, LBM:BBM, LBR:BBR}
        self.rotate_changes_correctly_test(base_cube, 'D', downs)
        self.rotate_changes_correctly_test(base_cube, 'd', {v:k for k,v in downs.items()})
    
    def test_rotate_single_turns_1(self):
        self.rotate_test_all_turns_of_cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_rotate_single_turns_2(self):
        self.rotate_test_all_turns_of_cube("wyrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    def test_rotate_single_turns_3(self):
        self.rotate_test_all_turns_of_cube("owoybbbgrgboyoygbowoyrgygowrgyorgbwrggbwwwbrwyrwoyrrby")
    def test_rotate_single_turns_4(self):
        self.rotate_test_all_turns_of_cube("ogroboogrwbbwowbbyowwrgrgrorbwyryggbbbwowrgwgyoyyyyygr")

    def test_rotate_no_turns_1(self):
        self.rotate_changes_correctly_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "", {})
    def test_rotate_no_turns_2(self):
        self.rotate_changes_correctly_test("wyrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg", "", {})
    def test_rotate_no_turns_3(self):
        self.rotate_changes_correctly_test("owoybbbgrgboyoygbowoyrgygowrgyorgbwrggbwwwbrwyrwoyrrby", "", {})
    def test_rotate_no_turns_4(self):
        self.rotate_changes_correctly_test("ogroboogrwbbwowbbyowwrgrgrorbwyryggbbbwowrgwgyoyyyyygr", "", {})

    def test_rotate_multiple_turns_1(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("FRBLUD")
        self.assertEqual("wwgwbyyyywwrooyrbywwbggyooywborrrggorggrwobbobbbryorgg", str(cube))
    def test_rotate_multiple_turns_2(self):
        cube = Cube("bbwbbybboboooooygyggggggooyrrrrrrgrrwwwwwwwwoyybyyyrbg")
        cube.rotate("drDRdrDR")
        self.assertEqual("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", str(cube))
    def test_rotate_multiple_turns_3(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("frblud")
        self.assertEqual("wwwybwyygrbwoowyyroowggwyybggorrryborggrwobbbbboryorgg", str(cube))
    
    def test_rotate_multiple_turns_incremental_1(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("F")
        self.assertEqual("bbbbbbbbbwoowoowoogggggggggrryrryrrywwwwwwrrroooyyyyyy", str(cube))
    def test_rotate_multiple_turns_incremental_2(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("FR")
        self.assertEqual("bbobbybbywwwoooooorggwggwggrryrryrrywwbwwbrrboogyygyyg", str(cube))
    def test_rotate_multiple_turns_incremental_3(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("FRB")
        self.assertEqual("bbobbybbywwgooyooywwrggggggbrywrywrywoowwbrrboogyygrrr", str(cube))
    def test_rotate_multiple_turns_incremental_4(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("FRBL")
        self.assertEqual("wbowbyrbywwgooyooywwrggyggowwbrrryyygoogwbrrbbogbygbrr", str(cube))
    def test_rotate_multiple_turns_incremental_5(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("FRBLU")
        self.assertEqual("wwgwbyrbywwrooyooywwbggyggowborrryyyrggrwobbobogbygbrr", str(cube))
    def test_rotate_multiple_turns_incremental_6(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        cube.rotate("FRBLUD")
        self.assertEqual("wwgwbyyyywwrooyrbywwbggyooywborrrggorggrwobbobbbryorgg", str(cube))


    def test_whereis_OOB_checks(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        for value in [FTL-1, DBR+1, float('nan'), float('inf')]:
            with self.assertRaises(ValueError) as result:
                cube.where_is(value)
            self.assertEqual("Error: Attempting to locate an out of bounds piece", str(result.exception))
    
    def whereis_helper_test(self, directions):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")

        # Same logic as in rotate
        expecteds = [piece for piece in range(len(cube.cube_data))]
        for rotation in directions:
            expecteds = [ROTATION_TRANSFERS.get(rotation, {}).get(piece, piece) for piece in expecteds]
            
        cube.rotate(directions)
        results = [cube.where_is(piece) for piece in range(len(cube.cube_data))]

        self.assertEqual(results, expecteds)
    
    def test_whereis_no_changes(self):
        self.whereis_helper_test("")
    def test_whereis_single_rotations(self):
        for key in ROTATION_TRANSFERS:
            self.whereis_helper_test(key)
    def test_whereis_multiple_rotations_1(self):
        self.whereis_helper_test("RUrurFRRuruRUrf")
    def test_whereis_multiple_rotations_2(self):
        self.whereis_helper_test("FR")


    def match_pattern_test_helper(self, base_pattern, expected_matches, expected_not_matches):
        for translation in [{'f':'b', 'r':'o', 'b':'g', 'l':'r', 'u':'w', 'd':'y'},
                            {'f':'1', 'r':'2', 'b':'3', 'l':'4', 'u':'5', 'd':'6'},
                            {},
                            {'f':'4', 'r':'a', 'b':'b', 'l':'d', 'u':'2', 'd':'l'}]:
            cube = Cube("".join(translation.get(piece, piece) for piece in base_pattern))
            for positive in expected_matches:
                self.assertTrue(cube.match_pattern(positive))
            for negative in expected_not_matches:
                self.assertFalse(cube.match_pattern(negative))
    
    def test_match_pattern_1(self):
        self.match_pattern_test_helper( "fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd",
                                       ["fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", #solved
                                        ".f..f.....r..r.....b..b.....l..l.....u.uuu.u.....d....", #topcross
                                        "......................................................"],#all wildcards
                                       ["....b.................................................", #incorrect face center
                                        "fffffffffrrrrrrrrrbbbbbbbbblllllllllddddddddduuuuuuuuu"])#switched faces
        
    def test_match_pattern_2(self): 
        self.match_pattern_test_helper( "rfbbffubdrrldrfbblfbdrbdfdbrlurldulffuuuuubudrrlfdllld",
                                       [".f..f.....r..r.....b..b.....l..l.....u.uuu.u.....d....", #topcross
                                        "......................................................"],#all wildcards
                                       ["fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", #solved
                                        "....b.................................................", #incorrect face center
                                        "....f........r........b........l........d........u...."])#switched faces
        


if __name__ == '__main__':
    unittest.main()