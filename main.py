"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    ### TODO
    n = max(len(x.binary_vec), len(y.binary_vec))
    if n <= 1:
        return x.decimal_val * y.decimal_val
    if n%2 != 0:
        n +=1
    x_vec = ['0']*(n-len(x.binary_vec))+x.binary_vec
    y_vec = ['0']*(n-len(y.binary_vec))+y.binary_vec

    mid = n // 2
    x_L = BinaryNumber(int(''.join(x_vec[:mid]), 2))
    x_R = BinaryNumber(int(''.join(x_vec[mid:]), 2))
    y_L = BinaryNumber(int(''.join(y_vec[:mid]), 2))
    y_R = BinaryNumber(int(''.join(y_vec[mid:]), 2))

    #based off of equation from class
    term1 = quadratic_multiply(x_L, y_L) * (2 ** n)
    term2 = (quadratic_multiply(x_L, y_R) + quadratic_multiply(x_R, y_L)) * (2 ** mid)
    term3 = quadratic_multiply(x_R, y_R)
    
    return term1 + term2 + term3
    pass
    ###

def subquadratic_multiply(x, y):
    ### TODO
    n = max(len(x.binary_vec), len(y.binary_vec))
    
    if n <= 1:
        return x.decimal_val * y.decimal_val
        
    if n % 2 != 0:
        n += 1
        
    x_vec = ['0'] * (n - len(x.binary_vec)) + x.binary_vec
    y_vec = ['0'] * (n - len(y.binary_vec)) + y.binary_vec
    
    mid = n // 2
    x_L = BinaryNumber(int(''.join(x_vec[:mid]), 2))
    x_R = BinaryNumber(int(''.join(x_vec[mid:]), 2))
    y_L = BinaryNumber(int(''.join(y_vec[:mid]), 2))
    y_R = BinaryNumber(int(''.join(y_vec[mid:]), 2))
    
    z0 = subquadratic_multiply(x_R, y_R)
    z2 = subquadratic_multiply(x_L, y_L)
    
    sum_x = BinaryNumber(x_L.decimal_val + x_R.decimal_val)
    sum_y = BinaryNumber(y_L.decimal_val + y_R.decimal_val)
    z1 = subquadratic_multiply(sum_x, sum_y)
    
    middle_term = z1 - z2 - z0
    
    term1 = z2 * (2 ** n)
    term2 = middle_term * (2 ** mid)
    term3 = z0
    
    return term1 + term2 + term3
    pass
    ###

def time_multiply(x, y, f):
    start = time.time()
    return (time.time() - start)*1000
    
def compare_multiply():
    pass
    # compare the empirical runtimes of multiplication functions
    ### TODO - add test cases and measure runtime
    test_sizes = [1000, 10000, 100000, 1000000, 10000000, 100000000]
    
    results = []
    for size in test_sizes:
        x = BinaryNumber(2**(size - 1) + 1)
        y = BinaryNumber(2**(size - 1) + 3)
    
        quad_time = time_multiply(x, y, quadratic_multiply)

        subquad_time = time_multiply(x, y, subquadratic_multiply)
        
        results.append((size, quad_time, subquad_time))
        
    print(f"{'Bits (n)':<10} | {'Quadratic (ms)':<15} | {'Subquadratic (ms)':<15}") #formatted table with the help of claude
    print("-" * 46)
    for size, q_time, s_time in results:
        print(f"{size:<10} | {q_time:<15.6f} | {s_time:<15.6f}")
        
    return results

    

