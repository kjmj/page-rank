import numpy as np
from problem4 import pagerank

#-------------------------------------------------------------------------
'''
    Problem 5: use PageRank (implemented in Problem 4) to compute the ranked list of nodes in a real-world network. 
    In this problem, we import a real-world network and use pagerank algorithm to rank the nodes in the network.
    File `network.csv` contains a network adjacency matrix. 
    (1) import the network from the file
    (2) compute the pagerank scores for the network
    You could test the correctness of your code by typing `nosetests test5.py` in the terminal.
'''

#--------------------------
def import_A(filename ='network.csv'):
    '''
        import the addjacency matrix A from a CSV file. delimiter is ','
        Input:
                filename: the name of csv file, a string 
        Output: 
                A: the ajacency matrix, a numpy matrix of shape (n by n)
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    A = np.asmatrix(np.loadtxt(filename, delimiter=','))
    #########################################
    return A


#--------------------------
def score2rank(x):
    '''
        compute a list of node IDs sorted by descending order of pagerank scores in x.
        Note the node IDs start from 0. So the IDs of the nodes are 0,1,2,3, ...
        Input: 
                x: the numpy array of pagerank scores, shape (n by 1) 
        Output: 
                sorted_ids: a python list of node IDs (starting from 0) in descending order of their pagerank scores, a python list of integer values, such as [2,0,1,3].
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    sorted_ids = list(np.argsort(np.array(x).reshape(-1))[::-1])
    #########################################
    return sorted_ids

#--------------------------
def node_ranking(filename = 'network.csv', alpha = 0.95):
    ''' 
        Rank the nodes in the network imported from a CSV file.
        (1) import the adjacency matrix from `filename` file.
        (2) compute pagerank scores of all the nodes
        (3) return a list of node IDs sorted by descending order of pagerank scores 

        Input: 
                filename: the csv filename for the adjacency matrix, a string.
                alpha: a float scalar value, which is the probability of choosing option 1 (randomly follow a link on the node)

        Output: 
                sorted_ids: the list of node IDs (starting from 0) in descending order of their pagerank scores, a python list of integer values, such as [2,0,1,3].
        
    '''
    A = import_A(filename)
    x = pagerank(A,alpha)
    sorted_ids = score2rank(x)
    return sorted_ids


