import unittest
import argparse
import sys
import os
import shutil

sys.path.insert(1, os.path.join(os.getcwd(), '..'))

from gits_super_init import gits_super_init
from gits_logging import init_gits_logger
from mock import patch

def remove_extras(path):
    files = os.listdir(path)
    for file in files:
        if "py" in file:
            continue
        try:
            shutil.rmtree(file)
        except:
            os.remove(file)

def test_gits_super_init_normal():
    """
    Function to test gits super_init, success case
    """
    init_gits_logger()

    test_result = gits_super_init(None, None, False)
    remove_extras(".")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

#def test_gits_super_init_with_remote():
#    """
#    Function to test gits super_init with remote URL, success case
#    """
#    init_gits_logger()
#
#    test_result = gits_super_init(None, None, "https://example.com/test_repo.git")
#    remove_extras(".")
#    if test_result:
#        assert True, "Normal Case"
#    else:
#        assert False
