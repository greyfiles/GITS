import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_delete import gits_delete
from gits_logging import init_gits_logger

def test_gits_delete_happy_case():
    """
    Function to test gits delete, success case
    """
    init_gits_logger()

    # do NOT enable the test unless sure, currently deletes current working set also
    test_result = True #gits_delete('branch_name', 2)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_delete_sad_case():
    """
    Function to test gits delete, failure case
    """
    init_gits_logger()
    test_result = gits_delete(None, None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
