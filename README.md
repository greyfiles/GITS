
# GITS 
### GIT Simplified

![GitHub](https://img.shields.io/github/license/harshitpatel96/GITS)
[![Build Status](https://travis-ci.com/harshitpatel96/GITS.svg?branch=master)](https://travis-ci.com/harshitpatel96/GITS)
[![codecov](https://codecov.io/gh/harshitpatel96/GITS/branch/master/graph/badge.svg?token=G6RG52G2YO)](https://codecov.io/gh/harshitpatel96/GITS/)
![YouTube Video Views](https://img.shields.io/youtube/views/6Y8_RQecnZ8?style=social)

[![DOI](https://zenodo.org/badge/295480790.svg)](https://zenodo.org/badge/latestdoi/295480790)

![GitHub issues](https://img.shields.io/github/issues/harshitpatel96/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/harshitpatel96/GITS)

![Lines of code](https://img.shields.io/tokei/lines/github/harshitpatel96/GITS)

[![](https://img.youtube.com/vi/6Y8_RQecnZ8/hqdefault.jpg)](https://youtu.be/6Y8_RQecnZ8 "GITS demo")

# About GITS
**GITS**, or **Git-Simplified**, is a wrapper for mainstream Git functionality. By using fewer commands we allow users to increase efficiency and create a better workflow

# Installation for Linux
1. Clone GITS repository
2. While in the root directory run the following command:
    ```
    pip install -r requirements.txt
    ```
3. Now go to the configurations directory and run the following command:

    For Linux systems with a bash terminal or Windows systems using WSL run:
    ```
    bash project_init.sh
    ```
    For Linux systems with a fish terminal run:
    ```
    fish project_init.fish
    ```
4. Source the bashrc file
    ```
    source ~/.bashrc
    ```
    
    Note: Open the .bashrc file in User home directory to make sure that the alias command does not have any white spaces in the path. If so, rename the directory to remove the white spaces and re-run the setup.

# Installation for Windows
Currently this project cannot be run on Windows<br>
If you are on a Windows machine we recommend setting up a virtual machine to run Linux using VMware Workstation Player or VirtualBox<br> Both are popular choices for setting up VMs
>   Reference for [VirtualBox](https://www.virtualbox.org/)<br>
>   Reference for [VMware Workplayer Station](https://www.vmware.com/content/vmware/vmware-published-sites/us/products/workstation-player.html.html#:~:text=Product,-See%20All&text=What%20is%20VMware%20Workstation%20Player,for%20free%20for%20personal%20use)

If you are on Windows 10 you can opt to use WSL if your prefer that over using a VM
>   Reference for [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

# GITS Commands Docs
For documentation of the implemented commands please visit [GITS/docs](https://github.com/greyfiles/GITS/tree/master/docs)
A few of the commands implemented are:
- [gits_branch](https://github.com/greyfiles/GITS/blob/master/code/gits_branch.py)
- [gits_commit](https://github.com/greyfiles/GITS/blob/master/code/gits_commit.py)
- [gits_status](https://github.com/greyfiles/GITS/blob/master/code/gits_status.py)

# Want to Contribute?
If you are looking to contribute please take a look at our [CONTRIBUTING.md](https://github.com/greyfiles/GITS/blob/master/CONTRIBUTING.md) where we provide instructions on contributing to the repository.


### Quantitative measures
Here are some measures that can help compare the results between traditional git and gits.
1. Time taken to finish a particular task.
2. Number of commands executed to complete each task.
3. Number of time participants referred to the documentation or any other resources.

### Qualitative measures
Along with quantitative measures described above, few qualitative measures can help to assess the performance better.
1. Familiarity with traditional git
2. hardness of the task
