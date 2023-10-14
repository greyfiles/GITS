# About GITS Super Reset
Have you ever run into a situation, where you had to clone the repository again? 
Yes, this functionality is exactly for that scenario. 
It will remove the current repository. 
It will clone it again, and add all the remote branches to this freshly cloned repository.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_super_reset.py).

# Code Description
## Functions
1. super_reset(args):
this function takes **args** object as an input which has an attribute **name** to store the name of the repository that you want to super-reset.
It simply deletes the repository from the file system and clone it again in the same directory. 
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Consider the scenario where you have made a mess in the whole repository and the only possible way out is by cloning the repo again.
Instead of manually deleting the repository and cloning it all again, you can use this command.
One thing to note here is that unlike all other gits command, this command needs to be executed from the parent directory of repository.
```
$ gits super-reset --name foo_repository
```
Successful execution of this command will delete the repository named "foo_repository" and reclone at the same location with all the remote branches.