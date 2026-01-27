
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
| `ANALYZE <table_name>;` | Update statistics for a specific table |
| `REINDEX TABLE <table_name>;` | Rebuild indexes on a table |
| `REINDEX DATABASE <database_name>;` | Rebuild all indexes in a database |

## 11. Advanced Query Techniques

### Window Functions
```sql
-- Rank rows within partitions
SELECT 
  employee_name, 
  department,
  salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
FROM employees;

-- Running totals
SELECT 
  date, 
  amount,
  SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;

-- Moving averages
SELECT 
  date,
  value,
  AVG(value) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg_7d
FROM metrics;
```

### Common Table Expressions (CTEs)
```sql
-- Basic CTE
WITH high_earners AS (
  SELECT * FROM employees WHERE salary > 100000
)
SELECT department, COUNT(*) FROM high_earners GROUP BY department;

-- Recursive CTE (organizational hierarchy)
WITH RECURSIVE employee_hierarchy AS (
  SELECT id, name, manager_id, 1 as level
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, eh.level + 1
  FROM employees e
  JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy ORDER BY level;
```

### JSON Operations
```sql
-- Query JSON data
SELECT data->>'name' as name FROM users WHERE data->>'age' > '25';

-- JSON aggregation
SELECT jsonb_agg(name) FROM products;

-- JSON path queries
SELECT * FROM documents WHERE data @> '{"status": "active"}';
```

## 12. Data Types and Functions

### String Functions
| Function | Description |
| -------- | ----------- |
| `CONCAT(str1, str2, ...)` | Concatenate strings |
| `SUBSTRING(string FROM start FOR length)` | Extract substring |
| `UPPER(string)` / `LOWER(string)` | Convert case |
| `TRIM(string)` | Remove leading/trailing spaces |
| `LENGTH(string)` | Get string length |
| `REPLACE(string, from, to)` | Replace substring |
| `SPLIT_PART(string, delimiter, field)` | Split string and get part |
| `REGEXP_MATCHES(string, pattern)` | Match regular expression |

### Date/Time Functions
| Function | Description |
| -------- | ----------- |
| `NOW()` / `CURRENT_TIMESTAMP` | Get current timestamp |
| `CURRENT_DATE` | Get current date |
| `AGE(timestamp)` | Calculate age from timestamp |
| `DATE_TRUNC('month', timestamp)` | Truncate to specified precision |
| `EXTRACT(YEAR FROM timestamp)` | Extract date/time component |
| `timestamp + INTERVAL '1 day'` | Add interval to timestamp |
| `GENERATE_SERIES(start, stop, interval)` | Generate series of timestamps |

### Aggregate Functions (Advanced)
| Function | Description |
| -------- | ----------- |
| `STRING_AGG(column, delimiter)` | Concatenate values with delimiter |
| `ARRAY_AGG(column)` | Aggregate values into array |
| `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY column)` | Calculate median |
| `MODE() WITHIN GROUP (ORDER BY column)` | Find most common value |
| `COUNT(DISTINCT column)` | Count distinct values |
| `FILTER (WHERE condition)` | Conditional aggregation |

## 13. Full-Text Search
```sql
-- Create full-text search column
ALTER TABLE articles ADD COLUMN search_vector tsvector;

-- Update search vector
UPDATE articles SET search_vector = 
  to_tsvector('english', title || ' ' || body);

-- Create GIN index for performance
CREATE INDEX search_idx ON articles USING GIN(search_vector);

-- Search
SELECT * FROM articles 
WHERE search_vector @@ to_tsquery('english', 'postgres & performance');

-- Ranked search
SELECT *, ts_rank(search_vector, query) AS rank
FROM articles, to_tsquery('english', 'database') query
WHERE search_vector @@ query
ORDER BY rank DESC;
```

## 14. Partitioning

### Range Partitioning
```sql
-- Create partitioned table
CREATE TABLE measurements (
  id SERIAL,
  date DATE NOT NULL,
  value NUMERIC
) PARTITION BY RANGE (date);

-- Create partitions
CREATE TABLE measurements_2024_01 PARTITION OF measurements
  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE measurements_2024_02 PARTITION OF measurements
  FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

### List Partitioning
```sql
CREATE TABLE orders (
  id SERIAL,
  region TEXT,
  amount NUMERIC
) PARTITION BY LIST (region);

CREATE TABLE orders_north PARTITION OF orders
  FOR VALUES IN ('North', 'Northeast');
```

## 15. Views and Materialized Views

### Regular Views
```sql
-- Create view
CREATE VIEW active_users AS
  SELECT * FROM users WHERE status = 'active';

-- Create or replace view
CREATE OR REPLACE VIEW user_summary AS
  SELECT user_id, COUNT(*) as order_count, SUM(amount) as total_spent
  FROM orders GROUP BY user_id;

-- Drop view
DROP VIEW active_users;
```

### Materialized Views
```sql
-- Create materialized view (stores results)
CREATE MATERIALIZED VIEW daily_sales AS
  SELECT date, SUM(amount) as total
  FROM sales
  GROUP BY date;

-- Refresh materialized view
REFRESH MATERIALIZED VIEW daily_sales;

-- Create index on materialized view
CREATE INDEX ON daily_sales(date);
```

## 16. Triggers and Functions

### Creating Functions
```sql
-- Simple function
CREATE OR REPLACE FUNCTION get_full_name(first_name TEXT, last_name TEXT)
RETURNS TEXT AS $$
BEGIN
  RETURN first_name || ' ' || last_name;
