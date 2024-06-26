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


    def test_match_pattern_invalid_input_type(self):
        cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
        with self.assertRaises(ValueError) as result:
            cube.match_pattern(213)
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(1)}", str(result.exception))

    def test_match_pattern_invalid_input_length_short(self):
        cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
        with self.assertRaises(ValueError) as result:
            cube.match_pattern("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuudddddddd")
        self.assertEqual("Error: Invalid pattern length: Expected 54 characters but recieved 53", str(result.exception))

    def test_match_pattern_invalid_input_length_long(self):
        cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
        with self.assertRaises(ValueError) as result:
            cube.match_pattern("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuudddddddddd")
        self.assertEqual("Error: Invalid pattern length: Expected 54 characters but recieved 55", str(result.exception))

    def test_match_pattern_invalid_input_characters_present(self):
        cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
        with self.assertRaises(ValueError) as result:
            cube.match_pattern(".f..f.....r..r.....b..b.....l..l..k..u.uuu.u.....d....")
        self.assertEqual("Error: Invalid pattern contents: Only use face characters \"frblud\" and wildcard \".\"", str(result.exception))

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
        

    def align_edge_test(self, piece, face, variant=0):
        cube_string = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"
        cube = Cube(cube_string)
        result = cube.align_edge(piece, face, variant)

        # effects test
        where_is = cube.where_is(piece)
        match variant:
            case 0:
                self.assertEqual(constants.FACE_OF[piece], constants.FACE_OF[where_is])
                self.assertEqual(face, constants.FACE_OF[constants.OTHER_SIDE_OF[where_is]])
            case 1:
                self.assertEqual(face, constants.FACE_OF[where_is])
                self.assertEqual(constants.FACE_OF[constants.OTHER_SIDE_OF[piece]], constants.FACE_OF[constants.OTHER_SIDE_OF[where_is]])

        # 2 turns or less, only turns 1 face at a time
        self.assertTrue(len(result) <= 2 and len(set(result)) <= 1) 

        # reproducability test
        second_cube = Cube(cube_string)
        second_cube.rotate(result)
        self.assertEqual(str(cube), str(second_cube))

    def test_align_edge_front(self):
        self.align_edge_test(FTM,'r',0)
        self.align_edge_test(FMR,'l',0)
        self.align_edge_test(FBM,'r',0)
        self.align_edge_test(FML,'l',0)
        
        self.align_edge_test(FTM,'r',1)
        self.align_edge_test(FMR,'b',1)
        self.align_edge_test(FBM,'l',1)
        self.align_edge_test(FML,'f',1)
        
    def test_align_edge_right(self):
        self.align_edge_test(RTM,'b',0)
        self.align_edge_test(RMR,'f',0)
        self.align_edge_test(RBM,'b',0)
        self.align_edge_test(RML,'f',0)

        self.align_edge_test(RTM,'b',1)
        self.align_edge_test(RMR,'l',1)
        self.align_edge_test(RBM,'f',1)
        self.align_edge_test(RML,'r',1)

    def test_align_edge_back(self):
        self.align_edge_test(BTM,'d',0)
        self.align_edge_test(BMR,'d',0)
        self.align_edge_test(BBM,'d',0)
        self.align_edge_test(BML,'d',0)

        self.align_edge_test(BTM,'l',1)
        self.align_edge_test(BMR,'f',1)
        self.align_edge_test(BBM,'r',1)
        self.align_edge_test(BML,'b',1)
        
    def test_align_edge_left(self):
        self.align_edge_test(LTM,'b',0)
        self.align_edge_test(LMR,'f',0)
        self.align_edge_test(LBM,'b',0)
        self.align_edge_test(LML,'f',0)
        
        self.align_edge_test(LTM,'f',1)
        self.align_edge_test(LMR,'r',1)
        self.align_edge_test(LBM,'b',1)
        self.align_edge_test(LML,'l',1)
        
    def test_align_edge_up(self):
        self.align_edge_test(UTM,'r',0)
        self.align_edge_test(UMR,'l',0)
        self.align_edge_test(UBM,'r',0)
        self.align_edge_test(UML,'l',0)
        
        self.align_edge_test(UTM,'r',1)
        self.align_edge_test(UMR,'d',1)
        self.align_edge_test(UBM,'l',1)
        self.align_edge_test(UML,'u',1)
        
    def test_align_edge_down(self):
        self.align_edge_test(DTM,'r',0)
        self.align_edge_test(DMR,'l',0)
        self.align_edge_test(DBM,'r',0)
        self.align_edge_test(DML,'l',0)
        
        self.align_edge_test(DTM,'r',1)
        self.align_edge_test(DMR,'u',1)
        self.align_edge_test(DBM,'l',1)
        self.align_edge_test(DML,'d',1)

    
    def align_corner_face_test(self, face):
        sum_of_corners = set(constants.CYCLE_OF[face][0] + constants.CYCLE_OF[face][2] + constants.CYCLE_OF[face][4])
        cube_string = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"

        # Valid corners
        for start_corner in sum_of_corners:
            for end_corner in sum_of_corners:
                cube = Cube(cube_string)
                result = cube.align_corner(start_corner, end_corner, face)
                self.assertIn(result, constants.ROTATION_TOKENS[face].values()) # result within expected parameters
                self.assertIn(end_corner, constants.ALL_SIDES_OF[cube.where_is(start_corner)]) # piece moved to expected position
                second_cube = Cube(cube_string)
                second_cube.rotate(result)
                self.assertEqual(str(cube), str(second_cube)) # reproducability
        
        # One invalid corner
        for valid_corner in sum_of_corners:
            for invalid_corner in (constants.CORNERS - sum_of_corners):
                cube = Cube(cube_string)
                with self.assertRaises(ValueError) as result:
                    cube.align_corner(valid_corner, invalid_corner, face)
                self.assertEqual("Error: Invalid corner to align: Corner not on target face", str(result.exception))

                self.assertEqual(cube_string, str(cube)) # don't corrupt cube
                with self.assertRaises(ValueError) as result:
                    cube.align_corner(invalid_corner, valid_corner, face)
                self.assertEqual("Error: Invalid corner to align: Corner not on target face", str(result.exception))
        
        # Two invalid corners
        for start_corner in (constants.CORNERS - sum_of_corners):
            for end_corner in (constants.CORNERS - sum_of_corners):
                cube = Cube(cube_string)
                with self.assertRaises(ValueError) as result:
                    cube.align_corner(valid_corner, invalid_corner, face)
                self.assertEqual("Error: Invalid corner to align: Corner not on target face", str(result.exception))
                self.assertEqual(cube_string, str(cube)) # don't corrupt cube
    
    def test_align_corner_front(self):
        self.align_corner_face_test('f')
    def test_align_corner_right(self):
        self.align_corner_face_test('r')
    def test_align_corner_back(self):
        self.align_corner_face_test('b')
    def test_align_corner_left(self):
        self.align_corner_face_test('l')
    def test_align_corner_up(self):
        self.align_corner_face_test('u')
    def test_align_corner_down(self):
        self.align_corner_face_test('d')


    def test_move_algorithm_invalid_faces(self):
        cube_string = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"
        cube = Cube(cube_string)
        for new_front,new_up in [('f','b'),('b','f'), ('u','d'),('d','u'), ('l','r'),('r','l'),
                                 ('f','f'),('b','b'), ('u','u'),('d','d'), ('l','l'),('r','r')]:
            with self.assertRaises(ValueError) as result:
                cube.move_algorithm("FRBLUDfrblud", new_front, new_up)
            self.assertEqual("Error: Invalid faces specified: Cannot assign front and up to non-adjacent faces", str(result.exception))

            self.assertEqual(cube_string, str(cube))

    def test_move_algorithm_default_functionality(self):
        cube_string = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"
        algorithm = "FRBLUDfrblud"
        for new_front in 'frbl':
            up_cube = Cube(cube_string)
            default_cube = Cube(cube_string)
            up_result = up_cube.move_algorithm(algorithm, new_front, new_up='u')
            default_result = default_cube.move_algorithm(algorithm, new_front)
            self.assertEqual(up_result, default_result)
            self.assertEqual(str(up_cube), str(default_cube))
    
    def move_algorithm_effects_test(self, algorithm, new_front, new_up, expected):
        cube_string = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"
        cube = Cube(cube_string)
        result = cube.move_algorithm(algorithm, new_front, new_up)
        self.assertEqual(expected, result) # matches expectation
        self.assertNotEqual(cube_string, str(cube)) # should rotate the cube in the process
        second_cube = Cube(cube_string)
        second_cube.rotate(result)
        self.assertEqual(str(cube), str(second_cube)) # reproducability

        counter_result = cube.move_algorithm(algorithm, 'f', 'u')
        self.assertEqual(algorithm, counter_result) # algorithm should be the same if 'moved back' to normal reference
    
    def test_move_algorithm_front(self):
        algorithm = "FRBLUDfrblud"
        for front,expected in [('u','ULDRFBuldrfb'),
                               ('l','LDRUFBldrufb'),
                               ('d','DRULFBdrulfb'),
                               ('r','RULDFBruldfb')]:
            self.move_algorithm_effects_test(algorithm, front, 'f', expected)
    
    def test_move_algorithm_right(self):
        algorithm = "FRBLUDfrblud"
        for front,expected in [('f','FDBURLfdburl'),
                               ('d','DBUFRLdbufrl'),
                               ('b','BUFDRLbufdrl'),
                               ('u','UFDBRLufdbrl')]:
            self.move_algorithm_effects_test(algorithm, front, 'r', expected)
    
    def test_move_algorithm_back(self):
        algorithm = "FRBLUDfrblud"
        for front,expected in [('u','URDLBFurdlbf'),
                               ('r','RDLUBFrdlubf'),
                               ('d','DLURBFdlurbf'),
                               ('l','LURDBFlurdbf')]:
            self.move_algorithm_effects_test(algorithm, front, 'b', expected)
    
    def test_move_algorithm_left(self):
        algorithm = "FRBLUDfrblud"
        for front,expected in [('f','FUBDLRfubdlr'),
                               ('u','UBDFLRubdflr'),
                               ('b','BDFULRbdfulr'),
                               ('d','DFUBLRdfublr')]:
            self.move_algorithm_effects_test(algorithm, front, 'l', expected)

    def test_move_algorithm_up(self):
        algorithm = "FRBLUDfrblud"
        for front,expected in [('f','FRBLUDfrblud'),
                               ('r','RBLFUDrblfud'),
                               ('b','BLFRUDblfrud'),
                               ('l','LFRBUDlfrbud')]:
            self.move_algorithm_effects_test(algorithm, front, 'u', expected)

    def test_move_algorithm_down(self):
        algorithm = "FRBLUDfrblud"
        for front,expected in [('f','FLBRDUflbrdu'),
                               ('l','LBRFDUlbrfdu'),
                               ('b','BRFLDUbrfldu'),
                               ('r','RFLBDUrflbdu')]:
            self.move_algorithm_effects_test(algorithm, front, 'd', expected)

if __name__ == '__main__':
    unittest.main()