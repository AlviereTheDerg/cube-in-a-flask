from rubik_redux.model.cube import Cube

def rotate(cube=None, dir=""):
    if cube is None:
        raise ValueError("Error: Input data: Expected parameter \"cube\"")
    cube = Cube(cube)
    cube.rotate(dir)
    return {"status":"ok", "cube":str(cube)}