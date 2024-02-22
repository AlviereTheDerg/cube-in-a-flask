import unittest
from rubik.view.rotate import rotate

class RotateTest(unittest.TestCase):
        
# Happy path
    def test_000_blankTurns(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        parms['dir'] = ''
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbbbbbbbbwoowoowoogggggggggrryrryrrywwwwwwrrroooyyyyyy', result['cube'])
        
    def test_001_missingTurn(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbbbbbbbbwoowoowoogggggggggrryrryrrywwwwwwrrroooyyyyyy', result['cube'])
    
    def test_100_oneTurn(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbbbbbbbbwoowoowoogggggggggrryrryrrywwwwwwrrroooyyyyyy', result['cube'])
    
    def test_110_twoTurns(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'Fr'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbwbbwbbroooooowwwyggyggoggrryrryrrywwgwwgrrgoobyybyyb', result['cube'])
    
    def test_120_tenTurns(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'FrBlUfRbLu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual('yryrbboyrgwwwobyyrgobyggwowywrwrbggwobrrwobgobrgoygoyb', result['cube'])

# Sad path
#    Test for missing cube
    def test_900_rotate_missingCube(self):
        parms = {}
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: missing cube', result['status'])
        
#    Test for cube length
    def test_910_rotate_invalidCubeLength(self):
        parms = {}
        parms['cube'] = 'grbyow'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube length', result['status'])
        
#    Test for unique face centers
    def test_920_rotate_invalidFaceCenters(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyoooowoooowwowwwwww'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid face centers', result['status'])

#    Test for 9 of each character, this + cube length check => 54 faces
    def test_930_rotate_invalidColourCounts(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyoooooooowwwwwwwwww'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid colour amounts', result['status'])

#    Test for invalid symbols in cube
    def test_940_rotate_invalidCubeCharacters(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy.........wwwwwwwww'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid symbols used', result['status'])
        
#    Test for a character appearing that doesn't match any face centers
    def test_950_rotate_characterMatchesNoFace(self):
        parms = {}
        parms['cube'] = 'ggTggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: symbol matches no face', result['status'])
        
#    Test for invalid symbols in rotation
    def test_960_rotate_invalidRotateCharacters(self):
        parms = {}
        parms['dir'] = 'RbfUd'
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
        
#    Test for extraneous keys
    def test_970_rotate_extraneousKeyPresent(self):
        parms = {}
        parms['dir'] = 'R'
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww'
        parms['bibl'] = 'bobl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: no extraneous keys allowed', result['status'])
    
#    Same as prior, but without a given dir
    def test_971_rotate_extraneousKeyPresentSansDir(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyyooooooooowwwwwwwww'
        parms['bibl'] = 'bobl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: no extraneous keys allowed', result['status'])
        
if __name__ == '__main__':
    unittest.main()