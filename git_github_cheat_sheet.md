
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

## 2. Git Configuration

### Configuration Levels
| Command | Description |
| ------- | ----------- |
| `git config --system` | System-wide configuration (all users, all repos) - stored in `/etc/gitconfig` |
| `git config --global` | User-level configuration (all repos for current user) - stored in `~/.gitconfig` |
| `git config --local` | Repository-level configuration (current repo only) - stored in `.git/config` |
| `git config --worktree` | Worktree-level configuration (specific worktree) |

### Basic Configuration
| Command | Description |
| ------- | ----------- |
| `git config --global --list` | lists all the key-values in `.gitconfig` file |
| `git config --global user.name "Your Name"` | Set your name for all commits |
| `git config --global user.email "your@email.com"` | Set your email for all commits |
| `git config --global core.editor "vim"` | Set default text editor (vim, nano, code, etc.) |
| `git config --global init.defaultBranch main` | Set default branch name for new repos (main or master) |

### Viewing Configuration
| Command | Description |
| ------- | ----------- |
| `git config --list` | List all configuration settings |
| `git config --list --show-origin` | Show configuration values with their file locations |
| `git config --global --list` | List only global configuration |
| `git config --local --list` | List only local (repo) configuration |
| `git config user.name` | Get value of a specific setting |
| `git config --get-regexp user.*` | Get all settings matching a pattern |

### Editing Configuration
| Command | Description |
| ------- | ----------- |
| `git config --global --edit` | Open global config file in default editor |
| `git config --local --edit` | Open local config file in default editor |
| `git config --global --unset key` | Remove a configuration key |
| `git config --global --unset-all key` | Remove all occurrences of a key |

### Common Configuration Options

#### User Information
```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
git config --global user.signingkey <gpg-key-id>
```

#### Core Settings
```bash
# Editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"
git config --global core.editor "nano"

# Line endings (important for cross-platform)
git config --global core.autocrlf true    # Windows (convert LF to CRLF on checkout)
git config --global core.autocrlf input   # macOS/Linux (convert CRLF to LF on commit)
git config --global core.autocrlf false   # Don't convert

# Whitespace
git config --global core.whitespace trailing-space,space-before-tab

# File permissions
git config --global core.fileMode false   # Ignore file permission changes

# Pagination
git config --global core.pager 'less -RFX'
git config --global core.pager ''  # Disable pager
```

#### Color Settings
```bash
# Enable colors
git config --global color.ui auto
git config --global color.ui true

# Specific color settings
git config --global color.branch auto
git config --global color.diff auto
git config --global color.status auto
```

#### Merge and Diff Tools
```bash
# Set merge tool
git config --global merge.tool vimdiff
git config --global merge.tool meld
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Set diff tool
git config --global diff.tool vimdiff
git config --global difftool.prompt false
```

#### Push and Pull Behavior
```bash
# Push behavior
git config --global push.default simple      # Push only current branch
git config --global push.default current     # Push current branch to same name
git config --global push.default upstream    # Push to upstream branch
git config --global push.default nothing     # Don't push anything without explicit ref

# Pull behavior (Git 2.27+)
git config --global pull.rebase false  # Merge (default)
git config --global pull.rebase true   # Rebase
git config --global pull.ff only       # Fast-forward only

# Automatically prune deleted branches on fetch
git config --global fetch.prune true
```

#### Credential Management
```bash
# Cache credentials (Linux/macOS)
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'

# Store credentials (Linux/macOS)
git config --global credential.helper store

# Windows credential manager
git config --global credential.helper manager

# macOS keychain
git config --global credential.helper osxkeychain
```

#### Aliases
```bash
# Status shorthand
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# More complex aliases
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all --decorate'
git config --global alias.amend 'commit --amend --no-edit'
git config --global alias.undo 'reset HEAD~1 --mixed'

# Aliases with shell commands (prefix with !)
git config --global alias.count '!git log --oneline | wc -l'
```

#### Commit and GPG Signing
```bash
# Enable commit signing
git config --global commit.gpgsign true
git config --global user.signingkey <your-gpg-key-id>

# Commit template
git config --global commit.template ~/.gitmessage.txt

# Verbose commits (show diff in commit message editor)
git config --global commit.verbose true
```

