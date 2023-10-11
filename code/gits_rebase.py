import subprocess
from subprocess import PIPE
import helper
import gits_logging


def gits_rebase(args):
    """This is a highly simplified version of git rebase command.
    This interactive command asks for the branch that you want to rebase and automatically rebases it off master.
    This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a
    confusion , about the source branch and the destination branch.
"""
    try:
        print("Is the rebase on current branch?")
        inp = input("[yes/no][y/n]")
        if inp.lower() == "yes" or inp.lower() == "y":
            process1 = subprocess.Popen(
                ['git', 'rebase', helper.get_trunk_branch_name()], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()
            print(stdout.decode("UTF-8"))
        else:
            inp2 = input("Enter the name of the branch you want to rebase: ")
            print(inp, inp2)
            process2 = subprocess.Popen(['git', 'checkout', inp2, 'git', 'rebase', helper.get_trunk_branch_name()],
                                        stdout=PIPE, stderr=PIPE)
            stdout, stderr = process2.communicate()
            gits_logging.gits_logger.info("gits rebase command invoked successfully")
            print(stdout.decode("UTF-8"))
    except Exception as e:
        gits_logging.gits_logger.error("gits rebase command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
