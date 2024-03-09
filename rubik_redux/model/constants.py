'''
Constants used across the microservice 
'''

#-----------------------------------
#  Mapping of cube element positions to mnemonic names
#  Each mnemonic is a three-character pattern, frc, where
#       f indicates the face and is one of F, R, B, L, U, D
#       r indicates the row and is one of T, M, B (for top, middle, bottom, respectively)
#       c indicates the column and is one of L, M, R (for left, middle, right, repectively)
#  The regex for the pattern is r'[FRBLUD][TMB][LMR]'
#
# Front face
FTL = 0
FTM = 1
FTR = 2
FML = 3
FMM = 4
FMR = 5
FBL = 6
FBM = 7
FBR = 8

# Right face
RTL = 9
RTM = 10
RTR = 11
RML = 12
RMM = 13
RMR = 14
RBL = 15
RBM = 16
RBR = 17

# Back face
BTL = 18
BTM = 19
BTR = 20
BML = 21
BMM = 22
BMR = 23
BBL = 24
BBM = 25
BBR = 26

# Left face
LTL = 27
LTM = 28
LTR = 29
LML = 30
LMM = 31
LMR = 32
LBL = 33
LBM = 34
LBR = 35

# Up face
UTL = 36
UTM = 37
UTR = 38
UML = 39
UMM = 40
UMR = 41
UBL = 42
UBM = 43
UBR = 44

#Down face
DTL = 45
DTM = 46
DTR = 47
DML = 48
DMM = 49
DMR = 50
DBL = 51
DBM = 52
DBR = 53

#Rotation cycles
FRONT = [[FTL,FTR,FBR,FBL], #Corners of the face
         [FTM,FMR,FBM,FML], #Edges of the face
         [UBL,RTL,DTR,LBR],
         [UBM,RML,DTM,LMR],
         [LTR,UBR,RBL,DTL]]
RIGHT = [[RTL,RTR,RBR,RBL],
         [RTM,RMR,RBM,RML],
         [UBR,BTL,DBR,FBR],
         [UMR,BML,DMR,FMR],
         [FTR,UTR,BBL,DTR]]
BACK =  [[BTL,BTR,BBR,BBL],
         [BTM,BMR,BBM,BML],
         [UTR,LTL,DBL,RBR],
         [UTM,LML,DBM,RMR],
         [RTR,UTL,LBL,DBR]]
LEFT =  [[LTL,LTR,LBR,LBL],
         [LTM,LMR,LBM,LML],
         [UTL,FTL,DTL,BBR],
         [UML,FML,DML,BMR],
         [BTR,UBL,FBL,DBL]]
UP =    [[UTL,UTR,UBR,UBL],
         [UTM,UMR,UBM,UML],
         [BTR,RTR,FTR,LTR],
         [BTM,RTM,FTM,LTM],
         [LTL,BTL,RTL,FTL]]
DOWN =  [[DTL,DTR,DBR,DBL],
         [DTM,DMR,DBM,DML],
         [FBL,RBL,BBL,LBL],
         [FBM,RBM,BBM,LBM],
         [LBR,FBR,RBR,BBR]]

#Cube specifications
PIECES_PER_FACE = 9
FACES_PER_CUBE = 6
VALID_CUBE_SYMBOLS = r"[a-zA-z0-9]+"
FACES = ['f','r','b','l','u','d']
VALID_ROTATE_SYMBOLS = set("FfRrBbLlUuDd")

#Piece classses
CENTERS = {FMM, RMM, BMM, LMM, UMM, DMM}
EDGES   = {FTM,FML,FMR,FBM, RTM,RML,RMR,RBM, BTM,BML,BMR,BBM,
           LTM,LML,LMR,LBM, UTM,UML,UMR,UBM, DTM,DML,DMR,DBM}
CORNERS = {FTL,FTR,FBL,FBR, RTL,RTR,RBL,RBR, BTL,BTR,BBL,BBR,
           LTL,LTR,LBL,LBR, UTL,UTR,UBL,UBR, DTL,DTR,DBL,DBR}

# Pre-calculated mappings
FACE_OF = {piece:FACES[piece // PIECES_PER_FACE] for piece in CENTERS | EDGES | CORNERS}
CYCLE_OF = {'f':FRONT, 'r':RIGHT, 'b':BACK, 'l':LEFT, 'u':UP, 'd':DOWN}
CYCLE_OF_FACE_OF = {piece:CYCLE_OF[FACE_OF[piece]] for piece in FACE_OF.keys()}
CENTER_OF = {'f':FMM, 'r':RMM, 'b':BMM, 'l':LMM, 'u':UMM, 'd':DMM}
OTHER_SIDE_OF = ({center:None for center in CENTERS} # Centers map to None
    | {edge:CYCLE_OF_FACE_OF[edge][3][CYCLE_OF_FACE_OF[edge][1].index(edge)] for edge in EDGES} # Edges map to the other piece touching them
    | {corner:( # Corners have 2 'other sides', if looking at the face the current piece is on:
            CYCLE_OF_FACE_OF[corner][4][CYCLE_OF_FACE_OF[corner][0].index(corner)], # 0 is more counter-clockwise
            CYCLE_OF_FACE_OF[corner][2][CYCLE_OF_FACE_OF[corner][0].index(corner)]  # 1 is more clockwise of the pair
        ) for corner in CORNERS})
ALL_SIDES_OF = {piece:{piece} for piece in CENTERS} | {piece:{piece, OTHER_SIDE_OF[piece]} for piece in EDGES} | {piece:({piece} | set(OTHER_SIDE_OF[piece])) for piece in CORNERS}

# Map how pieces move with rotations
# ROTATION_TRANSFERS[rotation].get(piece, piece) -> location that piece will be after applying rotation
ROTATION_TRANSFERS = (
    # CCW / lowercase rotations
    {face:{cycle[index]:cycle[(index - 1) % len(cycle)] for cycle in CYCLE_OF[face] for index in range(len(cycle))} for face in FACES}
    |
    # CW / uppercase rotations
    {face.upper():{cycle[index]:cycle[(index + 1) % len(cycle)] for cycle in CYCLE_OF[face] for index in range(len(cycle))} for face in FACES}
)