import unittest
from rubik_redux.view.solve import solve
from rubik_redux.model.cube import Cube

class SolveTest(unittest.TestCase):
    # Invalid (or missing) cube tests
    def test_missing_cube_parameter(self):
        with self.assertRaises(ValueError) as result:
            solve(**{})
        self.assertEqual("Error: Input data: Expected parameter \"cube\"", str(result.exception))

    def test_invalid_input_type_int(self):
        with self.assertRaises(TypeError) as result:
            solve(**{'cube':3241})
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(1)}", str(result.exception))

    def test_invalid_character_count_low(self):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffff"})
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 53', str(result.exception))

    def test_invalid_character_count_high(self):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffff"})
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 55', str(result.exception))

    def test_invalid_characters_present(self):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':"=========---------!!!!!!!!!;;;;;;;;;/////////?????????"})
        self.assertEqual('Error: Cube string contents: Please only use alphanumeric characters a-z, A-Z, 0-9', str(result.exception))

    def test_invalid_unique_centerpoints(self):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeefeeeffffeffff"})
        self.assertEqual('Error: Cube string contents: Centerpoints contain duplicates', str(result.exception))

    def test_invalid_piece_match_centers(self):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffg"})
        self.assertEqual('Error: Cube string contents: Non-center pieces need to match present centerpieces', str(result.exception))

    def test_invalid_piece_counts(self):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':"aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffa"})
        self.assertEqual('Error: Cube string contents: Require 9 pieces of each symbol', str(result.exception))
    
    
    # Tests for invalid cubes
    def unsolvable_impossible_piece_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':cube_string})
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
            solve(**{'cube':cube_string})
        self.assertEqual('Error: Cube unsolvable: Edge parity', str(result.exception))

    def test_unsolvable_edge_parity_1(self):
        self.unsolvable_edge_parity_test("bwbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwbwyyyyyyyyy")
    def test_unsolvable_edge_parity_2(self):
        self.unsolvable_edge_parity_test("wbrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwboyyogowygwbg")
    def test_unsolvable_edge_parity_3(self):
        self.unsolvable_edge_parity_test("wyrybybwggoyrooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    

    def unsolvable_corner_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            solve(**{'cube':cube_string})
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
            solve(**{'cube':cube_string})
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

    # Test for general cases of expected values
    def test_just_cube(self):
        solve(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"}) # raise no error
    def test_extraneous_keys(self):
        with self.assertRaises(TypeError):
            solve(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "hehehe":"hohoho"})
    def test_invalid_solve_style(self):
        with self.assertRaises(ValueError):
            solve(**{"cube":"bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy", "style":"THERE SHOULD BE NO SOLVE STYLE UNDER THIS NAME"})
    
    # Test for actual functioning
    def solve_test(self, cube_string, style):
        cube = Cube(cube_string)
        result = solve(cube_string, style)
        self.assertIn("cube", result)
        self.assertEqual(cube_string, result["cube"])
        self.assertIn("dir", result)
        cube.rotate(result["dir"])
        self.assertTrue(cube.match_pattern("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd"))

    def solve_from_scrambled_test(self, style):
        for cube in ["bbdufdrfurllrrfrlffuudbrdllrbuflrdfdbbuduulrfblfuddbbl",
                     "bbrffuflubldlrdfllbblbbrdurdrufldfddfrruufluurdlrdbufb",
                     "ururffudrbbflrrburlbdbbddlrlrffldffrbudfullulbbdudludf",
                     "dulrfbfbdufllrulurfrurbdbfdrfbbldflrbburudlfbuufddlrld",
                     "lbfrfdddrllbrrrffbubbbbulluruulluldrdlrfuffudffubdrbdd",
                     "bdbbfbfbdlullrdrulbffrbluufddrflrullrrdlubufuddbudfrrf",
                     "rrrlfrldrudbbrbdrbdbdlblrllffbulfurululuubddfbfffdufdu",
                     "rufbfdurdufrfruburfdbfbrubllbbullfffuldduldblrdlrdldrb",
                     "rulrfllrbfdffrfrrlrulububdrdldlldbbbfbubuffrudfuddbdlu",
                     "lddufflldbbrlrlfuburdbbdruffddflfluulffburbrrbdrbdrulu",
                     "blulfrbbrlrfdrbdbllurrbfbffbfdrluubdufdluurdfllfddurdu",
                     "uullfrlfbflrbrflrudlflbubbrlrrrludfuddbfubfbubdduddfdr",
                     "ufbufurlbrrrbrrrrdfflfbrlbbfdlblllluuudludbddfbufduddf",
                     "lfdufbrrrbburrbdffldulbdddlffdbllblbrlfduubrruuffduurl",
                     "dfrdflbddubfbrrbubdllbbduuuddrblrfruffrfuubrfrlludflll",
                     "ldfbfludldbdbrrbudbffububrrurflluulfllrfuddrrrfuddfbbl",
                     "lrdlfbrfuffrrrrbludbrdbufbbuubllblfffubfuluuldrrdddddl",
                     "frllffdbbbbrrrfufrbbfdblbllrrrfldubfuuududdudlllrdufud",
                     "fdbbfubudulufrrrfulrdubblrfrrduldubdfbfdudlfrllbldlrfb",
                     "dbldflrlrburbrffrbfbllbdurrfdlblfudduudluffrdbuurdfbul"]:
            self.solve_test(cube, style)

    def solve_from_bottom_cross_test(self, style):
        for cube in ["dbuufbffdlrrrrllrrffbbbuubbllrrllllruudfufbufudfdddddb",
                     "ulbufbufdlbdlrrfrdbbffbubbllubllrulfdrrfuurfurdrdddfdl",
                     "rurrflfflbbrbrldruffufbulbuflbrlbfllrrduuudfuddbdddldb",
                     "dbfufbffbdlbrrburbdfdubfrbubflllrrlurrluuuflrldldddfdu",
                     "bllbfflfubrfrrubruuudfbflburbdlllrldfrluubrudfdrdddfdb",
                     "ulblffffblufrrrrrflldubrrbbbufblbllrrudbuflfuududddddd",
                     "dblufurfuurrlrffrdfluuburbfrbbrlbdlubfdrufllbfdldddldb",
                     "blurfurfubfurrubrffflbbfdbdfblrlbfldulrluudulbdrdddrdl",
                     "rfdrffffdludrrurruflllbfrblfuuulbbldublburblbrdbdddudf",
                     "bluufrufbllufrblrrrudlbrdbrffublbblflrbuuulffrdddddddf",
                     "flrufffflbulrrbdrbfbdrbudblfuublfbldllurulrfurdbdddudr",
                     "dulffrufddulurlbrufurbbllbfdbfflrulrbburufrlfbdldddrdb",
                     "rrffflufrrudbrburflurubudbudfdrllflbbfbrulfbuldbdddldl",
                     "drfffbufddlflrulrbrbrfbbdbbbfbullullururuulurfdfdddldr",
                     "dfblfllfdurrurrrrdubufbrlblbffblbulblufuuurlrddbdddfdf",
                     "bbfffldfdurufrrlrrfbuubfbbdburulrblrlurlubullfdfdddldd",
                     "rrfffufffufubrburbrrrlbulbudfdllllllbbbuurfulddrdddbdd",
                     "luffflbfllfuurfdrffbrrbblbfdbbllurlubrruulurdrdbdddddu",
                     "dfuuffrfrludrrburdfbllbffblurrulrdlubulbulblffdbdddbdr",
                     "blfffubfdlbubrrrrrluuublfbfbulflrrlullffurdbdrdbdddddu"]:
            self.assertTrue(Cube(cube).match_pattern("....f..f.....r..r.....b..b.....l..l.....u.....d.ddd.d.")) # sanity check
            self.solve_test(cube, style)

    def solve_from_bottom_layer_test(self, style):
        for cube in ["rbrlfrfffbrbfrbrrrlllubfbbbflfulflllubuuuuuruddddddddd",
                     "uurbfrfffuflbrfrrrfllubfbbbulbllulllbbuuurrrfddddddddd",
                     "lubbfffffurflrlrrrrlbbbubbbluurlrllluuubufffrddddddddd",
                     "lrrffffffbruurlrrrfbuububbbbrublllllllrbuuffuddddddddd",
                     "uuuffbfffrbllrfrrrffbublbbblbrulllllururuufrbddddddddd",
                     "fuuufffffrfurrlrrrbluubrbbbfulblflllrblrulubbddddddddd",
                     "rluufrffffflbrbrrrulflbrbbbubuulfllllfbuurburddddddddd",
                     "uffrfffffrfbururrruufrbbbbbublllblllllruurbluddddddddd",
                     "ubruflfffullfrfrrruulrbbbbbfbbllflllurbruurufddddddddd",
                     "blfufbfffurulrbrrrfrbrbubbbuuullblllrfrfuulflddddddddd",
                     "ffulfffffbbuurfrrrruulbrbbbfllblulllrrbbuuurlddddddddd",
                     "lruffffffllfurlrrrrfbubrbbbuubblrlllrlububuufddddddddd",
                     "ufurfuffflurrrlrrrubuubbbbbrflrlflllblfuubblfddddddddd",
                     "uuubflffffubfrlrrrlrlubrbbbfbbblulllufulurrfrddddddddd",
                     "llubfbffffrrlrfrrrbbulbfbbbbruulullllruuuffurddddddddd",
                     "ulfufbfffrrlurfrrrfburbubbbrblllflllbruluubfuddddddddd",
                     "uuuuflfffrrrurfrrrubulbrbbblulblblllflffufbrbddddddddd",
                     "rfubfffffbfurrbrrrllflbrbbbruuulrllluufbulbulddddddddd",
                     "bblufuffffrulrfrrrfluubrbbbrruulblllbfrfublluddddddddd",
                     "ubbffbfffuufurlrrrulfbbrbbbrflulullluflrulbrrddddddddd"]:
            self.assertTrue(Cube(cube).match_pattern("....f.fff....r.rrr....b.bbb....l.lll....u....ddddddddd")) # sanity check
            self.solve_test(cube, style)

    def solve_from_middle_layer_test(self, style):
        for cube in ["rrbffffffuflrrrrrruufbbbbbbuuflllllllbbluuuurddddddddd",
                     "uffffffffrrlrrrrrrfuubbbbbbrulllllllbbuluubuuddddddddd",
                     "luuffffffrfurrrrrrbufbbbbbbrlullllllurluuufbbddddddddd",
                     "rbfffffffrlbrrrrrrlufbbbbbbuuulllllllfuruubuuddddddddd",
                     "rluffffffbrurrrrrrrfubbbbbblbfllllllfubuuuuulddddddddd",
                     "ullffffffuburrrrrrfuubbbbbblubllllllffrruurubddddddddd",
                     "uuuffffffrubrrrrrrlufbbbbbbrufllllllurufubllbddddddddd",
                     "rfufffffffufrrrrrrullbbbbbbuuullllllbulburburddddddddd",
                     "ubrffffffuuurrrrrrrfubbbbbbbuflllllllubrullufddddddddd",
                     "ulrffffffubbrrrrrruflbbbbbbfrllllllluuruuubufddddddddd",
                     "ublfffffffurrrrrrruulbbbbbburbllllllbffuulruuddddddddd",
                     "luufffffflrrrrrrrrburbbbbbbufbllllllfluuuuubfddddddddd",
                     "bulffffffubrrrrrrruufbbbbbbulrlllllllrfuuuufbddddddddd",
                     "rulfffffffubrrrrrrububbbbbbbrfllllllluruulufuddddddddd",
                     "urufffffflburrrrrrfulbbbbbbuubllllllbfrluurufddddddddd",
                     "fuuffffffbubrrrrrruufbbbbbbuuullllllllrrubrflddddddddd",
                     "brrffffffullrrrrrrffubbbbbbbbrllllllluuuuuuufddddddddd",
                     "ulrffffffbblrrrrrrurrbbbbbbuffllllllfubuuuluuddddddddd",
                     "fulfffffffubrrrrrruubbbbbbbluullllllubrfurrluddddddddd",
                     "uurffffffurbrrrrrrlubbbbbbbubfllllllrluuuulffddddddddd"]:
            self.assertTrue(Cube(cube).match_pattern("...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd")) # sanity check
            self.solve_test(cube, style)

    def solve_from_top_cross_test(self, style):
        for cube in ["lfrffffffurrrrrrrrbbbbbbbbbllulllllluuuuuufufddddddddd",
                     "lfbffffffurbrrrrrrlbfbbbbbbrlulllllluuuuuufurddddddddd",
                     "uflfffffffrurrrrrrbbrbbbbbbblrlllllluuluuufuuddddddddd",
                     "lffffffffurrrrrrrrbbubbbbbbflbllllllruuuuuuulddddddddd",
                     "ufrffffffbrfrrrrrrrbubbbbbblllllllllfuuuuubuuddddddddd",
                     "ffuffffffbrrrrrrrrubrbbbbbbblllllllluufuuuuulddddddddd",
                     "ffuffffffrrlrrrrrrfbubbbbbbblullllllluuuuurubddddddddd",
                     "ufbffffffururrrrrrbbubbbbbbflfllllllruluuulurddddddddd",
                     "lfufffffffrbrrrrrrublbbbbbbulullllllburuuufurddddddddd",
                     "ufrffffffurbrrrrrrlbfbbbbbbulbllllllluuuuurufddddddddd",
                     "lflffffffurrrrrrrrububbbbbbrlullllllbufuuufubddddddddd",
                     "uflffffffururrrrrrrbubbbbbbllrllllllfubuuufubddddddddd",
                     "rflffffffurrrrrrrrbbubbbbbbllfllllllfuuuuuuubddddddddd",
                     "uflffffffurbrrrrrrublbbbbbbflrlllllluuruuufubddddddddd",
                     "fffffffffrrurrrrrrrblbbbbbbullllllllbubuuuuuuddddddddd",
                     "ffrffffffbrurrrrrrlbubbbbbbblulllllllufuuuruuddddddddd",
                     "rfbffffffururrrrrrlbbbbbbbbllflllllluufuuuuurddddddddd",
                     "ufuffffffbrfrrrrrrrbrbbbbbbblflllllluuuuuululddddddddd",
                     "rfrffffffbrurrrrrrlblbbbbbbulfllllllbufuuuuuuddddddddd",
                     "ffuffffffrrbrrrrrrlbrbbbbbbullllllllfuuuuuuubddddddddd"]:
            self.assertTrue(Cube(cube).match_pattern(".f.ffffff.r.rrrrrr.b.bbbbbb.l.llllll.u.uuu.u.ddddddddd")) # sanity check
            self.solve_test(cube, style)
    
    def test_default_solve_from_scrambled(self):
        self.solve_from_scrambled_test(None)
    def test_default_solve_from_bottom_cross(self):
        self.solve_from_bottom_cross_test(None)
    def test_default_solve_from_bottom_layer(self):
        self.solve_from_bottom_layer_test(None)
    def test_default_solve_from_middle_layer(self):
        self.solve_from_middle_layer_test(None)
    def test_default_solve_from_top_cross(self):
        self.solve_from_top_cross_test(None)
    
    def test_classic_solve_from_scrambled(self):
        self.solve_from_scrambled_test("classic")
    def test_classic_solve_from_bottom_cross(self):
        self.solve_from_bottom_cross_test("classic")
    def test_classic_solve_from_bottom_layer(self):
        self.solve_from_bottom_layer_test("classic")
    def test_classic_solve_from_middle_layer(self):
        self.solve_from_middle_layer_test("classic")
    def test_classic_solve_from_top_cross(self):
        self.solve_from_top_cross_test("classic")

if __name__ == '__main__':
    unittest.main()