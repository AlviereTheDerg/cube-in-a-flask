from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    theCube = Cube.makeCube(parms.get('cube'))
    if (isinstance(theCube, str)):
        result['status'] = 'error: ' + theCube
        return result
    
    if ('dir' not in parms or len(parms['dir']) == 0):
        parms['dir'] = 'F'
    directions = parms['dir']
    
    if (len(parms.keys()) > 2):
        result['status'] = 'error: no extraneous keys allowed'
        return result
    
    rotateResult = theCube.rotate(directions)
    if (rotateResult != 'ok'):
        result['status'] = 'error: ' + rotateResult
        return result
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result
