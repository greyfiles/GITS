import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_profile import gits_set_profile
from gits_logging import init_gits_logger

def test_gits_profile_happy_case():
    """
    Function to test gits profile, success case
    """
    init_gits_logger()

    test_result = gits_set_profile("email@address.com", "name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_profile_sad_case_invalid_email():
    """
    Function to test gits profile, failure case when email is invalid
    """
    init_gits_logger()

    test_result = gits_set_profile("email", "name")
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_profile_sad_case_no_arguments():
    """
    Function to test gits profile, failure case when no arguments are passed
    """
    init_gits_logger()

    test_result = gits_set_profile(None, None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
