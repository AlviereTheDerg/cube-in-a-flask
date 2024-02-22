import unittest
from rubik.view.solve import solve
import re
from rubik.model.cube import Cube
import hashlib
 

class SolveTest(unittest.TestCase):

# Happy path
    def test_100_basicOutput_solvedCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result['solution']))
        
    def test_101_basicOutput_scrambledCube(self):
        parms = {}
        parms['cube'] = 'oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result['solution']))
        
    def test_102_basicOutput_almostSolvedCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        self.assertTrue(re.fullmatch(re.compile(r"[FfRrBbLlUu]*"), result['solution']))
        
    def test_200_bottomCross_solvedCube(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('bottomcross'))
        
    def test_201_bottomCross_scrambledCube(self):
        theCube = Cube('oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('bottomcross'))
        
    def test_202_bottomCross_almostSolvedCube(self):
        theCube = Cube('bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('bottomcross'))
        
    def test_300_bottomLayer_solvedCube(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_301_bottomLayer_scrambledCube(self):
        theCube = Cube('oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_302_bottomLayer_almostSolvedCube(self):
        theCube = Cube('bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('bottomlayer'))
        
    def test_400_middleLayer_solvedCube(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_401_middleLayer_scrambledCube(self):
        theCube = Cube('oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_402_middleLayer_almostSolvedCube(self):
        theCube = Cube('bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('middlelayer'))
        
    def test_500_topCross_solvedCube(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topcross'))
        
    def test_501_topCross_scrambledCube(self):
        theCube = Cube('oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topcross'))
        
    def test_502_topCross_almostSolvedCube(self):
        theCube = Cube('bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topcross'))
        
    def test_600_topSurface_solvedCube(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topsurface'))
        
    def test_601_topSurface_scrambledCube(self):
        theCube = Cube('oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topsurface'))
        
    def test_602_topSurface_almostSolvedCube(self):
        theCube = Cube('bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topsurface'))
        
    def test_603_topSurface_middleLayerSolved(self):
        theCube = Cube('rwobbbbbbgwooooooowbwggggggrogrrrrrrbwbwwrwgwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        self.assertTrue(theCube.status('middlelayer'))
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('topsurface'))

    def test_610_integrity(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        result = solve(parms)
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        tokenString = parms['cube'] + result['solution'] + "arg0070"
        sha256hash = hashlib.sha256()
        sha256hash.update(tokenString.encode())
        fullToken = sha256hash.hexdigest()
        self.assertTrue(result['integrity'] in fullToken)

    def test_611_integrity(self):
        parms = {}
        parms['cube'] = 'CuuiuxkCxCikuNiuCNNiNukxiNiiNkkxxuuxukCkiNxCNixCNCkxCk'
        result = solve(parms)
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        tokenString = parms['cube'] + result['solution'] + "arg0070"
        sha256hash = hashlib.sha256()
        sha256hash.update(tokenString.encode())
        fullToken = sha256hash.hexdigest()
        self.assertTrue(result['integrity'] in fullToken)

    def test_612_integrity(self):
        parms = {}
        parms['cube'] = 'tNy8mdNmtddNmNt8ydttNd8mmmd8ymNdt8NyyN8dy8Nymmtd8t8yyt'
        result = solve(parms)
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        tokenString = parms['cube'] + result['solution'] + "arg0070"
        sha256hash = hashlib.sha256()
        sha256hash.update(tokenString.encode())
        fullToken = sha256hash.hexdigest()
        self.assertTrue(result['integrity'] in fullToken)
        
    def test_700_topSurface_solvedCube(self):
        theCube = Cube('bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('solved'))
        
    def test_701_topSurface_scrambledCube(self):
        theCube = Cube('oogybgrbworbrowogrrbwbggwoyooywrrggwgyybwwbwygrbyyoryb')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('solved'))
        
    def test_702_topSurface_almostSolvedCube(self):
        theCube = Cube('bbbbbbrbooooooogobggggggogrrrrrrrbrgwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('solved'))
        
    def test_703_topSurface_topSurfaceSolved(self):
        theCube = Cube('bbobbbbbbgogoooooorgbggggggorrrrrrrrwwwwwwwwwyyyyyyyyy')
        parms = {}
        parms['cube'] = theCube.get()
        result = solve(parms)
        self.assertIn('solution', result)
        self.assertTrue(theCube.status('topsurface'))
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status('solved'))
        

# Sad path
#    Test for missing cube
    def test_900_solve_missingCube(self):
        parms = {}
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: missing cube', result['status'])
        
#    Test for cube length
    def test_910_solve_invalidCubeLength(self):
        parms = {}
        parms['cube'] = 'grbyow'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube length', result['status'])
        
#    Test for unique face centers
    def test_920_solve_invalidFaceCenters(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyoooowoooowwowwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid face centers', result['status'])

#    Test for 9 of each character, this + cube length check => 54 faces
    def test_930_solve_invalidColourCounts(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyoooooooowwwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid colour amounts', result['status'])

#    Test for invalid symbols in cube
    def test_940_solve_invalidCubeCharacters(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy.........wwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid symbols used', result['status'])
        
#    Test for a character appearing that doesn't match any face centers
    def test_950_solve_characterMatchesNoFace(self):
        parms = {}
        parms['cube'] = 'ggTggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: symbol matches no face', result['status'])
        
#    Test for extraneous keys
    def test_960_solve_extraneousKeyPresent(self):
        parms = {}
        parms['dir'] = 'R'
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: no extraneous keys allowed', result['status'])


# Tests grabbed from increments
    def increment_piece_test(self, cubestring, status):
        theCube = Cube(cubestring)
        parms = {}
        parms['cube'] = cubestring
        result = solve(parms)
        self.assertIn('solution', result)
        theCube.rotate(result['solution'])
        self.assertTrue(theCube.status(status))
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        
        self.assertIn('integrity', result)
        tokenString = parms['cube'] + result['solution'] + "arg0070"
        sha256hash = hashlib.sha256()
        sha256hash.update(tokenString.encode())
        fullToken = sha256hash.hexdigest()
        self.assertTrue(result['integrity'] in fullToken)
    
    def test_increment2(self):
        cubestrings = ['EEEEEEEEEQQQQQQQQQLLLLLLLLL333333333jjjjjjjjjkkkkkkkkk',
                       'pffMMfofMpXXooMfpfoOpopoMoOXOoXOXMOXOpMXfpfOOpMoMXfXpO',
                       'oOORoOODRoa8aa8888aoOoD8RDaDo8DRoORRaaDO8DaRRDRo8OaoOD',
                       'aTXCXawTLwwXXLwXXLaCLLTwCXwCLCTaaTLTTXCTwaTCaaawCCwLLX',
                       'CuuiuxkCxCikuNiuCNNiNukxiNiiNkkxxuuxukCkiNxCNixCNCkxCk',
                       'XeXa7f7f7a7a7XXXawea7eaXfwwXwawfw7ffwXffwXe7weaeeeef7a',
                       'AQtA4DDQtDtQqqAAqAq4qDtQD4DQ44AAtAq4tQ4DDDQtqqqQ4QttA4',
                       'XVJJsXbsXsVXbJJJVseXebXVbsVsXebVeXeVVeVJbXJsesbbseebJJ',
                       'eJCWCCuCeuCuGGuGWeeCCeeeJeWGGWJWuJGCJWGJJJuWGWuJuueCGW',
                       'b76brb75b7rr5Pr5PP55776rrb5666b56bPPP677bPP55rr6677rPb',
                       'jb2rbTbW2TbbrjjTjb2Wr2rTTTjTrrbT2WWjWbjjWj22rWTbr2Wr2W',
                       'jBBujiijuquuBqqzqqzBqjiuuiuBzBqzjqiBiqjBuzzjjzzizBijui',
                       'a88aR58aJaRYYJJRJ5aa8YaRYR5J8JY5J85RR55aY5YJJ5YY88Ra8R',
                       'XLXGLXOkLOLKOOKkGOXOKXGkGkOGKLOKXkXXkLGGXKKkGLGKLkOLKk',
                       'lXXdtdddlllXlaaTaXdtatXXdttXTtdlaTlaTllaTTdTTtttXdXaTa',
                       'taaaahrgtrtgathhgtrgaggratahrghrRttgrrhRhaRrRRtgRRRRhh',
                       '5LAZLRZLAEEE55555RRZ5AZE5ZELZAREEREER5LRALZRLAALARLZAZ',
                       '959v5v2mv2Hm9m59HHHmm9v25vHvm592m229H559Hvm2v5HmH95v22',
                       'cifHfatttttiHcactHfHtiafaaaiifcifHHfacHfHfHtciaaitcicc',
                       'Wb9b29WW9bP2bPWb22W9r29rb9r2992rr2W9brPWb2rPPPrrPWbWPP',
                       'qLdfq333df3Lf3MfdqqqdddqMML3dfLLqMMqM3fLfM3f3MdLqMfdLL']
        
        self.assertTrue(len(cubestrings) == 21) #Sanity check
        
        for cubestring in cubestrings:
            self.increment_piece_test(cubestring, 'bottomcross')
    
    
    def test_increment3(self):
        cubestrings = ['UgggrjUMUUUjMUrrgjMrppMjrMjMjMpjjpMMjUgrppgrrpUppgUrgg',
                       'tYYZBBFZBttBYOOZOBFBBtttFYZYFOFFBFYtOOYBZZZtOYFOOYZtFZ',
                       '00xQxB0YYQB00008BQ88YxB8YYB8QBYY0YQBBxxx8YQ808xxBQ8QQx',
                       'BfBDzAABAjjDfBADjDjzzBDDAzjjDzffBfAfBBfAADAjDzjBzjzzff',
                       'eyye3ekseseksveyvvevs3y3y3e33ssek3yvvsyksy3kv3ysvkkkvk',
                       '88xpxpM7ppxcc7p77Mpx8MMM88Mxcxcc77xp78xx87cc7c8MppM8Mc',
                       'Y272Z72hr2YY2rrZYZ72YY7Yh7Yrr7hhhhh7ZrrZ2ZhZrh72ZY7Zr2',
                       'JJrJHxJJJUHxrxDHxDrDxHUrHUDUUxHDxrDDrUHrrxUDDUHxrJUHJJ',
                       'pump1m1p1p1LuLmupm1uppYmu1uLu1Ym1LYLYYu1pLmLYpLmLuYYmY',
                       'KVoshiooiVohoVsVKoViKhisViiiVsiKVsKhoVsoshhhhKKshosKKi',
                       's5i42i4i552isi5q42254s554q2qs4q42sq52iq4ss54sq2iiqqi2s',
                       'Y5t9YY59CCCGtttGGY59CCGGtGYG95C9G95G959CCY9tYtYtY5tC55',
                       'EvWE8rE8Er7vWEvW7v8v77rr7v8878EvWE87vWW8WEWrvrErW7r78r',
                       'MMpOMyOypOyLLLLOppMOyCOOCOMOCCyppypCLLyMCpLLyLMCMyCpCM',
                       'GvvvVYGVVgcVggVYGYggVGccVYgvVcgGVcGcGvvgvYvccYYGcYvYGg',
                       'CRggCGCR1R1GkgCggCR1RgRRgRRGCkkG1kG11Gkk1CGG1G1CCkkggk',
                       'XX3XXTTTTryy3y33ypr33ppTyyTpp3y33yryTrXTrXrrpXXXpTpprr',
                       'ulskkkWklkuWWsssu5sW5lusW5Wll5u55sWuksukW5lul5su5lWklk',
                       'liciTooTiTViliiVViTTlTocTilVlVolVcliolccVTTolccoVcoocV',
                       'tvtthvhhmhhhmEhcmEEccvchvthEtcEmcEvvtEvEvmmEmmtvctctmc']
        
        self.assertTrue(len(cubestrings) == 20) #Sanity check
        
        for cubestring in cubestrings:
            self.increment_piece_test(cubestring, 'bottomlayer')
    
    def test_increment4(self):
        cubestrings = ['8To8UZZ2TZTU8TUo82ZZ2Z2ooUUZo2UZT82U8oo282To28ZU8oUTTT',
                       'CYYYVVYCVCCCmmCxx8YYxYY8m8V8xVmx8C88YmmV8Vmxxmm8VCCxxV',
                       'IIbLHjLjJjJHbJIHjjIJHHjHJbjbLLJIHLIJIbLJbjjLIHLbbLIJHb',
                       'PKqKn4KnnKpnp444nnqq4nKnqKPpppqPqnqqK4PPqKKPP4PpPppp44',
                       'ZfvffvzZffzxmxfZxzzmzmzzZzvmzfmmvfxZvZvxvZxZxmxmvZfmvx',
                       'Q6dQQzDzdQdDDlDQD66lDd6Ql6zd6ldDlldz6zzzdlzDlQQD6zQ6ld',
                       'I8WZZUZZI8808W0W888UZUUUZZUIIUI0IW00WWUW8Z00ZIWUIIW800',
                       'BySBSBFyBFFBSFFSWWSWLBWBBLLyFWyyWyyWSLySLLyLLLSFWBFWSF',
                       'PeIwJ8IPweJJJ888wwP88eeJPeIe8wPPeeI8wwIIwIJP8JwJPIJPIe',
                       'KqnZn2Z2n2qZKZKZ22FZqqqZFnnKZ2q2n2KKZKqFK2qFFnFFnFnKFq',
                       '4P4FPJxJPUxUxJFJF4JUJUUPUJFxxx4444xJP4FPx4PJFUUFUFPPFx',
                       'PPPEEyEGyGEyEPGEPGPPQQYQQYQYQEYQGYYGGGYyyQyyYPYQyGEyPE',
                       '8jZ5jj5jjj3388Z83Z55873Z78j57Z37773j387jZ73Z8755855ZZ3',
                       'ZmmXmPXVPZPpZZVppXmPpZPXppZVmPPpZVpZPVVZVpXXVmmXVXXPmm',
                       'mygaaQQQQmcaayycQagcmacygagaccgmmymaQmyQQgQccyyyggmcgm',
                       '2j2224dNyyj4Njd422Ndd244jyyNjdyNyjN444ydy4NyNj2jddj2Nd',
                       'K44ooxxo4AKx4AAAAAKKAx4AxAKYKYYKx4YooY4xYooKxKYY4xoY4o',
                       'KKQJKJJrmmrJkrJJJJKkkmmkmKkKkrmJKmQQrrkKkmQQrKQQmQQrrk',
                       'zARROzAzAhOOhFARRRhOzzzRhhRAAhAROAhOFhFOAFFFOFFzFhzORz',
                       'uApmcATcmmTpTpAuuucTcmucTmcTTppApmpcAcmpTuTuupAAummAcA']
        
        self.assertTrue(len(cubestrings) == 20) #Sanity check
        
        for cubestring in cubestrings:
            self.increment_piece_test(cubestring, 'middlelayer')
    
    def test_increment5(self):
        cubestrings = ['AwFAC0AFCACFAbbbCwCb00w0b0bCw0CACww0bFAb0bCFwwAFAFFFw0',
                       '6iC6iH6226lliH2CHi662CC22CCH2Hlll2lliCCi6Ci6HiHli26HHl',
                       '8c888MnMMnssnc88ssM8EcEscE8nnnMMnccEcMEEn8cnMMEsssEscE',
                       'tNy8mdNmtddNmNt8ydttNd8mmmd8ymNdt8NyyN8dy8Nymmtd8t8yyt',
                       '9bN9bCqnCnnn99q9nCbNbbN9bq9nNCnqbNCC99qqCbNCqNqbNnNnCq',
                       'OcwwwTcOcTwZcOTwEEEcTOZTwZOOcZZcTwOTZEcwTOEZcZEEZEwTEO',
                       '4XCzaa44Xza7z4Cz7XzXCXC74XXXa7zzCa47zza774Ca7aCa7XC44C',
                       '221sUUs2UsUUe2711e7U2esUU1Uses77177e11es12ee77s2se7122',
                       'ssgG22Bo2GGGgosgBoooBBsg2gs22BGgsgBogGsoG2oos2BGgB2BsG',
                       'BiWWGGGWhiiihkkWkhhBiGWBkGBGhkWiiWihBkGWBGGBBkkihhhkBW',
                       'smDsDsqmDyDD3yy3qD3yqDqDysm3Dqm3qyymsqm3ssyqs33smm3qym',
                       'X2l2GG2XGS2IIIlS2X2G2SlX2SXGllSXISXIXSlISlSGIGGIl2XGIl',
                       '5GN55NxxNVGNGxeVGGeee5NV5VV5VGeVxeeGxxxNeVV5eNNGNGx55x',
                       'mmmWJJWQQrrmmmQIQJJJQWWrrmmIWJIIrQIrJrrIQmQQWIIWJrJWWI',
                       'xV3j3Vj3VlVllljl33xggVx3lxjxgjgjx3g3jjglgxV3ggjxxVlVlV',
                       'P9P7oo7Poooo977CoEPE9EE77ECC7EP9CoEPEC7oCP9C9E97PPC99C',
                       'p9BO9OORBR9BBSppO999SSO9ROppBBpBS9RROSRpRB9ROSSOBppSRS',
                       'ZjjqiiUmUmZjZqUqqUZjjimjmiiiZUZZmqqmZmmUUmiqqZUiijUjjq',
                       'BPPsPPvNvB7P7sPBN77vPsvBs7PsvvPNB7B7Bss7BssNNNvNv7BNNv',
                       'NN5pppyN0pp25N0N525yy2y2p555N0520py0N0y052ppN2yy20N2y0']
        
        self.assertTrue(len(cubestrings) == 20) #Sanity check
        
        for cubestring in cubestrings:
            self.increment_piece_test(cubestring, 'topsurface')
        
if __name__ == '__main__':
    unittest.main()