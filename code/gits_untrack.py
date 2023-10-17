#!/usr/bin/python3

import gits_logging
from subprocess import PIPE
import subprocess


def gits_untrack(file_names):
    """
    Function that moves files from staging area to the working directory.
    Untracked files will not be considered for the upcoming commits.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("reset")
        subprocess_command.append("HEAD")
        file_names_list = file_names
        total_files = len(file_names_list)
        if total_files != 0:
            for i in range(0, total_files):
                subprocess_command.append(file_names_list[i])
            process = subprocess.Popen(
                subprocess_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            gits_logging.gits_logger.info("gits untrack command invoked successfully")

    except Exception as e:
        gits_logging.gits_logger.error(
            "gits untrack command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits untrack command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
