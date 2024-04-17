
import unittest
import rubik_redux.controller.CFOP_solve as solver
from rubik_redux.model.cube import Cube
from rubik_redux.test.solver_test_skeleton import solver_test_skeleton

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

if __name__ == '__main__':
    unittest.main()