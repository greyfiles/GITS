#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import gits_logging


def merge_branch(branch_name):
    """
    Function that allows user to merge any branch into current branch
    """
    try:
        merge_cmd = list()
        merge_cmd.append("git")
        merge_cmd.append("merge")
        merge_cmd.append(branch_name)
        process1 = subprocess.Popen(merge_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        gits_logging.gits_logger.info("gits merge command invoked successfully")
        print(stdout.decode("UTF-8"))

    except Exception as e:
        gits_logging.gits_logger.error("gits merge command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits merge command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
