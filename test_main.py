from main import *

# Feel free to expand and add your own tests here.
# Doing so won't impact the gradescope autograder tests (gradescope uses
# its own copy of this file so any changes you make here won't affect it).

def test_multiply_edge_cases():
    # Test multiplying by zero
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(5)) == 0
    assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(0)) == 0
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0

def test_multiply_single_bit():
    # Test 1-bit numbers (base case check)
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1 * 1
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1 * 1
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(0)) == 1 * 0
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(1)) == 0 * 1

def test_quadratic_multiply():
    # Provided test
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
    
    # Additional tests for quadratic multiplication
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3 * 4
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(5)) == 7 * 5
    assert quadratic_multiply(BinaryNumber(15), BinaryNumber(15)) == 15 * 15

def test_subquadratic_multiply():
    # Provided test
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
    
    # Additional tests for subquadratic (Karatsuba) multiplication
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3 * 4
    assert subquadratic_multiply(BinaryNumber(7), BinaryNumber(5)) == 7 * 5
    assert subquadratic_multiply(BinaryNumber(13), BinaryNumber(11)) == 13 * 11
    assert subquadratic_multiply(BinaryNumber(50), BinaryNumber(25)) == 50 * 25

def test_mixed_lengths():
    # Test numbers with different bit lengths (requires padding logic to work properly)
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(12)) == 3 * 12
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(12)) == 3 * 12
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(15)) == 1 * 15
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(15)) == 1 * 15

def test_gradescope_edge_cases():
    # Test zero multiplication
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(100)) == 0
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(100)) == 0

    # Test large numbers to check for recursion/performance limits
    large_1 = BinaryNumber(2**50)
    large_2 = BinaryNumber(2**50 - 1)
    # Only test subquadratic here, as quadratic might hang on 50+ bits
    assert subquadratic_multiply(large_1, large_2) == (2**50) * (2**50 - 1)