import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_untrack import gits_untrack
from gits_logging import init_gits_logger

def test_gits_track():
    """
    Function to test gits track, success case
    """
    init_gits_logger()

    test_result = gits_untrack(["test1", "test2"])
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_track_sad_case():
    """
    Function to test gits untrack, failure case
    """
    init_gits_logger()

    test_result = gits_untrack(None)
    if not test_result:
        assert True
    else:
        assert False

def test_gits_untrack_happy_case_no_files():
    """
    Function to test gits track, success case when no files are passed as argument
    """
    init_gits_logger()

    test_result = gits_untrack([])
    if test_result:
        assert True, "Normal Case"
    else:
        assert False
