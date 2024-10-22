# Start Redis Instance on the New Port
If you haven't already started a Redis instance on the new port (e.g., 6382), you'll need to do that. You can start Redis on a specific port using a configuration file or directly via the command line.

## Start
```bash
redis-server --port 6382
```

Alternatively, if you have a custom Redis configuration file, use it like this.
```bash
redis-server /path/to/redis_6382.conf
```

## Verify
After starting Redis on the new port, verify it's running using the following command.
```bash
redis-cli -p 6382 ping
```

If Redis is running correctly, it should return `PONG`.


## Service
Now, you will not always run `redis-server --port 6382` command, as you close your terminal, your `Redis Instance on port 6382` will be disable. So you need to run new instance a service, that on reboot your machine have running this new instance of Redis.

### Create a New Configuration File
#### Copy
Execute the command below.
```bash
sudo cp /etc/redis/redis.conf /etc/redis/redis_6382.conf
```

Before copying the `conf` file, you had only one file at `/etc/redis/` directory, named `redis.conf`, after the copy, you have another file named `redis_6382.conf`.

#### Edit
Now, you need to edit the port number of the new `conf` file. Open the file.
```bash
sudo nano /etc/redis/redis_6382.conf
```

Now, find the line with `port` and it is possible to be `port 6379`, update this line into `port 6382`, and make sure `supervised` is `systemd`, means `supervised systemd` then save and exit.

### Create a New Service File
#### Create File
Create a new systemd service file for the Redis instance on port `6382`. You can create a new service file using the command below.
```bash
sudo nano /etc/systemd/system/redis_6382.service
```

#### Add Instructions
Add the following instructions.
```bash
[Unit]
Description=Redis In-Memory Data Store for Port 6382
After=network.target

[Service]
ExecStart=/usr/bin/redis-server /etc/redis/redis_6382.conf
ExecStop=/usr/bin/redis-cli -p 6382 shutdown
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Copy Service File
Or you can copy `redis.service` file. To do so, execute the command below.
```bash
sudo cp /etc/systemd/system/redis.service /etc/systemd/system/redis_6832.service
```
And now need to edit a few lines, first open the file.
```bash
sudo nano /etc/sytemd/system/redis_6832.service
```

Then edit `ExecStart`
```bash
ExecStart=/usr/bin/redis-server /etc/redis/redis_6382.conf --supervised systemd --daemonize no
```

And edit `PIDFile`
```bash
PIDFile=/run/redis/redis-6832.pid
```

And edit `Alias`
```bash
Alias=redis_6832.service
```

Then save and exit.


Make sure `PIDFile` is unique. To do so, open the `redis_6832.conf` file.
```bash
sudo nano /etc/redis/redis_6382.conf
```

And then update `pidfile`
```bash
pidfile /var/run/redis/redis-6382.pid
```

Then save and exit.

#### Reload the daemon
```bash
sudo systemctl daemon-reload
```

#### Enable the Service
```bash
sudo systemctl enable redis_6382
```

#### Start the Service
```bash
sudo systemctl start redis_6382
```

#### Check Status
```bash
sudo systemctl status redis_6382
```

#### Verify
If everything looks good, execute the command to verify.
```bash
redis-cli -p 6382 ping
```

