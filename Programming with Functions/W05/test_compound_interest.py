"""
WARNING: This program will take QUITE some time to test!

    It took my computer 48.20s to completely finish, due to the test_get_user_inputs() taking some time with multiple
    terminal input data in sequence, and asserting each sequence in succession.
"""

import pytest
from pytest import approx
from compound_interest import get_user_inputs, convert_to_monthly, calculate_future_value, calculate_total_interest
import sys
from io import StringIO


def test_get_user_inputs(monkeypatch):
    """Verify that the get_user_inputs function works correctly."""
    stdin1 = StringIO("1000\n5\n12\n8\n25\nTrue")
    stdout1 = StringIO()
    stdin2 = StringIO("text\n1000\n5\n12\n8\n25\nTrue")
    stdout2 = StringIO()
    stdin3 = StringIO("1000\ntest\n-1\n1000\n5\n12\n8\n25\nTrue")
    stdout3 = StringIO()
    stdin4 = StringIO("1000\n5\ntest\n1000\n5\n-10\n1000\n5\n12\n8\n25\nTrue")
    stdout4 = StringIO()
    stdin5 = StringIO("1000\n5\n12\ntest\n1000\n5\n12\n8\n25\nTrue")
    stdout5 = StringIO()
    stdin6 = StringIO("1000\n5\n12\n8\n-1\n1000\n5\n12\n8\n25\nTrue")
    stdout6 = StringIO()
    stdin7 = StringIO("1000\n5\n12\n8\n25\ntrue\n1000\n5\n12\n8\n25\nTrue")
    stdout7 = StringIO()

    # Everything should come out with the same result, since the input is looped until "valid" is True...

    #Test 1
    monkeypatch.setattr(sys, "stdin", stdin1)
    monkeypatch.setattr(sys, "stdout", stdout1)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)
    #Test 2
    monkeypatch.setattr(sys, "stdin", stdin2)
    monkeypatch.setattr(sys, "stdout", stdout2)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)
    #Test 3
    monkeypatch.setattr(sys, "stdin", stdin3)
    monkeypatch.setattr(sys, "stdout", stdout3)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)
    #Test 4
    monkeypatch.setattr(sys, "stdin", stdin4)
    monkeypatch.setattr(sys, "stdout", stdout4)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)
    #Test 5
    monkeypatch.setattr(sys, "stdin", stdin5)
    monkeypatch.setattr(sys, "stdout", stdout5)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)
    #Test 6
    monkeypatch.setattr(sys, "stdin", stdin6)
    monkeypatch.setattr(sys, "stdout", stdout6)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)
    #Test 7
    monkeypatch.setattr(sys, "stdin", stdin7)
    monkeypatch.setattr(sys, "stdout", stdout7)
    tup = get_user_inputs()
    monkeypatch.undo()
    assert tup == (1000, 0.05, 12, 8, 25, True)

def test_convert_to_monthly():
    assert convert_to_monthly(144) == 12

def test_calculate_future_value():
    assert calculate_future_value(5000, 0.05, 12, 10, 100) == approx(23763.28)

def test_calculate_total_interest():
    assert calculate_total_interest(5000, 100, 12, 10, 23763.28) == approx(6763.28)

pytest.main(["-v", "--tb=line", "-rN", __file__])
