# About GITS Delete
Please use this functionality with caution since there would be no going back from this.
This function will delete a commit from the remote branch.
This functionality is useful when you have commited a mistake to the remote repo and do not
want it be visible in your commit history.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/greyfiles/GITS/blob/master/code/gits_delete.py)

# Code Description
## Functions
1. gits_delete(args):this function takes args object as an input which has an attribute count to determine how many commits are supposed to be deleted from the master branch. 


# How to run it? (Small Example)
Let's say that you want to delete last 2 commits from the master branch of your repository, then you can do so by passing master in the branch argument and 2 in the count argument. 
The following command can be used to fulfill the above-mentioned task.
```
gits delete --branch master --count 2
```
