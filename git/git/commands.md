# Git Commands

Comprehensive list of commonly used Git Commands.

## Configuring Git

### git config --global user.name "Your Name"
Here replace `Your Name` with your name which will be attached to your commits.

### git config --global user.email "example@mail.com"
Here, replace `example@mail.com` with your email address which will be attached to your commits.

### git config --global core.editor "code --wait"
Set the default editor used by Git.

### git config --list
List all the Git configurations.

## Getting and Creating Projects

### git init [project-name]
Create a new local repository.

### git clone [url]
Clone a repository into a new directory.

## Basic Snapshotting

### git add [file]
Add a file to the staging area.

### git add .
Add all new and changed files to the staging area.

### git commit -m "Commit Message"
Commit changes to the repository with a message.

### git status
Show the status of changes as untracked, modified or staged.

### git diff
Show differences between working directory and index.

### git diff --staged
Show differences between the index and the last commit.

### git reset [file]
Unstaged a file while retaining changes in working directory.

### git reset --hard
Reset the working directory to the last commit.