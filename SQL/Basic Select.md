# Basic Select Solutions
Solutions for challenges in SQL's subdomain Basic Select.

#### Revising the Select Query I
```SQL
SELECT *
  FROM city
 WHERE countrycode = 'USA'
   AND population > 100000;
```

#### Revising the Select Query II
```SQL
SELECT name
  FROM city
 WHERE population > 120000
   AND countrycode = 'USA';
```

#### Select All
```SQL
SELECT *
  FROM CITY;
```

#### Select By ID
```SQL
SELECT *
  FROM city
 WHERE ID = 1661;
```

#### Japanese Cities' Attributes
```SQL
SELECT *
  FROM city
 WHERE countrycode = 'JPN';
```

#### Japanese Cities' Names
```SQL
SELECT name
  FROM city
 WHERE countrycode = 'JPN';
```

#### Weather Observation Station 1
```SQL
SELECT city, state
  FROM station;
```

#### Weather Observation Station 3
```SQL
SELECT DISTINCT city
  FROM station
 WHERE MOD(id, 2) = 0;
```

#### Weather Observation Station 4
```SQL
SELECT COUNT(city) - COUNT(DISTINCT city)
  FROM station;
```

#### Weather Observation Station 5
```SQL
SELECT *
  FROM (
          SELECT city, LENGTH(city)
            FROM station
        ORDER BY LENGTH(city) ASC, city ASC
       )
 WHERE ROWNUM = 1
 UNION
SELECT *
  FROM (
         SELECT city, LENGTH(city)
           FROM station
       ORDER BY LENGTH(city) DESC, city ASC
       )
 WHERE ROWNUM = 1;
```

#### Weather Observation Station 6
```SQL
SELECT DISTINCT(city)
  FROM station
 WHERE SUBSTR(city, 1, 1) IN ('A', 'E', 'I', 'O', 'U');
```

#### Weather Observation Station 7
```SQL
SELECT DISTINCT city
  FROM station
 WHERE SUBSTR(city, -1) IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 8
```SQL
SELECT city
  FROM station
 WHERE SUBSTR(city, 1, 1) IN ('A', 'E', 'I', 'O', 'U')
   AND SUBSTR(city, -1) IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 9
```SQL
SELECT DISTINCT city
  FROM station
 WHERE SUBSTR(city, 1, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```

#### Weather Observation Station 10
```SQL
SELECT DISTINCT city
  FROM station
 WHERE SUBSTR(city, -1) NOT IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 11
```SQL
SELECT DISTINCT city
  FROM station
 WHERE SUBSTR(city, 1, 1) NOT IN ('A', 'E', 'I', 'O', 'U')
    OR SUBSTR(city, -1) NOT IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 12
```SQL
SELECT DISTINCT city
  FROM station
 WHERE SUBSTR(city, 1, 1) NOT IN ('A', 'E', 'I', 'O', 'U')
   AND SUBSTR(city, -1) NOT IN ('a', 'e', 'i', 'o', 'u');
```

#### Higher Than 75 Marks
```SQL
SELECT name
  FROM students
 WHERE marks > 75
 ORDER BY SUBSTR(name, -3) ASC, id ASC;
```

#### Employee Names
```SQL
  SELECT name
    FROM employee
ORDER BY name ASC;
```

#### Employee Salaries
```SQL
   SELECT name
     FROM employee
    WHERE salary > 2000
      AND months < 10
 ORDER BY employee_id ASC;
```