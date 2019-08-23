# Advanced Join Solutions
Solutions for challenges in SQL's subdomain Advanced Join.

#### Projects
```SQL
 WITH p(task_id, start_date, end_date, level, min_conn_day) AS 
 (
  SELECT task_id
         , start_date
         , end_date
         , 1 AS level
         , start_date AS min_conn_day
    FROM projects
         UNION ALL
  SELECT p1.task_id
         , p1.start_date
         , p1.end_date
         , level + 1
         , p.min_conn_day
    FROM projects AS p1
         JOIN p ON p.end_date = p1.start_date)

  SELECT min_conn_day, end_date
    FROM (
          SELECT *,
                 RANK() OVER(PARTITION BY min_conn_DAY ORDER BY LEVEL DESC) r 
            FROM p
         ) tmp
   WHERE r = 1
         AND min_conn_day NOT IN (
                                  SELECT end_date
                                    FROM p
                                 )
ORDER BY level ASC
		 , min_conn_day ASC
```

#### Placements
```SQL
SELECT name
  FROM friends 
       JOIN packages friend_package ON friends.friend_id = friend_package.id
       JOIN packages own_package ON friends.id = own_package.id
       JOIN students ON friends.id = Students.id
WHERE friend_package.salary > own_package.salary
ORDER BY friend_package.salary
```

#### Symmetric Pairs
```SQL
to be done
```

#### Interviews
```SQL
to be done
```


#### 15 Days of Learning SQL
```SQL
to be done
```