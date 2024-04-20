
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
            self.assertEqual(str(secondary_cube), str(confirm_cube), f"While solving targer {target}") # reproducable

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