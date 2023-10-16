import unittest
import argparse
import sys
import os
import shutil

sys.path.insert(1, os.path.join(os.getcwd(), '..'))

from Code.gits_super_init import gits_super_init
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

class TestGitsSuperInit(unittest.TestCase):

    @patch("argparse.ArgumentParser.parse_args",
           return_value=argparse.Namespace(remote_url=None))
    @patch("subprocess.Popen", return_value="anything")
    def test_gits_super_init_normal(self, mock_var1, mock_args):
        """
        Function to test gits super_init, success case
        """
        test_result = gits_super_init(mock_args)
        remove_extras(".")
        self.assertTrue(test_result, "Normal super_init")

    @patch("argparse.ArgumentParser.parse_args",
           return_value=argparse.Namespace(remote_url="https://example.com/test_repo.git"))
    @patch("subprocess.Popen", return_value="anything")
    def test_gits_super_init_with_remote(self, mock_var1, mock_args):
        """
        Function to test gits super_init with remote URL, success case
        """
        test_result = gits_super_init(mock_args)
        remove_extras(".")
        self.assertTrue(test_result, "Super init with remote")

if __name__ == '__main__':
    unittest.main()
