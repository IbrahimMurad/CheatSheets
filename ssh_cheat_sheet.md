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

## 12. SSH Configuration Best Practices

### Client Configuration (~/.ssh/config)
```
# Global defaults
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    Compression yes
    
# Production servers
Host prod-*
    User deploy
    IdentityFile ~/.ssh/id_ed25519_prod
    StrictHostKeyChecking yes
    
# Development servers
Host dev-*
    User developer
    IdentityFile ~/.ssh/id_rsa_dev
    # WARNING: Disabling host key checking is a security risk (MITM attacks)
    # Only use for isolated development environments or trusted networks
    # Consider using 'ask' instead: StrictHostKeyChecking ask
    StrictHostKeyChecking no
    
# Specific server example
Host myserver
    HostName example.com
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_custom
    ForwardAgent yes
    LocalForward 8080 localhost:80
```

### Server Configuration (/etc/ssh/sshd_config)
```
# Security best practices
Port 2222                          # Change default port
PermitRootLogin no                 # Disable root login
PasswordAuthentication no          # Force key-based auth
PubkeyAuthentication yes
MaxAuthTries 3
MaxSessions 5
ClientAliveInterval 300
ClientAliveCountMax 2

# Allow specific users only
AllowUsers deploy developer

# Disable dangerous features
X11Forwarding no
PermitEmptyPasswords no
Protocol 2
```

## 13. Advanced SSH Features

### ProxyJump (Jump Host)
```bash
# Connect through jump host
ssh -J jumphost@jump.example.com user@target.example.com

# Multiple jump hosts
ssh -J user1@host1,user2@host2 user3@target

# In config file
Host target
    HostName target.example.com
    ProxyJump jumphost@jump.example.com
```

### SSH Agent Forwarding
```bash
# Enable agent forwarding
ssh -A user@host

# In config
Host myserver
    ForwardAgent yes

# Add keys to agent on login (for macOS)
# Add to ~/.ssh/config:
Host *
    AddKeysToAgent yes
    UseKeychain yes
```

### SSH Escape Sequences
While in an SSH session, type `~` followed by:
- `~.` - Terminate connection
- `~^Z` - Suspend SSH
- `~#` - List forwarded connections
- `~&` - Background SSH (when waiting for connections to terminate)
- `~?` - Display all escape characters

### SOCKS Proxy (Dynamic Port Forwarding)
```bash
# Create SOCKS proxy
ssh -D 8080 user@host

# Configure browser to use localhost:8080 as SOCKS5 proxy
# Now all browser traffic goes through the SSH tunnel
```

### Remote Command Execution
```bash
# Run single command
ssh user@host "ls -la /var/log"

# Run multiple commands
ssh user@host "cd /var/www && git pull && sudo systemctl restart nginx"

# Run local script on remote server
ssh user@host 'bash -s' < local_script.sh

# Pipe local data to remote command
cat data.txt | ssh user@host "cat > remote_file.txt"
```

### SSH Multiplexing (Reuse Connections)
```bash
# In ~/.ssh/config
Host *
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h:%p
    ControlPersist 10m

# First connection creates master
ssh user@host

# Subsequent connections reuse the master (much faster)
ssh user@host
```

## 14. SSH Key Types Comparison

| Key Type | Security | Performance | Compatibility | Recommended |
| -------- | -------- | ----------- | ------------- | ----------- |
| RSA 4096 | High | Moderate | Excellent | Yes (legacy systems) |
| Ed25519 | Very High | Excellent | Good (modern) | Yes (preferred) |
| ECDSA | High | Good | Good | Acceptable |
| RSA 2048 | Moderate | Fast | Excellent | No (use 4096+) |
| DSA | Low | N/A | Deprecated | No |

### When to Use Each Type
- **Ed25519**: Default choice for new keys (fast, secure, small)
- **RSA 4096**: When Ed25519 isn't supported (older systems)
- **ECDSA**: Acceptable alternative, but Ed25519 preferred
- **Avoid**: DSA (deprecated), RSA 1024/2048 (insufficient)

## 15. Security Hardening

### Fail2Ban Integration
```bash
# Install Fail2Ban
sudo apt install fail2ban

# Configure for SSH
# /etc/fail2ban/jail.local
[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
```

