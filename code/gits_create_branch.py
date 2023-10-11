#!/usr/bin/python3

from subprocess import PIPE
import helper
import subprocess
import gits_logging


def create_branch(args):
    """
    Function that creates a new local branch
    from local master after updating local master
    from remote master. The idea here is that the new branch should have all the latest commits.
    """
    try:
        # checkout main/master first
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append(helper.get_trunk_branch_name())
        process1 = subprocess.Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()

        # update with remote
        update_master = list()
        update_master.append("git")
        update_master.append("pull")
        process2 = subprocess.Popen(update_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()

        # checkout new branch
        if not args.b:
            print("Name of new branch not provided. Use -b branchName")
            return False
        checkout_feature = list()
        checkout_feature.append("git")
        checkout_feature.append("checkout")
        checkout_feature.append("-b")
        checkout_feature.append(args.b)
        process3 = subprocess.Popen(checkout_feature, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()
        gits_logging.gits_logger.info("gits create command invoked successfully")
        print("Branch created successfully. Currently you are on branch:", args.b)

    except Exception as e:
        gits_logging.gits_logger.error("gits create command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits create command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
