
import unittest
import rubik_redux.controller.CFOP_solve as solver
from rubik_redux.model.cube import Cube
from rubik_redux.test.solver_test_skeleton import solver_test_skeleton
import rubik_redux.model.constants as constants
from rubik_redux.test.symbol_scrambler import symbol_scramble_decorator

class CFOP_solve_tests(solver_test_skeleton):
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
        for _ in range(4):
            cube.rotate("U")
            secondary_cube = Cube(str(cube))
            result = solver._first_two_layers_easy_cases(secondary_cube, target)
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
    def reduce_to_first_two_layers_easy_case_test(self, cube_string, target):
        cube = Cube(cube_string)
        result = [solver._reduce_to_first_two_layers_easy_case(cube, target)] # reduce the target to an easy case
        result.append(solver._first_two_layers_easy_cases(cube, target)) # previous tests confirm this functioning
        result = "".join(result) # combine motions to a single string

        targets = [constants.OTHER_SIDE_OF[target][0]]
        targets.append(constants.CYCLE_OF_FACE_OF[targets[0]][1][1]) # get the piece IDs of the target pillar pieces
        actuals = [cube.where_is(piece) for piece in targets] # find where they are on the cube
        self.assertEqual(targets, actuals, f"While solving target {target}") # check that they were moved into place correctly

        confirm_cube = Cube(cube_string)
        confirm_cube.rotate(result)
        self.assertEqual(str(cube), str(confirm_cube), f"While solving target {target}") # test reproducability
    
    def all_permutations_reduce_to_first_two_layers_easy_case(self, solve_algorithm: str):
        for faces, dest_target in zip(["frbl", "rblf", "blfr", "lfrb"], [constants.DTR, constants.DBR, constants.DBL, constants.DTL]):
            cube = Cube("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")
            for face in faces:
                cube.move_algorithm(solve_algorithm[::-1].swapcase(), face)
                self.reduce_to_first_two_layers_easy_case_test(str(cube), dest_target)
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

    """
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
        self.all_permutations_reduce_to_first_two_layers_easy_case("RUr")
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
    """
    
    """
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
    """

if __name__ == '__main__':
    unittest.main()