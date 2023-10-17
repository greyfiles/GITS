# /usr/bin/python3

import sys
import argparse
import gits_logging
import click
from gits_hello import gits_hello_world
from gits_add import gits_add_func
from gits_commit import gits_commit_func
from gits_set import gits_set_func
from gits_setupstream import upstream
from gits_create_branch import create_branch
from gits_super_reset import super_reset

from gits_rebase import gits_rebase
from gits_reset import gits_reset
from gits_delete import gits_delete

from gits_profile import gits_set_profile
from gits_track import gits_track
from gits_untrack import gits_untrack
from gits_undo import gits_undo
from gits_sync import gits_sync
from gits_push import gits_push
from gits_switch import switch_branch
from gits_merge import merge_branch
from gits_status import gits_status
from gits_diff import gits_diff
from gits_branch import gits_branch
from gits_init import gits_init
from gits_pull import gits_pull
from gits_super_init import gits_super_init

logger_status = gits_logging.init_gits_logger()
if not logger_status:
    print("ERROR: logger not initialised")
    sys.exit(1)


@click.group()
def cli():
    """gits: the wrapper CLI for git functions"""
    pass

#parser = argparse.ArgumentParser()
#subparsers = parser.add_subparsers()
@cli.command('hello', short_help='should be hidden...', hidden=True)
def hello():
    gits_hello_world()

#gits_hello_subparser = subparsers.add_parser('hello_world')
#gits_hello_subparser.set_defaults(func=gits_hello_world)

@cli.command('set', short_help='set an environment variable')
@click.argument('parent', nargs=1, type=click.STRING)
def set(parent):
    """
    Function that is used to set important
    environment variables
    """
    gits_set_func(parent)

#gits_set_subparser = subparsers.add_parser('set')
#gits_set_subparser.add_argument('--parent', help='git parent branch')
#gits_set_subparser.set_defaults(func=gits_set_func)

@cli.command('add', short_help='add files to be committed')
@click.argument('file_names', nargs=-1)
def add(file_names):
    """
    Function that adds files as passed
    to the gits add command.
    Performs operation as similar to git
    add command
    """
    gits_add_func(file_names)

#gits_add_subparser = subparsers.add_parser('add')
#gits_add_subparser.add_argument('file_names',
#                                metavar='N',
#                                type=str,
#                                nargs='+',
#                                help='all file names')
#gits_add_subparser.set_defaults(func=gits_add_func)

@cli.command('commit', short_help='create a changeset with added files')
@click.argument('message', nargs=1, type=click.STRING)
@click.option('--amend', is_flag=True, default=False)
def commit(message, amend):
    """
    Function that commit files as staged
    in the git command line internface
    Performs operation as similar to git
    commit command. Future additions : user 
    can specify if the commit should be rejected,
    if the unit test fails.
    """
    gits_commit_func(message, amend)

#gits_commit_subparser = subparsers.add_parser('commit')
#gits_commit_subparser.add_argument('-m',
#                                   required=True,
#                                   help='git commit message')
#gits_commit_subparser.add_argument('--amend',
#                                   action='store_true',
#                                   help='amend commit message')
#gits_commit_subparser.set_defaults(func=gits_commit_func)

@cli.command('create', short_help='create a branch')
@click.argument('name', nargs=1, type=click.STRING)
def create(name):
    """
    Function that creates a new local branch
    from local master after updating local master
    from remote master. The idea here is that the 
    new branch should have all the latest commits.
    """
    create_branch(name)

#gits_create_subparser = subparsers.add_parser('create')
#gits_create_subparser.add_argument('-b', help="branch name to create")
#gits_create_subparser.set_defaults(func=create_branch)

@cli.command('switch', short_help='swap to a branch')
@click.argument('branch_name', nargs=1, type=click.STRING)
def switch(branch_name):
    """
    Function that allows user to switch between branches
    """
    switch_branch(branch_name)

#gits_switch_subparser = subparsers.add_parser('switch')
#gits_switch_subparser.add_argument('branch_name', help="branch name to switch")
#gits_switch_subparser.set_defaults(func=switch_branch)

@cli.command('merge', short_help='merge a branch into current repo')
@click.argument('branch_name', nargs=1, type=click.STRING)
def merge(branch_name):
    """
    Function that allows user to merge any branch into current branch
    """
    merge_branch(branch_name)

#gits_merge_subparser = subparsers.add_parser('merge')
#gits_merge_subparser.add_argument('branch_name', help="branch name to merge")
#gits_merge_subparser.set_defaults(func=merge_branch)

@cli.command('upstream', short_help='set an upstream branch')
@click.option('--remote', nargs=1, type=click.STRING, help='remote branch to set as upstream')
@click.option('--local', nargs=1, type=click.STRING, help='local branch to be set as downstream')
@click.option('--upstream', nargs=1, type=click.STRING, help='set upstream for remote branch')
def upstream(remote, local, upstream):
    """
    Function that allows user to merge any branch into current branch
    """
    upstream(remote, local, upstream)

