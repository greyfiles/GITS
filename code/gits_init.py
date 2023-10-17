from subprocess import Popen, PIPE
import gits_logging


def gits_init(bare, template, clone_url):
    """
    This function allows user to transform current
    directory into a Git repository.
    There are three ways to do it.
    1) Simple git init
         gits init
    2) Initialize with a bare flag
         gits init --bare
    3) Initialize using a preexisting template
         gits init --template path-to-template
    """
    try:
        if clone_url:
            process_commands = ["git", "clone", clone_url]
        else:
            process_commands = ["git", "init"]
            if bare is not False and bare is not None:
                process_commands.append("--bare")
            elif template is not None:
                process_commands.append("--template")
                process_commands.append(template)

        process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        gits_logging.gits_logger.info("gits init command invoked successfully")
        print(stdout.decode("UTF-8"))

    except Exception as e:
        gits_logging.gits_logger.error("gits init command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits init command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