END;
$$ LANGUAGE plpgsql;

-- Function with table return
CREATE OR REPLACE FUNCTION get_high_earners(min_salary NUMERIC)
RETURNS TABLE(name TEXT, salary NUMERIC) AS $$
BEGIN
  RETURN QUERY
  SELECT employee_name, employee_salary
  FROM employees
  WHERE employee_salary > min_salary;
END;
$$ LANGUAGE plpgsql;
```

### Creating Triggers
```sql
-- Create trigger function
CREATE OR REPLACE FUNCTION update_modified_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.modified_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_modified_timestamp();
```

## 17. Security and Permissions

### Row Level Security (RLS)
```sql
-- Enable RLS
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Create policy
CREATE POLICY user_documents ON documents
  FOR ALL TO public
  USING (user_id = current_user_id());

-- Create policy for SELECT only
CREATE POLICY read_own_data ON sensitive_data
  FOR SELECT TO regular_user
  USING (owner = current_user);
```

### Advanced Permissions
```sql
-- Grant specific column permissions
GRANT SELECT (id, name) ON users TO readonly_user;

-- Grant execute on function
GRANT EXECUTE ON FUNCTION calculate_bonus() TO manager_role;

-- Grant usage on schema
GRANT USAGE ON SCHEMA analytics TO analyst_role;
GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO analyst_role;

-- Set default privileges
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO readonly_user;
```

## 18. Performance and Maintenance

### Index Types and Usage
```sql
-- B-tree index (default)
CREATE INDEX idx_name ON users(last_name);

-- Partial index (for specific conditions)
CREATE INDEX idx_active ON users(email) WHERE status = 'active';

-- Unique index
CREATE UNIQUE INDEX idx_email ON users(email);

-- Multi-column index
CREATE INDEX idx_name_date ON orders(customer_id, order_date);

-- GIN index (for arrays, JSONB, full-text)
CREATE INDEX idx_tags ON posts USING GIN(tags);

-- BRIN index (for large sequential data)
CREATE INDEX idx_timestamp ON logs USING BRIN(created_at);
```

### Connection and Session Management
```sql
-- Show active connections
SELECT * FROM pg_stat_activity;

-- Terminate connection by PID (replace 12345 with actual process ID)
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE pid = 12345;
```

### Database and Table Sizes
```sql
-- Show database size
SELECT pg_database_size('<database_name>');

-- Show table sizes
SELECT 
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

### Lock Monitoring
```sql
-- View locks
SELECT * FROM pg_locks;

-- View blocking queries
SELECT 
  blocked.pid AS blocked_pid,
  blocked.usename AS blocked_user,
  blocking.pid AS blocking_pid,
  blocking.usename AS blocking_user,
  blocked.query AS blocked_query
FROM pg_stat_activity AS blocked
JOIN pg_stat_activity AS blocking ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));
```

## 19. Import/Export Data

### COPY Command
```sql
-- Export to CSV
COPY users TO '/tmp/users.csv' CSV HEADER;

-- Import from CSV
COPY users FROM '/tmp/users.csv' CSV HEADER;

-- Export query results
COPY (SELECT * FROM users WHERE active = true) TO '/tmp/active_users.csv' CSV HEADER;

-- Import with specific columns
COPY users(id, name, email) FROM '/tmp/users.csv' CSV HEADER;
```

### Using psql for Import/Export
```bash
# Export database
pg_dump -U username -d database_name -f backup.sql

# Export specific tables
pg_dump -U username -d database_name -t table_name -f table_backup.sql

# Export in custom format
pg_dump -U username -d database_name -Fc -f backup.dump

# Import
psql -U username -d database_name -f backup.sql
```

## 20. Common Patterns and Examples

### Upsert (INSERT ... ON CONFLICT)
```sql
-- Insert or update
INSERT INTO users (id, name, email) 
VALUES (1, 'John', 'john@example.com')
ON CONFLICT (id) 
DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;

-- Insert or do nothing
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com')
ON CONFLICT (id) DO NOTHING;
```

### Lateral Joins
```sql
-- Get top 3 orders for each customer
SELECT c.name, o.*
FROM customers c
CROSS JOIN LATERAL (
  SELECT * FROM orders
  WHERE customer_id = c.id
  ORDER BY created_at DESC
  LIMIT 3
) o;
```

### Array Operations
```sql
-- Array contains
SELECT * FROM posts WHERE 'postgresql' = ANY(tags);

-- Array overlap
SELECT * FROM posts WHERE tags && ARRAY['database', 'sql'];

-- Array aggregation
SELECT author, ARRAY_AGG(title) as articles
FROM posts GROUP BY author;
```

### Time-Series Queries
```sql
-- Daily aggregation
SELECT 
  DATE_TRUNC('day', created_at) as day,
  COUNT(*) as count,
  AVG(amount) as avg_amount
FROM transactions
GROUP BY day
ORDER BY day;

-- Fill gaps with generate_series
SELECT 
  d.date,
  COALESCE(COUNT(t.id), 0) as transactions
FROM generate_series(
  '2024-01-01'::date,
  '2024-01-31'::date,
  '1 day'::interval
) AS d(date)
LEFT JOIN transactions t ON DATE(t.created_at) = d.date
GROUP BY d.date
ORDER BY d.date;
```

