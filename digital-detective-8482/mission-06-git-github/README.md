# Mission 06 — Git and GitHub

## 1. Task / objective

Understand version control, practise the basic Git workflow, create a branch, open a Pull Request and explain how GitHub supports collaboration.

## 2. Work completed

### Task 6.1 — Basic Git workflow

| Git operation | Command | What it does |
|---|---|---|
| Check repository status | `git status` | Shows changed, staged and untracked files. |
| Stage selected changes | `git add path/to/file` | Selects a file's current changes for the next commit. |
| Create a commit | `git commit -m "message"` | Saves the staged snapshot in the local repository history. |
| View commit history | `git log --oneline` | Displays recent commits in a compact format. |

Staging and committing are not the same. Staging chooses which changes will be included in the next snapshot. Committing records those staged changes in the local Git history with a message.

### Task 6.2 — Branch activity

The assignment asks for a branch named `update-about` and a section titled **My Learning** in the root README. Perform this activity after creating the GitHub repository:

```bash
git switch -c update-about
```

Add a short `## My Learning` section to the root README. For example, write two or three points that are genuinely true for you, such as what you learned about Terminal commands, the difference between staging and committing, or number conversion. Then run:

```bash
git status
git add README.md
git commit -m "Add my learning notes to README"
git push -u origin update-about
```

If the branch already exists locally, use `git switch update-about` instead of creating it again.

### Task 6.3 — Pull Request

1. Open the repository on GitHub.
2. Use the comparison prompt for `update-about` and `main` (the default branch may have another name if configured differently).
3. Create a Pull Request from `update-about` into `main`.
4. Describe the README update in the PR description.
5. Review the changed file. Merge only if the instructor asks for it.
6. Record whether the PR is open or merged. If it is merged, update the local main branch:

```bash
git switch main
git pull origin main
```

### Task 6.4 — Git command glossary

| Operation | Command | Explanation |
|---|---|---|
| Initialise repository | `git init` | Starts Git tracking in the current folder. |
| Check status | `git status` | Shows the state of the working folder and staging area. |
| Stage changes | `git add` | Selects changes for the next commit. |
| Commit changes | `git commit` | Records staged changes in local history. |
| View history | `git log` | Shows earlier commits. |
| Create / list branches | `git branch` | Lists branches; `git branch name` creates one. |
| Switch branches | `git switch name` | Moves the working folder to another branch. |
| Publish changes | `git push` | Sends local commits to the remote repository. |
| Retrieve remote changes | `git pull` | Fetches and integrates changes from the remote branch. |

A branch is a separate line of work. It lets me make changes without immediately changing the main version. A Pull Request asks for those changes to be reviewed and potentially merged. This is useful when several people contribute to the same project.

## 3. Commands / tools used

`git init`, `git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git push` and `git pull`; GitHub's Pull Request page in a browser.

## 4. My understanding

Git records the history of a project locally, while GitHub hosts a remote copy and provides tools for collaboration. A commit is a saved point in the history. A branch gives a separate place to work, and a Pull Request makes it possible to review those changes before merging them.

## 5. Difficulties faced

[Record actual Git or GitHub errors, such as an incorrect remote URL, an authentication prompt or a branch-name mismatch. Do not claim the PR exists until it does.]

## 6. How I resolved them

[Write the actual fix. For example, verify the remote with `git remote -v` or check the branch with `git branch`.]

## 7. Evidence / files

- This README
- Root README's `My Learning` section after you add it on the branch
- GitHub branch and Pull Request links or privacy-safe screenshots

## 8. Commit details

Suggested commit message: `Complete Git and GitHub collaboration mission`

**Branch:** [Record the branch URL after publishing.]  
**Pull Request:** [Paste the PR URL and record Open / Merged.]  
**Mission commit:** [Add the actual commit ID or link after pushing.]
