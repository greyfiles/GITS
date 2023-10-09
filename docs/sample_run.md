## Sample Run
Here is basic draft of a sample run that covers almost each enhancement of GITS so you can understand how it works. 
Feel free to edit this list as per your convenience. Add few tasks if you got more time for the experiment.

1. Create a test repository that can be used by participants to complete their tasks.
2. Ask participant to clone the repository on their local machine.
3. Ask participant to set their git profile name and email to "dummy_name" and "dummy@name.com" respectively. Once they are done, ask them to switch it back to the original ones.
4. Create two branches with name: branch1 and branch2.
5. List all the branches.
6. From current branch, switch to the branch1.
7. Create a file named "foo.txt" and write some text in it.
8. Track the file "foo.txt" so that it gets considered for the next commit.
9. Create another file named "bar.txt" and add some text in it.
10. Track this file "bar.txt" so that it gets considered for the next commit.
11. Commit these changes with appropriate commit message.
12. Make some change to the "bar.txt" and track those changes so that they get considered for the next commit.
13. You found some issues with changes to this file and now you don't want it to be considered for the next commit. remove those changes from commit area.
14. Also remove those changes from working directory.
15. Commit these changes with appropriate commit message and switch to the main branch.
16. Merge changes from the branch1 into this main branch and push those changes to the remote main branch.
17. Now switch to branch2.
18. Main branch has changed since we created this branch so this branch is working behind in changes. Make this branch up to date with local main branch.
19. You just got to know that some other developer merged his changes to the remote main branch. Since you have checked out from the main branch, you also want those changes in development branch. So, make your branch up to date with remote main branch.
20. Now switch to main branch again.
21. Create new file "temp.txt" and write some text in it and commit those changes.
22. You just realized you directly made changes to the main branch rather than your development branch by mistake. Undo those changes by making current main branch same as remote main branch.
23. You just got to know that someone merged their changes to the remote main branch. Sync your main branch.
24. Last commit that is present in the main branch is not working well so you want to remove changes made by that commit entirely on both: local and remote.
25. You are doing great till now but assume a hypothetical scenario where you have made a mess in your local repo and want to delete the current repo and fork it all again.
