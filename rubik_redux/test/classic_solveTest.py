
import unittest
import rubik_redux.controller.classic_solve as solver
from rubik_redux.model.cube import Cube
from rubik_redux.test.solver_test_skeleton import solver_test_skeleton

class classic_solve_tests(solver_test_skeleton):
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
    def test_bottom_layer_change_nothing_middle_layer_solved_1(self):
        self.change_nothing_test("ffbfffffflufrrrrrrrlrbbbbbbbullllllluuurubuuuddddddddd", solver._bottom_layer)
    def test_bottom_layer_change_nothing_middle_layer_solved_2(self):
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

    
    def test_middle_layer_unmet_requisite_1(self): # scrambled
        self.raise_unmet_requisite_stage_test("dfdrfuluufrflrdlfbrrllbbddbfbfdldrbbuuurufruldbbldlufr", solver._middle_layer, "middle layer")
    def test_middle_layer_unmet_requisite_2(self): # bottom cross
        self.raise_unmet_requisite_stage_test("fuubfflfrrrllrubrlbbfrbrbbulurblurlfdldfufdlbudddddfdu", solver._middle_layer, "middle layer")
    def test_middle_layer_unmet_requisite_3(self): # bottom layer solved incorrectly
        self.raise_unmet_requisite_stage_test("bbrufblfluflrrlfrfubfubfrbrurrllfblblubuurulfddddddddd", solver._middle_layer, "middle layer")
    
    def test_middle_layer_change_nothing_middle_layer_solved_1(self):
        self.change_nothing_test("rulffffffffurrrrrrbrubbbbbbfuullllllrulbuubluddddddddd", solver._middle_layer)
    def test_middle_layer_change_nothing_middle_layer_solved_2(self):
        self.change_nothing_test("buuffffffruurrrrrrfulbbbbbbfuullllllulrrublfbddddddddd", solver._middle_layer)
    def test_middle_layer_change_nothing_top_cross_solved_1(self):
        self.change_nothing_test("rffffffffurbrrrrrrlbubbbbbbrlfllllllbuuuuuuulddddddddd", solver._middle_layer)
    def test_middle_layer_change_nothing_top_cross_solved_2(self):
        self.change_nothing_test("bffffffffrrurrrrrrlbubbbbbbrlullllllbufuuuluuddddddddd", solver._middle_layer)
    def test_middle_layer_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._middle_layer)
    
    def solve_middle_layer_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._middle_layer, "...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd")
    
    def test_middle_layer_1(self): # no pieces in middle layer
        self.solve_middle_layer_test("fbfufffffubburrrrrufuubbbbbbfuullllllrrlurrllddddddddd")
    def test_middle_layer_2(self): # all but one solved - LHS
        self.solve_middle_layer_test("fufffufffurbfrrrrruuubbbbbbbbullllllllruufrrlddddddddd")
    def test_middle_layer_3(self): # all but one solved - RHS
        self.solve_middle_layer_test("ufbffffffuluurrrrrbbubbbbbbfrfllllllruluuulrrddddddddd")
    def test_middle_layer_4(self): # all but one solved - in place backwards
        self.solve_middle_layer_test("bbuffrfffflffrrrrrufbbbbbbbuuullllllrulruulurddddddddd")
    def test_middle_layer_5(self): # all but two solved - switched
        self.solve_middle_layer_test("buuffrffffbfbrrrrruubfbbbbbuuullllllrrlluulfrddddddddd")
    
    def test_middle_layer_barrage(self):
        for cube in ["frrbfbfffbuuururrrblrfbrbbburlflllllfflbuluuuddddddddd",
                     "bfrbfbfffurlurrrrrffrbbubbbbuuflllllululuulrfddddddddd",
                     "uflrflfffullururrrfrbbblbbburrblflllruubuffubddddddddd",
                     "urrffffffuulrrurrrurlbblbbbfubbllllluubfulrbfddddddddd",
                     "urlfffffffubrrrrrruurbbbbbbuflllllllfbruulbuuddddddddd",
                     "uuuufrffffffurbrrrurulbfbbbbfbullllllbllurrbrddddddddd",
                     "fufffffffururrbrrrblblbfbbbubuulllllrulruurblddddddddd"]:
            self.solve_middle_layer_test(cube)

    
    def test_top_cross_unmet_requisite_1(self): # scrambled
        self.raise_unmet_requisite_stage_test("rdluffbbfubfurflrfluddbfuurlfullrdlrbbdrudbrbdluddbflr", solver._top_cross, "top cross")
    def test_top_cross_unmet_requisite_2(self): # bottom cross
        self.raise_unmet_requisite_stage_test("budbfbfffruurrflrlrudubffbulfdlllllrbbbrulrrfududddbdd", solver._top_cross, "top cross")
    def test_top_cross_unmet_requisite_3(self): # bottom layer
        self.raise_unmet_requisite_stage_test("flbrflffflllurrrrrfububfbbburuulflllrbubufrbuddddddddd", solver._top_cross, "top cross")
    def test_top_cross_unmet_requisite_4(self): # middle layer incorrectly
        self.raise_unmet_requisite_stage_test("fbblfffffuuurrrrrrflbbbbbbblrlllfllluuruufuurddddddddd", solver._top_cross, "top cross")
    
    def test_top_cross_change_nothing_top_cross_solved_1(self):
        self.change_nothing_test("ufbffffffurlrrrrrrfblbbbbbbulrllllllbuuuuufurddddddddd", solver._top_cross)
    def test_top_cross_change_nothing_top_cross_solved_2(self):
        self.change_nothing_test("ufuffffffrrbrrrrrrlbfbbbbbbrlflllllluuuuuulubddddddddd", solver._top_cross)
    def test_top_cross_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._top_cross)
    
    def solve_top_cross_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._top_cross, ".f.ffffff.r.rrrrrr.b.bbbbbb.l.llllll.u.uuu.u.ddddddddd")
    
    def test_top_cross_1(self): # none facing correctly
        self.solve_top_cross_test("rulffffffuuurrrrrrfufbbbbbbuuulllllllfrbulbrbddddddddd")
    def test_top_cross_2(self): # L shape
        self.solve_top_cross_test("ruuffffffbffrrrrrrulrbbbbbbbuflllllluulruuublddddddddd")
    def test_top_cross_3(self): # bar shape
        self.solve_top_cross_test("fluffffffrufrrrrrrrblbbbbbbuulllllllbuufuruubddddddddd")
    def test_top_cross_4(self): # opposites in place
        self.solve_top_cross_test("uffffffffulbrrrrrrlbrbbbbbburbllllllfuuuuurulddddddddd")
    def test_top_cross_5(self): # adjacents in place
        self.solve_top_cross_test("ufufffffffrbrrrrrrulubbbbbblblllllllfuruuuburddddddddd")


    def test_top_layer_unmet_requisite_scrambled(self):
        self.raise_unmet_requisite_stage_test("rddrflblrfrubrddbdllbbbdruulufflfbuduffbuuurlldffdrrlb", solver._top_layer, "top layer")
    def test_top_layer_unmet_requisite_bottom_cross(self):
        self.raise_unmet_requisite_stage_test("dbulfulflrfrrruurlfldlbfdbffurulbululfdburbrbbdfdddrdb", solver._top_layer, "top layer")
    def test_top_layer_unmet_requisite_bottom_layer(self):
        self.raise_unmet_requisite_stage_test("uflbflfffufuururrrfbubbrbbblfbulllllfrruulrrbddddddddd", solver._top_layer, "top layer")
    def test_top_layer_unmet_requisite_middle_layer(self):
        self.raise_unmet_requisite_stage_test("urlffffffuuurrrrrrfuubbbbbbllbllllllfbruufrubddddddddd", solver._top_layer, "top layer")
    def test_top_layer_unmet_requisite_top_cross_improper(self):
        self.raise_unmet_requisite_stage_test("frrffffffublrrrrrrulbbbbbbbuflllllllrubuuuuufddddddddd", solver._top_layer, "top layer")

    def test_top_layer_change_nothing_solved(self):
        self.change_nothing_test("fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd", solver._top_layer)
    
    def solve_top_layer_test(self, cube_string):
        self.solve_successful_test(cube_string, solver._top_layer, "fffffffffrrrrrrrrrbbbbbbbbbllllllllluuuuuuuuuddddddddd")

    def test_top_layer_1(self): # rotate two corners
        self.solve_top_layer_test("ufufffffffrrrrrrrrbbbbbbbbbllflllllluuuuuulurddddddddd")
    def test_top_layer_2(self): # rotate three corners
        self.solve_top_layer_test("lfufffffffrurrrrrrrbbbbbbbbllulllllluubuuufurddddddddd")
    def test_top_layer_3(self): # rotate four corners
        self.solve_top_layer_test("lfrffffffurbrrrrrrububbbbbbblullllllluruuufufddddddddd")
    def test_top_layer_4(self): # cycle 3 corners CW
        self.solve_top_layer_test("lffffffffrrlrrrrrrfbrbbbbbbblblllllluuuuuuuuuddddddddd")
    def test_top_layer_5(self): # cycle 3 corners CCW
        self.solve_top_layer_test("bffffffffrrbrrrrrrlblbbbbbbflrlllllluuuuuuuuuddddddddd")
    def test_top_layer_6(self): # align all 4 corners: face-pairs swapped
        self.solve_top_layer_test("rflfffffffrbrrrrrrlbrbbbbbbblflllllluuuuuuuuuddddddddd")
    def test_top_layer_7(self): # align all 4 corners: corners swapped
        self.solve_top_layer_test("bfbfffffflrlrrrrrrfbfbbbbbbrlrlllllluuuuuuuuuddddddddd")

if __name__ == '__main__':
    unittest.main()