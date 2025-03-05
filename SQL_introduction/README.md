# SQL - Introduction

## 0. List databases
Write a script that lists all databases of your MySQL server.

### Expectation
```sql
-- show
-- list database
SHOW DATABASES;
```
### Result
```bash
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```

## 1. Create a database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.

### Objectives
- If the database `hbtn_0c_0` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

### Expectation
```sql
-- create
-- database hbtn_0c_0
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```
### Result
```bash
Enter password: 
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
```

## 2. Delete a database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

### Objectives
- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

### Expectation
```sql
-- delete
-- database hbtn_0c_0
DROP DATABASE IF EXISTS hbtn_0c_0;
```
### Result
```bash
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```

## 3. List tables 
Write a script that lists all the tables of a database in your MySQL server.

### Objectives
The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

### Expectation
```sql
-- show
-- list tables
SHOW TABLES;
```
### Result
```bash
Enter password: 
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
global_grants
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
password_history
plugin
procs_priv
proxies_priv
replication_asynchronous_connection_failover
replication_asynchronous_connection_failover_managed
replication_group_configuration_version
replication_group_member_actions
role_edges
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
```

## 4. First table
Write a script that creates a table called `first_table` in the current database in your MySQL server.

### Objectives
- `first_table`description:
    `id` INT
    `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `first_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

### Expectation
```sql
-- create
-- table first_table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```
### Result
```bash
Enter password: 
Tables_in_hbtn_0c_0
first_table
```

## 5. Full description
Write a script that prints the following description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

### Objectives
- The database name will be passed as an argument of the `mysql` command
- You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

### Expectation
```sql
-- show
-- description of first_table
SHOW CREATE TABLE first_table;
```
### Result
```bash
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

## 6. List all in table
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

### Objectives
- All fields should be printed
- The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
-- select
-- all rows of first_tables
SELECT * FROM first_table;
```
### Result
```bash
Enter password: 
➜  SQL_introduction git:(main) ✗
```

## 7. First add
Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

### Objectives
- New row:
    - `id` = 89
    - `name` = Best School
The database name will be passed as an argument of the mysql command

### Expectation
```sql
-- insert
-- new value into first_name
INSERT INTO first_table (id, nom) VALUES ('89', 'Best School');
```
### Result
```bash
id      nom
89      Best School
```

## 8. Count 89
Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```

##

### Objectives

### Expectation
```sql
```
### Result
```bash
```