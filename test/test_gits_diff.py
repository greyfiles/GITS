import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_diff import gits_diff
from gits_logging import init_gits_logger

def test_gits_diff_happy_case():
    """
    Function to test gits diff, success case
    """
    init_gits_logger()

    test_result = gits_diff()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

#def test_gits_diff_sad_case():
#    """
#    Function to test gits diff, failure case
#    """
#    init_gits_logger()
#
#    test_result = gits_diff()
#    if not test_result:
#        assert True, "Normal Case"
#    else:
#        assert False
