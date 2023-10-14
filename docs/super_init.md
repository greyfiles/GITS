# About gits super_init
The `gits super_init` command is a supercharged version of the regular `git init`. It not only initializes the repository but also creates a default `README.md` and `.gitignore` file. These files are immediately staged and committed. Optionally, if a remote repository URL is provided, it pushes the initial commit to the specified remote, making the setup process efficient and seamless.

# Location of Code
The code that implements this enhanced gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_super_init.py).

# Code Description
## Functions
1. `gits_super_init(args)`:
This function takes an optional argument `--remote_url`. If `--remote_url` is provided, after the repository initialization and committing the default files, the command will link the repository to the provided remote URL and push the initial commit. This is especially handy when starting a new project that you know will be pushed to a remote repository.

# How to run it? (Small Example)
There are two main ways to use `gits super_init`:

- Basic usage without linking to a remote repository:
$ gits super_init
This will initialize the directory, create and commit a `README.md` and `.gitignore` file.

- Linking to a remote repository:
$ gits super_init --remote_url https://github.com/username/repo.git
This will perform all the above actions and additionally add the provided URL as a remote named `origin`. The initial commit will then be pushed to the `master` or `main` branch of this remote repository.