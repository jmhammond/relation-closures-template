import closures;

# Test cases for the closure functions
M = [[0, 1, 0, 0], 
     [0, 0, 0, 1],
     [0, 0, 0, 0], 
     [1, 0, 1, 0]]
 
A = [[1, 0, 1, 0], 
     [0, 0, 1, 1],
     [0, 1, 1, 0], 
     [1, 0, 0, 0]]

B = [[0,0,1,0,1],
     [0,1,0,0,1],
     [0,0,0,0,0],
     [1,0,0,1,0],
     [0,0,1,0,0]]

def test_warshall():
    assert(closures.warshall(M) == [[1, 1, 1, 1], # wrong on row 1 
                                    [1, 1, 1, 1], # wrong on row 2
                                    [0, 0, 0, 0], # wrong on row 3
                                    [1, 1, 1, 1]]) # wrong on row 4
    assert(closures.warshall(A) == [[1, 1, 1, 1], # wrong on row 1
                                    [1, 1, 1, 1], # wrong on row 2
                                    [1, 1, 1, 1], # wrong on row 3
                                    [1, 1, 1, 1]]) # wrong on row 4
    assert(closures.warshall(B) == [[0, 0, 1, 0, 1], # wrong on row 1
                                    [0, 1, 1, 0, 1], # wrong on row 2
                                    [0, 0, 0, 0, 0], # wrong on row 3
                                    [1, 0, 1, 1, 1], # wrong on row 4
                                    [0, 0, 1, 0, 0]]) # wrong on row 5

def test_reflexive_closure():
    assert(closures.reflexive_closure(A) == [[1, 0, 1, 0],  #wrong on row 1
                                             [0, 1, 1, 1],  # wrong on row 2
                                             [0, 1, 1, 0],  # wrong on row 3
                                             [1, 0, 0, 1]]) # wrong on row 4
    assert(closures.reflexive_closure(B) == [[1,0,1,0,1],  #wrong on row 1
                                             [0,1,0,0,1],  # wrong on row 2
                                             [0,0,1,0,0], # wrong on row 3
                                             [1,0,0,1,0],  # wrong on row 4
                                             [0,0,1,0,1]]) # wrong on row 5
    
def test_symmetric_closure():
    assert(closures.symmetric_closure(A) == [[1, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 0]])
    assert(closures.symmetric_closure(B) == [[0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 1, 1, 0, 0]])
