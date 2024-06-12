# Deploy Frontend on Ubuntu

## Prerequisitions
- [nginx](nginx.md)
- node
- [Git](../git/README.md)

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
Serve you application at HTTP

### default
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