# SQL basics

1. Install postgresql database
```shell
sudo apt update
```
```shell
sudo apt install postgresql postgresql-contrib
```
2. Enter to the PostgreSQL
```shell
sudo -i -u postgres
```
```shell
psql
```
3. Create database for work
```sql
create database test;
```
4. Connect to created database under DBMS
```shell
\c test
```
5. Create schema of data (table)
6. Insert tuple / row into the table
7. Filter operations WHERE, HAVING
8. Update tuple / row in the table with condition
9. Delete tuple / row in the table with condition
10. SQL constraints for data:
    1. PRIMARY KEY
    2. NOT NULL
    3. UNIQUE
    4. FOREIGHN KEY
    5. CHECK
11. PostgreSQL unique constraints (acatual only for postgresql DBMS)
12. Join operations (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN)
13. Normalization of data. Why and when?
14. Existing normal forms
15. Main builtin agregetaion functions:
    1.  MAX
    2.  MIN
    3.  COUNT
    4.  SUM

[Back](../README.md)