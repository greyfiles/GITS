import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_merge import merge_branch
from gits_logging import init_gits_logger

def test_git_create_branch_happy_case():
    """
    Function to test gits_merge_branch, success case
    """
    init_gits_logger()

    test_result = merge_branch("branch_name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_git_create_branch_sad_case():
    """
    Function to test gits_merge_branch, failure case when no arguments
    """
    init_gits_logger()

    test_result = merge_branch(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
