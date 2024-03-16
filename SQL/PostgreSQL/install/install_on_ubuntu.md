# Install PostgreSQL on Ubuntu

**Copy the command and execute on terminal.**


```
sudo apt update
```
updates package lists for latest information.

```
sudo apt install postgresql postgresql-contrib
```
installs PostgreSQL with contrib package which includes additional utilities and extensions for PostgreSQL.

```
sudo systemctl start postgresql.service
```
starts the PostgreSQL service.

```
sudo systemctl enable postgresql.service
```
enables PostgreSQL to start at boot.
