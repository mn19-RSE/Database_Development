# Database_Development

## Purpose:
This project was created to aid in learning database usage. The goal is to be able to:
1. Create a database file
2. Write to the database file using Python or C++
3. Pull information from the database 
4. Create an API to allow microcontrollers to query information from the database file
5. Scale to multiple writers and readers

In the future this project may become a submodule in the [HMI_Development](https://github.com/mn19-RSE/HMI_Development) repo. 


## First steps:

### Windows:
- [Installing SQLite3 on Windows](https://sqldocs.org/install-sqlite3-on-windows/)

### Linux
- Installing SQLite3 in a Linux environment:
    - ~$ sudo apt install sqlite3
    - ~$ sqlite3 test.db
    - sqlite3-> CREATE TABLE measurements (
                time    REAL,
                channel TEXT,
                value   REAL
                );
    - Database file now has a structure
        - time → when measurement happened (Unix time)
        - channel → sensor name
        - value → number
- Write a python script to write to test.db file
