import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_create_branch import create_branch
from gits_logging import init_gits_logger

def test_git_create_branch_happy_case():
    """
    Function to test gits_create_branch, success case
    """
    init_gits_logger()

    test_result = create_branch("branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_git_create_branch_sad_case_with_no_branch():
    """
    Function to test gits_create_branch, failure case with no branch name provided
    """
    init_gits_logger()

    test_result = create_branch(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_git_create_branch_sad_case_with_no_arguments():
    """
    Function to test gits_create_branch, failure case with no arguments passed
    """
    init_gits_logger()
    
    test_result = create_branch("")
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
