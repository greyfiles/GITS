#!/usr/bin/python3

import gits_logging
from subprocess import PIPE
import subprocess


def gits_add_func(args):
    """
    Function that adds files as passed
    to the gits add command.
    Performs operation as similar to git
    add command
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("add")
        file_names_list = args.file_names
        total_files = len(file_names_list)
        if total_files == 0:
            # do nothing
            pass
        else:
            for i in range(0, total_files):
                subprocess_command.append(file_names_list[i])
            process = subprocess.Popen(
                subprocess_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            gits_logging.gits_logger.info("gits add command invoked successfully")

    except Exception as e:
        gits_logging.gits_logger.error("gits add command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits add command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
