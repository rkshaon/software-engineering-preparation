# Deploy Frontend on Ubuntu

## Prerequisitions
- [nginx](nginx.md)
- node
- [Git](../git/README.md)
- CertBot (for SSL certification)

## Prepare Ubuntu Server
Update the package list
```
sudo apt-get update
```

Install Node.js and npm
```
sudo apt-get install -y nodejs npm
```

Install build-essential package (optional but recommended for building native addons)
```
sudo apt-get install -y build-essential
```

## Pull `Node.js` applicaton
Prefered directory to pull the application is `/var/www/`

Change directory
```
sudo cd /var/www/
```
Create a new directory
```
sudo mkdir app_name
```
Change directory
```
sudo cd app_name
```
Git initialize
```
sudo git init
```
Git add origin
```
sudo git remote add origin `your-repo-link.git`
```
Git pull
```
sudo git pull origin branch_name
```

Consider you have build version of your `Node.js` application.

## `nginx` configuration for Node.js application
### Serve at HTTP

#### default
Open the `default` file.

Using `nano`
```
sudo nano /etc/nginx/sites-available/default
```
Using `vim`
```
sudo vi /etc/nginx/sites-available/default
```

Replace the contents with below
```
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/app_name/dist;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files $uri $uri/ =404;
	}
}
```
Here, considered `Node.js` application's build is deploying.

### domain_name.com

There will be no file under `domain_name.com`.

Execute the command below.
```
sudo vi /etc/nginx/sites-available/domain_name.com
```
This will automatically create the configuration file if file does not exist, if file exist then it will open the file.

Replace the contents with below.
```
server {
    listen 80;
    server_name domain_name.com;
    root /var/www/app_name/dist;
    index index.html index.htm;

    access_log /var/log/nginx/domain_name.com.log;
    error_log /var/log/nginx/domain_name.com.error.log;

    keepalive_timeout 60;

    proxy_buffers 16 64k;
    proxy_buffer_size 128k;

    location / {
        include /etc/nginx/mime.types;
        try_files $uri $uri/ /index.html?/$request_uri;
    }
}
```
Here, considered `Node.js` application's build is deploying.

### Server as HTTPS
You need cert bot.

Install certbot from snap
```
sudo snap install --classic certbot
```

After installing `certbot` you need to generate SSL certificate.

#### default
Execute the command below.
```
sudo certbot --nginx
```

#### domain_name.com
Execute the command below.

```
sudo certbot --nginx -d domain_name.com
```
This will generate SSL certification and update `nginx` configuration file according to certification.