#### Performance Settings
```bash
# Parallel operations
git config --global checkout.workers 8
git config --global fetch.parallel 8

# Optimize for large repos
git config --global core.preloadIndex true
git config --global core.fscache true  # Windows

# Git garbage collection
git config --global gc.auto 256
git config --global gc.autopacklimit 4
```

#### URL Rewrites (Shortcuts)
```bash
# Rewrite GitHub URLs
git config --global url."https://github.com/".insteadOf "gh:"
git config --global url."git@github.com:".insteadOf "gh:"

# Now you can use: git clone gh:user/repo
```

#### Branch Settings
```bash
# Always show remote tracking info
git config --global branch.autoSetupMerge always

# Automatically rebase on pull for specific branch
git config --local branch.main.rebase true
```

#### Submodule Settings
```bash
# Automatically update submodules
git config --global submodule.recurse true

# Parallel submodule operations
git config --global submodule.fetchJobs 8
```

#### Advanced Settings
```bash
# Rerere (Reuse Recorded Resolution) - remember conflict resolutions
git config --global rerere.enabled true

# Show more context in diffs
git config --global diff.context 5

# Use better diff algorithm
git config --global diff.algorithm histogram

# Show more information in status
git config --global status.showStash true
git config --global status.submoduleSummary true

# Default for new branches
git config --global init.defaultBranch main
```

### Configuration Examples by Use Case

#### For Open Source Contributors
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global pull.rebase true
git config --global fetch.prune true
git config --global diff.colorMoved zebra
```

#### For Team Collaboration
```bash
git config --global user.name "Your Name"
git config --global user.email "work@company.com"
git config --global commit.gpgsign true
git config --global pull.ff only
git config --global push.default current
```

#### For Windows Users
```bash
git config --global core.autocrlf true
git config --global core.fscache true
git config --global credential.helper manager
git config --global core.longpaths true
```

#### For macOS Users
```bash
git config --global core.autocrlf input
git config --global credential.helper osxkeychain
git config --global core.trustctime false
```

#### For Linux Users
```bash
git config --global core.autocrlf input
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
```

### Troubleshooting Configuration

#### View All Settings and Origins
```bash
# See where each config value comes from
git config --list --show-origin --show-scope

# Check specific setting
git config --get user.email

# Check if setting exists
git config --get-regexp user
```

#### Reset Configuration
```bash
# Remove specific setting
git config --global --unset user.name

# Remove all matching settings
git config --global --unset-all core.autocrlf

# Remove entire section
git config --global --remove-section alias
```

#### Import/Export Configuration
```bash
# Export global config
cat ~/.gitconfig

# Backup config
cp ~/.gitconfig ~/.gitconfig.backup

# Import config (copy file)
cp ~/dotfiles/gitconfig ~/.gitconfig
```

## 3. Branching & Merging
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

## 13. Advanced Branching

### Branch Management
| Command | Description |
| ------- | ----------- |
| `git branch -r` | List remote branches |
| `git branch -a` | List all branches (local and remote) |
| `git branch -m <old_name> <new_name>` | Rename a branch |
| `git branch --merged` | List branches merged into current branch |
| `git branch --no-merged` | List branches not yet merged |
| `git push -u origin <branch_name>` | Push branch and set upstream tracking |

### Branch Comparison
```bash
# Show commits in branch A but not in branch B
git log branch_A ^branch_B

# Show files changed between branches
git diff --name-only branch1..branch2

# Show branches containing a specific commit
git branch --contains <commit_hash>
```

## 14. Cherry-Picking and Patching

### Cherry-Pick
| Command | Description |
| ------- | ----------- |
| `git cherry-pick <commit_hash>` | Apply a specific commit to current branch |
| `git cherry-pick <commit1> <commit2>` | Apply multiple commits |
| `git cherry-pick --continue` | Continue after resolving conflicts |
| `git cherry-pick --abort` | Cancel cherry-pick operation |

### Patch Files
```bash
# Create patch file
git format-patch -1 <commit_hash>

