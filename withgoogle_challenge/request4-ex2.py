import numpy as np

def detectStates(m):
    active, terminal = [], []
    for rowN, row in enumerate(m):
        (active if sum(row) else terminal).append(rowN)
    return(active,terminal)

# Convert each elements of array to simplest
def simplest_form(ar):
    ar = ar.round().astype(int).A1                   # np.matrix --> np.array
    gcd = np.gcd.reduce(ar)
    ar = np.append(ar, ar.sum())                      # append the common denom
    return (ar / gcd).astype(int)

# calculate absorb probability
def solution(m):
    active, terminal = detectStates(m)
    if 0 in terminal:                              # special case when s0 is terminal
        res= [1] + [0]*len(terminal[1:]) + [1]
        # print(res,m)
        return res
    m = np.matrix(m, dtype=float)[active, :]       # list --> np.matrix (active states only)
    comm_denom = np.prod(m.sum(1))                 # product of sum of all active rows (used later)
    P = m / m.sum(1)                               # divide by sum of row to convert to probability matrix
    Q, R = P[:, active], P[:, terminal]            # separate Q & R
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)                            # calc fundamental matrix
    B = N[0] * R * comm_denom / np.linalg.det(N)   # get absorbing probs & get them close to some integer
    res=simplest_form(B)
    # print(res,m)
    return res

# Case where state 0 itself is a terminal state

assert(solution([[0],])) == [1, 1]

m=[[0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
r=solution(m)
assert(r == [7, 6, 8, 21],"Incorrect!")

r=solution([
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],])
assert(r == [0, 3, 2, 9, 14] ,"Incorrect!")
