# Install Redis on Ubuntu

**Copy the command and execute on your terminal**

```
sudo apt update
```
To update local `apt` package cache.

```
sudo apt install redis-server
```
To download and install `redis-server`

```
sudo nano /etc/redis/redis.conf
```
Open on any text editor you want to edit the `redis.conf`, I am here using `nano`, you may use `vim`.

Then inside the file, find the supervised directive.
Change it to systemd (since Ubuntu uses systemd as the init system)
```
supervised systemd
```
Then save and close the file.

```
sudo systemctl restart redis.service
```
To restart the service.

<!-- ```
sudo systemctl enable redis
```
To start redis on boot. -->

## Test Redis
```
$ redis-cli ping
```
To test redis-cli if the output is below
```
PONG
```
Then it's fine.

### References
- [Redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)
- [Digitcal Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04)