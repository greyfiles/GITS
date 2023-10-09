# About GITS reate
This automatically checks out a new branch from local master, after pulling all the changes from the remote master to local master. 
The idea behind this is that this new branch should have all the latest commits before a developer starts 
working on them.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_create_branch.py).


# Code Description
## Functions
1. create_branch(args):
This function takes **args** object as an input which has an attribute **b** to store the name of the branch to be created. 
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Let say you are about to start working on a particular feature for the product your team is building.
It is general practice to implement a feature in a separate branch off the master and merge the changes back once you are done.
To do so, you can use the gits create command as follow which will create new branch from the master. 
```
$ gits create -b foo
```
Successful execution of this command will create a branch named foo which is in sync with the upstream main branch.