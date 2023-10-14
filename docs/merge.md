# About GITS Merge
This command is used to merge your changes back to the base branch from which you've checked out your personal development branch.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_merge.py).

# Code Description
## Functions
1. merge_branch(args): 
this function takes **args** object as an input which has an attribute **branch_name** to store the name of the branch to be merged with current branch.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Consider the scenario where you checked out branch **foo** from the master to work on a particular task.
Now, you are done with that task and you want your changes to be merged back in to the master branch. 
To do so, you can use this command in following way from master branch:
```
$ gits merge foo
```
This will merge all the commits from branch **foo** to current branch.