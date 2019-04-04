'''
Author: Rebecca Dang
Date Started: April 2, 2019
Date Completed (Ver 1): [in progress]

Program Objectives:
Use python classes to:
(be able to take in user input for these)
1. Create and store matrices
    -subclasses: rows, cols

    -init method
    -str method

    -get rows
    -get cols

    -add/subtract matrices
    -multiply matrices

    -find cofactors, minors, determinants
    -find REF, RREF
2. Be able to encode and decode messages using matrices
'''

# =================================
# Row Class
# =================================

class Row(object):
    def __init__(self):
        '''
        Initializes a Row object, a row of a Matrix object
        '''
        # to do
        pass
    def __str__(self):
        '''
        String method to print the Row formatted as such:
        [ # # # ... # ]
        '''
        # to do
        pass

# =================================
# Col Class
# =================================

class Col(object):
    def __init__(self):
        '''
        '''
        # to do
        pass
    def __str__(self):
        '''
        String method to print the Col formatted as such:
        [ # ]
        [ . ]
        [ . ]
        [ # ]
        '''
        # to do
        pass

# =================================
# Matrix Class
# =================================

class Matrix(object):
    def __init__(self, rows, cols):
        ''' 
        Initializes a Matrix object

        rows: list of lists of the entries in each row
        cols: list of lists of the entries in each column
        '''
        # initialize row and col objects
        pass

    def getNumRows(self):
        '''
        Returns the number of rows in the Matrix
        '''
        # to do
        pass

    def getNumCols(self):
        '''
        Returns the number of cols in the Matrix
        '''
        # to do
        pass

    def getDimension(self):
        '''
        Returns the dimension of the Matrix
        '''
        # use getNumRows and getNumCols
        pass
    
    def isSquare(self):
        '''
        Returns True if the Matrix is a square Matrix, else False
        '''
        # use getDimension
        # to do
        pass

    def getRow(self, row):
        '''
        Returns the row object of the row number, row (an int)
        '''
        # to do
        pass

    def getCol(self, col):
        '''
        Returns the col object of the col number, col (an int)
        '''
        # to do
        pass

    def getMinor(self, row, col):
        '''
        row: int, the row of the entry
        col: int, the col of the entry

        Returns the minor of an entry in the Matrix
        '''
        # to do
        pass

    def getCofactor(self, row, col):
        '''
        row: int, the row of the entry
        col: int, the col of the entry

        Returns the cofactor of an entry in the Matrix
        '''
        # to do
        pass

    def getDeterminant(self):
        '''
        Returns the determinant of the Matrix
        '''
        # to do
        pass

    def getREF(self):
        '''
        Returns a Matrix object, the Row-Echelon Form (REF) of the Matrix
        '''
        # to do
        pass

    def getRREF(self):
        '''
        Returns a Matrix object, the Reduced Row-Echelon Form (RREF) of the Matrix
        '''
        # to do
        pass

    def isInREF(self):
        '''
        Returns True if the Matrix is in REF, else False
        '''
        # to do
        pass

    def isInRREF(self):
        '''
        Returns True if the Matrix is in RREF, else False
        '''
        # to do
        pass

    def getInverse(self):
        '''
        Returns a Matrix object, the inverse of the Matrix
        Returns None if the Matrix is non-invertible 
        '''
        # to do
        pass

    def __str__(self):
        '''
        String method to print the entire Matrix formatted as such:
        [ # # # ... # ]
        [ . . . ... . ]
        [ . . . ... . ]
        [ # # # ... # ]
        '''
        # to do
        pass

# =================================
# Matrix Operations (Functions)
# =================================

def create_matrix():
    '''
    Creates a Matrix object from user input

    Returns: None
    '''
    # take in user input
    # initialize a matrix object
    pass

def scale_matrix(matrix, scale_factor):
    '''
    matrix: a Matrix object
    scale_factor: int, the factor the user wants to scale the given matrix by

    Returns a Matrix object, the scaled version of the inputted matrix
    '''
    # to do
    pass

def add_matrices(a, b):
    '''
    a, b: Matrix objects with the same dimensions

    Returns a Matrix object, the sum/difference of matrices a and b
    '''
    # to do
    pass

def multiply_matrices(a, b):
    '''
    a, b: Matrix objects with the same inner dimensions

    Returns a Matrix object, the product of matrices a and b
    '''
    # to do
    pass

def create_identity_matrix(dimension):
    '''
    dimension: int, the number of rows/cols of the identity matrix

    Returns a Matrix object, the identity matrix with the dimension passed in
    '''
    # to do
    pass

def is_inverse(a, b):
    '''
    a, b: Matrix objects with the same dimensions

    Returns True if a and b are inverses, else False
    '''
    # to do
    pass

# =================================
# User Interface
# =================================

# to do