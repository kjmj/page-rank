from problem4 import *
import sys
'''
    Unit test 4: 
    This file includes unit tests for problem4.py. 
    You could test the correctness of your code by typing `nosetests test4.py` in the terminal.
'''
#-------------------------------------------------------------------------
def test_python_version():
    ''' ---------- Problem 4 (20 points in total) ------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)



#-------------------------------------------------------------------------
def test_compute_G():
    '''(10 points) compute_G()'''

    # adjacency matrix of shape (3 by 3)
    A = np.mat([[0., 1., 1.],
                [1., 0., 0.],
                [1., 1., 0.]])

    # call the function
    G = compute_G(A, 1.0) 

    # test whether or not G is a numpy matrix 
    assert type(G) == np.matrixlib.defmatrix.matrix

    # test the shape of the matrix
    assert G.shape == (3,3)
    
    # check the correctness of the result 
    G_real=np.mat([[ 0. ,  0.5,  1. ],
                   [ 0.5,  0. ,  0. ],
                   [ 0.5,  0.5,  0. ]] )
    assert np.allclose(G, G_real)
   
    #---------------------
    # test with another matrix (no sink node)

    # test on another adjacency matrix of shape (2 by 2)
    A = np.mat( [ [0., 1.],
                  [1., 0.]])
    
    # call the function again
    G = compute_G(A, 0.5) 

    # test the shape of the matrix
    assert G.shape == (2,2)

    # check the correctness of the result 
    G_real = [[ 0.25, 0.75],
              [ 0.75, 0.25]]
    assert np.allclose(G, G_real)

    #---------------------
    # test with a sink node 

    # test on another adjacency matrix of shape (2 by 2)
    A = np.mat( [ [0., 0.],
                  [1., 0.]])

    # call the function again
    G = compute_G(A,0.5) 

    # test the shape of the matrix
    assert G.shape == (2,2)

    # check the correctness of the result 
    G_real = np.mat( [ [0.25, 0.5],
                       [0.75, 0.5]])
    assert np.allclose(G, G_real)

    # call the function again
    G = compute_G(A,0.) 

    # check the correctness of the result 
    G_real = np.mat( [ [0.5, 0.5],
                       [0.5, 0.5]])
    assert np.allclose(G, G_real)

#-------------------------------------------------------------------------
def test_pagerank():
    '''(10 points) pagerank'''

    # adjacency matrix of shape (3 by 3)
    A = np.mat( [ [0., 1., 1.],
                  [1., 0., 0.],
                  [1., 1., 0.]])
    
    # call the function
    x= pagerank(A, 1.0) 

    # test whether or not x is a numpy matrix
    assert type(x) == np.matrixlib.defmatrix.matrix

    # test the shape of the vector
    assert x.shape == (3,1)

    # check the correctness of the result 
    x_real = np.mat( [[ 1.33333333],
                      [ 0.66666667],
                      [ 1.        ]] )
    assert np.allclose(x_real, x)

    # call the function
    x= pagerank(A, 0.0) 

    # check the correctness of the result 
    x_real = np.mat( [[ 1.],
                      [ 1.],
                      [ 1.]] )
    assert np.allclose(x_real, x)

