#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import gits_logging


def get_current_branch():
    """
    This function returns current checked out branch.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("rev-parse")
        subprocess_command.append("--abbrev-ref")
        subprocess_command.append("HEAD")
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        branch = stdout.decode('UTF-8')
        gits_logging.gits_logger.info("get current branch helper returned successfully")
        return branch.rstrip()
    except:
        gits_logging.gits_logger.error("get current branch helper encountered an exception")
        print("Error occured while getting current branch name!")
        return None


def get_trunk_branch_name():
    """
    This function returns the name of the trunk branch for the project
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("branch")
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        all_branches = stdout.decode('UTF-8')
        list_of_branch_names = all_branches.split()
        list_of_branch_names.remove('*')
        gits_logging.gits_logger.info("get trunk branch name helper returned successfully")
        if "master" in list_of_branch_names:
            return "master"
        elif "main" in list_of_branch_names:
            return "main"
        else:
            print("h")
            return list_of_branch_names[0]

    except:
        gits_logging.gits_logger.error("get trunk branch name helper encountered an exception")
        print("error occured while getting trunk branch name!")
        return None
