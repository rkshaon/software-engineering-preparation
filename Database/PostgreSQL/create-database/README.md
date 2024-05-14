# Create Database

## Enter in `psql`
```
sudo -u postgres psql
```

## Create `User` with password
```
CREATE USER username WITH PASSWORD 'your-password';
```
Note: Replace `username` with your database user, and password with `your password`.

## Create `Database` with giving ownership to `User`
```
CREATE DATABASE db-name OWNER username;
```
Note: Replace `db-name` with your project database name and `username` with your dabatase user.

## Grant previleges on database
```
GRANT ALL PRIVILEGES ON DATABASE db-name TO username;
```
Note: Replace `db-name` with your project database name and `username` with your database user.

