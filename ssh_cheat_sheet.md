# SSH Usage Cheat Sheet

## 1. Generate SSH Keys
To securely authenticate using SSH, you need to generate a pair of keys (public and private).

| Command | Description |
| ------- | ----------- |
| `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"` | Generate a new SSH key pair with RSA 4096-bit encryption and attach a comment (email) |
| `ssh-keygen -t ed25519 -C "your_email@example.com"` | Generate a new SSH key pair using Ed25519 algorithm (faster and more secure) |
| `eval "$(ssh-agent -s)"` | Start the SSH agent in the background (needed for adding keys to the agent) |
| `ssh-add ~/.ssh/id_rsa` | Add the private RSA key to the SSH agent |
| `ssh-add ~/.ssh/id_ed25519` | Add the private Ed25519 key to the SSH agent |

## 2. Copy Public Key to Remote Host
You need to place your public key on the remote server in the `~/.ssh/authorized_keys` file for passwordless login.

### Method 1: Using `ssh-copy-id` (If Password is Available)
If you have the remote user's password, this is the easiest and recommended method:

| Command | Description |
| ------- | ----------- |
| `ssh-copy-id user@host` | Copy the default public key to the remote host for passwordless SSH login |
| `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host` | Copy a specific public key to the remote host |

**Note:** You'll be prompted for the remote user's password once. After successful authentication, your public key will be automatically added to `~/.ssh/authorized_keys` on the remote server with correct permissions.

### Method 2: Manual Copy (If Password is Not Available)
If password authentication is disabled, or you don't have the password but have alternative access (console access, root access, another user, etc.), you need to copy the key manually:

**Step 1:** On your local machine, display your public key:
```bash
cat ~/.ssh/id_rsa.pub
# or for Ed25519
cat ~/.ssh/id_ed25519.pub
```

