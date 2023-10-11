import subprocess
from subprocess import PIPE
import gits_logging


def gits_reset(args):
    """'Reset' intuitively means a HARD reset.
    This functionality does a HARD reset on your branch, and makes it even with the remote branch.
    This aims to simplify the confusion between HARD and the SOFT reset."""
    print("Hello from GITS command line tools- GITS reset")
    try:
        process1 = subprocess.Popen(
            ['git', 'checkout', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        # print(stdout)
        process2 = subprocess.Popen(
            ['git', 'reset', '--hard', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        gits_logging.gits_logger.info("gits reset command invoked successfully")
        print("Current branch reset successful.")
    except Exception as e:
        gits_logging.gits_logger.error("gits reset command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
