#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import gits_logging


def gits_branch(args):
    """
    Function that allows users to show difference from last commit
    """
    try:
        diff_cmd = list()
        diff_cmd.append("git")
        diff_cmd.append("branch")
        process1 = subprocess.Popen(diff_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        gits_logging.gits_logger.info("gits branch command invoked successfully")
        print(stdout.decode("UTF-8"))

    except Exception as e:
        gits_logging.gits_logger.error("gits branch command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
