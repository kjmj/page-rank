from problem2 import *
import sys

'''
    Unit test 2: 
    This file includes unit tests for problem2.py. 
    You could test the correctness of your code by typing `nosetests -v test2.py` in the terminal.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ---------- Problem 2 (30 points in total) ------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_compute_P():
    ''' (10 points) compute_P'''

    # adjacency matrix of shape (3 by 3)
    A = np.mat( [[0., 1., 1.],
                 [1., 0., 0.],
                 [1., 1., 0.]])

    # call the function
    P= compute_P(A) 

    # test whether or not P is a numpy matrix 
    assert type(P) == np.matrixlib.defmatrix.matrix

    # test the shape of the matrix
    assert P.shape == (3,3)
    
    # check the correctness of the result 
    P_real=np.mat([[ 0. ,  0.5,  1. ],
                   [ 0.5,  0. ,  0. ],
                   [ 0.5,  0.5,  0. ]] )
    assert np.allclose(P, P_real)
   
    #---------------------
    # test with another matrix

    # test on another adjacency matrix of shape (2 by 2)
    A = np.mat( [ [0., 1.],
                  [1., 0.]])
    
    # call the function again
    P = compute_P(A) 

    # test the shape of the matrix
    assert P.shape == (2,2)

    # check the correctness of the result 
    assert np.allclose(P, A)

    #---------------------
    # test with a random matrix
    for _ in range(20):
        n = np.random.randint(2,20) 
        # random n by n matrix
        A = np.asmatrix(np.random.random((n,n)))
        A = A + A.T # symmetric
        A[A>0]=1.
        P = compute_P(A)
        i = np.random.randint(n)
        assert np.allclose(P.sum(axis=0), np.ones(n))


#-------------------------------------------------------------------------
def test_random_walk_one_step():
    ''' (10 points) random_walk_one_step'''

    # transition matrix of shape (3 by 3) 
    P = np.mat([[ 0. ,  0.5,  1. ],
                [ 0.5,  0. ,  0. ],
                [ 0.5,  0.5,  0. ]] )

    # an all-one vector of shape (3 by 1)
    x_i =  np.asmatrix(np.ones((3,1)))
    
    # call the function 
    x_i_plus_1 = random_walk_one_step(P, x_i) 

    # test whether or not x_i_plus_1 is a numpy matrix 
    assert type(x_i_plus_1) == np.matrixlib.defmatrix.matrix

    # check the shape of the vector
    assert x_i_plus_1.shape == (3,1)

    # check the correctness of the result 
    x_real=np.mat([[1.5],
                   [0.5],
                   [1.0]] )
    assert np.allclose(x_real, x_i_plus_1)

    #---------------------
    # test with another matrix

    # another transition matrix of shape (2 by 2) 
    P = np.mat([[ 0.1,  0.4],
                [ 0.9,  0.6]])

    # an all-one vector of shape (2 by 1)
    x_i =  np.asmatrix(np.ones((2,1)))

    # call the function 
    x_i_plus_1 = random_walk_one_step(P, x_i) 

    # check the shape of the vector
    assert x_i_plus_1.shape == (2,1)

    # check the correctness of the result 
    x_real=np.mat([[0.5],
                   [1.5]] )
    assert np.allclose(x_real, x_i_plus_1)
 


#-------------------------------------------------------------------------
def test_random_walk():
    ''' (5 points) random_walk'''

    # a transition matrix of shape (3 by 3) 
    P = np.mat([[ 0. ,  0.5,  1. ],
                [ 0.5,  0. ,  0. ],
                [ 0.5,  0.5,  0. ]] )
 
    # an all-one vector of shape (3 by 1)
    x_0 =  np.asmatrix(np.ones((3,1)))

    # call the function 
    x, n_steps = random_walk(P, x_0) 

    # check the shape of the vector
    assert x.shape == (3,1)

    # check number of random walks 
    # assert n_steps == 18
    assert n_steps < 100

    # check the correctness of the result 
    x_real = np.mat( [[ 1.33333333],
                      [ 0.66666667],
                      [ 1.        ]] )
    assert np.allclose(x_real, x,atol=1e-3)
    
    #---------------------
    # test max_steps
    x, n_steps = random_walk(P, x_0,max_steps=2)

    # check number of random walks 
    assert n_steps == 2

    # check the correctness of the result 
    x_real = np.mat( [[ 1.25],
                      [ 0.75],
                      [ 1.  ]] )
    assert np.allclose(x_real, x)

    #---------------------
    # test with another matrix

    # another transition matrix of shape (2 by 2) 
    P = np.mat([[ 0.5,  0.5],
                [ 0.5,  0.5]])

    # an all-one vector of shape (2 by 1)
    x_0 =  np.asmatrix(np.ones((2,1)))

    # call the function 
    x, n_steps = random_walk(P, x_0) 

    # test whether or not x is a numpy matrix 
    assert type(x) == np.matrixlib.defmatrix.matrix

    # check the shape of the vector
    assert x.shape == (2,1)

    # check number of random walks 
    assert n_steps == 1

    # check the correctness of the result 
    x_real=np.array([[1.],
                     [1.]] )
    assert np.allclose(x_real, x)


#-------------------------------------------------------------------------
def test_pagerank_v1():
    ''' (5 points) random_walk'''

    # adjacency matrix of shape (3 by 3)
    A = np.mat( [ [0., 1., 1.],
                  [1., 0., 0.],
                  [1., 1., 0.]])
    
    # call the function
    x= pagerank_v1(A) 

    # test whether or not x is a numpy matrix 
    assert type(x) == np.matrixlib.defmatrix.matrix

    # test the shape of the vector
    assert x.shape == (3,1)

    # check the correctness of the result 
    x_real = np.mat( [[ 1.33333333],
                      [ 0.66666667],
                      [ 1.        ]] )
    assert np.allclose(x_real, x,atol=1e-2)

