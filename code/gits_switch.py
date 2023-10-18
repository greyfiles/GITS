#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import gits_logging


def switch_branch(branch_name):
    """
    Function that allows user to switch between branches
    """
    try:
        switch_cmd = list()
        switch_cmd.append("git")
        switch_cmd.append("checkout")
        switch_cmd.append(branch_name)
        process1 = subprocess.Popen(switch_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        gits_logging.gits_logger.info("gits switch command invoked successfully")
        print("Switched to branch:", branch_name)

    except Exception as e:
        gits_logging.gits_logger.error("gits switch command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits switch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
