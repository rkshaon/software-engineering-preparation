# Install

## Ubuntu / Debian

### Install
#### Update package list
```bash
sudo apt update
```

#### Install MySQL server
```bash
sudo apt install mysql-server -y
```

#### Verify installation
```bash
mysql --version
```
Expected output: `mysql  Ver 8.0.45-0ubuntu0.24.04.1 for Linux on x86_64 ((Ubuntu))
`

#### Start MySQL
```bash
sudo systemctl start mysql
```

#### Stop MySQL
```bash
sudo systemctl stop mysql
```

#### Restart MySQL
```bash
sudo systemctl restart mysql
```

#### Check status
```bash
sudo systemctl status mysql
```

#### Enable auto-start on boot
```bash
sudo systemctl enable mysql
```

### Secure MySQL Installation
Run the security setup:
```bash
sudo mysql_secure_installation
```

Recommended options:
- Set root password → Yes
- Remove anonymous users → Yes
- Disallow remote root login → Yes
- Remove test database → Yes
- Reload privilege tables → Yes

## CentOS / RHEL

```bash
sudo yum install mysql-server
```

or

```bash
sudo dnf install mysql-server
```

## Windows

Download installer from: [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/).

Install:
- MySQL Server
- MySQL Workbench (recommended GUI)
- MySQL Shell

## macOS

Using Homebrew:

```bash
brew install mysql
```

Start service:
```bash
brew services start mysql
```


## Login to MySQL
### Login as root
```bash
sudo mysql
```

or

```bash
mysql -u root -p
```

## Exit from MySQL
```sql
EXIT();
```
