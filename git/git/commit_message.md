# Git Commit Message


## What is commit message?
A commit message in Git is a concise description of the changes made in a specific commit. It serves as a record of what was modified, why it was changed, and any relevant context.

## The Anatomy of a Commit Message
Basic
```
git commit -m <message>
```

Detailed
```
git commit -m <title> -m <description>
```

## Why commit message is important?
- Future-Proofing
    - By providing a thoughtful commit message, you’re essentially writing a letter to your future self.
    - Well-crafted messages help you and your colleagues understand the purpose of the changes made, even months or years later.
- Troubleshooting and Debugging
    - When troubleshooting issues or debugging code, commit messages act as breadcrumbs.
    - They guide you to the relevant code changes and explain why those changes were made.
- Collaboration and Communication
    - In team environments, good commit messages enhance collaboration.
    - Team members can quickly grasp the intent behind each commit, making code reviews and collaboration smoother.

## What is good commit message?
A good commit message succinctly describes the purpose of a code change, using the imperative mood and providing relevant context. It should be specific, future-proof, and follow any team conventions. Well-crafted commit messages enhance collaboration, troubleshooting, and code maintenance by serving as a clear record of each change made in the project.

A good commit message is essential for maintaining a clear and organized project history. It serves as a concise yet informative record of the changes made in a specific commit.

## Why good commit message is important?
Good commit messages play a crucial role in software development.

- Understanding Changes
    - A good commit message enables you and your team to understand what the commit does without diving into the code itself.
    - It provides context about the purpose of the change, making it easier to grasp the motivation behind each modification.
- Historical Record
    - Commit messages serve as a historical record of the project’s evolution.
    - They document how the codebase has changed over time, allowing developers to trace back decisions and understand the project’s progression.
- Code Reviews and Debugging
    - During code reviews, clear commit messages help reviewers quickly assess the impact of a change.
    - When debugging or troubleshooting, well-structured messages guide developers to relevant code sections.
- Collaboration and Communication
    - Good commit messages facilitate collaboration among team members.
    - They allow contributors to communicate effectively about changes, especially in distributed or remote teams.

## What makes a bad commit message?
A bad commit message can hinder collaboration, code maintenance, and understanding of project history. 

- Vagueness
    - A vague commit message lacks clarity and doesn’t explain the purpose of the change.
    - Example of a bad commit message: “Fix a bug.”
- Lack of Context
    - A commit message should provide context about the problem being solved.
    - Without context, other developers may struggle to understand why the change was made.
    - Example of a bad commit message: “Update code.”
- Cryptic or Abbreviated Messages
    - Commit messages like “WIP,” “Refactor,” or “Cleanup” don’t convey meaningful information.
    - Abbreviations or acronyms without explanation can confuse readers.
    - Example of a bad commit message: “WIP: Refactor API.”
- Overly Long Messages
    - While being too brief is bad, excessively long messages can also be problematic.
    - Aim for a concise summary with additional details in the commit body if needed.
    - Example of a bad commit message: A multi-paragraph explanation without a clear summary.
- Ignoring Conventions
    - Ignoring team conventions or established commit message formats can lead to inconsistency.
    - Consistent conventions improve readability and maintainability.
    - Example of a bad commit message: Not following the team’s agreed-upon format.

## Characteristics of good commit message
Avoding bad commit message characteristics makes a commit message good.

### Mention type
This is where you specify the kind of change you’re making to the codebase. This makes it easier for maintainers and other contributors to gain a better understanding of your contribution.

Here are some other common abbreviations that are used to categorize commits:
- `feat`: This often is used to describe contributions where information or a new feature is added to an open source project.
- `docs`: This is commonly used to describe revisions to current versions of or updates to an open source project's documentation.
- `fix`: This is typically used for fixing bugs in the project's codebase or small grammar errors in the project's documentation.
- `chore`: This is often used for a contribution that make take longer that usual to finish.
- `refactor`: refactored code that neither fixes a bug nor adds a feature.
- `style`: changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
- `test`: including new or correcting previous tests
- `perf`: performance improvements
- `ci`: continuous integration related
- `build`: changes that affect the build system or external dependencies
- `revert`: reverts a previous commit.

#### Example
```
feat: mention information
```

### Summarize the changes
This is where you give an overview of the change and how you did it. This helps maintainers understand how your contribution solves the problem you’re trying to solve.

Now it’s important to note that GitHub has a 72-character limit so you'll need to keep your description within that range.

#### Example
```
feat: mentioning Christine Peterson in the course's intro
```

### Add a description
This is where you describe the change in more detail by mentioning why you made it. While this step is optional, consider doing this so that maintainers can get an idea of how your contribution enhances or solves an issue in their project.

#### Example
```
feat: mentioning Christine Peterson in the course's intro

I decided to add this information so participants can get accurate information
```

## Tips of writing good Commit Message
- Capitalization and Punctuation: Capitalize the first word and do not end in punctuation. If using Conventional Commits, remember to use all lowercase.
- Mood: Use imperative mood in the subject line. Example – Add fix for dark mode toggle state. Imperative mood gives the tone you are giving an order or request.
- Type of Commit: Specify the type of commit. It is recommended and can be even more beneficial to have a consistent set of words to describe your changes. Example: Bugfix, Update, Refactor, Bump, and so on. See the section on Conventional Commits below for additional information.
- Length: The first line should ideally be no longer than 50 characters, and the body should be restricted to 72 characters.
- Content: Be direct, try to eliminate filler words and phrases in these sentences (examples: though, maybe, I think, kind of). Think like a journalist.

## Example of good Commit Message
```
fix: fix foo to enable bar

This fixes the broken behavior of the component by doing xyz. 

BREAKING CHANGE
Before this fix foo wasn't enabled at all, behavior changes from <old> to <new>

Closes D2IQ-12345
```

## Comparisons of good and bad Commit Message
Commit Message Comparisons
Review the following messages and see how many of the suggested guidelines they check off in each category.

### Good
```
feat: improve performance with lazy load implementation for images
chore: update npm dependency to latest version
Fix bug preventing users from submitting the subscribe form
Update incorrect client phone number within footer body per client request
```

### Bad
```
fixed bug on landing page
Changed style
oops
I think I fixed it this time?
empty commit messages
```

#### References
- [How to Write Commit Messages that Project Maintainers Will Appreciate by CHRISTINE T. BELZIE @ freecodecamp.org](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/)
- [How to Write Better Git Commit Messages – A Step-By-Step Guide by Natalie Pina @ freecodecamp.org](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)