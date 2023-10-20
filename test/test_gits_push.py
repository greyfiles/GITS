import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_push import gits_push
from gits_logging import init_gits_logger

def test_gits_push_happy_case_with_rebase():
    """
    Function to test gits push, success case with rebase
    """
    init_gits_logger()

    test_result = gits_push("branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


#@patch("argparse.ArgumentParser.parse_args",
#       return_value=argparse.Namespace(rebase="branch name"))
#@patch("subprocess.Popen")
#def test_gits_push_sad_case_with_uncommitted_changes(mock_var, mock_args):
#    """
#    Function to test gits push, failure case with uncommitted changes
#    """
#    init_gits_logger()
#
#    test_result = gits_push(mock_args)
#    if not test_result:
#        assert True, "Normal Case"
#    else:
#        assert False

def test_gits_push_sad_case_with_no_arguments():
    """
    Function to test gits push, failure case with no arguments
    """
    init_gits_logger()

    test_result = gits_push(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
