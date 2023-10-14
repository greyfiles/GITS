# About GITS Pull
This function allows user to pull remote branch and merge it into local branch.

# Location of Code
The code that implements this gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_pull.py)

# Code Description
## Functions
1. gits_pull(args):
This function has three optional arguments. Those arguments are **nocommit**, **rebase and **branch**. **nocommit** fetches the remote content but does not create a new merge commit, **rebase** merges the remote branch with local branch using git rebase instead of git merge. **branch** is used to tell the function which branch you want to pull if it is not current branch.

# How to run it? (Small Example)
There are three ways you can pull the remote branch. In each of the commands described below branch is optional argument.
1) Simple pull
```
$ gits pull --branch branchname
```
2) Using nocommit method
``` 
$ gits pull --nocommit --branch branchname
```
3) Using rebase method
```
$ gits pull --rebase --branch branchname
```

After executing this command you would get remote branch pulled into your local repository. You may be required to resolve some merge conflicts.


