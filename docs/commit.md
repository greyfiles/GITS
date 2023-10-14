# About GITS Commit
This command is used to commit changes present inside the staging area. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_commit.py).

# Code Description
## Functions
1. gits_commit_func(args):
This function takes **args** object as an input which has an attribute **-m** to store the commit message and another boolean attribute **-amend**. 
If **-amend** is set to true, command will not create new commit. Instead, it will simply add changes to the last commit.
Function returns True for successful execution and False otherwise with an exception.


# How to run it? (Small Example)
Let say you are on a particular branch working on some feature X. 
You've made some changes so far and you want to commit those chnages.
You can use the following command to do so:
```
$ gits commit -m "My first commit"
```
Soon after you realized a mistake in the last commit and want to fix that mistake.
However you do not want others to notice that mistake. 
In this situation, you can use the amend argument as shown below to update the last commit.
```
$ gits commit -m "My first commit with mistake fixed" --amend
``` 
After successful execution of this command, you will still have only one commit for the changes you have made so far.