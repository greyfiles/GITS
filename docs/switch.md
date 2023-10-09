# About GITS Switch
This command is useful for switching between two branches during implementation.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_switch.py).

# Code Description
## Functions
1. switch_branch(args): 
this function takes **args** object as an input which has an attribute **branch_name** to store the name of the branch to be checked out.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Let say you are currently on branch **foo** and now you want to work on branch **bar**.
Use this command in following way to switch to branch **bar**.
```
$ gits switch foo
```