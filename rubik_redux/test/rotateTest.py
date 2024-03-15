import unittest
from rubik_redux.view.rotate import rotate
from rubik_redux.model.constants import *

class RotateTest(unittest.TestCase):
    # Invalid (or missing) cube tests
    def test_missing_cube_parameter(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{})
        self.assertEqual("Error: Input data: Expected parameter \"cube\"", str(result.exception))

    def test_invalid_input_type_int(self):
        with self.assertRaises(TypeError) as result:
            rotate(**{'cube':3241})
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(1)}", str(result.exception))

    def test_invalid_character_count_low(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffff"})
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 53', str(result.exception))

    def test_invalid_character_count_high(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffff"})
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 55', str(result.exception))

    def test_invalid_characters_present(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':"=========---------!!!!!!!!!;;;;;;;;;/////////?????????"})
        self.assertEqual('Error: Cube string contents: Please only use alphanumeric characters a-z, A-Z, 0-9', str(result.exception))

    def test_invalid_unique_centerpoints(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeefeeeffffeffff"})
        self.assertEqual('Error: Cube string contents: Centerpoints contain duplicates', str(result.exception))

    def test_invalid_piece_match_centers(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffg"})
        self.assertEqual('Error: Cube string contents: Non-center pieces need to match present centerpieces', str(result.exception))

    def test_invalid_piece_counts(self):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffa"})
        self.assertEqual('Error: Cube string contents: Require 9 pieces of each symbol', str(result.exception))

    
    # Tests for unsolvable cubes
    def unsolvable_impossible_piece_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':cube_string})
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
            rotate(**{'cube':cube_string})
        self.assertEqual('Error: Cube unsolvable: Edge parity', str(result.exception))

    def test_unsolvable_edge_parity_1(self):
        self.unsolvable_edge_parity_test("bwbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwbwyyyyyyyyy")
    def test_unsolvable_edge_parity_2(self):
        self.unsolvable_edge_parity_test("wbrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwboyyogowygwbg")
    def test_unsolvable_edge_parity_3(self):
        self.unsolvable_edge_parity_test("wyrybybwggoyrooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    

    def unsolvable_corner_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            rotate(**{'cube':cube_string})
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
            rotate(**{'cube':cube_string})
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

    
    # Invalid dir values
    def test_rotate_invalid_characters(self):
        cube = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"
        for char in r"aceghijkmnopqstvwxyzACEGHIJKMNOPQSTVWXYZ1234567890!@#$%^&*()`-=~_+[]\{}|":
            # checking that an error happened
            with self.assertRaises(ValueError) as result:
                rotate(cube, char)
            self.assertEqual(f"Error: Invalid Cube turn: Expected char in \"FfRrBbLlUuDd\", recieved \"{char}\"", str(result.exception))
    

    # Valid rotation tests
    def rotate_changes_correctly_test(self, input_cube_string: str, turn_input: str, expected_cube_string_changes: dict[int, int]):
        result = rotate(input_cube_string, turn_input)
        expected_cube_string = "".join(input_cube_string[expected_cube_string_changes.get(piece, piece)] for piece in range(len(input_cube_string)))
        self.assertEqual({'cube':expected_cube_string, 'status':'ok'}, result)

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

    def rotate_matches_expected_test(self, start_cube, rotates, end_cube):
        result = rotate(start_cube, rotates)
        self.assertEqual({"cube":end_cube, "status":"ok"}, result)

    def test_rotate_multiple_turns_1(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "FRBLUD", 
                                          "wwgwbyyyywwrooyrbywwbggyooywborrrggorggrwobbobbbryorgg")
    def test_rotate_multiple_turns_2(self):
        self.rotate_matches_expected_test("bbwbbybboboooooygyggggggooyrrrrrrgrrwwwwwwwwoyybyyyrbg", "drDRdrDR",
                                          "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_rotate_multiple_turns_3(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "frblud",
                                          "wwwybwyygrbwoowyyroowggwyybggorrryborggrwobbbbboryorgg")
    
    def test_rotate_multiple_turns_incremental_1(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "F",
                                          "bbbbbbbbbwoowoowoogggggggggrryrryrrywwwwwwrrroooyyyyyy")
    def test_rotate_multiple_turns_incremental_2(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "FR",
                                          "bbobbybbywwwoooooorggwggwggrryrryrrywwbwwbrrboogyygyyg")
    def test_rotate_multiple_turns_incremental_3(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "FRB",
                                          "bbobbybbywwgooyooywwrggggggbrywrywrywoowwbrrboogyygrrr")
    def test_rotate_multiple_turns_incremental_4(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "FRBL",
                                          "wbowbyrbywwgooyooywwrggyggowwbrrryyygoogwbrrbbogbygbrr")
    def test_rotate_multiple_turns_incremental_5(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "FRBLU",
                                          "wwgwbyrbywwrooyooywwbggyggowborrryyyrggrwobbobogbygbrr")
    def test_rotate_multiple_turns_incremental_6(self):
        self.rotate_matches_expected_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "FRBLUD",
                                          "wwgwbyyyywwrooyrbywwbggyooywborrrggorggrwobbobbbryorgg")
    
    # Key quantities
    def test_no_keys(self):
        with self.assertRaises(ValueError):
            rotate(**{})
    def test_no_cube(self):
        with self.assertRaises(ValueError):
            rotate(**{"dir":"FRBLUD"})
    def test_just_cube(self):
        rotate(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"})
    def test_cube_dir(self):
        rotate(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "dir":"FRBLUD"})
    def test_non_dir_extra_keys(self):
        with self.assertRaises(TypeError):
            rotate(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "hehehe":"hohoho"})
    def test_dir_present_extra_keys(self):
        with self.assertRaises(TypeError):
            rotate(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "dir":"FRBLUD", "hehehe":"hohoho"})

if __name__ == '__main__':
    unittest.main()