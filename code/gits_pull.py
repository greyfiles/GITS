import subprocess
from subprocess import PIPE
import helper
import gits_logging


def gits_pull(args):
    """
    This function is used to pull remote branch and
    merge it into local branch.
    Usage: gits pull
           gits pull --no-commit
           gits pull --rebase
           gits pull --verbose
    """
    try:
        untracked_file_check_status = ["git", "status", "--porcelain"]
        process0 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)
        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stdout != b'':
            print("Note: Please commit uncommited changes before pulling")
            return False

        arguments = []
        curr_branch = helper.get_current_branch()
        if args.nocommit is True and args.rebase is True:
            print("You cannot use both nocommit and rebase at the same time")
            return False
        elif args.nocommit is True:
            arguments += ["--no-commit"]
        elif args.rebase is True:
            arguments += ["--rebase"]

        if args.branch is not False and args.branch is not None:
            arguments += [args.branch]
        else:
            arguments += [curr_branch]

        pull_command = ["git", "pull"] + ["origin"] + arguments
        process1 = subprocess.Popen(pull_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        gits_logging.gits_logger.info("gits pull command invoked successfully")
        print(stdout.decode("utf-8"))

    except Exception as e:
        gits_logging.gits_logger.error("gits pull command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits pull command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
