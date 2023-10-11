import subprocess
from subprocess import PIPE
import helper
import gits_logging


def gits_sync(args):
    try:
        untracked_file_check_status = list()
        untracked_file_check_status.append("git")
        untracked_file_check_status.append("status")
        untracked_file_check_status.append("--porcelain")

        process1 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)

        stdout, stderr = process1.communicate()

        if stdout != b'':
            print("Note: Please commit uncommitted changes")
            return False

        curr_branch = helper.get_current_branch()
        if args.source:
            source_branch = args.source
        else:
            source_branch = helper.get_trunk_branch_name()

        print("Checking out source branch..")
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append(source_branch)
        process2 = subprocess.Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        print(stdout.decode('utf-8'))

        print("Pulling Changes from Upstream source branch..")
        pull_upstream = list()
        pull_upstream.append("git")
        pull_upstream.append("pull")
        process3 = subprocess.Popen(pull_upstream, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()
        print(stdout.decode('utf-8'))

        print("Checking out current branch..")
        checkout_current = list()
        checkout_current.append("git")
        checkout_current.append("checkout")
        checkout_current.append(curr_branch)
        process4 = subprocess.Popen(checkout_current, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process4.communicate()
        print(stdout.decode('utf-8'))

        print("Syncing current branch from the updated source branch..")
        rebase_cmd = list()
        rebase_cmd.append("git")
        rebase_cmd.append("rebase")
        rebase_cmd.append(source_branch)
        process5 = subprocess.Popen(rebase_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process5.communicate()
        print(stdout.decode('utf-8'))

        gits_logging.gits_logger.info("gits sync command invoked successfully")

    except Exception as e:
        gits_logging.gits_logger.error("gits sync command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits sync command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
