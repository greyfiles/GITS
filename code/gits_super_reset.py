#!/usr/bin/python3

import os
from subprocess import check_output
import shutil
import gits_logging


def super_reset(name):
    """
    Function that removes the local repository
    and does a fresh clone.
    This command should be run in the directory
    which consists your git repository.
    It takes the name of the git repository as a parameter
    """
    try:
        if not name:
            print("Required parameters are not provided. "
                  "Please add --name parameter.")
            return False
        os.chdir("./" + name)
        remote_loc = check_output(["git", "config", "remote.origin.url"])

        if not remote_loc:
            print("Remote location not found. Update git config")
            return False

        remote_loc = remote_loc.strip().decode("utf-8")
        os.chdir("../")
        print("Removing the current repository...")
        shutil.rmtree(name)
        print("Freshly cloning...")
        check_output(["git", "clone", remote_loc])
        gits_logging.gits_logger.info("gits super reset command invoked successfully")

    except Exception as e:
        gits_logging.gits_logger.error("gits super reset command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits super reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
