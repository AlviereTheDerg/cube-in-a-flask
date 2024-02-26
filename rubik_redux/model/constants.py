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
         [UBR,RBL,DTL,LTR]]
RIGHT = [[RTL,RTR,RBR,RBL],
         [RTM,RMR,RBM,RML],
         [UBR,BTL,DBR,FBR],
         [UMR,BML,DMR,FMR],
         [UTR,BBL,DTR,FTR]]
BACK =  [[BTL,BTR,BBR,BBL],
         [BTM,BMR,BBM,BML],
         [UTR,LTL,DBL,RBR],
         [UTM,LML,DBM,RMR],
         [UTL,LBL,DBR,RTR]]
LEFT =  [[LTL,LTR,LBR,LBL],
         [LTM,LMR,LBM,LML],
         [UTL,FTL,DTL,BBR],
         [UML,FML,DML,BMR],
         [UBL,FBL,DBL,BTR]]
UP =    [[UTL,UTR,UBR,UBL],
         [UTM,UMR,UBM,UML],
         [BTR,RTR,FTR,LTR],
         [BTM,RTM,FTM,LTM],
         [BTL,RTL,FTL,LTL]]
DOWN =  [[DTL,DTR,DBR,DBL],
         [DTM,DMR,DBM,DML],
         [FBL,RBL,BBL,LBL],
         [FBM,RBM,BBM,LBM],
         [FBR,RBR,BBR,LBR]]

#Cube specifications
PIECES_PER_FACE = 9
FACES_PER_CUBE = 6
VALID_CUBE_SYMBOLS = r"[a-zA-z0-9]+"

#Piece classses
CENTERS = {FMM, RMM, BMM, LMM, UMM, DMM}
EDGES   = {FTM,FML,FMR,FBM, RTM,RML,RMR,RBM, BTM,BML,BMR,BBM,
           LTM,LML,LMR,LBM, UTM,UML,UMR,UBM, DTM,DML,DMR,DBM}
CORNERS = {FTL,FTR,FBL,FBR, RTL,RTR,RBL,RBR, BTL,BTR,BBL,BBR,
           LTL,LTR,LBL,LBR, UTL,UTR,UBL,UBR, DTL,DTR,DBL,DBR}

# Pre-calculated mappings
FACES = ['f','r','b','l','u','d']
FACE_OF = {piece:FACES[piece // PIECES_PER_FACE] for piece in range(PIECES_PER_FACE * FACES_PER_CUBE)}
CYCLE_OF = {'f':FRONT, 'r':RIGHT, 'b':BACK, 'l':LEFT, 'u':UP, 'd':DOWN}
CENTER_OF = {'f':FMM, 'r':RMM, 'b':BMM, 'l':LMM, 'u':UMM, 'd':DMM}