import argparse
import sys
import os

sys.path.insert(1, os.getcwd())

from gits_undo import gits_undo
from gits_logging import init_gits_logger

def test_gits_undo_happy_case():
    """
    Function to test gits_undo, success case
    """
    init_gits_logger()

    test_result = gits_undo(["test1", "test2"])
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_undo_sad_case():
    """
    Function to test gits undo, failure case
    """
    init_gits_logger()

    test_result = gits_undo(None)
    if not test_result:
        assert True
    else:
        assert False

def test_gits_undo_happy_case_no_files():
    """
    Function to test gits undo, success case when no files are passed as argument
    """
    init_gits_logger()

    test_result = gits_undo([])
    if test_result:
        assert True, "Normal Case"
    else:
        assert False
