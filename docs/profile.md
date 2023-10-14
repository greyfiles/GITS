# About GITS Profile
This functionality allows the user to change the git account quickly with a single command. 
There are situations when a developer has a personal github account and a enterprise github account as well. 
Changing between these accounts is a little complicated. This functionality aims to simplify it.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_profile.py).

# Code Description
## Functions
1. gits_set_profile(args):
This function takes **args** object as an input which has an attribute **email** to store the email address to be updated and **name** to store the name to be updated. 
Function returns True for successful execution and False otherwise with an exception.

2. check(email):
This function takes a string **email** as an input and returns True if it is valid email address and False otherwise.

# How to run it? (Small Example)
Use the command in following way to update user name and email address to "foo" and "foo@bar.com" respectively.
```
$ gits profile --name foo --email foo@bar.com
```