import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_sync import gits_sync
from gits_logging import init_gits_logger

def test_gits_sync_happy_case_source_branch():
    """
    Function to test gits sync, success case when source branch is given
    """
    init_gits_logger()

    test_result = gits_sync("branch name")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

def test_gits_sync_sad_case_no_args():
    """
    Function to test gits sync, success case when source branch is not given
    """
    init_gits_logger()

    test_result = gits_sync(None)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

#def test_gits_sync_sad_case_uncommitted_changes():
#    """
#    Function to test gits sync, failure case when there are uncommitted changes
#    """
#    init_gits_logger()
#
#    mock_args = parse_args(mock_args)
#    test_result = gits_sync(mock_args)
#    if not test_result:
#        assert True
#    else:
#        assert False
