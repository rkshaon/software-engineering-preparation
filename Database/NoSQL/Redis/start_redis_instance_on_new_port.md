# Start Redist Instance on the New Port
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
