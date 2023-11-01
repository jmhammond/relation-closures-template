import closures;

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
    assert(closures.warshall(A) == [[1, 0, 1, 0], 
                                    [1, 0, 1, 1],
                                    [1, 1, 1, 1], 
                                    [1, 0, 1, 1]])
    assert(closures.warshall(B) == [[0, 0, 1, 0, 1],
                                    [1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1],
                                    [0, 0, 1, 0, 0]])

def test_reflexive_closure():
    assert(closures.reflexive_closure(A) == [[1, 0, 1, 0],
                                             [0, 1, 1, 1],
                                             [0, 1, 1, 0],
                                             [1, 0, 0, 1]])
    assert(closures.reflexive_closure(B) == [[1,0,1,0,1],
                                             [0,1,0,0,1],
                                             [0,0,1,0,0],
                                             [1,0,0,1,0],
                                             [0,0,1,0,1]])
    
def test_symmetric_closure():
    assert(closures.symmetric_closure(A) == [[1, 0, 1, 1],
                                             [0, 0, 1, 1],
                                             [1, 1, 1, 0],
                                             [1, 1, 0, 0]])
    assert(closures.symmetric_closure(B) == [[0,0,1,1,1],
                                             [0,1,0,0,1],
                                             [1,0,0,0,1],
                                             [1,0,0,1,0],
                                             [1,1,1,0,0]])