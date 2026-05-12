# Remote Access
## Configuration
### Edit MySQL config
```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Find:
```text
bind-address = 127.0.0.1
```

Change to:
```text
bind-address = 0.0.0.0
```

Restart MySQL:
```bash
sudo systemctl restart mysql
```

### Open firewall port
```bash
sudo ufw allow 3306
```
