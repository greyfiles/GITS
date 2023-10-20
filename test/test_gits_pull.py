import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_pull import gits_pull
from gits_logging import init_gits_logger

def test_gits_pull_happy_case_with_no_commit_and_given_branch():
    """
    Function to test gits pull, success case with no commits, no rebase and given branch
    """
    init_gits_logger()

    test_result = gits_pull(True, False, "branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_pull_happy_case_with_commit_and_given_branch():
    """
    Function to test gits pull, success case with commits, rebase and given branch
    """
    init_gits_logger()

    test_result = gits_pull(False, True, "branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_pull_sad_case_with_no_commit_and_rebase():
    """
    Function to test gits pull, failure case with no commits, but rebase
    """
    init_gits_logger()

    test_result = gits_pull(True, True, "branch name")
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_pull_sad_case_with_uncommitted_changes():
    """
    Function to test gits pull, failure case with uncommited changes
    """
    init_gits_logger()

    test_result = gits_pull(True, True, "branch name")
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
