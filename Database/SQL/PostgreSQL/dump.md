# Dump PostgreSQL
The `pg_dump` command is used to create a backup of a **PostgreSQL database**. Here is a basic example of the `pg_dump` command:
```
pg_dump -U username -h hostname -d database_name -f output_file.sql
```

Here,
- `-U username`: The username for the database connection.
- `-h hostname`: The hostname of the database server. If the database is on the same machine, you can omit this or use localhost.
- `-d database_name`: The name of the database you want to dump.
- `-f output_file.sql`: The file where the dump will be saved.

Additionally options,
- -`F c`: Output the dump in the custom format, which can be restored with pg_restore.

Example
```
pg_dump -U myuser -h localhost -d mydatabase -F c -f mydatabase_backup.dump
```
- `-W`: Force pg_dump to prompt for a password before connecting to the database.
- `-n schema`: Dump only schemas matching the specified schema.
- `-t table`: Dump only tables matching the specified table.
- `-v`: Verbose mode. Prints more detailed information about the progress of the dump.

Example
```
pg_dump -U myuser -h localhost -d mydatabase -F c -v -f mydatabase_backup.dump
```

**Note**: Replace `myuser`, `localhost`, `mydatabase`, and `mydatabase_backup.sql` with your actual PostgreSQL `username`, `hostname`, `database name`, and desired output file name.