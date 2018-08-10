# Aggregation Solutions
Solutions for challenges in SQL's subdomain Aggregation.

#### Revising Aggregations - The Count Function
```SQL
SELECT COUNT(*)
  FROM city
 WHERE population > 100000;
```

#### Revising Aggregations - The Sum Function
```SQL
SELECT SUM(population)
  FROM city
 WHERE district = 'California';
```

#### Revising Aggregations - Averages
```SQL
SELECT AVG(population)
  FROM city
 WHERE district = 'California';
```

#### Average Population
```SQL
SELECT FLOOR(AVG(population))
  FROM city;
```

#### Japan Population
```SQL
SELECT SUM(population)
  FROM city
 WHERE countrycode = 'JPN';
```

#### Population Density Difference
```SQL
SELECT MAX(population) - MIN(population)
  FROM city;
```

#### The Blunder
```SQL
SELECT CAST(CEILING(AVG(CAST(salary AS float)) - AVG(CAST(REPLACE(salary, 0, '') AS float))) AS int)
  FROM employees;
```

#### Top Earners
```SQL
SELECT TOP(1) earnings, COUNT(*)
  FROM (
         SELECT (months * salary) AS earnings
           FROM employee
       ) AS summary
GROUP BY earnings
ORDER BY earnings DESC;
```

#### Weather Observation Station 2
```SQL
SELECT CAST(SUM(lat_n) AS NUMERIC(10,2)), CAST(SUM(long_w) AS NUMERIC(10,2)) 
  FROM station;
```

#### Weather Observation Station 13
```SQL
SELECT CAST(SUM(lat_n) AS NUMERIC(10,4))
  FROM station
 WHERE lat_n BETWEEN 38.7881 AND 137.2344;

/*
Greater than 38.7880 and less than 137.2345 "translates"
as 38.7881 and 137.2344 in this context because
BETWEEN includes both limits / bounds.
*/
```

#### Weather Observation Station 14
```SQL
SELECT CAST(MAX(lat_n) AS NUMERIC(10,4))
  FROM station
 WHERE lat_n < 137.2345;
```

#### Weather Observation Station 15
```SQL
SELECT CAST(long_w AS NUMERIC(10,4))
  FROM station
 WHERE lat_n = (
               SELECT MAX(lat_n)
                 FROM station
                WHERE lat_n < 137.2345
			   );
```

#### Weather Observation Station 16
```SQL
SELECT CAST(MIN(lat_n) AS NUMERIC(10,4))
  FROM station
 WHERE lat_n > 38.7780;
```

#### Weather Observation Station 17
```SQL
SELECT CAST(long_w AS NUMERIC(10,4))
  FROM station
 WHERE lat_n = (
               SELECT MIN(lat_n)
                 FROM station
                WHERE lat_n > 38.7780
			   );
```

#### Weather Observation Station 18
```SQL
SELECT CAST(
           ABS(p1.a - p2.c)
		   +
		   ABS(p1.b - p2.d)
		   AS NUMERIC(10,4)
		   )
  FROM (
       SELECT MIN(lat_n) AS a, MIN(long_w) AS b
         FROM station
       ) AS p1,
       (
       SELECT MAX(lat_n) AS c, MAX(long_w) AS d
         FROM station
       ) AS p2;
```

#### Weather Observation Station 19
```SQL
SELECT CAST(
           SQRT(
		       POWER(p1.b - p1.a, 2)
			   +
			   POWER(p2.d - p2.c, 2)
			   )
		   AS NUMERIC(10,4)
		   )
  FROM (
       SELECT MIN(lat_n) AS a, MAX(lat_n) AS b
         FROM station
       ) AS p1,
       (
       SELECT MIN(long_w) AS c, MAX(long_w) AS d
         FROM station
       ) AS p2;
```

#### Weather Observation Station 20
```SQL
SELECT CAST(median AS NUMERIC(10,4))
  FROM (
       SELECT TOP(1) PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY lat_n ASC) OVER () AS median
         FROM station
       ) AS result;
```