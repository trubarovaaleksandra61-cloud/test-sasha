import pytest
from math import sqrt, sin, cos, pi


class TestMathOperations:
    """Test suite for mathematical operations"""
    
    def test_addition(self):
        """Test 1: Basic addition"""
        assert 2 + 2 == 4
        assert 10 + 5 == 15
        assert -5 + 3 == -2
    
    def test_subtraction(self):
        """Test 2: Basic subtraction"""
        assert 10 - 5 == 5
        assert 3 - 10 == -7
        assert 0 - 5 == -5
    
    def test_multiplication(self):
        """Test 3: Basic multiplication"""
        assert 5 * 3 == 15
        assert 10 * 0 == 0
        assert -3 * 4 == -12
    
    def test_division(self):
        """Test 4: Basic division"""
        assert 10 / 2 == 5
        assert 9 / 3 == 3
        assert 7 / 2 == 3.5
    
    def test_power(self):
        """Test 5: Power operation"""
        assert 2 ** 3 == 8
        assert 5 ** 2 == 25
        assert 10 ** 0 == 1
    
    def test_square_root(self):
        """Test 6: Square root"""
        assert sqrt(4) == 2
        assert sqrt(9) == 3
        assert sqrt(16) == 4
    
    def test_modulo(self):
        """Test 7: Modulo operation"""
        assert 10 % 3 == 1
        assert 20 % 5 == 0
        assert 7 % 2 == 1


class TestStringOperations:
    """Test suite for string operations"""
    
    def test_string_concatenation(self):
        """Test 8: String concatenation"""
        assert "Hello" + " " + "World" == "Hello World"
        assert "Python" + "3" == "Python3"
    
    def test_string_length(self):
        """Test 9: String length"""
        assert len("Python") == 6
        assert len("") == 0
        assert len("Test") == 4
    
    def test_string_upper(self):
        """Test 10: String uppercase"""
        assert "hello".upper() == "HELLO"
        assert "World".upper() == "WORLD"
    
    def test_string_lower(self):
        """Test 11: String lowercase"""
        assert "HELLO".lower() == "hello"
        assert "Python".lower() == "python"
    
    def test_string_replace(self):
        """Test 12: String replacement"""
        assert "Hello World".replace("World", "Python") == "Hello Python"
        assert "test".replace("t", "T") == "TesT"


class TestListOperations:
    """Test suite for list operations"""
    
    def test_list_creation(self):
        """Test 13: List creation and access"""
        lst = [1, 2, 3, 4, 5]
        assert lst[0] == 1
        assert lst[-1] == 5
        assert len(lst) == 5
    
    def test_list_append(self):
        """Test 14: List append operation"""
        lst = [1, 2, 3]
        lst.append(4)
        assert lst == [1, 2, 3, 4]
    
    def test_list_sum(self):
        """Test 15: List sum"""
        assert sum([1, 2, 3, 4, 5]) == 15
        assert sum([10, 20, 30]) == 60
    
    def test_list_sort(self):
        """Test 16: List sorting"""
        lst = [3, 1, 4, 1, 5, 9]
        assert sorted(lst) == [1, 1, 3, 4, 5, 9]


class TestDictOperations:
    """Test suite for dictionary operations"""
    
    def test_dict_creation(self):
        """Test 17: Dictionary creation and access"""
        d = {"name": "Alice", "age": 30}
        assert d["name"] == "Alice"
        assert d["age"] == 30
    
    def test_dict_keys(self):
        """Test 18: Dictionary keys"""
        d = {"a": 1, "b": 2, "c": 3}
        assert set(d.keys()) == {"a", "b", "c"}
    
    def test_dict_values(self):
        """Test 19: Dictionary values"""
        d = {"x": 10, "y": 20}
        assert set(d.values()) == {10, 20}
    
    def test_dict_get(self):
        """Test 20: Dictionary get method"""
        d = {"key": "value"}
        assert d.get("key") == "value"
        assert d.get("missing", "default") == "default"
