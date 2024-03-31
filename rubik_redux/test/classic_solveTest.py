
import unittest
import rubik_redux.controller.classic_solve as solver
from rubik_redux.model.cube import Cube
import functools

class solver_tests(unittest.TestCase):
    def symbol_scramble_decorator(func):
        @functools.wraps(func)
        def symbols_scrambled(self, cube_string, *args, **kwargs):
            for translation in [{'f':'b', 'r':'o', 'b':'g', 'l':'r', 'u':'w', 'd':'y'},
                                {'f':'1', 'r':'2', 'b':'3', 'l':'4', 'u':'5', 'd':'6'},
                                {},
                                {'f':'4', 'r':'a', 'b':'b', 'l':'d', 'u':'2', 'd':'l'}]:
                return func(self, "".join(translation.get(piece, piece) for piece in cube_string), *args, **kwargs)
        return symbols_scrambled
    
    @symbol_scramble_decorator
    def raise_unmet_requisite_stage_test(self, cube_string, solve_function, solve_stage_name):
        cube = Cube(cube_string)
        with self.assertRaises(ValueError) as result:
            solve_function(cube)
        self.assertEqual(f"Error: Solving stage \"{solve_stage_name}\": missing prerequisite", str(result.exception))
        self.assertEqual(cube_string, str(cube))

    @symbol_scramble_decorator
    def change_nothing_test(self, cube_string, solve_function):
        cube = Cube(cube_string)
        self.assertEqual("", solve_function(cube))
        self.assertEqual(cube_string, str(cube))
    
    @symbol_scramble_decorator
    def solve_successful_test(self, cube_string, solve_function, expected_pattern):
        cube = Cube(cube_string)
        result = solve_function(cube)
        self.assertTrue(cube.match_pattern(expected_pattern)) # updates existing cube
        output_cube = str(cube)
        cube = Cube(cube_string)
        cube.rotate(result)
        self.assertTrue(output_cube, str(cube)) # using the result makes a matching cube

    def test_bottom_cross_change_nothing_cross_solved(self):
        self.change_nothing_test("fuluflufldllbrrdrrulbfbubbrurlblfdlfrfbbuuurfrdbdddfdd", solver._bottom_cross)
    def test_bottom_cross_change_nothing_bottom_layer_solved(self):
        self.change_nothing_test("ruulfrfffrbubrrrrrbbufbubbblffrlflllfuluululbddddddddd", solver._bottom_cross)
    def test_bottom_cross_change_nothing_bottom_two_layers_solved(self):
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
    

    def test_bottom_layer_unmet_requisite_1(self):
        self.raise_unmet_requisite_stage_test("bufbffbdfdlrdrrubfdrlfbrluluuldldfrububbufdlrrlrbdldfu", solver._bottom_layer, "bottom layer")
    def test_bottom_layer_unmet_requisite_2(self):
        self.raise_unmet_requisite_stage_test("frfdfbfrrdrlurdblbbfubbbuudrlurlfldubudbuurfrlddldffll", solver._bottom_layer, "bottom layer")
    def test_bottom_layer_unmet_requisite_3(self):
        self.raise_unmet_requisite_stage_test("ddrlffflbuurrrbuflbfrlbdddbfrlfludbudluburfrfldludurbb", solver._bottom_layer, "bottom layer")
    def test_bottom_layer_unmet_requisite_4(self):
        self.raise_unmet_requisite_stage_test("ffudfrfbrlbrbrubrbbuflbllluruddlrlddufubullrfrddfdubfd", solver._bottom_layer, "bottom layer")

    def test_bottom_layer_change_nothing_bottom_layer_solved_1(self):
        self.change_nothing_test("rurbfffffbfllrlrrrfbbbbubbblffrlullluruuuruluddddddddd", solver._bottom_layer)
    def test_bottom_layer_change_nothing_bottom_layer_solved_2(self):
        self.change_nothing_test("brurfufffllrbrrrrrulbfbfbbbuluululllrbfuuflbfddddddddd", solver._bottom_layer)
    def test_bottom_layer_change_nothing_bottom_two_solved_1(self):
        self.change_nothing_test("ffbfffffflufrrrrrrrlrbbbbbbbullllllluuurubuuuddddddddd", solver._bottom_layer)
    def test_bottom_layer_change_nothing_bottom_two_solved_2(self):
        self.change_nothing_test("uulffffffururrrrrrlbubbbbbbrurllllllbuffuuflbddddddddd", solver._bottom_layer)
    def test_bottom_layer_change_nothing_top_cross_solved(self):
        self.change_nothing_test("ufrffffffbrurrrrrrlbbbbbbbbllrlllllluufuuufuuddddddddd", solver._bottom_layer)
    def test_bottom_layer_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._bottom_layer)

    def solve_bottom_layer_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._bottom_layer, "....f.fff....r.rrr....b.bbb....l.lll....u....ddddddddd")

    def test_bottom_layer_from_cross_1(self):
        self.solve_bottom_layer_test("uudbfbufdbflurbfrlbuurbfubffrlllldlrrrdfuublrbdrdddldf")
    def test_bottom_layer_from_cross_2(self):
        self.solve_bottom_layer_test("rldlfbfffbrrrrurrubfbbbufbblufflbllluruluuufrddddddddl")
    def test_bottom_layer_from_cross_3(self):
        self.solve_bottom_layer_test("fublfbffflulrrlrrdfrrfburbbbfuflbllluuurulrbuddddddddb")
    def test_bottom_layer_from_cross_4(self):
        self.solve_bottom_layer_test("brrlfbfffbufrrurrbufrlbudbburuflblllflluublfuddddddddr")
    def test_bottom_layer_from_cross_5(self):
        self.solve_bottom_layer_test("bbrlfuffrurfbrubrfufulburbbrruflblllblluuflrfddddddddd")

    def test_bottom_layer_barrage(self):
        for cube in ["ubdffbufrblfurburlduulbrdblburulrfllllrfuffrrfdbdddddb",
                     "flrbfufffbffrrfrrrrublbubbblulllrlllufuburubuddddddddd",
                     "rubbflffbdruurfdrblfulbrrbrbudbllflllrfbuufflddrdddudu",
                     "lbbuflfffrrffrbdrudfulbulbdrfubllblrburruufrdudldddldb",
                     "ubdffudfdlrulrblrlluuububbbrlrrlrdlrbfffubflbfdfdddrdu",
                     "rflbffufldlflrrdruuurbburbbfrbfllulrdbluuudrfbdbdddldf"]:
            self.solve_bottom_layer_test(cube)

if __name__ == '__main__':
    unittest.main()