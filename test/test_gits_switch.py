import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_switch import switch_branch
from gits_logging import init_gits_logger


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)

def test_gits_switch_happy_case():
    """
    Function to test gits switch, success case
    """
    init_gits_logger()

    test_result = switch_branch("branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_switch_sad_case():
    """
    Function to test gits switch, failure case
    """
    init_gits_logger()

    test_result = switch_branch(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
