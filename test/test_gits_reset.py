import os
import sys

sys.path.insert(1, os.getcwd())

from gits_reset import gits_reset
from gits_logging import init_gits_logger

def test_gits_reset_happy_case():
    """
    Function to test gits reset, success case
    """
    init_gits_logger()
    
    test_result = gits_reset("branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_reset_sad_case():
    """
    Function to test gits reset, failure case
    """
    init_gits_logger()

    test_result = gits_reset(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
