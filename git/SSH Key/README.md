# SSH Keys

SSH keys are essential for secure communication between your local machine and the remote Git server.

## Generate an SSH Key
- Open the terminal (Git Bash, Command Prompt, or Terminal).
- Run the following command to generate an SSH key.

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

replace `your_email@example.com` with your `actual email address`.

- This will create a pair of files: id_ed25519 (private key) and id_ed25519.pub (public key).

## Locate Your SSH Key Files
- By default, SSH keys are stored in the ~/.ssh directory.
- Check if you already have an SSH key by navigating to that directory:

```
cd ~/.ssh
ls
```

- Look for files named `id_rsa` or `id_ed25519` (private key) and their corresponding `.pub` files (public key).

## Send Public Key to Git Account
- Open the `id_ed25519.pub` file (use any text editor) and copy its contents.
```
/
```
- Go to your GitHub/GitLab/other account settings.
- Go to `"SSH Key"` option.
- Click `“New SSH key”` and paste your public key there.
- Save the changes.

## Importance of SSH Key
1. Security:
- SSH keys provide a more secure way to authenticate with remote servers compared to passwords.
- Passwords can be intercepted or guessed, but SSH keys are much harder to compromise.
- The private key remains on your local machine, while the public key is shared with the server.
2. Authentication:
- When you connect to a remote server (like GitHub), the server verifies your identity using your SSH key.
- If the server recognizes your public key, it allows you access without requiring a password.
3. Automation and Scripting:
- SSH keys enable automated processes (e.g., deploying code, running scripts) without manual intervention.
- Tools like Git, SCP, and rsync can use SSH keys for secure communication.
4. Ease of Use:
- Once set up, SSH keys allow seamless access to remote servers without typing passwords repeatedly.
- They simplify the authentication process for developers.
5. Multiple Accounts:
- You can associate different SSH keys with different services or accounts.
- This flexibility allows you to manage access to various platforms securely.

### [References](references.md)