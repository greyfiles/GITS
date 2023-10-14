# About GITS Init
This function allows user to transform current directory into a Git repository. 
It also allow user to clone an already existing repository.

# Location of Code
The code that implements this gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_init.py)

# Code Description
## Functions
1. gits_init(args):
This function takes optional arguments as an input. Those arguments are **bare** which is a boolean attribute, **template** which takes path to template file as input and **clone_url** which represents the url for repository in case of cloning. 
If **bare** is set to true, then an empty git repository would be initialized but the working directory would be omitted. 
Whereas, if **template** argument is used, then the directory is initialized with the provided template repository.
If **clone_url** is provided, it will create and initialize new repository inside current directory with specified url.

# How to run it? (Small Example)
There are three different ways to initialize the repository.
- Simple git initialization
```
$ gits init
```
- Using bare flag
```
$ gits init --bare
```
- Using templates
```
$ gits init --template pathtotemplate
```
After using any of these commands your directory would have a version control system.

To clone a repository inside current directory:
```
$ gits init --clone_url repository_url_here
```
It will create and initialize new repository inside current directory.