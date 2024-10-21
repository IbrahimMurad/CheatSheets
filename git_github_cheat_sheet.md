
# Git & GitHub Cheat Sheet

## 1. Basic Git Commands
| Command | Description |
| ------- | ----------- |
| `git init` | Initialize a new Git repository locally |
| `git clone <repo_url>` | Clone a remote repository to your local machine |
| `git status` | Check the current status of your repository (staged, unstaged, untracked files) |
| `git add <file>` | Stage a specific file for commit |
| `git add .` | Stage all changes (new, modified, deleted) in the repository |
| `git commit -m "message"` | Commit staged changes with a message |
| `git log` | View commit history |
| `git diff` | Show changes between working directory and the staging area |
| `git diff --staged` | Show changes between staging area and the last commit |

## 2. Branching & Merging
| Command | Description |
| ------- | ----------- |
| `git branch` | List all branches |
| `git branch <branch_name>` | Create a new branch |
| `git checkout <branch_name>` | Switch to another branch |
| `git checkout -b <branch_name>` | Create a new branch and switch to it |
| `git merge <branch_name>` | Merge the specified branch into the current branch |
| `git branch -d <branch_name>` | Delete a branch locally |
| `git push origin --delete <branch_name>` | Delete a branch remotely |

## 3. Syncing with Remote Repositories
| Command | Description |
| ------- | ----------- |
| `git remote add origin <repo_url>` | Link a local repo to a remote repository |
| `git pull origin <branch_name>` | Fetch and merge changes from the remote branch |
| `git push origin <branch_name>` | Push local changes to the remote branch |
| `git fetch` | Fetch updates from the remote without merging |
| `git remote -v` | View your remote repositories |

## 4. Undoing Changes
| Command | Description |
| ------- | ----------- |
| `git reset <file>` | Unstage a file (remove from staging area) |
| `git checkout -- <file>` | Discard changes in the working directory |
| `git revert <commit_hash>` | Create a new commit that undoes the specified commit |
| `git reset --hard <commit_hash>` | Reset the working directory and staging area to a specific commit (destructive) |

## 5. Stashing Changes
| Command | Description |
| ------- | ----------- |
| `git stash` | Save changes not ready to commit (clean working directory) |
| `git stash apply` | Reapply stashed changes |
| `git stash list` | List stashed changes |
| `git stash drop` | Remove a specific stash from the list |

## 6. Collaborating with GitHub
| Command | Description |
| ------- | ----------- |
| `git fork <repo_url>` | Create a copy of another user’s repository (done on GitHub) |
| `git clone <fork_url>` | Clone your forked repo locally |
| `git remote add upstream <repo_url>` | Add the original repo as the upstream repository |
| `git pull upstream <branch>` | Sync your fork with the original repository |
| `git push origin <branch>` | Push your local changes to your GitHub repository |

## 7. Pull Requests (PRs)
1. **Create a PR**: After pushing your feature branch, go to GitHub, open your repo, and create a pull request from your branch to the `main` (or `develop`) branch.
2. **Describe Your PR**: Add a meaningful title and description, link any related issues, and request a review.
3. **Merge PR**: Once approved, merge the PR on GitHub.

## 8. Viewing Commit History
| Command | Description |
| ------- | ----------- |
| `git log --oneline` | Show a compact view of commit history |
| `git log --graph` | View commits in a graphical tree structure |
| `git log -p` | Show commits and the actual changes made in each commit |
| `git show <commit_hash>` | Show detailed information about a specific commit |

## 9. Resolving Merge Conflicts
| Command | Description |
| ------- | ----------- |
| `git merge <branch_name>` | Start merging the branch |
| (If conflicts occur) | Open the conflicting files and resolve them manually |
| `git add <file>` | Mark conflict resolution as complete |
| `git commit` | Commit the merge after resolving conflicts |

## 10. Tagging Commits
| Command | Description |
| ------- | ----------- |
| `git tag <tag_name>` | Create a tag for a specific commit |
| `git tag -a <tag_name> -m "message"` | Create an annotated tag with a message |
| `git push origin <tag_name>` | Push the tag to the remote repository |
| `git tag -d <tag_name>` | Delete a local tag |
| `git push origin --delete <tag_name>` | Delete a tag remotely |

## 11. Squashing Commits
| Command | Description |
| ------- | ----------- |
| `git rebase -i HEAD~<n>` | Interactively rebase the last `n` commits |
| Mark `pick` as `squash` | Squash commits into one |
| `git push --force` | Push squashed commits (overwrite remote history) |

## 12. Checking Changes
| Command | Description |
| ------- | ----------- |
| `git diff <branch_name>` | View differences between current branch and another branch |
| `git blame <file>` | View who made changes to each line in a file |
| `git show <commit_hash>` | Show detailed information for a specific commit |