# Create patches for last 3 commits
git format-patch -3

# Apply patch
git apply <patch_file>

# Apply patch from email
git am <patch_file>
```

## 15. Searching and Finding

### Search Commands
| Command | Description |
| ------- | ----------- |
| `git grep <pattern>` | Search for text in tracked files |
| `git log -S <string>` | Find commits that added or removed a string |
| `git log -G <regex>` | Find commits matching regex pattern |
| `git log --grep="<pattern>"` | Search commit messages |
| `git log --author="<name>"` | Filter commits by author |
| `git bisect` | Binary search to find bug-introducing commit |

### Git Bisect (Finding Bugs)
```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark a known good commit
git bisect good <commit_hash>

# Mark current as good/bad after testing
git bisect good  # or git bisect bad

# Finish bisect
git bisect reset
```

## 16. Submodules and Subtrees

### Submodules
```bash
# Add submodule
git submodule add <repository_url> <path>

# Initialize submodules after clone
git submodule init
git submodule update

# Clone with submodules
git clone --recursive <repository_url>

# Update all submodules
git submodule update --remote

# Remove submodule
git submodule deinit <path>
git rm <path>
```

### Subtrees
```bash
# Add subtree
git subtree add --prefix=<directory> <repository_url> <branch> --squash

# Pull updates from subtree
git subtree pull --prefix=<directory> <repository_url> <branch> --squash

# Push changes to subtree
git subtree push --prefix=<directory> <repository_url> <branch>
```

## 17. Reflog and Recovery

### Using Reflog
| Command | Description |
| ------- | ----------- |
| `git reflog` | Show history of HEAD movements |
| `git reflog show <branch>` | Show reflog for specific branch |
| `git reset --hard HEAD@{n}` | Reset to a specific reflog entry |
| `git checkout HEAD@{n}` | Checkout a specific reflog state |

### Recovery Commands
```bash
# Recover deleted branch
git reflog
git checkout -b <branch_name> HEAD@{n}

# Recover lost commits
git fsck --lost-found
git show <dangling_commit_hash>

# Undo last reset
git reset --hard HEAD@{1}
```

## 18. Working with Remotes (Advanced)

### Remote Management
| Command | Description |
| ------- | ----------- |
| `git remote show origin` | Show detailed remote information |
| `git remote prune origin` | Remove stale remote-tracking branches |
| `git remote set-url origin <new_url>` | Change remote URL |
| `git remote rename <old> <new>` | Rename remote |
| `git remote remove <name>` | Remove remote |
| `git ls-remote` | List references in remote repository |

### Fetching and Pulling
```bash
# Fetch all remotes
git fetch --all

# Fetch and prune deleted branches
git fetch --prune

# Pull with rebase instead of merge
git pull --rebase

# Pull specific branch
git pull origin <branch_name>
```

## 19. Rewriting History

### Interactive Rebase
```bash
# Start interactive rebase
git rebase -i HEAD~n

# Options in interactive rebase:
# pick   = use commit
# reword = use commit, but edit message
# edit   = use commit, but stop for amending
# squash = use commit, but meld into previous
# fixup  = like squash, but discard message
# drop   = remove commit

# Continue after resolving conflicts
git rebase --continue

# Skip problematic commit
git rebase --skip

# Abort rebase
git rebase --abort
```

### Amending Commits
```bash
# Amend last commit
git commit --amend -m "New message"

# Add files to last commit
git add <file>
git commit --amend --no-edit

# Change author of last commit
git commit --amend --author="Name <email>"
```

### Filter-Branch (Advanced)
```bash
# Remove file from all history
git filter-branch --tree-filter 'rm -f <file>' HEAD

# Change email in all commits
git filter-branch --env-filter '
  if [ "$GIT_COMMITTER_EMAIL" = "old@email.com" ]; then
    export GIT_COMMITTER_EMAIL="new@email.com"
  fi
' HEAD
```

## 20. Git Hooks

Common hooks you can create in `.git/hooks/`:

### Pre-commit Hook Example
```bash
#!/bin/sh
# .git/hooks/pre-commit

