# About GITS Reset
'Reset' intuitively means a HARD reset. 
This functionality does a HARD reset on your branch, and makes it even with the remote branch. 
This aims to simplify the confusion between HARD and the SOFT reset.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_reset.py).

# Code Description
## Functions
1. gits_reset(args):
this function takes **args** object as an input which has an attribute **branch** to store the name of the branch that you want to reset.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Consider the scenario where you are experimenting with someone else's work and to do so, you've cloned that person's development branch "foo" on your local machine.
You tried a bunch of stuff but nothing seem to work out well and you want to get the clean copy back for that branch.
Instead of manually deleting the cloned branch and cloning it again, you can use this command this way:
```
$ gits reset --branch foo
```
This will discard any changes present in you local machine and make it in sync with upstream branch.