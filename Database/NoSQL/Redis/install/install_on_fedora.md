# Install Redis on Fedora

**Copy the command and execute on terminal.**

```
sudo dnf install redis
```
Install redis cli and server

```
sudo systemctl start redis
```
Initialize redis server

```
sudo systemctl enable redis
```
To start redis on boot

## Test Redis
To test redis-cli
```
$ redis-cli ping
```
if the output is below
```
PONG
```
Then it's fine.

### [References]
- [Fedora Project](https://developer.fedoraproject.org/tech/database/redis/about.html)