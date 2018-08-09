# Basic Select Solutions
Solutions for challenges in SQL's subdomain Basic Select.

#### Revising the Select Query I
```SQL
SELECT * FROM city WHERE population > 100000 AND countrycode = 'USA';
```

#### Revising the Select Query II
```SQL
SELECT name FROM city WHERE population > 120000 AND countrycode = 'USA';
```

#### Select All
```SQL
SELECT * FROM city;
```

#### Select By ID
```SQL
SELECT * FROM city WHERE ID = 1661;
```

#### Japanese Cities' Attributes
```SQL
SELECT * FROM city WHERE countrycode = 'JPN';
```

#### Japanese Cities' Names
```SQL
SELECT name FROM city WHERE countrycode = 'JPN';
```

#### Weather Observation Station 1
```SQL
SELECT city, state FROM station;
```

#### Weather Observation Station 3
```SQL
SELECT DISTINCT(city) FROM station WHERE id % 2 = 0;
```

#### Weather Observation Station 4
```SQL
SELECT COUNT(*) - COUNT(DISTINCT(city)) FROM station;
```

#### Weather Observation Station 5
```SQL
SELECT * FROM (SELECT TOP(1) city, LEN(city) AS length FROM station ORDER BY LEN(city) ASC, city ASC) AS min_city UNION
SELECT * FROM (SELECT TOP(1) city, LEN(city) AS length FROM station ORDER BY LEN(city) DESC, city ASC)  AS max_city;
```

#### Weather Observation Station 6
```SQL
SELECT DISTINCT(city) FROM station WHERE LEFT(city,1) IN ('A', 'E', 'I', 'O', 'U');
```

#### Weather Observation Station 7
```SQL
SELECT DISTINCT(city) FROM station WHERE RIGHT(city,1) IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 8
```SQL
SELECT city FROM station WHERE LEFT(city,1) IN ('A', 'E', 'I', 'O', 'U') AND RIGHT(city,1) IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 9
```SQL
SELECT DISTINCT(city) FROM station WHERE LEFT(city, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```

#### Weather Observation Station 10
```SQL
SELECT DISTINCT(city) FROM station WHERE RIGHT(city,1) NOT IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 11
```SQL
SELECT DISTINCT(city) FROM station WHERE LEFT(city,1) NOT IN ('A', 'E', 'I', 'O', 'U') OR RIGHT(city,1) NOT IN ('a', 'e', 'i', 'o', 'u');
```

#### Weather Observation Station 12
```SQL
SELECT DISTINCT(city) FROM station WHERE LEFT(city,1) NOT IN ('A', 'E', 'I', 'O', 'U') AND RIGHT(city,1) NOT IN ('a', 'e', 'i', 'o', 'u');
```

#### Higher Than 75 Marks
```SQL
SELECT name FROM students WHERE marks > 75 ORDER BY RIGHT(name, 3) ASC, id ASC;
```

#### Employee Names
```SQL
SELECT name FROM employee ORDER BY name ASC;
```

#### Employee Salaries
```SQL
SELECT name FROM employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id ASC;
```