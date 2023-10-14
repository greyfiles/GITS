# About GITS Track
This command is used to move files from current working directory to the staging area. 
Only those files which are moved to the staging area are considered for the upcoming commits.  

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_track.py).

# Code Description
## Functions
1. gits_track(args): 
this function takes **args** object as an input which has an attribute **filenames** to store the list of files to move from working directory to staging area. 
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Let say you have made changes to the two files since last commit: foo.py and bar.py. You want these changes to be considered for the next commit. Here are some examples on how to use this command. 
```
$ gits track foo.py
$ gits track bar.py
$ gits track foo.py bar.py
```
If these are the only changes made after last commit, you can also use the following command:
```
$ gits track .   
```