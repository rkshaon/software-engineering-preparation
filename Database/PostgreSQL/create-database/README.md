# Create Database

## Enter in `psql`
```
sudo -u postgres psql
```

## Create `User`
```
CREATE USER username WITH PASSWORD 'your-password';
```

## Create `Database` with giving ownership to `User`
```
CREATE DATABASE db-name OWNER username;
```

