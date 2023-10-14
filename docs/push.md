# About GITS Push
This function allows user to push local commits to remote branch.

# Location of Code
The code that implements this gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_push.py)

# Code Description
## Functions
1. gits_push(args):
This function takes option argument **rebase** as input. When you use **rebase**, gits first pulls the specified remote branch and rebase's current branch on top of the last commit on remote branch.

# How to run it? (Small Example)
You can use this command in two different ways.
1) Simple push
```
gits push
```
2) Using rebase
```
gits push --rebase branchname
```
After using this command, your local branch would be pushed to the remote branch.
