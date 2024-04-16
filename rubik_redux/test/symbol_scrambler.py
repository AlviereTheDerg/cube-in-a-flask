
import functools

def symbol_scramble_decorator(func):
    @functools.wraps(func)
    def symbols_scrambled(self, cube_string, *args, **kwargs):
        for translation in [{'f':'b', 'r':'o', 'b':'g', 'l':'r', 'u':'w', 'd':'y'},
                            {'f':'1', 'r':'2', 'b':'3', 'l':'4', 'u':'5', 'd':'6'},
                            {},
                            {'f':'4', 'r':'a', 'b':'b', 'l':'d', 'u':'2', 'd':'l'}]:
            return func(self, "".join(translation.get(piece, piece) for piece in cube_string), *args, **kwargs)
    return symbols_scrambled