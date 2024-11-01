
# PostgreSQL Commands Cheat Sheet

## 1. Connecting to PostgreSQL
| Command | Description |
| ------- | ----------- |
| `psql -U <username>` | Connect to PostgreSQL using a specific username |
| `psql -h <host> -p <port> -U <username> -d <database>` | Connect to a remote PostgreSQL server and database |
| `\q` | Quit the PostgreSQL command-line interface |

## 2. Basic SQL Operations
| Command | Description |
| ------- | ----------- |
| `CREATE DATABASE <database_name>;` | Create a new database |
| `DROP DATABASE <database_name>;` | Delete an existing database |
| `CREATE TABLE <table_name> (column_name TYPE, ...);` | Create a new table with specified columns and types |
| `DROP TABLE <table_name>;` | Delete a table |
| `INSERT INTO <table_name> (columns) VALUES (values);` | Insert data into a table |
| `SELECT * FROM <table_name>;` | Retrieve all data from a table |
| `UPDATE <table_name> SET column_name = value WHERE condition;` | Update data in a table |
| `DELETE FROM <table_name> WHERE condition;` | Delete specific data from a table |

## 3. User Management
| Command | Description |
| ------- | ----------- |
| `CREATE USER <username> WITH PASSWORD '<password>';` | Create a new user with a password |
| `ALTER USER <username> WITH SUPERUSER;` | Grant superuser privileges to a user |
| `DROP USER <username>;` | Delete a user |
| `GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <username>;` | Grant all privileges on a database to a user |
| `REVOKE ALL PRIVILEGES ON DATABASE <database_name> FROM <username>;` | Revoke all privileges from a user |

## 4. Database and Table Information
| Command | Description |
| ------- | ----------- |
| `\l` | List all databases |
| `\c <database_name>` | Connect to a specific database |
| `\dt` | List all tables in the current database |
| `\d <table_name>` | Show the structure of a specific table |
| `\du` | List all roles/users |
| `\conninfo` | Show connection information |

## 5. Backing Up and Restoring
| Command | Description |
| ------- | ----------- |
| `pg_dump <database_name> > backup.sql` | Back up a database to a file |
| `pg_dump -U <username> -h <host> -F c -b -v -f <output_file> <database_name>` | Perform a custom-format backup |
| `psql <database_name> < backup.sql` | Restore a database from a file |
| `pg_restore -U <username> -d <database_name> < backup_file` | Restore from a custom-format backup |

## 6. Managing Tables and Indexes
| Command | Description |
| ------- | ----------- |
| `CREATE INDEX <index_name> ON <table_name> (column_name);` | Create an index on a table column |
| `DROP INDEX <index_name>;` | Delete an index |
| `ALTER TABLE <table_name> ADD COLUMN <column_name> TYPE;` | Add a new column to a table |
| `ALTER TABLE <table_name> DROP COLUMN <column_name>;` | Remove a column from a table |

## 7. Constraints and Relationships
| Command | Description |
| ------- | ----------- |
| `ALTER TABLE <table_name> ADD CONSTRAINT <constraint_name> UNIQUE (column_name);` | Add a unique constraint |
| `ALTER TABLE <table_name> ADD CONSTRAINT <constraint_name> FOREIGN KEY (column_name) REFERENCES <other_table>(other_column);` | Add a foreign key constraint |
| `ALTER TABLE <table_name> ADD CONSTRAINT <constraint_name> CHECK (condition);` | Add a check constraint |

## 8. Transaction Management
| Command | Description |
| ------- | ----------- |
| `BEGIN;` | Start a new transaction |
| `COMMIT;` | Save changes made during the transaction |
| `ROLLBACK;` | Undo changes made during the transaction |

## 9. Useful Meta-Commands in `psql`
| Command | Description |
| ------- | ----------- |
| `\?` | Show help for `psql` commands |
| `\g` | Execute the current query buffer |
| `\i <file_path>` | Execute commands from a file |
| `\timing` | Toggle timing of queries on or off |
| `\set <variable> <value>` | Set a psql variable |

## 10. Analyzing and Optimizing Queries
| Command | Description |
| ------- | ----------- |
| `EXPLAIN <query>;` | Show the execution plan for a query |
| `EXPLAIN ANALYZE <query>;` | Execute a query and show the execution plan and timing |
| `VACUUM;` | Clean up the database and optimize performance |
| `VACUUM ANALYZE;` | Analyze the database to update statistics for the query planner |

