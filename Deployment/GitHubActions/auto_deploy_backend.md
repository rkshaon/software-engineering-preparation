# Auto Deployment (CI/CD)

## Overview

🚀 Deploying a Python Backend with GitHub Actions and Systemd (Zero-Drama CI/CD)

Modern backend systems must be deployable, repeatable, and safe.
In this guide, we’ll set up GitHub Actions to deploy a Python backend (FastAPI/Django) to a Linux server and restart associated services using systemd.

This approach avoids Docker complexity and works perfectly for traditional VPS deployments.

## 🎯 What We Are Building

A CI/CD pipeline that:

- Triggers on main branch push

- Uploads backend code to the server

- Installs dependencies

- Runs database migrations

- Restarts backend + workers

- Fails fast on errors

## 🧱 Architecture Overview

```bash
GitHub Push → GitHub Actions
               ↓
        SSH to Server
               ↓
     Update Source Code
               ↓
     Install Dependencies
               ↓
       Run Migrations
               ↓
     Restart systemd Services
```

## 🖥️ Server Prerequisites
OS & Packages

- Ubuntu 20.04+

- Python 3.10+

- systemd

- openssh-server

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

## 📁 Backend Directory Structure
```bash
/var/www/backend/
├── app/
├── alembic/
├── requirements.txt
├── alembic.ini
├── venv/
└── .env   (NOT in git)
```

## 🔐 GitHub Secrets Configuration
Add these under

`Repository` → `Settings` → `Secrets` → `Actions`

| Secret           | Purpose             |
| ---------------- | ------------------- |
| `SERVER_HOST`    | Server IP or domain |
| `SERVER_USER`    | SSH username        |
| `SERVER_SSH_KEY` | Private SSH key     |
| `SERVER_PATH`    | `/var/www/backend`  |

***⚠️ Never commit .env or secrets to GitHub***

## 🔁 GitHub Actions Workflow
Create:

📁 `.github/workflows/deploy-backend.yml`

```yml
name: Deploy Backend

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Upload backend
        uses: appleboy/scp-action@v0.1.7
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          source: "."
          target: ${{ secrets.SERVER_PATH }}

      - name: Deploy and restart services
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            set -e

            cd ${{ secrets.SERVER_PATH }}

            source venv/bin/activate

            pip install -r requirements.txt

            alembic upgrade head

            sudo systemctl restart backend-api
            sudo systemctl restart celery-worker

            echo "Deployment successful"
```

## ♻️ Restart vs Reload (Important)
| Action    | When to Use                                 |
| --------- | ------------------------------------------- |
| `restart` | Code changes, dependency changes            |
| `reload`  | Config-only change (Gunicorn supports this) |


## 🔒 Security Hardening
### Passwordless Restart Permission
Execute the command
```bash
sudo visudo
```

Add the below line
```bash
deployuser ALL=(ALL) NOPASSWD:/bin/systemctl restart backend-api
```

## 🧪 Failure Handling

GitHub Actions automatically:

- Stops execution on error

- Shows logs

- Prevents half-deployments

To roll back:

```bash
git reset --hard HEAD~1
sudo systemctl restart backend-api
```