#gits_upstream_subparser = subparsers.add_parser('upstream')
#gits_upstream_subparser.add_argument('--remote',
#                                     help='the remote branch name')
#gits_upstream_subparser.add_argument('--local',
#                                     help="local branch name")
#gits_upstream_subparser.add_argument('--upstream',
#                                     help="the upstream branch name")
#gits_upstream_subparser.set_defaults(func=upstream)

@cli.command('profile', short_help='setup git user')
@click.argument('email', nargs=1, type=click.STRING)
@click.argument('name', nargs=1, type=click.STRING)
def profile(email, name):
    """
    Setup the git email and username with EMAIL and NAME

    EMAIL is the github email to set for the profile
    NAME  is the github username to set for the profile 
    """
    gits_set_profile(email, name)

#gits_profile_subparser = subparsers.add_parser('profile', help='profie help')
#gits_profile_subparser.set_defaults(func=gits_set_profile)
#gits_profile_subparser.add_argument('--email',
#                                    required=True,
#                                    help='email to be used')
#gits_profile_subparser.add_argument('--name',
#                                    required=True,
#                                    help='name to be used')

@cli.command('super-reset', short_help='re-pull the repository')
@click.option('--name', nargs=1, type=click.STRING)
def super_reset(name):
    """
    Completely restores the current repo to the state of the remote
    """
    super_reset(name)

#gits_super_reset_subparser = subparsers.add_parser('super-reset')
#gits_super_reset_subparser.add_argument('--name',
#                                        help="Name of the repository to super reset")
#gits_super_reset_subparser.set_defaults(func=super_reset)

@cli.command('rebase', short_help='rebase from master')
def rebase():
    """
    Function that allows user to interactively rebase from the master branch
    """
    gits_rebase()

#gits_rb_subparser = subparsers.add_parser('rebase', help='sync help')
#gits_rb_subparser.set_defaults(func=gits_rebase)

@cli.command('status', short_help='print current working status')
def status():
    """
    Function that outputs the current state of the local repository
    """
    gits_status()

#gits_status_subparser = subparsers.add_parser('status', help='sync help')
#gits_status_subparser.set_defaults(func=gits_status)

@cli.command('diff', short_help='show differences from last commit')
def diff():
    """
    Function that outputs the changes made since the last commit
    """
    gits_diff()

#gits_diff_subparser = subparsers.add_parser('diff', help='sync help')
#gits_diff_subparser.set_defaults(func=gits_diff)

@cli.command('branch', short_help='show all local branches')
def branch():
    """
    Function that outputs the branches currently pulled in the local repo
    """
    gits_branch()

#gits_branch_subparser = subparsers.add_parser('branch', help='sync help')
#gits_branch_subparser.set_defaults(func=gits_branch)

@cli.command('reset', short_help='hard reset a branch')
@click.argument('branch', nargs=1, type=click.STRING)
def merge(branch):
    """
    Function that hard resets BRANCH to the same state as remote

    BRANCH is the name of the branch to be reset
    """
    gits_reset(branch)

#gits_reset_subparser = subparsers.add_parser('reset', help='sync help')
#gits_reset_subparser.set_defaults(func=gits_reset)
#gits_reset_subparser.add_argument(
#    '--branch', required=True, help='branch to be used')

@cli.command('delete', short_help='delete a commit from remote')
@click.argument('branch', nargs=1, type=click.STRING)
@click.argument('count', nargs=1, type=click.INT)
def delete(branch, count):
    """
    Function that deletes COUNT commits from BRANCH on the remote

    BRANCH is the name of the branch to remove commits from
    COUNT  is the number of commits to remove
    """
    gits_delete(branch, count)

#gits_reset_subparser = subparsers.add_parser('delete', help='sync help')
#gits_reset_subparser.set_defaults(func=gits_delete)
#gits_reset_subparser.add_argument(
#    '--branch', required=True, help='branch to be used')
#gits_reset_subparser.add_argument(
#    '--count', required=True, help='Last commits to be deleted')
#

@cli.command('track', short_help='add untracked files to working changes')
@click.argument('file_names', nargs=-1)
def track(file_names):
    """
    Function that adds the passed files to the working set
    """
    gits_track(file_names)

#gits_track_subparser = subparsers.add_parser('track')
#gits_track_subparser.add_argument('file_names',
#                                  metavar='N',
#                                  type=str,
#                                  nargs='+',
#                                  help='all file names')
#gits_track_subparser.set_defaults(func=gits_track)

@cli.command('untrack', short_help='remove files from working changes')
@click.argument('file_names', nargs=-1)
def untrack(file_names):
    """
    Function that removes the passed files from the working changeset
    """
    gits_untrack(file_names)

