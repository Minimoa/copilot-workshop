import pytest
from factorial import is_prime

class TestIsPrime:
    def test_is_prime_with_negative_number(self):
        assert is_prime(-5) == False
    
    def test_is_prime_with_zero(self):
        assert is_prime(0) == False
    
    def test_is_prime_with_one(self):
        assert is_prime(1) == False
    
    def test_is_prime_with_two(self):
        assert is_prime(2) == True
    
    def test_is_prime_with_three(self):
        assert is_prime(3) == True
    
    def test_is_prime_with_four(self):
        assert is_prime(4) == False
    
    def test_is_prime_with_small_prime(self):
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(13) == True
    
    def test_is_prime_with_small_composite(self):
        assert is_prime(6) == False
        assert is_prime(9) == False
        assert is_prime(15) == False
    
    def test_is_prime_with_large_prime(self):
        assert is_prime(97) == True
        assert is_prime(101) == True
    
    def test_is_prime_with_large_composite(self):
        assert is_prime(100) == False
        assert is_prime(144) == False