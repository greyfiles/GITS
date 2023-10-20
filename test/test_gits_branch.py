import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_branch import gits_branch
from gits_logging import init_gits_logger

def test_gits_branch_happy_case():
    """
    Function to test gits branch, success case
    """
    init_gits_logger()

    test_result = gits_branch()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

#
#def test_gits_branch_sad_case():
#    """
#    Function to test gits branch, failure case
#    """
#    test_result = gits_branch()
#    if not test_result:
#        assert True, "Normal Case"
#    else:
#        assert False
