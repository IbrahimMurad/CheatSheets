
# SSH Usage Cheat Sheet

## 1. Generate SSH Keys
To securely authenticate using SSH, you need to generate a pair of keys (public and private).

| Command | Description |
| ------- | ----------- |
| `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"` | Generate a new SSH key pair with RSA 4096-bit encryption and attach a comment (email) |
| `ssh-keygen -t ed25519 -C "your_email@example.com"` | Generate a new SSH key pair using Ed25519 algorithm (faster and more secure) |
| `eval "$(ssh-agent -s)"` | Start the SSH agent in the background (needed for adding keys to the agent) |
| `ssh-add ~/.ssh/id_rsa` | Add the private SSH key to the SSH agent |

## 2. Copy Public Key to Remote Host
You need to place your public key on the server for passwordless login.

| Command | Description |
| ------- | ----------- |
| `ssh-copy-id user@host` | Copy the public key to the remote host for passwordless SSH login |

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
| `ssh -X user@host` | Enable X11 forwarding (run GUI apps from a remote machine) |
| `ssh-keyscan -t rsa host` | Fetch and print the SSH host key for a remote server |
| `ssh-keygen -R host` | Remove a server's host key from the known_hosts file |

## 10. Exiting SSH Sessions
| Command | Description |
| ------- | ----------- |
| `exit` | Exit the SSH session |
| `~.` | Forcefully exit an SSH session in case it is unresponsive |

