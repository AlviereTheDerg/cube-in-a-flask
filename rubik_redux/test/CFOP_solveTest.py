
import unittest
import rubik_redux.controller.CFOP_solve as solver
from rubik_redux.model.cube import Cube
from rubik_redux.test.solver_test_skeleton import solver_test_skeleton
import rubik_redux.model.constants as constants
from rubik_redux.test.symbol_scrambler import symbol_scramble_decorator

class CFOP_solve_tests(solver_test_skeleton):
    def test_solve_full_cube_change_nothing(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver.solve)

    def solve_full_cube_test(self, cube_string):
        self.solve_successful_test(cube_string, solver.solve, "fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
    
    def test_solve_full_cube_top_layer_unsolved(self):
        self.solve_full_cube_test("bfufffffffrlrrrrrrublbbbbbbflrlllllluubuuuuurddddddddd")
    def test_solve_full_cube_top_cross_unsolved(self):
        self.solve_full_cube_test("buufffffflfbrrrrrrlrrbbbbbbuurllllllfuubuuulfddddddddd")
    def test_solve_full_cube_middle_layer_unsolved(self):
        self.solve_full_cube_test("blubfbffflfblrrrrrlurubrbbbuurflrlllffubuluufddddddddd")
    def test_solve_full_cube_bottom_layer_unsolved(self):
        self.solve_full_cube_test("dubfflrfulufurlfrblubbbflbfurfllruldrfdbubrrubdldddrdd")
    def test_solve_full_cube_bottom_cross_unsolved(self):
        self.solve_full_cube_test("ddrlfdrfbfulrrulrrudfbbbbdrurlrlbululbbuulffdfudfdfbld")
    
    def test_solve_full_cube_scrambled_barrage(self):
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
            self.solve_full_cube_test(cube)

    def test_solve_full_cube_bottom_cross_barrage(self):
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
            self.solve_full_cube_test(cube)

    def test_solve_full_cube_bottom_layer_barrage(self):
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
            self.solve_full_cube_test(cube)

    def test_solve_full_cube_middle_layer_barrage(self):
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
            self.solve_full_cube_test(cube)

    def test_solve_full_cube_top_cross_barrage(self):
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
            self.solve_full_cube_test(cube)

    
    def test_bottom_cross_change_nothing_cross_solved(self):
        self.change_nothing_test("fuluflufldllbrrdrrulbfbubbrurlblfdlfrfbbuuurfrdbdddfdd", solver._bottom_cross)
    def test_bottom_cross_change_nothing_bottom_layer_solved(self):
        self.change_nothing_test("ruulfrfffrbubrrrrrbbufbubbblffrlflllfuluululbddddddddd", solver._bottom_cross)
    def test_bottom_cross_change_nothing_middle_layer_solved(self):
        self.change_nothing_test("ruuffffffbuurrrrrrlufbbbbbbruullllllurfbulbflddddddddd", solver._bottom_cross)
    def test_bottom_cross_change_nothing_top_cross_solved(self):
        self.change_nothing_test("ffufffffffrurrrrrrrbubbbbbbblllllllllubuuuuurddddddddd", solver._bottom_cross)
    def test_bottom_cross_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._bottom_cross)
    
    def solve_bottom_cross_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._bottom_cross, "....f..f.....r..r.....b..b.....l..l.....u.....d.ddd.d.")

    def test_bottom_cross_from_unsolved_1(self):
        self.solve_bottom_cross_test("udlrfufdddlbbrbfublbulbbldrrfrdlfbuubruluufrflfrfdrdld")
    def test_bottom_cross_from_unsolved_2(self):
        self.solve_bottom_cross_test("urrlflrbfdrfbrudddrlufbrbrblbbdluudfffuuubrfbddlfdllul")
    def test_bottom_cross_from_unsolved_3(self):
        self.solve_bottom_cross_test("udrlfrfudbrlfrbrdlbuuubufbufdffldlldrldbublrurrbfdfbld")
    def test_bottom_cross_From_unsolved_4(self):
        self.solve_bottom_cross_test("fffffffffurrurrurrbbbbbbbbblldlldllduuuuuulllrrrdddddd")
    def test_bottom_cross_From_unsolved_5(self):
        self.solve_bottom_cross_test("ffuffufflrrrrrruuudbbdbbrbblldlldllduubuubllbrrfddfddf")
    def test_bottom_cross_From_unsolved_6(self):
        self.solve_bottom_cross_test("ffuffuffrrrrrrrddddbbdbblbbllullulluuubuubrrbllfddfddf")
    def test_bottom_cross_From_unsolved_7(self):
        self.solve_bottom_cross_test("fflffdffddddrrrrrrrbbubbubbllullulluuufuufrrfllbddbddb")
    
    def test_bottom_cross_barrage(self):
        for cube in ["fbfbfuufuddbfrdrdurrubbufbbrddlllllbbudlurlurlrffdfdrl",
                     "urudffbddlrfdrrbuulurbbrbbufllfllrbrdfdfuubdfdbludlflr",
                     "bufdffdbbrdflrfrrduudrburldlrullllrrbfluuflbufduddbfbb",
                     "rflufflufflrlruddfbbufbrrddfrbbllbdurluuuddrubblrdblfd",
                     "flbdfffufldudrrdrlrubbbdurbrbubllluddfblurrfurblldfduf",
                     "brfuflffdrrlururrdubffbbfblufrrlbdllllblufuuuddbdddbdr",
                     "rllufufrfurbbrldbbuudfbflffrubrlluluffrrubdbbldldddrdd",
                     "urufflfffbuufrurrrfrflbbbbbubbulullllbrlurrflddddddddd"]:
            self.solve_bottom_cross_test(cube)

    # be able to solve the 'easy cases' regardless of top face orientation
    @symbol_scramble_decorator
    def solve_first_two_layers_easy_cases_test(self, cube_string, target):
        cube = Cube(cube_string)
        target_corner = constants.OTHER_SIDE_OF[target][0]
        for _ in range(4):
            cube.rotate("U")
            secondary_cube = Cube(str(cube))
            result = solver._first_two_layers_easy_cases(secondary_cube, target_corner)
            self.assertTrue(secondary_cube.match_pattern("...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd"), f"While solving target {target}") # solves stage
            confirm_cube = Cube(str(cube))
            confirm_cube.rotate(result)
            self.assertEqual(str(secondary_cube), str(confirm_cube), f"While solving target {target}") # reproducable

    # in order: FRONT RIGHT, BACK RIGHT, BACK LEFT, FRONT LEFT
    def test_first_two_layers_help_easy_case__RHS_together(self):
        self.solve_first_two_layers_easy_cases_test("ffdffuffurrrrrrfrrbllbbbbbbubullllllbuuuufrufddldddddd", constants.DTR)
        self.solve_first_two_layers_easy_cases_test("ubfffffffurdrrfrrrbbuubbfbbrulllllllbrrluubulddddddddu", constants.DBR)
        self.solve_first_two_layers_easy_cases_test("furffffffbrrrrrrrruudbbubbllllbllbllblfbuuufuddddddudd", constants.DBL)
        self.solve_first_two_layers_easy_cases_test("fffrffuffrbfrrrrrruulbbbbbbuudllullrbllfuullubdddddddd", constants.DTL)
    def test_first_two_layers_help_easy_case__LHS_together(self):
        self.solve_first_two_layers_easy_cases_test("rffffbfffdllurrlrrurubbbbbbffullllllrubuuubrrddudddddd", constants.DTR)
        self.solve_first_two_layers_easy_cases_test("urbffffffurrrrbrrfdulubbubbuufllllllblbfublurddddddddr", constants.DBR)
        self.solve_first_two_layers_easy_cases_test("bbrffffffuuurrrrrrlbbbbrbbbdurullullllffuluufddddddldd", constants.DBL)
        self.solve_first_two_layers_easy_cases_test("dbflffbffurlrrrrrruuubbbbbbfllllullurfbfuufulrdddddddd", constants.DTL)
    def test_first_two_layers_help_easy_case__RHS_apart(self):
        self.solve_first_two_layers_easy_cases_test("ubfffuffrdllfrrfrrurlbbbbbbfrbllllllufbuuururddudddddd", constants.DTR)
        self.solve_first_two_layers_easy_cases_test("furffffffbbrrrurrldulrbbubbubullllllblbruurfuddddddddf", constants.DBR)
        self.solve_first_two_layers_easy_cases_test("bluffffffbbfrrrrrrurbbblbbfdurullulllulfuuublddddddrdd", constants.DBL)
        self.solve_first_two_layers_easy_cases_test("dbfuffuffufbrrrrrrurrbbbbbbuulllfllbfurlulfulldddddddd", constants.DTL)
    def test_first_two_layers_help_easy_case__LHS_apart(self):
        self.solve_first_two_layers_easy_cases_test("ffdfflfflrrburrbrrubfbbbbbbufulllllllurruurufddudddddd", constants.DTR)
        self.solve_first_two_layers_easy_cases_test("rrfffffffurdrrurrlburlbbbbbbbfllllllufruuuublddddddddu", constants.DBR)
        self.solve_first_two_layers_easy_cases_test("urbfffffflbrrrrrrruudbbubbrlbffllullblfuulluuddddddbdd", constants.DBL)
        self.solve_first_two_layers_easy_cases_test("frrufflffuuurrrrrrrllbbbbbbuudllbllfbfbfullufudddddddd", constants.DTL)

    
    @symbol_scramble_decorator
    def reduce_to_first_two_layers_easy_case_test(self, cube_string, target, target_corner, where_is_target_corner, where_is_target_edge):
        cube = Cube(cube_string)
        
        targets = [constants.OTHER_SIDE_OF[target][0]]
        targets.append(constants.CYCLE_OF_FACE_OF[targets[0]][1][1]) # get the piece IDs of the target pillar pieces

        # store current pieces of pillars that should not be touched
        anti_targets = [constants.FMR, constants.FBR, constants.RMR, constants.RBR, constants.BMR, constants.BBR, constants.LMR, constants.LBR] # blank
        if len(shared := (constants.ALL_SIDES_OF[where_is_target_corner] | constants.ALL_SIDES_OF[where_is_target_edge]) & set(anti_targets)) != 0:
            pillar_id = anti_targets.index(shared.pop()) // 2
            pillar_contents = {anti_targets[2*pillar_id], anti_targets[2*pillar_id+1]}
            anti_targets = [piece for piece in anti_targets if piece not in pillar_contents] # remove pillars containing target pieces
        anti_targets = [piece for piece in anti_targets if piece not in targets] # remove target pillar
        anti_target_data = [cube.cube_data[piece] for piece in anti_targets] # store current pieces
        
        result = [solver._reduce_to_first_two_layers_easy_case(cube, target_corner, where_is_target_corner, where_is_target_edge)] # reduce the target to an easy case
        self.assertEqual(anti_target_data, [cube.cube_data[piece] for piece in anti_targets]) # determine current pieces unmoved
        result.append(solver._first_two_layers_easy_cases(cube, target_corner)) # previous tests confirm this functioning
        result = "".join(result) # combine motions to a single string

        actuals = [cube.where_is(piece) for piece in targets] # find where they are on the cube
        self.assertEqual(targets, actuals, f"While solving target {target}") # check that they were moved into place correctly

        confirm_cube = Cube(cube_string)
        confirm_cube.rotate(result)
        self.assertEqual(str(cube), str(confirm_cube), f"While solving target {target}") # test reproducability
    
    def all_permutations_reduce_to_first_two_layers_easy_case(self, solve_algorithm: str):
        for faces, dest_target in zip(["frbl", "rblf", "blfr", "lfrb"], [constants.DTR, constants.DBR, constants.DBL, constants.DTL]):
            cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
            target_corner = constants.OTHER_SIDE_OF[dest_target][0]
            target_edge = constants.CYCLE_OF_FACE_OF[target_corner][1][1]

            for face in faces:
                cube.move_algorithm(solve_algorithm[::-1].swapcase(), face)
                self.reduce_to_first_two_layers_easy_case_test(str(cube), dest_target, target_corner, cube.where_is(target_corner), cube.where_is(target_edge))
                cube.move_algorithm(solve_algorithm, face)
                cube.move_algorithm("RUrBuub", face)

    def test_reduce_to_first_two_layers_easy_case_2nd_corner_down_LHS(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("URurufUF")
    def test_reduce_to_first_two_layers_easy_case_2nd_corner_down_RHS(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("ufUFURur")
    def test_reduce_to_first_two_layers_easy_case_2nd_corner_right_LHS(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("fUFufUF")
    def test_reduce_to_first_two_layers_easy_case_2nd_corner_right_RHS(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RUruRUr")
    def test_reduce_to_first_two_layers_easy_case_2nd_corner_left_LHS(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("fuFUfuF")
    def test_reduce_to_first_two_layers_easy_case_2nd_corner_left_RHS(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RurURur")

    def test_reduce_to_first_two_layers_easy_case_3rd_corner_up(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RUruRUruRUr")
    def test_reduce_to_first_two_layers_easy_case_3rd_corner_up_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RurUfUF")
    def test_reduce_to_first_two_layers_easy_case_3rd_corner_right(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfUFUfUUF")
    def test_reduce_to_first_two_layers_easy_case_3rd_corner_right_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfuFuRUr")
    def test_reduce_to_first_two_layers_easy_case_3rd_corner_left(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRuruRUUr")
    def test_reduce_to_first_two_layers_easy_case_3rd_corner_left_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRUrUfuF")

    def test_reduce_to_first_two_layers_easy_case_4th_corner_right_RHS_together_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RurUUfuF")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_left_LHS_together_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("fUFuuRUr")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_right_RHS_apart_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfUUFUfUUF")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_left_LHS_apart_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRUUruRUUr")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_right_LHS_apart(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfuFUfUUF")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_left_RHS_apart(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRUruRUUr")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_right_RHS_together(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRurURUr")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_left_LHS_together(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfUFufuF")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_right_LHS_apart_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRUrURUr")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_left_RHS_apart_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfuFufuF")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_right_LHS_together_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UfUUFuRUr")
    def test_reduce_to_first_two_layers_easy_case_4th_corner_left_RHS_together_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("uRUUrUfuF")
    
    def test_reduce_to_first_two_layers_easy_case_5th_LHS_together_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RUruuRUruRUr")
    def test_reduce_to_first_two_layers_easy_case_5th_RHS_together_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("fuFUUfuFUfuF")
    def test_reduce_to_first_two_layers_easy_case_5th_LHS_apart_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UURUrURur")
    def test_reduce_to_first_two_layers_easy_case_5th_RHS_apart_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("UUfuFufUF")
    def test_reduce_to_first_two_layers_easy_case_5th_RHS_apart(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("URUUrURur")
    def test_reduce_to_first_two_layers_easy_case_5th_LHS_apart(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("ufUUFufUF")
    def test_reduce_to_first_two_layers_easy_case_5th_RHS_together(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RUUruRUr")
    def test_reduce_to_first_two_layers_easy_case_5th_LHS_together(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("fUUFUfuF")
    
    def test_reduce_to_first_two_layers_easy_case_6th_corner_down(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("FUfRuur")
    def test_reduce_to_first_two_layers_easy_case_6th_corner_down_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RurUfUUFUfUUF")
    def test_reduce_to_first_two_layers_easy_case_6th_corner_right(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RurURUUrURur")
    def test_reduce_to_first_two_layers_easy_case_6th_corner_right_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RUruRurUUfuF")
    def test_reduce_to_first_two_layers_easy_case_6th_corner_left(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RuruRUruRUUr")
    def test_reduce_to_first_two_layers_easy_case_6th_corner_left_flip(self):
        self.all_permutations_reduce_to_first_two_layers_easy_case("RurUfuFufuF")
    
    def test_first_two_layers_unmet_requisite_1(self): # scrambled
        self.raise_unmet_requisite_stage_test("rbuffbllrlfldrbuurddrrbrdlbdffflulrubrfludulfbubudbddf", solver._first_two_layers, "first two layers")
    def test_first_two_layers_unmet_requisite_2(self): # scrambled
        self.raise_unmet_requisite_stage_test("burlfrlbufuudrbbdfblldbudffffdrlfudbubluubrlddrrldfrrl", solver._first_two_layers, "first two layers")

    def test_first_two_layers_change_nothing_first_two_layers_solved_1(self):
        self.change_nothing_test("fulffffffuurrrrrrrbrubbbbbbfblllllllruuuufulbddddddddd", solver._first_two_layers)
    def test_first_two_layers_change_nothing_first_two_layers_solved_2(self):
        self.change_nothing_test("fuuffffffruurrrrrrllbbbbbbblrulllllluufuubrfbddddddddd", solver._first_two_layers)
    def test_first_two_layers_change_nothing_OLL_solved_1(self):
        self.change_nothing_test("fbbfffffflrfrrrrrrrlrbbbbbbbfllllllluuuuuuuuuddddddddd", solver._first_two_layers)
    def test_first_two_layers_change_nothing_OLL_solved_2(self):
        self.change_nothing_test("rbbffffffllrrrrrrrbflbbbbbbfrflllllluuuuuuuuuddddddddd", solver._first_two_layers)
    def test_first_two_layers_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._first_two_layers)
    
    def solve_first_two_layers_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._first_two_layers, "...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd")

    def test_first_two_layers_easy_case(self): # can solve from a single easy case
        self.solve_first_two_layers_test("rruffufffbrrbrrurrbllbbbbbbffdlllllluuuuuufflddrdddddd")
    def test_first_two_layers_mild_case(self): # can solve from a single secondary case (reduce to easy -> solve easy)
        self.solve_first_two_layers_test("uffffufffruubrrrrrlrrbbbbbbbfllllllluufuulbruddddddddd")
    def test_first_two_layers_multiple_mild_cases(self): # can solve multiple secondary cases
        self.solve_first_two_layers_test("lffffufffruubrrrrrbubbbubbudburllblllfllulfruddddddrdd")
    def test_first_two_layers_complex_case(self): # corner piece and edge piece are in different pillars
        self.solve_first_two_layers_test("fuffflfffrrrurfrrrbbbrbbbbblfllllllluruuuuubuddddddddd")
    def test_first_two_layers_multiple_complex_cases(self): # two pillars have edge pieces swapped
        self.solve_first_two_layers_test("flfrflfffrbrfrrrrrbubbbbbbblulllflllufuruuuuuddddddddd")
    
    def test_first_two_layers_barrage(self):
        for cube in ["rllbflrffuflurbrrubrllbufbrdubblrflbfudfurdfbudddddudl",
                     "uluffrdfrbbbbrrbrdulffblfbduurblublflfrruufulldddddldr",
                     "fbfffudfdrrrbrlfrrbrlfbrbbufudululllufulubllubdrdddbdd",
                     "ffdlfflffflrrrrrrrdurubfublurlllbdlufbbbuuuulbdddddbdb",
                     "rrrufbuffbrllrrdrdbflbbfrbuubdlllflfbuduuuffurdldddldb",
                     "uurffbffldlllrubrfbufrbblbdlubrlrflrdldbufrfbududddrdu",
                     "dulfffufddfurrubrblbrlblubbfrrbllrlfdrfuuubbfrdldddudl",
                     "uurrfubfduldfrfrrrrrflbbubllbflludlldffruulbfudbdddbdb",
                     "rubufrufduudfrlbrurlfbbrrbllrbblfulbdffuuldbrldldddfdf",
                     "ubflfflflubrlrffrdbrrrbbbbdduruluflubuufurfllbdddddrdl",
                     "lffufuffllubfrudruubrlbflbrfrullbblrdlrburfrdudbdddddb",
                     "bulffuufdbblbrffrudburburbrllurllblrflfuurlfdbdrdddddf"]:
            self.solve_bottom_cross_test(cube)
    

    def test_OLL_unmet_requisite_scrambled_1(self): # scrambled
        self.raise_unmet_requisite_stage_test("rbuffbllrlfldrbuurddrrbrdlbdffflulrubrfludulfbubudbddf", solver._orient_last_layer, "orient last layer")
    def test_OLL_unmet_requisite_scrambled_2(self): # scrambled
        self.raise_unmet_requisite_stage_test("burlfrlbufuudrbbdfblldbudffffdrlfudbubluubrlddrrldfrrl", solver._orient_last_layer, "orient last layer")
    def test_OLL_unmet_requisite_bottom_cross_1(self): # bottom cross solved
        self.raise_unmet_requisite_stage_test("urrffluffdbdbrrlrbrlubbflbdbubllrllfluffuurubrdudddfdd", solver._orient_last_layer, "orient last layer")
    def test_OLL_unmet_requisite_bottom_cross_2(self): # bottom cross solved
        self.raise_unmet_requisite_stage_test("bfbffbdfluudurburdbuulbblbbfuurllllrrfrrullrrfdfdddddf", solver._orient_last_layer, "orient last layer")

    def test_OLL_change_nothing_OLL_solved_1(self):
        self.change_nothing_test("fbbfffffflrfrrrrrrrlrbbbbbbbfllllllluuuuuuuuuddddddddd", solver._orient_last_layer)
    def test_OLL_change_nothing_OLL_solved_2(self):
        self.change_nothing_test("rbbffffffllrrrrrrrbflbbbbbbfrflllllluuuuuuuuuddddddddd", solver._orient_last_layer)
    def test_OLL_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._orient_last_layer)
    
    def solve_OLL_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._orient_last_layer, "...ffffff...rrrrrr...bbbbbb...lllllluuuuuuuuuddddddddd")

    def all_permutations_OLL(self, solve_algorithm: str):
        cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
        cube.rotate(solve_algorithm[::-1].swapcase())
        if not cube.match_pattern("...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd"): # sanity check
            raise ValueError("Input breaks F2L")
        for _ in range(4):
            self.solve_OLL_test(str(cube))
            cube.rotate("U")

    def test_OLL_dot_A(self):
        self.all_permutations_OLL("RUbRBRRurFRf") # R U B' l U l2' x' U' R' F R F'
    def test_OLL_dot_B(self):
        self.all_permutations_OLL("rFRfUUrFRFFUUF") # R' F R F' U2 R' F R y' R2 U2 R
    def test_OLL_dot_C(self):
        self.all_permutations_OLL("UlRRBrBLUUlBLr") # y L' R2 B R' B L U2' L' B M'
    def test_OLL_dot_D(self):
        self.all_permutations_OLL("rUUrFRfufuFuR") # R' U2 x R' U R U' y R' U' R' U R' F
    def test_OLL_dot_E(self):
        self.all_permutations_OLL("RUrUrFRfUUrFRf") # (R U R' U) R' F R F' U2 R' F R F'
    def test_OLL_dot_F(self):
        self.all_permutations_OLL("LrFFlRUULrFlRUULrFFlR") # M' U2 M U2 M' U M U2 M' U2 M
    def test_OLL_dot_G(self):
        self.all_permutations_OLL("rUUFRUruFFUUFR") # R' U2 F (R U R' U') y' R2 U2 x' R U
    def test_OLL_dot_H(self):
        self.all_permutations_OLL("FRUrUfUUfLFl") # F (R U R' U) y' R' U2 (R' F R F')

    def test_OLL_line_A(self):
        self.all_permutations_OLL("rufUfLFlFR") # R' U' y L' U L' y' L F L' F R
    def test_OLL_line_B(self):
        self.all_permutations_OLL("RuBBDbUUBdBBUr") # R U' y R2 D R' U2 R D' R2 d R'
    def test_OLL_line_C(self):
        self.all_permutations_OLL("FURurURurf") # F U R U' R' U R U' R' F'
    def test_OLL_line_D(self):
        self.all_permutations_OLL("lbLurURurURlBL") # L' B' L U' R' U R U' R' U R L' B L
        
    def test_OLL_cross_A(self):
        self.all_permutations_OLL("LurUlURUrUR") # L U' R' U L' U (R U R' U) R
    def test_OLL_cross_B(self):
        self.all_permutations_OLL("RUrURurURUUr") # (R U R' U) R U' R' U R U2 R'
    def test_OLL_cross_C(self):
        self.all_permutations_OLL("lURuLUr") # L' U R U' L U R'
    def test_OLL_cross_D(self):
        self.all_permutations_OLL("rUURUrUR") # R' U2 (R U R' U) R
    def test_OLL_cross_E(self):
        self.all_permutations_OLL("rfLFRflF") # R' F' L F R F' L' F
    def test_OLL_cross_F(self):
        self.all_permutations_OLL("RRDrUURdrUUr") # R2 D R' U2 R D' R' U2 R'
    def test_OLL_cross_G(self):
        self.all_permutations_OLL("rflFRfLF") # R' F' L' F R F' L F
        
    def test_OLL_4_corners_A(self):
        self.all_permutations_OLL("LrflRUULrflR") # M' U' M U2' M' U' M
    def test_OLL_4_corners_B(self):
        self.all_permutations_OLL("lRUruLrFRf") # L' (R U R' U') L R' F R F'
        
    def test_OLL_L_upleft_A(self):
        self.all_permutations_OLL("LFrFRFFl") # L F R' F R F2 L'
    def test_OLL_L_upleft_B(self):
        self.all_permutations_OLL("FrfRURur") # F R' F' R U R U' R'
    def test_OLL_L_upleft_C(self):
        self.all_permutations_OLL("ruRFrfUFRf") # R' U' R y' x' R U' R' F R U R'
    def test_OLL_L_upleft_D(self):
        self.all_permutations_OLL("uRUUruRuRRfuFUR") # U' R U2' R' U' R U' R2 y' R' U' R U B
    def test_OLL_L_upleft_E(self):
        self.all_permutations_OLL("FRUruRUruf") # F (R U R' U') (R U R' U') F'
    def test_OLL_L_upleft_F(self):
        self.all_permutations_OLL("LflFUULLBLbL") # L F' L' F U2 L2 y' L F L' F
        
    def test_OLL_L_upright_A(self):
        self.all_permutations_OLL("urUURUrURRBUbur") # U' R' U2 (R U R' U) R2 y (R U R' U') F'
    def test_OLL_L_upright_B(self):
        self.all_permutations_OLL("LFFrfRfl") # r U2 R' U' R U' r'
    def test_OLL_L_upright_C(self):
        self.all_permutations_OLL("rUURRbrBrUUR") # R' U2 l R U' R' U l' U2 R
    def test_OLL_L_upright_D(self):
        self.all_permutations_OLL("fluLUluLUF") # F' L' U' L U L' U' L U F
    def test_OLL_L_upright_E(self):
        self.all_permutations_OLL("rFrfRRUUbRBr") # R' F R' F' R2 U2 x' U' R U R'
    def test_OLL_L_upright_F(self):
        self.all_permutations_OLL("rFRfUURRbrBr") # R' F R F' U2 R2 y R' F' R F'
        
    def test_OLL_L_downleft_A(self):
        self.all_permutations_OLL("RUrbRBubrB") # R U R' y R' F R U' R' F' R
    def test_OLL_L_downleft_B(self):
        self.all_permutations_OLL("lbLurURlBL") # L' B' L U' R' U R L' B L
    def test_OLL_L_downleft_C(self):
        self.all_permutations_OLL("UULRRfRfrFFRflR") # U2 r R2' U' R U' R' U2 R U' M
    def test_OLL_L_downleft_D(self):
        self.all_permutations_OLL("bRbRRURUruRBB") # x' U' R U' R2' F x (R U R' U') R B2
        
    def test_OLL_L_downright_A(self):
        self.all_permutations_OLL("LufUUfUFuFUUFul") # L U' y' R' U2' R' U R U' R U2 R d' L'
    def test_OLL_L_downright_B(self):
        self.all_permutations_OLL("UUrLLFlFLFFlFlR") # U2 l' L2 U L' U L U2 L' U M
    def test_OLL_L_downright_C(self):
        self.all_permutations_OLL("RRUrbRuRRURBr") # R2' U R' B' R U' R2' U l U l'
    def test_OLL_L_downright_D(self):
        self.all_permutations_OLL("lBBRBrBL") # r' U2 (R U R' U) r
        
    def test_OLL_C_A(self):
        self.all_permutations_OLL("RURbrBur") # R U x' R U' R' U x U' R'
    def test_OLL_C_B(self):
        self.all_permutations_OLL("RUrubrFRfB") # (R U R' U') x D' R' U R E'
        
    def test_OLL_L_A(self):
        self.all_permutations_OLL("rFRUrfRFuf") # R' F R U R' F' R y L U' L'
    def test_OLL_L_B(self):
        self.all_permutations_OLL("LfluLFlfUF") # L F' L' U' L F L' y' R' U R
    def test_OLL_L_C(self):
        self.all_permutations_OLL("lbLruRUlBL") # L' B' L R' U' R U L' B L
    def test_OLL_L_D(self):
        self.all_permutations_OLL("RBrLUluRbr") # R B R' L U L' U' R B' R'
        
    def test_OLL_P_A(self):
        self.all_permutations_OLL("FURurf") # F U R U' R' F'
    def test_OLL_P_B(self):
        self.all_permutations_OLL("ruFURurfR") # R' d' L d R U' R' F' R
    def test_OLL_P_C(self):
        self.all_permutations_OLL("LUfulULFl") # L d R' d' L' U L F L'
    def test_OLL_P_D(self):
        self.all_permutations_OLL("fulULF") # F' U' L' U L F
        
    def test_OLL_T_A(self):
        self.all_permutations_OLL("FRUruf") # F (R U R' U') F'
    def test_OLL_T_B(self):
        self.all_permutations_OLL("RUrurFRf") # (R U R' U') R' F R F'
        
    def test_OLL_W_A(self):
        self.all_permutations_OLL("LUlULululBLb") # L U L' U L U' L' U' y2' R' F R F'
    def test_OLL_W_B(self):
        self.all_permutations_OLL("ruRurURURbrB") # R' U' R U' R' U R U y F R' F' R
        
    def test_OLL_Z_A(self):
        self.all_permutations_OLL("rFRUrufUR") # R' F (R U R' U') y L' d R
    def test_OLL_Z_B(self):
        self.all_permutations_OLL("LfluLUFul") # L F' L' U' L U y' R d' L'
    

    def test_PLL_unmet_requisite_scrambled_1(self): # scrambled
        self.raise_unmet_requisite_stage_test("rbuffbllrlfldrbuurddrrbrdlbdffflulrubrfludulfbubudbddf", solver._permute_last_layer, "permute last layer")
    def test_PLL_unmet_requisite_scrambled_2(self): # scrambled
        self.raise_unmet_requisite_stage_test("burlfrlbufuudrbbdfblldbudffffdrlfudbubluubrlddrrldfrrl", solver._permute_last_layer, "permute last layer")
    def test_PLL_unmet_requisite_bottom_cross_1(self): # bottom cross solved
        self.raise_unmet_requisite_stage_test("urrffluffdbdbrrlrbrlubbflbdbubllrllfluffuurubrdudddfdd", solver._permute_last_layer, "permute last layer")
    def test_PLL_unmet_requisite_bottom_cross_2(self): # bottom cross solved
        self.raise_unmet_requisite_stage_test("bfbffbdfluudurburdbuulbblbbfuurllllrrfrrullrrfdfdddddf", solver._permute_last_layer, "permute last layer")
    def test_PLL_unmet_requisite_middle_layer_1(self): # F2L solved
        self.raise_unmet_requisite_stage_test("ubbfffffflfbrrrrrruufbbbbbbuurlllllllrrluufuuddddddddd", solver._permute_last_layer, "permute last layer")
    def test_PLL_unmet_requisite_middle_layer_2(self): # F2l solved
        self.raise_unmet_requisite_stage_test("fbuffffffluurrrrrrburbbbbbbbfullllllulluurrufddddddddd", solver._permute_last_layer, "permute last layer")

    def test_PLL_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._permute_last_layer)
    
    def solve_PLL_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._permute_last_layer, "fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")

    def all_permutations_PLL(self, solve_algorithm: str):
        cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
        cube.rotate(solve_algorithm[::-1].swapcase())
        if not cube.match_pattern("...ffffff...rrrrrr...bbbbbb...lllllluuuuuuuuuddddddddd"): # sanity check
            raise ValueError("Input breaks OLL")
        for _ in range(4):
            self.solve_PLL_test(str(cube))
            cube.rotate("U")
    
    def test_PLL_A1(self):
        self.all_permutations_PLL("rFrBBRfrBBRR") # x [(R' U R') D2] [(R U' R') D2] R2
    def test_PLL_A2(self):
        self.all_permutations_PLL("RbRFFrBRFFRR") # x' [(R U' R) D2] [(R' U R) D2] R2
    def test_PLL_U1(self):
        self.all_permutations_PLL("RRURUrururUr") # R2 U [R U R' U'] (R' U') (R' U R')
    def test_PLL_U2(self):
        self.all_permutations_PLL("RuRURURuruRR") # [R U'] [R U] [R U] [R U'] R' U' R2
    def test_PLL_H(self):
        self.all_permutations_PLL("LLRRDLLRRUULLRRDLLRR") # M2 U M2 U2 M2 U M2
    def test_PLL_T(self):
        self.all_permutations_PLL("RUrurFRRuruRUrf") # [R U R' U'] [R' F] [R2 U' R'] U' [R U R' F']
    def test_PLL_J1(self):
        self.all_permutations_PLL("rUlUURurUURLu") # [R' U L'] [U2 R U' R' U2] [R L U']
    def test_PLL_J2(self):
        self.all_permutations_PLL("RUrfRUrurFRRuru") # [R U R' F'] {[R U R' U'] [R' F] [R2 U' R'] U'}
    def test_PLL_R1(self):
        self.all_permutations_PLL("LUUlUULfluLULFLLU") # [L U2' L' U2'] [L F'] [L' U' L U] [L F] L2' U
    def test_PLL_R2(self):
        self.all_permutations_PLL("rUURUUrFRUrurfRRu") # [R' U2 R U2] [R' F] [R U R' U'] [R' F'] R2 U'
    def test_PLL_V(self):
        self.all_permutations_PLL("rUrubrBBubUbRBR") # [R' U R' d'] [R' F'] [R2 U' R' U] [R' F R F]
    def test_PLL_G1(self):
        self.all_permutations_PLL("RRDbUbuBdRRfUF") # R2 u R' U R' U' R u' R2 [y' R' U R]
    def test_PLL_G2(self):
        self.all_permutations_PLL("ruRBBDlULuLdBB") # [R' U' R] y R2 u R' U R U' R u' R2
    def test_PLL_G3(self):
        self.all_permutations_PLL("RRdFuFUfDRRBub") # R2 u' R U' R U R' u R2 [y R U' R']
    def test_PLL_G4(self):
        self.all_permutations_PLL("RUrFFdLulUlDFF") # [R U R'] y' R2 u' R U' R' U R' u R2
    def test_PLL_F(self):
        self.all_permutations_PLL("rUUrubrBBubUbRBuR") # [R' U2 R' d'] [R' F'] [R2 U' R' U] [R' F R U' F]
    def test_PLL_Z(self):
        self.all_permutations_PLL("LLRRDLLRRULrFFLLRRBBLrUU") # M2 U M2 U M' U2 M2 U2 M' U2
    def test_PLL_Y(self):
        self.all_permutations_PLL("FRuruRUrfRUrurFRf") # F R U' R' U' [R U R' F'] {[R U R' U'] [R' F R F']}
    def test_PLL_N1(self):
        self.all_permutations_PLL("LuRUUlUrLuRUUlUrU") # {(L U' R) U2 (L' U R')} {(L U' R) U2 (L' U R')} U
    def test_PLL_N2(self):
        self.all_permutations_PLL("rUlUURuLrUlUURuLu") # {(R' U L') U2 (R U' L)} {(R' U L') U2 (R U' L)} U'
    def test_PLL_E(self):
        self.all_permutations_PLL("RbrFRBrFFlBLFlbL") # X' (R U' R') D (R U R') u2 (R' U R) D (R' U' R)

if __name__ == '__main__':
    unittest.main()