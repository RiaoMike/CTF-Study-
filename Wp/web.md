# 1. 强网杯2019随便注

I want to note the method while "select/insert/delete/where..." are forbidden.

First use stacked injection to get all databases,tables and columns.

You want to query the`select * from table_name;`. Then convert it to hex first, 
and then set payload as follows:
```
1';SeT@a=0x{hex_code_here};Prepare execsql from @a;execute execsql;#
```

One more word, if you take "set", "prepare" all in lower-case, you'll get **strstr** error.

Look for php manual, you'll find it is case-sensitive, you need to spell "Set","PrepAre" etc.

#2. 
