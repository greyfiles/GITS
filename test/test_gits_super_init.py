import argparse
import sys
import os
import shutil

sys.path.insert(1, os.getcwd())

from gits_super_init import gits_super_init
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


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(remote_url=None))
@patch("subprocess.Popen", return_value="anything")
def test_gits_super_init_normal(mock_var1, mock_args):
    """
    Function to test gits super_init, success case
    """
    test_result = gits_super_init(mock_args)
    remove_extras(".")
    if test_result:
        assert True, "Normal super_init"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(remote_url="https://example.com/test_repo.git"))
@patch("subprocess.Popen", return_value="anything")
def test_gits_super_init_with_remote(mock_var1, mock_args):

    """
    Function to test gits super_init with remote URL, success case
    """
    test_result = gits_super_init(mock_args)
    remove_extras(".")
    if test_result:
        assert True, "Super init with remote"
    else:
        assert False

# You can add more test cases as needed.

if __name__ == "__main__":
    test_gits_super_init_normal()
    test_gits_super_init_with_remote()
