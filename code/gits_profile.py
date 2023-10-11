import subprocess
import re
from subprocess import PIPE
import gits_logging


def gits_set_profile(args):
    """
    This functionality allows the user to change the git account quickly with a single command.
    There are situations when a developer has a personal github account and a enterprise github account as well.
    Changing between these accounts is a little complicated. This functionality aims to simplify it.
    """
    # print(args.email)
    # print("Hello from GITS Commandline Tools-Profile")
    try:
        # check regex
        check_val = check(args.email)
        # print(check_val)
        if check_val:
            print("here")

            process = subprocess.Popen(["git", "config", "--global",
                                        "--unset", "user.email"],
                                       stdout=PIPE,
                                       stderr=PIPE)
            stdout, stderr = process.communicate()

            process1 = subprocess.Popen(["git", "config", "--global",
                                         "--unset", "user.name"],
                                        stdout=PIPE,
                                        stderr=PIPE)
            stdout, stderr = process1.communicate()

            process2 = subprocess.Popen(["git", "config", "--global",
                                         "user.name", args.name],
                                        stdout=PIPE,
                                        stderr=PIPE)
            stdout, stderr = process2.communicate()

            process3 = subprocess.Popen(["git", "config", "--global",
                                         "user.email", args.email],
                                        stdout=PIPE,
                                        stderr=PIPE)
            stdout, stderr = process3.communicate()

            profile_verify_name_command = list()
            profile_verify_name_command.append("git")
            profile_verify_name_command.append("config")
            profile_verify_name_command.append("--list")

            profile_verify_name = list()
            profile_verify_name.append("grep")
            profile_verify_name.append('user.name')

            process4 = subprocess.Popen(profile_verify_name_command,
                                        stdout=PIPE,
                                        stderr=PIPE)
            process41 = subprocess.Popen(profile_verify_name,
                                         stdin=process4.stdout,
                                         stdout=PIPE,
                                         stderr=PIPE)
            stdout, stderr = process41.communicate()
            print("Setting name and email..\n")
            print(stdout.decode('utf-8'))

            profile_verify_email_command = list()
            profile_verify_email_command.append("git")
            profile_verify_email_command.append("config")
            profile_verify_email_command.append("--list")

            profile_verify_email = list()
            profile_verify_email.append("grep")
            profile_verify_email.append("user.email")

            process5 = subprocess.Popen(profile_verify_email_command,
                                        stdout=PIPE,
                                        stderr=PIPE)
            process51 = subprocess.Popen(profile_verify_email,
                                         stdin=process5.stdout,
                                         stdout=PIPE,
                                         stderr=PIPE)
            stdout, stderr = process51.communicate()

            gits_logging.gits_logger.info("gits profile command invoked successfully")
            print(stdout.decode('utf-8'))

        else:
            print("Enter a valid email id")
            return False

    except Exception as e:
        gits_logging.gits_logger.error("gits profile command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits profile command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True

# Define a function for
# for validating an Email


def check(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, email)):
        return True
    else:
        return False
