# About GITS Rebase
This is a highly simplified version of git rebase command. 
This interactive command asks for the branch that you want to rebase and automatically rebases it off master. 
This is the most common scenario. 
The original GIT rebase command is a little un-intuitive and there is always a confusion, about the source branch and the destination branch.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_rebase.py).

# Code Description
## Functions
1. gits_rebase(args):
On execution, this commands asks for the user input about whether the rebase is for current branch or some other branch.
If user chooses the second option, user has to specify name of the branch in another input.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Consider the scenario where you've been working on some feature on your branch which is checked out from the master.
Now, other developers from your team has merged their part to the master and you need to use those changes in the feature you are working on currently.
You can use this command in this way to get those changes:
```
$ gits rebase
Is the rebase on current branch?
[yes/no][y/n]y
```
If you are interested in rebasing some other branch names "foo", use the command in following way:
```
$ gits rebase
Is the rebase on current branch?
[yes/no][y/n]n
Enter the name of the branch you want to rebase: foo
```