# Run tests before commit
npm test
if [ $? -ne 0 ]; then
  echo "Tests failed, commit aborted"
  exit 1
fi
```

### Common Hooks
- `pre-commit` - Run before commit is created
- `prepare-commit-msg` - Edit default commit message
- `commit-msg` - Validate commit message format
- `post-commit` - Run after commit is created
- `pre-push` - Run before push
- `post-merge` - Run after merge

## 21. Git Aliases

### Creating Aliases
```bash
# Short status
git config --global alias.st status

# Pretty log
git config --global alias.lg "log --graph --oneline --all --decorate"

# Undo last commit (keep changes)
git config --global alias.undo "reset HEAD~1 --mixed"

# Show branches with last commit
git config --global alias.br "branch -v"

# Quick commit
git config --global alias.cm "commit -m"
```

### Useful Aliases
```bash
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
git config --global alias.visual "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

## 22. Git Worktrees

### Managing Multiple Working Directories
```bash
# Add new worktree
git worktree add ../hotfix-branch hotfix

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../hotfix-branch

# Prune stale worktree references
git worktree prune
```

## 23. GitHub CLI (gh)

### Installation and Setup
```bash
# Install (macOS)
brew install gh

# Authenticate
gh auth login
```

### Common gh Commands
```bash
# Create repository
gh repo create <repo_name> --public

# Clone repository
gh repo clone <owner>/<repo>

# Create pull request
gh pr create --title "Title" --body "Description"

# List pull requests
gh pr list

# View pull request
gh pr view <number>

# Checkout pull request
gh pr checkout <number>

# Merge pull request
gh pr merge <number>

# Create issue
gh issue create --title "Title" --body "Description"

# View issues
gh issue list

# View repository in browser
gh repo view --web
```

## 24. Best Practices

### Commit Messages
```
Format: <type>(<scope>): <subject>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Formatting, missing semicolons, etc.
- refactor: Code restructuring
- test: Adding tests
- chore: Updating build tasks, package manager

Examples:
feat(auth): add password reset functionality
fix(api): resolve null pointer exception in user endpoint
docs(readme): update installation instructions
```

### Workflow Tips
1. **Commit often** - Small, focused commits
2. **Write clear messages** - Explain why, not what
3. **Pull before push** - Stay in sync with remote
4. **Use branches** - Keep main/master stable
5. **Review before commit** - Use `git diff --staged`
6. **Don't commit secrets** - Use `.gitignore`
7. **Rebase vs Merge** - Rebase for clean history, merge for feature branches

### Security Tips
```bash
# Check for secrets before committing
git diff --staged | grep -i "password\|secret\|key\|token"

# Use .gitignore for sensitive files
echo ".env" >> .gitignore
echo "*.key" >> .gitignore
echo "secrets.yml" >> .gitignore

# Remove committed secrets (⚠️ DANGER: Rewrites history, requires force push)
# WARNING: This is destructive! Only use on repositories you control.
# Consider using git-filter-repo (modern, safer alternative) instead:
# https://github.com/newren/git-filter-repo
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/secret" \
  --prune-empty --tag-name-filter cat -- --all

# After running, you MUST force push (dangerous in shared repos):
# git push --force --all
```

## 25. Troubleshooting

### Common Issues and Solutions

#### Detached HEAD State
```bash
# Create branch from detached HEAD
git checkout -b new-branch-name
```

#### Merge Conflicts
```bash
# View conflicted files
git status

# After manually resolving conflicts
git add <resolved-file>
git commit

# Abort merge
git merge --abort
```

#### Accidentally Committed to Wrong Branch
```bash
# Move commit to correct branch
git log  # Copy commit hash
git checkout correct-branch
git cherry-pick <commit-hash>
git checkout wrong-branch
git reset --hard HEAD~1
```

#### Large Files
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.psd"

# Add .gitattributes
git add .gitattributes
```

#### Undo Public Commits
```bash
# Use revert instead of reset for public commits
git revert <commit-hash>

# Or create a new commit that undoes changes
git revert HEAD
```

