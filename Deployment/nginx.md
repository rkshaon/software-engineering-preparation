# nginx

## nginx Overview
- NGINX (pronounced “engine-x”) is an open-source web server known for its speed, flexibility, and reliability.
- It was created in 2004 by Igor Sysoev to address the C10K problem (simultaneously managing 10,000 client connections).
- NGINX efficiently handles large numbers of simultaneous connections with low memory usage.

## Main Features of NGINX

### Web Server
- NGINX excels in performance and efficiency.
- Unlike other servers that use a thread or process per connection, NGINX uses an event-driven architecture.
- This allows it to serve more clients with fewer resources, making it advantageous for high-traffic sites.

### Reverse Proxy
- NGINX can act as a reverse proxy, forwarding client requests to appropriate backend servers.
- It efficiently distributes traffic, caches content, and provides protection against DDoS attacks.

### Load Balancer
- NGINX offers robust load balancing capabilities.
- It distributes network traffic across multiple servers to optimize resource usage and prevent server overload.

### HTTP Caching
- NGINX can cache HTTP responses locally, improving response times and reducing load on origin servers.

### SSL & TLS Support
- NGINX handles secure communication between clients and servers.
- It can terminate or initiate SSL/TLS connections, offloading processing from application servers.

## Installation Steps (on Ubuntu)

### Install NGINX
Run the following command to install NGINX.
```
sudo apt-get update
sudo apt-get install nginx
```

### Adjust Firewall Rules
If you have a firewall enabled, allow HTTP and HTTPS traffic.
```
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 'Nginx HTTPS'
```

### Check Web Server Status
Confirm that NGINX is running.
```
sudo systemctl status nginx
```

### Set Up Server Blocks (Recommended)
- Configure NGINX to serve multiple websites (server blocks)
    - Create configuration files in `/etc/nginx/sites-available/`.
    - Enable the desired server blocks using symbolic links in `/etc/nginx/sites-enabled/`.