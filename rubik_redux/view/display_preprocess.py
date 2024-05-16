from rubik_redux.model.cube import Cube

def rotate_display_preprocess(cube=None, dir=""):
    if cube is None:
        raise ValueError("Error: Input data: Expected parameter \"cube\"")
    cube = Cube(cube)
    colour_flattening = {v:k for k,v in cube.colours.items()}
    def flatten():
        return "".join(colour_flattening[char] for char in cube.cube_data)
    cube_strings = [flatten()]
    dir = [char for char in dir]
    for turn in dir:
        cube.rotate(turn)
        cube_strings.append(flatten())
    return cube_strings, dir