#gits_untrack_subparser = subparsers.add_parser('untrack')
#gits_untrack_subparser.add_argument('file_names',
#                                    metavar='N',
#                                    type=str,
#                                    nargs='+',
#                                    help='all file names')
#gits_untrack_subparser.set_defaults(func=gits_untrack)

@cli.command('undo', short_help='un-stage files added to staging directory')
@click.argument('file_names', nargs=-1)
def undo(file_names):
    """
    Function that moves files from the staging directory to the working directory
    """
    gits_undo(file_names)

#gits_undo_subparser = subparsers.add_parser('undo')
#gits_undo_subparser.add_argument('file_names',
#                                 metavar='N',
#                                 type=str,
#                                 nargs='+',
#                                 help='all file names')
#gits_undo_subparser.set_defaults(func=gits_undo)

@cli.command('sync', short_help='get current state of trunk')
@click.option('--source', nargs=1, type=click.STRING, help='name of the trunk branch')
def sync(source):
    """
    Function that updates the working directory to be current with a source branch (trunk if unspecified)
    """
    gits_sync(source)

#gits_sync_subparser = subparsers.add_parser('sync')
#gits_sync_subparser.add_argument('-source', help="name of the trunk branch")
#gits_sync_subparser.set_defaults(func=gits_sync)

@cli.command('push', short_help='get current state of trunk')
@click.option("--rebase", nargs=1, default=False, help="do a pull rebase before pushing the changes")
def push(rebase):
    """
    Function that sends the record of local commits to remote
    """
    gits_push(rebase)

#gits_push_subparser = subparsers.add_parser('push')
#gits_push_subparser.add_argument("--rebase", nargs=1, default=False,
#                                 help="do a pull rebase before pushing the changes",
#                                 required=False)
#gits_push_subparser.set_defaults(func=gits_push)

@cli.command('init', short_help='setup current folder as git repository')
@click.option("--bare", is_flag=True, default=False, help='intialize an empty git repositories but omit the working directory')
@click.option("--template", nargs=1, default=False, help='initialize a git repository using predifined templates')
@click.option("--clone-url", nargs=1, default=False, help='url for cloning an already existing repo')
def init(bare, template, clone_url):
    """
    Function that sends the record of local commits to remote
    """
    gits_init(bare, template, clone_url)

#gits_init_subparser = subparsers.add_parser("init")
#gits_init_subparser.add_argument("--bare", action="store_true",
#                                 help="intialize an empty git repositories but omit the working directory")
#gits_init_subparser.add_argument(
#    "--template", help="initialize a git repository using predifined templates")
#gits_init_subparser.add_argument(
#    "--clone_url", help="url for cloning an already existing repo")
#gits_init_subparser.set_defaults(func=gits_init)

@cli.command('pull', short_help='get latest state from remote')
@click.option("--nocommit", is_flag=True, default=False, help='fetch remote without making a merge commit')
@click.option("--rebase", is_flag=True, default=False, help='use git rebase to merge with remote branch')
@click.option("--branch", nargs=1, default=False, help='branch to pull')
def pull(nocommit, template, branch):
    """
    Function that pulls down the latest state from remote
    """
    gits_pull(nocommit, template, branch)

#gits_pull_subparser = subparsers.add_parser("pull")
#gits_pull_subparser.add_argument("--nocommit", action='store_true',
#                                 help="fetches the remote contain but does not create a new merge commit",
#                                 required=False)
#gits_pull_subparser.add_argument("--rebase", action='store_true',
#                                 help="uses git rebase to merge with the remote branch",
#                                 required=False)
#gits_pull_subparser.add_argument("--branch", nargs="?", default=False,
#                                 help="you can specify the branch you want to pull",
#                                 required=False)
#gits_pull_subparser.set_defaults(func=gits_pull)

@cli.command('super-init', short_help='setup and initialize a repo')
@click.option("--readme-name", nargs=1, default=False, help='custom name for README')
@click.option('--gitignore-content', nargs=1, default=False, help='initial contents of gitignore file')
@click.option("--remote-url", nargs=1, default=False, help='url for pushing an already existing repo')
def super_init(readme_name, gitignore_content, remote_url):
    """
    Function that initializes and adds files to a generic repository
    """
    gits_super_init(readme_name, gitignore_content, remote_url)

#gits_super_init_subparser = subparsers.add_parser('super_init', 
#    help='Initializes a new git repo, adds default README.md and .gitignore, and commits them.')
#gits_super_init_subparser.add_argument('--readme-name', default='README.md',
#    help='Custom name for the README file. Default is README.md.')
#gits_super_init_subparser.add_argument('--gitignore-content', default='',
#    help='Content to add in the .gitignore file. By default, it will be empty.')
#gits_super_init_subparser.set_defaults(func=gits_super_init)
#
#
#args = parser.parse_args()

#if hasattr(args, 'func'):
#    args.func(args)
#else:
#    parser.print_help()
#    sys.exit(1)

cli(prog_name='gits')

if __name__ == '__main__':
    cli()