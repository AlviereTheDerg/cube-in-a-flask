from rubik_redux.model.cube import Cube

from rubik_redux.controller import classic_solve, CFOP_solve

def solve(cube=None, style=None):
    if cube is None:
        raise ValueError("Error: Input data: Expected parameter \"cube\"")
    result = {"cube":cube}
    cube = Cube(cube)
    match style:
        case "classic" | None:
            result["dir"] = classic_solve.solve(cube)
        case "CFOP":
            result["dir"] = CFOP_solve.solve(cube)
        case _:
            raise ValueError("Error: Input data: Could not recognize \"style\" parameter")
    return result