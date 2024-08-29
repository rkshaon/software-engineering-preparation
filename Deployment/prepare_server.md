# Prepare Server
This guide will walk you through the steps to prepare an Ubuntu server for deploying your application. Follow these steps to ensure your server is ready for production.

## Update and Upgrade the Server
Start by updating the package lists and upgrading the installed packages to the latest versions.

```bash
sudo apt update
sudo apt upgrade -y
```

This ensures that your server is up-to-date with the latest security patches and software versions.

## Install Essential Packages
Install essential packages such as Git, Curl, and other utilities that will be needed.

```bash
sudo apt install -y git curl
```

## Install Node.js and npm
To run your application, you need to install Node.js and npm. Use the following commands to install Node.js version 18.x

```bash
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```

Verify the installation by checking the versions.

```bash
node -v
npm -v
```

## Install Nginx
Nginx will be used to serve your application. Install it using the following command.

```bash
sudo apt install nginx -y
```

After installation, start Nginx and enable it to start at boot.

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Configure the Firewall
Configure the firewall to allow HTTP and HTTPS traffic.

```bash
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

## Obtain Your Server's Public IP Address
You'll need your server's public IP address to configure your domain. You can obtain it with.

```bash
curl ifconfig.me
```

## Clone Your Project Repository
Clone your project from GitHub to your server.

```bash
git clone https://github.com/your-username/your-repository.git /var/www/yourdomain.com
cd /var/www/yourdomain.com
```

## Install Project Dependencies and Build
Navigate to your project directory, install the dependencies, and build the project.

```bash
npm install
npm run build
```

## Configure Nginx to Serve Your Application
Create a new Nginx configuration file for your domain.

```bash
sudo nano /etc/nginx/sites-available/yourdomain.com
```

Add the following content.

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    root /var/www/yourdomain.com/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

Enable the configuration and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/yourdomain.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Secure Your Server with Let's Encrypt SSL
Install Certbot and configure HTTPS for your domain.

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Certbot will handle the SSL certificate installation and renewal.

## Final Steps
Your Ubuntu server is now prepared for deployment. Ensure everything is working correctly by accessing your domain in a web browser. You can further configure the server or set up CI/CD pipelines as needed.
