# Auto Deployment (CI/CD)

## Overview

This article uses GitHub Actions to automatically build and deploy a `Vue 3 + TypeScript` frontend application.

## Key Principles

- ✅ Build happens in CI, not on the server

- ✅ Server only serves static files

- ✅ Uses pnpm for dependency management

- ✅ Secure deployment via SSH key

- ✅ Zero manual intervention after setup

## 🧱 Tech Stack

| Layer           | Technology           |
| --------------- | -------------------- |
| Frontend        | Vue 3 + TypeScript   |
| Package Manager | pnpm                 |
| CI/CD           | GitHub Actions       |
| Runtime         | Static files (Nginx) |
| Node Version    | 22.x                 |
| pnpm Version    | 10.x                 |

## 📁 Deployment Flow
```bash
GitHub Repository
   ↓ (push to main)
GitHub Actions
   - Install pnpm
   - Install dependencies
   - Build project
   ↓
dist/
   ↓ (SCP over SSH)
Server (/var/www/your-app)
   ↓
Nginx serves static files
```

⚠️ No source code is pulled to the server

⚠️ No build happens on the server

## 🔐 SSH Authentication Setup (One-Time)

### 1. Generate SSH Key (Local Machine)

```bash
ssh-keygen -t ed25519 -C "github-deploy"
```

- File: ~/.ssh/github_deploy

- Passphrase: leave empty

### 2. Add Public Key to Server

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

Paste contents of:

```bash
cat ~/.ssh/github_deploy.pub
```

Then:
```bash
chmod 600 ~/.ssh/authorized_keys
```

### 3. Add Private Key to GitHub Secrets

`GitHub` → `Repository` → `Settings` → `Secrets` → `Actions`

| Secret Name      | Description                        |
| ---------------- | ---------------------------------- |
| `SERVER_HOST`    | Server IP / domain                 |
| `SERVER_USER`    | Deploy user                        |
| `SERVER_SSH_KEY` | **Private SSH key (full content)** |

⚠️ Must include:
```bash
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
```

## ⚙️ GitHub Actions Workflow

File: `.github/workflows/deploy.yml`

```yaml
name: Deploy Vue App

on:
  push:
    branches:
      - main # update branch if needed

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 10   # update version if needed
          run_install: false

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22  # update version if needed
          cache: pnpm

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Build project
        run: pnpm build

      - name: Deploy dist to server
        uses: appleboy/scp-action@v0.1.7
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          source: "dist/*"
          target: "/var/www/your-app"   # update directory if needed
```

## 🖥️ Server Configuration

### Directory Setup

```bash
sudo mkdir -p /var/www/your-app
sudo chown -R deploy:deploy /var/www/your-app
```

### Nginx Configuration

Open the `nginx` file.
```bash
nano /etc/nginx/sites-available/domain_name
```

I prefer keep the `nginx` file name based on the `domain name`.

Update the file according to below:

```bash
server {
    listen 80;
    server_name yourdomain.com;

    root /var/www/your-app;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

Check `nginx configuration`.
```bash
sudo nginx -t
```
The command should response like below:
```bash
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Create a `symbolic link (symlink)` for an Nginx site configuration
```bash
sudo ln -s /etc/nginx/sites-available/file_name /etc/nginx/sites-enabled 
```

Restart `nginx service`
```bash
sudo systemctl reload nginx.service
```

## 🚀 Deployment Process

1. Push code to `main`

2. `GitHub Actions` triggers automatically

3. Vue app is built in CI

4. Only `dist/` files are uploaded

5. Nginx serves updated frontend


***⏱️ Typical deployment time: < 1 minute***

## 🧠 Why This Approach

- ✔ Deterministic builds

- ✔ Faster deployments

- ✔ No server CPU/RAM spikes

- ✔ Secure (no credentials on server)

- ✔ Easy rollback

- ✔ Production-grade workflow

## 🔄 Rollback Strategy (Manual)
To rollback, redeploy a previous commit:
```bash
git revert <commit>
git push origin main
```
Or rerun an earlier GitHub Actions workflow.

## 🚫 Anti-Patterns Avoided

- ❌ Building on the server

- ❌ SSH + git pull in production

- ❌ Installing Node/pnpm on server runtime

- ❌ Deploying as root

## 🧩 Possible Enhancements (Future)

- Atomic deployments (releases/ + symlink)

- Zero-downtime rollback

- Separate environments (dev / staging / prod)

- CDN (Cloudflare)

- Deployment notifications

