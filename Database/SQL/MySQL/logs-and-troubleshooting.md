# Logs and Troubleshooting
## View MySQL logs
```bash
sudo journalctl -u mysql
```

or
```bash
sudo tail -f /var/log/mysql/error.log
```

## Check if port is running
```bash
sudo ss -tulnp | grep 3306
```
