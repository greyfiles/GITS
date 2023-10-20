import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_set import gits_set_func
from gits_logging import init_gits_logger

def test_gits_set_happy_case():
    """
    Function to test gits set, success case
    """
    init_gits_logger()

    test_result = gits_set_func("parent")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_set_sad_case_invalid_parent():
    """
    Function to test gits set, failure case when parent is not valid
    """
    init_gits_logger()

    test_result = gits_set_func(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
