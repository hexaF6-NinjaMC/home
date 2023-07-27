import os
clear = lambda:os.system("cls")
clear()

from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Manuel Flores", "Yanez") == "Yanez; Manuel Flores"
    assert make_full_name("Manuel","Flores-Yanez") == "Flores-Yanez; Manuel"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Yanez; Manuel Flores") == "Yanez"
    assert extract_family_name("Flores-Yanez; Manuel") == "Flores-Yanez"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Yanez; Manuel Flores") == "Manuel Flores"
    assert extract_given_name("Flores-Yanez; Manuel") == "Manuel"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
