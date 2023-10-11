#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import gits_logging


def gits_commit_func(args):
    """
    Function that commit files as staged
    in the git command line internface
    Performs operation as similar to git
    commit command. Future additions : user can specify if the commit should be rejected , if the unit test fails.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("commit")
        commit_message = args.m
        if not commit_message:
            print("ERROR: gits commit message not present, aborting")
            return False
        subprocess_command.append("-m")
        subprocess_command.append(commit_message)
        if not args.amend:
            # do nothing
            pass
        else:
            subprocess_command.append("--amend")

        # print(subprocess_command)
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        gits_logging.gits_logger.info("gits commit command invoked successfully")
        print("your changes committed successfully.")

    except Exception as e:
        gits_logging.gits_logger.error("gits commit command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits commit command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
