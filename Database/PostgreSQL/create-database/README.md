# Create Database

## Enter in `psql`
```
sudo -u postgres psql
```

## See `User` list
```
\u
```
Note: This command will return list of the users.

## Create `User` with password
```
CREATE USER username WITH PASSWORD 'your-password';
```
Note: Replace `username` with your database user, and password with `your password`.

## See `Database` list
```
\l
```
Note: This command will return the list of databases.

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

## Connect to database
```
\c database_name;
```
Note: This will enter in your database;

## See tables list
```
\dt
```
Note: This command will return the list of table under the database.