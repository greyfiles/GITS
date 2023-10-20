import argparse
import sys
import os
import shutil

sys.path.insert(1, os.getcwd())

from gits_init import gits_init
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

def test_gits_init_normal():
    """
    Function to test gits init, success case
    """
    test_result = gits_init(None, None)
    remove_extras(".")
    if test_result:
        assert True, "Normal Init"
    else:
        assert False

def test_gits_init_bare():
    """
    Function to test gits init --bare, success case
    """
    test_result = gits_init(True, None)
    remove_extras(".")
    if test_result:
        assert True, "Bare Init"
    else:
        assert False

def test_gits_init_template():
    """
    Function to test gits init --template, success case
    """
    test_result = gits_init(None, "test_template")
    remove_extras(".")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False
