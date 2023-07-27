import os
clear = lambda:os.system("cls")
clear()

from address import extract_city
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    # assert extract_city("Rexburg, ID 83460") == "Rexburg"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
