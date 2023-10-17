import subprocess
import os

def gits_super_init(readme_name, gitignore_contents, remote_url):
    """
    Initializes a new git repository, adds a default README.md and .gitignore file,
    and commits them. Also, allows the option to push the initial commit to a remote repository.
    """
    try:
        # Initialize a new git repository
        subprocess.check_call(['git', 'init'])
        
        # Create README.md file
        readme_name = "README.md"
        with open(readme_name, 'w') as f:
            f.write('# ' + os.path.basename(os.getcwd()) + '\n')
            f.write('This is the default README for the project.\n')

        # Create .gitignore file
        with open('.gitignore', 'w') as f:
            f.write("# Add files and directories to ignore\n")
        
        # Add the files to staging
        subprocess.check_call(['git', 'add', readme_name, '.gitignore'])

        # Commit the files
        commit_msg = f"Initialize repository with {readme_name} and .gitignore"
        subprocess.check_call(['git', 'commit', '-m', commit_msg])
        
        print(f"Repository initialized and committed with {readme_name} and .gitignore.")
        
        # Optional: Push to a remote repository if provided
        if remote_url:
            subprocess.check_call(['git', 'remote', 'add', 'origin', remote_url])
            subprocess.check_call(['git', 'push', '-u', 'origin', 'master'])
            print(f"Initial commit pushed to remote: {remote_url}")

    except Exception as e:
        print("ERROR: gits super_init command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
