
import unittest
from rubik_redux.model.cube import Cube
from rubik_redux.test.symbol_scrambler import symbol_scramble_decorator

class solver_test_skeleton(unittest.TestCase):
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