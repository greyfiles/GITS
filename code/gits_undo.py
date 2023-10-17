#!/usr/bin/python3

import gits_logging
from subprocess import PIPE
import subprocess


def gits_undo(file_names):
    """
    Function that moves files from working directory to the staging directory.
    Only tracked files will be considered for any upcoming files.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("checkout")
        file_names_list = file_names
        total_files = len(file_names_list)
        if total_files != 0:
            for i in range(0, total_files):
                subprocess_command.append(file_names_list[i])
            process = subprocess.Popen(
                subprocess_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            gits_logging.gits_logger.info("gits undo command invoked successfully")

    except Exception as e:
        gits_logging.gits_logger.error("gits undo command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits undo command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