### Two-Factor Authentication (2FA)
```bash
# Install Google Authenticator
sudo apt install libpam-google-authenticator

# Setup for user
google-authenticator

# Configure PAM
# /etc/pam.d/sshd
auth required pam_google_authenticator.so

# Configure sshd
# /etc/ssh/sshd_config
ChallengeResponseAuthentication yes
AuthenticationMethods publickey,keyboard-interactive
```

### SSH Certificates (Advanced)
```bash
# Generate CA key
ssh-keygen -t ed25519 -f ca_key

# Sign user key
ssh-keygen -s ca_key -I user_id -n username -V +52w user_key.pub

# Configure server to trust CA
# /etc/ssh/sshd_config
TrustedUserCAKeys /etc/ssh/ca_key.pub
```

## 16. Monitoring and Auditing

### View SSH Login History
```bash
# Last logins
last -a

# Failed login attempts
sudo grep "Failed password" /var/log/auth.log

# Successful logins
sudo grep "Accepted" /var/log/auth.log

# Currently logged in users
w
who
```

### Active SSH Connections
```bash
# View active SSH sessions
netstat -tnpa | grep 'ESTABLISHED.*sshd'

# Or using ss
ss -tnpa | grep 'ESTABLISHED.*sshd'

# Detailed connection info
sudo lsof -i :22

# Kill specific connection (replace 12345 with actual PID)
sudo kill 12345
```

## 17. Performance Optimization

### Compression
```bash
# Enable compression
ssh -C user@host

# In config
Host *
    Compression yes
```

### Cipher Selection
```bash
# Use faster cipher (less secure, use only on trusted networks)
ssh -c aes128-gcm@openssh.com user@host

# In config for fast but secure
Host fastserver
    Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
```

### Keep-Alive Settings
```bash
# Prevent connection timeout
# In ~/.ssh/config
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    TCPKeepAlive yes
```

## 18. Automation and Scripts

### Passwordless Automation
```bash
# SSH without password prompt (keys must be set up)
ssh -o BatchMode=yes user@host "command"

# Run script on multiple servers
for host in server1 server2 server3; do
    ssh user@$host "uptime"
done
```

### Parallel SSH (pssh)
```bash
# Install
sudo apt install pssh

# Run command on multiple hosts
parallel-ssh -h hosts.txt -l user "uptime"

# Copy file to multiple hosts
parallel-scp -h hosts.txt file.txt /remote/path/
```

### Expect Scripts (Handle Interactive Prompts)
```bash
#!/usr/bin/expect
spawn ssh user@host
expect "password:"
send "mypassword\r"
interact
```

## 19. Cross-Platform Considerations

### Windows (OpenSSH Client)
```powershell
# Start SSH Agent (PowerShell as Admin)
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent

# Add key
ssh-add $HOME\.ssh\id_ed25519

# Windows paths in config
# C:\Users\username\.ssh\config
```

### macOS Keychain Integration
```bash
# Add to ~/.ssh/config
Host *
    UseKeychain yes
    AddKeysToAgent yes

# Add key to keychain
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

## 20. Useful SSH Tools and Utilities

### autossh (Auto-Reconnect)
```bash
# Install
sudo apt install autossh

# Auto-reconnect tunnel
autossh -M 0 -f -N -L 8080:localhost:80 user@host

# With monitoring
autossh -M 20000 -f -N -L 8080:localhost:80 user@host
```

### mosh (Mobile Shell)
```bash
# Install
sudo apt install mosh

# Connect (UDP-based, better for mobile/unreliable connections)
mosh user@host

# Survives connection drops and IP changes
```

### sshfs (Mount Remote Filesystem)
```bash
# Install
sudo apt install sshfs

# Mount remote directory
sshfs user@host:/remote/path /local/mount/point

# Unmount
fusermount -u /local/mount/point

# With options
sshfs user@host:/remote/path /local/mount/point -o reconnect,ServerAliveInterval=15
```

### rsync over SSH
```bash
# Sync directory
rsync -avz -e ssh /local/path/ user@host:/remote/path/

# Sync with progress
rsync -avz --progress -e ssh /local/path/ user@host:/remote/path/

# Exclude files
rsync -avz --exclude='*.log' -e ssh /local/path/ user@host:/remote/path/

# Dry run (test without copying)
rsync -avz --dry-run -e ssh /local/path/ user@host:/remote/path/
```