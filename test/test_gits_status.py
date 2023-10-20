import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_status import gits_status
from gits_logging import init_gits_logger

def test_gits_status_happy_case():
    """
    Function to test gits status, success case
    """
    init_gits_logger()

    test_result = gits_status()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

#def test_gits_status_sad_case():
#    """
#    Function to test gits status, failure case
#    """
#    init_gits_logger()
#
#    test_result = gits_status()
#    if not test_result:
#        assert True, "Normal Case"
#    else:
#        assert False
