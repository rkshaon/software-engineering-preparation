# ls

The `ls` command in Linux is used to list the contents of a directory. It provides information about files and directories, such as their names, sizes, permissions, and modification dates.

## Basic Syntax
```
ls [options] [file|directory...]
```

## Common Usage
### List Files in the Current Directory
```
ls
```

### List Files with Detailed Information
```
ls -l
```

This command lists files and directories in long format, showing detailed information such as permissions, number of links, owner, group, size, and modification date.

### List All Files Including Hidden Files
```
ls -a
```

This command lists all files, including hidden files (those starting with a dot `.`).

### List Files with Human-Readable File Sizes
```
ls -lh
```
This command lists files with detailed information and displays file sizes in a human-readable format (e.g., K, M, G for kilobytes, megabytes, gigabytes).

### Combining Options
```
ls -alh
```

This command lists all files, including hidden ones, with detailed information and human-readable file sizes.

#### Key Options
- `-l`: Use a long listing format.
- `-a`: Include directory entries whose names begin with a dot (hidden files).
- `-h`: With `-l`, print sizes in human-readable format (e.g., 1K, 234M, 2G).
- `-t`: Sort by modification time, newest first.
- `-R`: List subdirectories recursively.
- `-S`: Sort by file size, largest first.
- `-r`: Reverse the order of the sort.

