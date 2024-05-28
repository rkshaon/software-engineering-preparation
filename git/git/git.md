# Git

Git is a distributed version control system (VCS) that allows developers to track changes in their codebase, collaborate with others, and manage different versions of their projects.

## Key points about Git
- Snapshots, Not Differences
    - Unlike traditional VCSs (such as CVS or Subversion), Git doesn’t store changes as a list of file-based differences. Instead, it thinks of its data as a series of snapshots of the entire project.
    - When you commit changes, Git captures a snapshot of all files at that moment and stores a reference to it. If files haven’t changed, Git links to the previous identical version rather than duplicating the entire file.
- Local Operations
    - Git operates primarily with local files and resources. Most operations don’t require information from a remote server, making them incredibly fast.
    - You have the entire project history on your local disk, allowing instant access to project history, diffs, and other operations.
- Branching and Merging
    - Git excels at branching and merging. You can create branches to work on features or bug fixes independently.
    - Merging branches is efficient because Git tracks changes as snapshots.
- Collaboration and Remotes
    - Git enables collaboration among developers. You can push your local changes to a remote repository (e.g., GitHub, GitLab, Bitbucket) and pull changes from others.
    - Remotes allow distributed teams to work together seamlessly.
- Popular Platforms
    - GitHub, GitLab, and Bitbucket are popular platforms for hosting Git repositories.
    - Developers use Git commands to interact with these platforms and manage their projects.

In summary, Git’s snapshot-based approach, local operations, and powerful branching capabilities make it a versatile and widely adopted version control system

#### References
- [What is Git @git-scm.com](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)
- [w3schools.com](https://www.w3schools.com/git/default.asp)