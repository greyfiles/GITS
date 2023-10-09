# About GITS Upstream
This command will set upstream for a local branch to a remote branch.
It can also be used to set upstream for a remote branch to the original branch in case of a forked repo.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_setupstream.py).

# Code Description
## Functions
1. upstream(args):
This function takes **args** object as an input which has an attribute **local** to store the name of the local branch, **remote** to store the name of the remote branch and **upstream** to store the name of the branch present on the original repository in case of forked repo. 
Function returns True for successful execution and False otherwise with an exception.


# How to run it? (Small Example)
There are two variation of this command. If you want your local branch names "foo" to be upstream with remote branch "bar", you can use this command like this:
```
$ gits upstream --local foo --remote bar
```
In case of forked repository, if you want your remote branch "foo" to track an upstream branch "bar" from the original repository, you can use the following command:
```
$ gits upstream --remote foo --upstream bar
```