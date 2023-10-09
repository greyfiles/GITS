# About GITS Status
This function allows users to see status about
- changes present in the working directory but not moved to the staging area yet. [untracked files]
- changes to the files present inside staging area. [tracked files]
- changes to the files which are not being tracked.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_status.py).

# Code Description
## Functions
1. gits_status(args): 
This function simply displays the difference as mentioned in the above section.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Use the command as below to see the status:
```
$ gits status
```

