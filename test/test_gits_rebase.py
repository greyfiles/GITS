import os
import sys

sys.path.insert(1, os.getcwd())

from gits_rebase import gits_rebase
from gits_logging import init_gits_logger
from mock import patch

def test_gits_rebase_happy_case_current_branch():
    """
    Function to test gits rebase, success case with rebase on current branch
    """
    init_gits_logger()

    with patch('builtins.input', return_value="yes"):
        test_result = gits_rebase()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_rebase_happy_case_given_branch():
    """
    Function to test gits rebase, success case with rebase on given branch
    """
    init_gits_logger()

    with patch('builtins.input', side_effect=["yes", "branch name"]):
        test_result = gits_rebase()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_rebase_sad_case():
    """
    Function to test gits rebase, failure case
    """
    init_gits_logger()

    with patch('builtins.input', side_effect=["no", None]):
        test_result = gits_rebase()
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
