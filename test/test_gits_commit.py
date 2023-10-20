import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_commit import gits_commit_func
from gits_logging import init_gits_logger

def test_gits_commit_happy_case_with_amend():
    """
    Function to test gits_commit, success case with amend message
    """
    
    init_gits_logger()
    test_result = gits_commit_func("test_commit", True)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_commit_happy_case_without_amend():
    """
    Function to test gits_commit, success case with no amend message
    """
    init_gits_logger()

    test_result = gits_commit_func("test_commit", False)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_commit_sad_case_with_no_message():
    """
    Function to test gits_commit, failure case with no commit message
    """
    init_gits_logger()

    test_result = gits_commit_func(None, False)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_commit_sad_case_with_no_arguments():
    """
    Function to test gits_commit, failure case with no arguments passed
    """
    init_gits_logger()

    test_result = gits_commit_func(None, None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
