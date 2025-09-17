import pytest

def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4, "we are in a different universe"   # if assert statement succeeds, the test passes

def test_true_is_true():
    assert True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])    