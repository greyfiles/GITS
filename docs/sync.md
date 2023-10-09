# About GITS Sync
This command is particularly useful for developers who always work off the master branch on their own development branch. 
In this type of development, it is necessary to keep the development branch upto date with upstream master in order to avoid any merge comflicts in future.
gits sync command basically sync the current branch with upstream trunk (main/master) branch by first syncing the trunk branch and rebasing current branch on the synced trunk.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_sync.py).

# Code Description
## Functions
1. gits_sync(args):
this function takes **args** object as an input which has an attribute **source** which represents the branch to be considered as a source for the syncing.
Function returns True for successful execution and False otherwise with an exception.


# How to run it? (Small Example)
Let say your team maintains a branch named **main** for any project with upto date changes. 
Every developer in the team uses this branch as a source for their personal development tasks and merge the changes to this **main** branch again when they are done with their task.
Just like others, you also checked out you personal branch off the **main** and started working your task. 
However, you realized that it has been a few days ever since you started working on this task and other developers have already merged some changes to the **main** branch.
Here, you can use the following command to sync your local development branch with upstream **main** branch:
```
$ gits sync -source main
```
If you do not provide source, it will take the trunk branch by default.
```
$ gits sync
```