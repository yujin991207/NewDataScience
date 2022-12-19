# mysql> show databases;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | mysql              |
# | performance_schema |
# | sakila             |
# | sys                |
# | world              |
# +--------------------+
# 6 rows in set (0.00 sec)
#
# create user open_source@localhost identified by '1111';
# grant all privileges on *.* to 'open_source'@'localhost';
# select host, user from user;
# flush privileges;
# mysql> create database my_suppliers;
# Query OK, 1 row affected (0.00 sec)

# install mysql-connector
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='open_source', passwd='1111')
my_cursor = mydb.cursor()
# my_cursor.execute('create database test_database')
# mysql> show databases;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | my_suppliers       |
# | mysql              |
# | performance_schema |
# | sakila             |
# | sys                |
# | test_database      |
# | world              |
# +--------------------+
# 8 rows in set (0.00 sec)

# database 삭제하려면
# my_cursor.execute('drop database test_database;')