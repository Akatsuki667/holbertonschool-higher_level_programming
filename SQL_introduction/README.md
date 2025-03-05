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
CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    nom VARCHAR(256)
);
```
### Result
```bash
Enter password: 
Tables_in_hbtn_0c_0
first_table
```
