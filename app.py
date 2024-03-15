'''
Rubik cube microservice

This is the entry point for a microservice that enumerates the face rotations
needed to transform the input cube to a solved state.
'''
import os
import json
from flask import Flask, request
from rubik.view.solve import solve
from rubik.view.rotate import rotate

from rubik_redux.view.rotate import rotate as rotate_redux

app = Flask(__name__)

#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /
#  It returns a welcome string
#
@app.route('/')
def default():
    '''Return welcome information'''
    return "Welcome to Alviere's Rubik's Cube microservice"

#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /about
#  It returns the author identifier
#
@app.route('/about')
def about():
    '''Return author information'''
    return str(_getAuthor())

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches
#         /rubik/solve
#
#  The cube is passed as a URL query:
#        /rubik/solve?cube=<value>
#
@app.route('/rubik/solve')
def solveServer():
    '''Return face rotation solution set'''
    try:
        userParms = _parseParms(request.args)
        result = solve(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)
    
#-----------------------------------
#  The following code is invoked when the path portion of the URL matches
#         /rubik/rotate
#
#  The cube and the face rotation(s) are passed as a URL query:
#        /rubik/rotate?cube=<value>&dir=<value>
#
@app.route('/rubik/rotate')
def rotateServer():
    '''Return rotated cube'''
    try:
        userParms = _parseParms(request.args)
        result = rotate(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)
    
@app.route('/rubik_redux/rotate')
def rotateServerRedux():
    '''Return rotated cube'''
    try:
        userParms = _parseParms(request.args)
        result = rotate_redux(**userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)

#-----------------------------------
#  URL parsing support code
def _parseParms(queryString):
    '''Convert URL query string items into dictionary form'''
    userParms = {}
    for key in queryString:
        userParms[key] = str(queryString.get(key,''))
    return userParms

#-----------------------------------
#  SBOM support code
#
def _getAuthor(sbomDirectory = ''):
    '''Return author information from SBOM'''
    with open(os.path.join(sbomDirectory,"sbom.json"), encoding="utf-8") as sbomFile:
        parsedSbom = json.load(sbomFile)
    return {'author': parsedSbom.get("metadata", {}).get("component", {}).get("author", "unknown")}
 
#-----------------------------------
if __name__ == "__main__":
    port = os.getenv('PORT', '8080')
    app.run(debug=False, host = '0.0.0.0', port = int(port))
