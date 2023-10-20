import sys
import os

sys.path.insert(1, os.getcwd())

from gits_add import gits_add_func

from gits_logging import init_gits_logger

def test_gits_add_happy_case():
    """
    Function to test gits_add, success case
    """

    init_gits_logger()

    file_names = ["test1", "test2"]
    test_result = gits_add_func(file_names)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_add_sad_case():
    """
    Function to test gits add, failure case
    """
    init_gits_logger()

    file_names = 2
    test_result = gits_add_func(file_names)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_add_happy_case_no_files():
    """
    Function to test gits add, success case when no files are passes as argument
    """
    init_gits_logger()

    file_names = ['']
    test_result = gits_add_func(file_names)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False
