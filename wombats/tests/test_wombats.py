import pytest

from wombats import sample_function
from wombats import Wombats

@pytest.fixture
def Wombats_object():
    obj = Wombats()
    return obj

def test_Wombats_instance_has_sample_method(Wombats_object):
    assert hasattr(Wombats_object, "sample_method")

def test_wombats_has_sample_function():
    assert sample_function() is None  # no return value
