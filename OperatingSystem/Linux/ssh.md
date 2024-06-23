# SSH

The `ssh` command in Linux is used to securely log into a remote machine and execute commands on it. `SSH` stands for `Secure Shell`, and it uses encryption to secure the connection between the client and the server.

## Basic Syntax
```
ssh [user@]hostname [command]
```

## Common Usage
### Connecting to a Remote Server
```
ssh user@hostname
```

***Note:*** Replace user by `username` of the server and `hostname` by `IP address` or `Domain Name`.

### Running a Command on a Remote Server
```
ssh user@hostname 'command'
```

#### Example
```
ssh user@hostname 'ls -l /var/www'
```

This command lists the contents of the `/var/www` directory on the remote server.

### Specify a Port
```
ssh -p port user@hostname
```

***Note***: This connects to the remote server using a specified port. By default, `SSH uses port 22`.

### Using SSH Key
SSH keys provide a more secure way of logging into a remote server than using a password. To use SSH keys, you need to generate a key pair and place the public key on the server.

```
ssh-keygen
ssh-copy-id user@hostname
ssh user@hostname
```

#### Key Options
- `-i identity_file`: Specifies an identity (private key) file to use for public key authentication.
- `-L [bind_address:]port:host:hostport`: Specifies that the given port on the local (client) host is to be forwarded to the given host and port on the remote side.
- `-R [bind_address:]port:host:hostport`: Specifies that the given port on the remote (server) host is to be forwarded to the given host and port on the local side.
- `-X`: Enables X11 forwarding.
- `-C`: Requests compression of all data.

