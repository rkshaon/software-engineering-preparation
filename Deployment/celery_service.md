# Celery

## Celery Worker
Navigate to `systemd` directory.
```bash
cd /etc/systemd/system
```

Open a file with service name
```bash
sudo nano celery_worker.service
```

Then copy and paste
```bash
[Unit]
Description=Celery Worker for CRM Service
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/var/www/backend
Environment="PATH=/var/www/backend/env/bin"
ExecStart=/var/www/backend/env/bin/celery -A app.celery worker --loglevel=INFO
Restart=always

[Install]
WantedBy=multi-user.target
```

Then edit if required to update the path.

```bash
# ensure ubuntu user owns project and venv (if appropriate)
sudo chown -R ubuntu:ubuntu /var/www/backend

# create log dir if you plan to use file logging
sudo mkdir -p /var/log/backend
sudo chown ubuntu:ubuntu /var/log/backend

# ensure the pidfile directory is writable if you used --pidfile
sudo touch /var/www/backend/celerybeat.pid
sudo chown ubuntu:ubuntu /var/www/backend/celerybeat.pid
```
(Adjust ownership if you prefer a different user.)

Reload systemd so your new/changed unit is picked 
up:
```bash
sudo systemctl daemon-reload
```

Enable the service so it starts on boot:
```bash
sudo systemctl enable celery_worker.service
```

Start it now:
```bash
sudo systemctl start celery_worker.service
```
or
```bash
sudo systemctl restart celery_worker.service
```

Check status
```bash
```bash
sudo systemctl status celery_worker.service
```

Follow logs in real time (journal):
```bash
sudo journalctl -u celery_worker.service -f
```

## Celery Beat

Navigate to `systemd` directory.
```bash
cd /etc/systemd/system
```

Open a file with service name
```bash
sudo nano celery_beat.service
```

Then copy and paste
```bash
[Unit]
Description=Celery Beat Scheduler for CRM Service
After=network.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
WorkingDirectory=/var/www/backend
Environment="PATH=/var/www/backend/env/bin"
ExecStart=/var/www/backend/env/bin/celery -A app.celery beat --loglevel=INFO
Restart=always

[Install]
WantedBy=multi-user.target
```

Then edit if required to update the path.
```bash
# ensure ubuntu user owns project and venv (if appropriate)
sudo chown -R ubuntu:ubuntu /var/www/backend

# create log dir if you plan to use file logging
sudo mkdir -p /var/log/backend
sudo chown ubuntu:ubuntu /var/log/mie_auth

# ensure the pidfile directory is writable if you used --pidfile
sudo touch /var/www/backend/celerybeat.pid
sudo chown ubuntu:ubuntu /var/www/backend/celerybeat.pid
```
(Adjust ownership if you prefer a different user.)

Reload systemd so your new/changed unit is picked 
up:
```bash
sudo systemctl daemon-reload
```

Enable the service so it starts on boot:
```bash
sudo systemctl enable celery_beat.service
```

Start it now:
```bash
sudo systemctl start celery_beat.service
```
or
```bash
sudo systemctl restart celery_beat.service
```

Check status
```bash
```bash
sudo systemctl status celery_beat.service
```

Follow logs in real time (journal):
```bash
sudo journalctl -u celery_beat.service -f
```
