from problem3 import *
import sys
'''
    Unit test 3: 
    This file includes unit tests for problem3.py. 
    You could test the correctness of your code by typing `nosetests test3.py` in the terminal.
'''
#-------------------------------------------------------------------------
def test_python_version():
    ''' ---------- Problem 3 (20 points in total) ------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)



#-------------------------------------------------------------------------
def test_compute_S():
    '''(10 points) compute_S'''

    # adjacency matrix of shape (3 by 3)
    A = np.mat( [ [0., 1., 0.],
                  [1., 0., 0.],
                  [1., 1., 0.]])

    # call the function
    S = compute_S(A) 

    # test whether or not S is a numpy matrix 
    assert type(S) == np.matrixlib.defmatrix.matrix

    # test the shape of the matrix 
    assert S.shape == (3,3)
    
    # check the correctness of the result 
    S_real=np.mat([[ 0. ,  0.5,  0.333333 ],
                   [ 0.5,  0. ,  0.333333 ],
                   [ 0.5,  0.5,  0.333333 ]] )
    assert np.allclose(S, S_real)
   
    #---------------------
    # test with another matrix (no sink node)

    # test on another adjacency matrix of shape (2 by 2)
    A = np.mat( [ [0., 1.],
                  [1., 0.]])
    
    # call the function again
    S = compute_S(A) 

    # test the shape of the matrix 
    assert S.shape == (2,2)

    # check the correctness of the result 
    assert np.allclose(S, A)

    #---------------------
    # test with a sink node 

    # test on another adjacency matrix of shape (2 by 2)
    A = np.mat( [ [0., 0.],
                  [1., 0.]])

    # call the function again
    S = compute_S(A) 

    # test the shape of the matrix 
    assert S.shape == (2,2)

    # check the correctness of the result 
    S_real = np.mat( [ [0., 0.5],
                       [1., 0.5]])
    assert np.allclose(S, S_real)

#-------------------------------------------------------------------------
def test_pagerank_v2():
    '''(10 points) pagerank_v2'''

    # adjacency matrix of shape (3 by 3)
    A = np.mat( [ [0., 1., 1.],
                  [1., 0., 0.],
                  [1., 1., 0.]])
    
    # call the function
    x= pagerank_v2(A) 

    # test the shape of the vector
    assert x.shape == (3,1)

    # check the correctness of the result 
    x_real = np.mat( [[ 1.33333333],
                      [ 0.66666667],
                      [ 1.        ]] )
    assert np.allclose(x_real, x)

