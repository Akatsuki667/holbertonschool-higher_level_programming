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
-- count
--  number of records
SELECT COUNT(*) FROM first_table WHERE id = 89;
```
### Result
```bash
Enter password: 
1
```

## 9. Full creation
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

### Objectives
- `second_table` description:
    - `id` INT
    - `name` VARCHAR(256)
    - `score` INT
- The database name will be passed as an argument to the `mysql` command
- If the table `second_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` and `SHOW` statements
- Your script should create these records:
    `id` = 1, `name` = “John”, `score` = 10
    `id` = 2, `name` = “Alex”, `score` = 3
    `id` = 3, `name` = “Bob”, `score` = 14
    `id` = 4, `name` = “George”, `score` = 8

### Expectation
```sql
-- create second_table
-- inserrt values in second_table
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES ('1', 'John', 10);
INSERT INTO second_table (id, name, score) VALUES ('2', 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES ('3', 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES ('4', 'George', 8);
```
### Result
```bash
Enter password: 
id      name    score
1       John    10
2       Alex    3
3       Bob     14
4       George  8
```

## 10. List by best
Write a script that lists all records of the table` second_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
-- lists
-- score and name ordered by high score
SELECT score, name FROM second_table ORDER BY score DESC
```
### Result
```bash
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
```

## 11. Select the best
Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
-- lists
-- score and name ordered by high score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
```
### Result
```bash
Enter password: 
score   name
14  Bob
10  John
```

## 12. Cheating is bad
Write a script that updates the score of Bob to `10` in the table `second_table`.

### Objectives
- You are not allowed to use Bob’s id value, only the `name` field
- The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
-- update
-- value score of bob
UPDATE second_table SET score = 10 WHERE name = 'Bob';
```
### Result
```bash
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
```

## 13. Score too low
Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
- The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
-- delete
-- records with a score <= 5
DELETE FROM second_table WHERE score <= 5
```
### Result
```bash
Enter password: 
score   name
10  John
10  Bob
8   George
```

## 14. Average
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
- The result column name should be `average`
- The database name will be passed as an argument of the `mysql` command

### Expectation
```sql
-- average
-- records in second_table
SELECT AVG(score) AS average FROM second_table
```
### Result
```bash
Enter password: 
average
9.3333
```

## 15. Number by score
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
- The result should display:
    - the `score`
    - the number of records for this `score` with the label `number`
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the `mysql` command
### Expectation
```sql
-- lists
-- recordswith smae score in second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
```
### Result
```bash
Enter password: 
score   number
10  2
8   1
```

## 16. Say my name
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Objectives
- Don’t list rows where the `name` column does not contain a value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the `mysql` command

### Expectation
```sql
-- lists
-- records of second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC
```
### Result
```bash
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
```