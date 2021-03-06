def roll_the_dice(n_simulations=1000):
    '''
    INPUT: INT
    OUTPUT: FLOAT

    Two unbiased, six sided, dice are thrown once and the sum of the showing
    faces is observed (so if you rolled a 3 and a 1, you would observe the sum,
    4). Use a simulation to find the estimated probability that the total score
    is an even number or a number greater than 7.  Your function should return
    an estimated probability, based on rolling the two dice n_simulations times.
    '''
    pass


def pandas_query(df):
    '''
    INPUT: DATAFRAME
    OUTPUT: DATAFRAME

    Given a DataFrame containing university data with these columns:
        name, address, Website, Type, Size

    Return the DataFrame containing the average size for each university
    type ordered by average size in ascending order.
    '''
    pass


def df_to_numpy(df, y_column):
    '''
    INPUT: DATAFRAME, STRING
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY

    Make the column named y_column into a numpy array (y) and make the rest of
    the DataFrame into a 2 dimensional numpy array (X). Return (X, y).

    E.g.
                a  b  c
        df = 0  1  3  5
             1  2  4  6
        y_column = 'c'

        output: np.array([[1, 3], [2, 4]]), np.array([5, 6])
    '''
    pass


def only_positive(arr):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing only the rows from arr where all the values
    in that row are positive.

    E.g.  np.array([[1, -1, 2],
                    [3, 4, 2],
                    [-8, 4, -4]])
              ->  np.array([[3, 4, 2]])

    Use numpy methods to do this, full credit will not be awarded for a python
    for loop.
    '''
    pass


def add_column(arr, col):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing arr with col added as a final column. You
    can assume that the number of rows in arr is the same as the length of col.

    E.g.  np.array([[1, 2], [3, 4]]), np.array([5, 6))
              ->  np.array([[1, 2, 5], [3, 4, 6]])
    '''
    pass


def size_of_multiply(A, B):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: TUPLE

    If matrices A (dimensions m x n) and B (dimensions p x q) can be
    multiplied (AB), return the shape of the result of multiplying them. Use the
    shape function. Do not actually multiply the matrices, just return the
    shape.

    If A and B cannot be multiplied, return None.
    '''
    pass


def linear_regression(X_train, y_train, X_test, y_test):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: TUPLE OF FLOATS, FLOAT

    The R^2 statistic, also known as the coefficient of determination, is a
    popular measure of fit for a linear regression model.  If you need a
    refresher, this wikipedia page should help:

    https://en.wikipedia.org/wiki/Coefficient_of_determination

    Use the sklearn LinearRegression to find the best fit line for X_train and
    y_train. Calculate the R^2 value for X_test and y_test.

    Return a tuple of the coefficients and the R^2 value. Your returned data
    should be in this form:
    (12.3, 9.5), 0.567
    '''
    pass
