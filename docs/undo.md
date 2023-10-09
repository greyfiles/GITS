# About GITS Undo
This command is useful when the changes you've made after last commit is not working well and you want to update your working directory with last stable commit instead of manually undoing the changes.
Be careful while using this command because changes present in the working directory will be lost after execution of this command.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_undo.py).

# Code Description
## Functions
1. gits_undo(args):
this function takes **args** object as an input which has an attribute **filenames** to store the list of files for which we want to undo the changes. 
Function returns True for successful execution and False otherwise with an exception.


# How to run it? (Small Example)
let say since your last commit, you've made changes to the files: foo.py and bar.py. However, changes are not showing expected result and you want to undo those changes.
To undo those changes, consider the following examples:
```
$ gits undo foo.py
$ gits undo bar.py
$ gits undo foo.py bar.py
```