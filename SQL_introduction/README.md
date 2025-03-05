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
Write a script that creates the database hbtn_0c_0 in your MySQL server.

### Objectives
If the database `hbtn_0c_0` already exists, your script should not fail
You are not allowed to use the `SELECT` or `SHOW` statements

### Expectation
```sql
-- create
-- database hbtn_0c_0
CREATE DATABASE IF NOT EXISTS hbtn_0c_0
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