**Step 2:** Copy the entire output (it's a single long line starting with `ssh-rsa` or `ssh-ed25519`)

**Step 3:** On the remote server, as the target user, run:
```bash
# Create .ssh directory if it doesn't exist
mkdir -p ~/.ssh

# Add your public key to authorized_keys (paste your key after the echo command)
echo "paste-your-public-key-here" >> ~/.ssh/authorized_keys

# Set correct permissions (CRITICAL - SSH won't work without these!)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

**Step 4:** Verify the key was added correctly:
```bash
cat ~/.ssh/authorized_keys
```

### Understanding authorized_keys
- **Location:** `~/.ssh/authorized_keys` on the remote server (in the target user's home directory)
- **Format:** One public key per line
- **Multiple keys:** You can add multiple public keys (from different machines) - each on its own line
- **Comments:** The comment at the end of each key (usually an email) helps identify which machine/user the key belongs to
- **Security:** The file must have `600` permissions and the `.ssh` directory must have `700` permissions.

## 3. Connecting to a Remote Server
To remotely connect to a server using SSH, use the following commands.

| Command | Description |
| ------- | ----------- |
| `ssh user@host` | Connect to a remote server using default SSH settings |
| `ssh user@host -p <port>` | Connect to a remote server on a non-default port |
| `ssh -i ~/.ssh/id_rsa user@host` | Connect using a specific private key |
| `ssh -L local_port:remote_host:remote_port user@host` | Create an SSH tunnel with port forwarding |
| `ssh -R remote_port:localhost:local_port user@host` | Reverse port forwarding from the remote server |

## 4. Managing SSH Configurations
To simplify and manage multiple connections, you can configure the `~/.ssh/config` file.

### Example `~/.ssh/config`:
```
Host myserver
    HostName example.com
    User myuser
    Port 22
    IdentityFile ~/.ssh/id_rsa

Host production
    HostName 192.168.1.100
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

| Command | Description |
| ------- | ----------- |
| `ssh myserver` | Use the shorthand defined in the SSH config file to connect to the server |

## 5. Copying Files via SCP
SCP (Secure Copy Protocol) allows you to copy files to and from a remote server over SSH.

| Command | Description |
| ------- | ----------- |
| `scp file.txt user@host:/remote/directory/` | Copy a file from your local machine to a remote server |
| `scp user@host:/remote/file.txt /local/directory/` | Copy a file from a remote server to your local machine |
| `scp -r directory user@host:/remote/directory/` | Recursively copy a directory from your local machine to a remote server |
| `scp -P <port> file.txt user@host:/remote/directory/` | Copy a file using a non-default SSH port (note: uppercase -P) |

## 6. SSH Tunneling (Port Forwarding)
SSH tunneling forwards local network traffic securely through SSH to a remote server.

| Command | Description |
| ------- | ----------- |
| `ssh -L local_port:remote_host:remote_port user@host` | Forward traffic from a local port to a remote server |
| `ssh -D local_port user@host` | Set up a dynamic SOCKS proxy on the local machine via SSH |
| `ssh -R remote_port:localhost:local_port user@host` | Reverse tunnel, forward a remote port to a local port |

## 7. Transferring Files via SFTP
SFTP (SSH File Transfer Protocol) allows file transfer over an SSH connection.

| Command | Description |
| ------- | ----------- |
| `sftp user@host` | Start an SFTP session with a remote server |
| `put file.txt` | Upload a file to the remote server in an SFTP session |
| `get file.txt` | Download a file from the remote server in an SFTP session |
| `ls` | List files on the remote server |
| `lcd /local/path` | Change local directory |
| `cd /remote/path` | Change remote directory |
| `exit` | Exit the SFTP session |

## 8. Managing Remote Processes
SSH allows you to run commands and manage processes on remote servers.

| Command | Description |
| ------- | ----------- |
| `ssh user@host "command"` | Run a command on the remote server (e.g., `ssh user@host "uptime"`) |
| `ssh user@host -f "command"` | Run a command in the background on the remote server |
| `ssh user@host -t "command"` | Force pseudo-terminal allocation (useful for interactive commands like `top`) |

## 9. Security and Debugging
| Command | Description |
| ------- | ----------- |
| `ssh -v user@host` | Verbose mode, output detailed debugging information |
| `ssh -vvv user@host` | Extra verbose mode for detailed troubleshooting |
| `ssh -X user@host` | Enable X11 forwarding (run GUI apps from a remote machine) |
| `ssh-keyscan -t rsa host` | Fetch and print the SSH host key for a remote server |
| `ssh-keygen -R host` | Remove a server's host key from the known_hosts file |

## 10. Troubleshooting SSH Key Authentication

### Common Issues When SSH Still Asks for Password

If you've copied your public key but SSH still prompts for a password, check these common issues:

#### 1. SSH Agent Not Running or Key Not Loaded
```bash
# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your private key
ssh-add ~/.ssh/id_rsa
# or for Ed25519
ssh-add ~/.ssh/id_ed25519

# Verify keys are loaded
ssh-add -l
```

#### 2. Incorrect File Permissions
SSH is strict about permissions for security reasons.

**On the remote server:**
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 755 ~  # Home directory should not be writable by group/others
```

**On your local machine:**
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa  # or id_ed25519
chmod 644 ~/.ssh/id_rsa.pub  # or id_ed25519.pub
```

#### 3. Wrong Key Being Used
```bash
# Specify which key to use
ssh -i ~/.ssh/id_ed25519 user@host
```

#### 4. Server Configuration Issues
Check `/etc/ssh/sshd_config` on the remote server:
```bash
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
PasswordAuthentication yes  # Can be set to 'no' after key auth works
```

After changing sshd_config, restart SSH:
```bash
sudo systemctl restart sshd
# or on some systems
sudo service ssh restart
```

#### 5. SELinux Context Issues (Linux)
On servers with SELinux enabled:
```bash
restorecon -R -v ~/.ssh
```

#### 6. Debug the Connection
Use verbose mode to see exactly where authentication fails:
```bash
ssh -v user@host
# or for more detail
ssh -vvv user@host
```

Look for messages like:
- `debug1: Offering public key` - Your key is being sent
- `debug1: Authentication succeeded` - Success!
- `debug1: No more authentication methods to try` - Key wasn't accepted

#### 7. Verify Key is on Server
On the remote server, check if your key is present:
```bash
cat ~/.ssh/authorized_keys
```
Your public key should be there as a single line.

## 11. Exiting SSH Sessions
| Command | Description |
| ------- | ----------- |
| `exit` | Exit the SSH session |
| `~.` | Forcefully exit an SSH session in case it is unresponsive |
| `Ctrl+D` | Alternative way to exit an SSH session |