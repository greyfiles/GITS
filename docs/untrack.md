# About GITS Untrack
This functionality is exactly opposite of another Gits feature: track. 
This command moves files from staging area to the working directory back.
These untracked files will not be considered for the upcoming commits.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_untrack.py).

# Code Description
## Functions
1. gits_untrack(args):
This function takes **args** object as an input which has an attribute **filenames** to store the list of files to move from staging area to working directory. 
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Let say you have already used track command to move foo.py and bar.py from working directory to staging area. 
To untrack these files, consider following examples:
```
$ gits untrack foo.py
$ gits untrack bar.py
$ gits untrack foo.py bar.py
```
To untrack all the files currently present inside staging area, use the following command:
```
$ gits untrack . 
```