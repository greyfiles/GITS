#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import gits_logging


def gits_status(args):
    """
    Function that allows users to show status about
    1. changes present in the working directory but not in the staging area.
    2. changes present inside staging area.
    3. changes to the files which are not being tracked.
    """
    try:
        status_cmd = list()
        status_cmd.append("git")
        status_cmd.append("status")
        process1 = subprocess.Popen(status_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        gits_logging.gits_logger.info("gits status command invoked successfully")
        print(stdout.decode("UTF-8"))

    except Exception as e:
        gits_logging.gits_logger.error("gits status command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits status command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
