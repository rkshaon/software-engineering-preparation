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

## Branching

### git branch
List branches.

### git branch [branch-name]
Create a new branch but will not switch to new created branch.

### git checkout [branch-name]
Merge a branch into the current branch

### git checkout -b [branch-name]
Create a new branch and switch to created branch.

### git branch -d [branch-name]
Delete a branch.

## Sharing and Updating Projects

### git remote add [alias] [url]
Add a remote repository

```
git remote add origin git@github.com:rkshaon/software-engineering-preparation.git
```

### git fetch [alias]
Fetch changes from a remote repository.

### git pull [alias] [branch]
Fetch and merge changes from a remote branch.

```
git pull origin master
```

### git push [alias] [branch]
Push changes to a remote branch.

```
git push origin rkshaon
```

### git push --set-upstream [alias] [branch]
Push a branch to a remote repository and set it as the upstream branch.

## Inspection and Comparison

### git log
Show the commit history

```
git log
```

and output will be like below

```
commit b07a824133acb924879a378dac656fac9a84f599 (HEAD -> rkshaon, origin/rkshaon, shaon)
Author: Rezaul Karim Shaon <rkshaon.ist@gmail.com>
Date:   Mon Jul 15 19:01:07 2024 +0600

    feat: Git - commands

commit 2b35411c2b8ef6f740a710d195eebbb94b1b5b55 (main)
Author: Rezaul Karim Shaon <rkshaon.ist@gmail.com>
Date:   Mon Jul 15 18:49:23 2024 +0600

    feat: Git - commands

commit 045eeca452421e056cef74a3e9932a873d9671cd (origin/main)
Author: Rezaul Karim Shaon <rkshaon.ist@gmail.com>
Date:   Sat Jul 13 18:27:25 2024 +0600

    feat: Database - PostgreSQL - Schema - added
```

### git log --oneline --graph --decorate --all
Show a graph of the commit history.

```
git log --oneline --graph --decorate --all
```

and the output will be like below.

```
* b07a824 (HEAD -> rkshaon, origin/rkshaon, shaon) feat: Git - commands
| *   6644959 (origin/master) Merge pull request #104 from rkshaon/rkshaon
| |\  
| |/  
|/|   
* | 2b35411 (main) feat: Git - commands
| *   0ca0905 Merge pull request #103 from rkshaon/main
| |\  
| |/  
|/|   
* | 045eeca (origin/main) feat: Database - PostgreSQL - Schema - added
|/  
*   0822708 (origin/shaon) Merge pull request #102 from rkshaon/shaon
|\  
| * 71ee215 updt: Concept and Comparison - npm vs Yarn
* | 7758d77 Merge pull request #101 from rkshaon/shaon
|\| 
| * c6fd66b updt: Concept and Comparison - npm vs Yarn
* | d53be77 Merge pull request #100 from rkshaon/shaon
|\| 
| * 72156fa feat: Concept and Comparison - npm vs Yarn
| * 7f45c58 feat: Books - Design Patterns Elements of Reusable Object-Oriented Software - added
* | ad7f21e Update install_on_ubuntu.md
* | d1163a8 Update install_on_ubuntu.md
* | 6812023 Merge pull request #99 from rkshaon/shaon
|\| 
```

### git show [commit]
Show information about a specific commit.

### git diff [commit1] [commit2]
Show differences between two commits.

## Undoing Changes

### git revert [commit]
Create a new commit that undoes the changes from a previous commit.

### git reset --hard [commit]
Reset the working directory and staging area to match a commit.

### git clean -f
Remove untracked files from the working directory.

## Stashing

### git stash
Save change temporarily.

### git stash apply
Apply the most recently stashed changes.

### git stash list
List stashed changes.

### git stash drop
Remove a stashed state.

## Advanced Branching and Merging

### git rebase [branch]
Re-apply commits on top of another base tip.

### git cherry-prick [commit]
Apply the changes introduced by some existing commit.

## Tagging

### git tag
List tags.

### git tag [tag-name]
Create a new tag.

### git tag -d [tag-name]
Delete a tag.

### git push [alias] [tag-name]
Push a tag to a remote repository.

## Rewriting History

### git commit --amend
Modify the most recent commit.

### git rebase -i [base]
Interactively rebase commits onto another base.

## Submodules

### git submodule add [url] [path]
Add a submodule.

### git submodule init
Initialize the submodules.

### git sobmodule update
Update the submodules.

