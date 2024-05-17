# Install PostgreSQL on Fedora

**Copy the command and execute on terminal.**

```
sudo dnf update
```
updates package lists for latest information.

```
sudo dnf install postgresql-server postgresql-contrib
```
installs PostgreSQL with contrib package which includes additional utilities and extensions for PostgreSQL.

```
sudo systemctl enable postgresql
```
enables PostgreSQL to start at boot.

```
sudo postgresql-setup --initdb --unit postgresql
```
The database needs to be populated with initial data after installation. The database initialization could be done using following command. It creates the configuration files postgresql.conf and pg_hba.conf

```
sudo systemctl start postgresql
```
starts the PostgreSQL service.

## Check version
Excute the command below to get the PostgreSQL version
```
postgres --version
```
or
```
postgres -V
```

## psql shell
```
sudo -u postgres psql
```

[For references](https://docs.fedoraproject.org/en-US/quick-docs/postgresql/)