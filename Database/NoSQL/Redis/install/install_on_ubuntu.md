# Install Redis on Ubuntu


#### Update
```
sudo apt update
```
To update local `apt` package cache.

#### Install
```
sudo apt install redis-server
```
To download and install `redis-server`

#### Edit Configuration
```
sudo nano /etc/redis/redis.conf
```
Open on any text editor you want to edit the `redis.conf`, I am here using `nano`, you may use `vim`.

Then inside the file, find the supervised directive.
Change it to systemd (since Ubuntu uses systemd as the init system)

Before
```
supervised no
```

After
```
supervised systemd
```
Then save and close the file.

#### Start the Service
```
sudo systemctl start redis.service
```
To start the service.

```
sudo systemctl restart redis.service
```
To restart the service.

#### Add at Boot
```bash
sudo systemctl enable redis-server
```

This will add on boot.

<!-- ```
sudo systemctl enable redis
```
To start redis on boot. -->

## Test Redis
```
redis-cli ping
```
To test redis-cli if the output is below
```
PONG
```
Then it's fine.

### References
- [Redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)
- [Digitcal Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04)
