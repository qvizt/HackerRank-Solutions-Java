# Aggregation Solutions
Solutions for challenges in SQL's subdomain Aggregation.

#### Revising Aggregations - The Count Function
```SQL
SELECT COUNT(id)
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
SELECT ROUND(AVG(population), 0)
  FROM city;
```

#### Japan Population
```SQL
SELECT SUM(population)
  FROM city
 WHERE countrycode ='JPN';
```

#### Population Density Difference
```SQL
SELECT MAX(population) - MIN(population)
  FROM city;
```

#### The Blunder
```SQL
SELECT CEIL(AVG(salary) - AVG(REPLACE(salary, 0, '')))
  FROM employees;
```

#### Top Earners
```SQL
  SELECT max_earning, COUNT(*)
    FROM employee, (
                   SELECT MAX(months * salary) AS max_earning
                     FROM employee
                   )
   WHERE (months * salary) = max_earning
GROUP BY max_earning;
```

#### Weather Observation Station 2
```SQL
SELECT ROUND(SUM(lat_n), 2), ROUND(SUM(long_w), 2)
  FROM station;
```

#### Weather Observation Station 13
```SQL
SELECT ROUND(SUM(lat_n), 4)
  FROM station
 WHERE lat_n > 38.7880
   AND lat_n < 137.2345;
```

#### Weather Observation Station 14
```SQL
SELECT ROUND(MAX(lat_n), 4)
  FROM station
 WHERE lat_n < 137.2345;
```

#### Weather Observation Station 15
```SQL
SELECT ROUND(long_w, 4)
  FROM station
 WHERE lat_n = (
               SELECT MAX(lat_n)
                 FROM station
                WHERE lat_n < 137.2345
               );
```

#### Weather Observation Station 16
```SQL
SELECT ROUND(MIN(lat_n), 4)
  FROM station
 WHERE lat_n > 38.7780;
```

#### Weather Observation Station 17
```SQL
SELECT ROUND(long_w, 4)
  FROM station
 WHERE lat_n = (
               SELECT MIN(lat_n)
                 FROM station
                WHERE lat_n > 38.7780
               );
```

#### Weather Observation Station 18
```SQL
SELECT ROUND(
            ABS(
               MIN(lat_n) - MAX(lat_n)
               )
               +
            ABS(
               MIN(long_w) - MAX(long_w)
               )
         , 4)
  FROM station;
```

#### Weather Observation Station 19
```SQL
SELECT ROUND(
            SQRT(
                POWER(
                     MIN(lat_n) - MAX(lat_n)
                  , 2)
                     +
                POWER(
                     MIN(long_w) - MAX(long_w)
                  , 2)
                )
         , 4)
  FROM station;
```

#### Weather Observation Station 20
```SQL
SELECT ROUND(MEDIAN(lat_n), 4)
  FROM station;
```

Alternative without built-in function:
```SQL
SELECT ROUND(lat_n, 4)
  FROM (
       SELECT ROWNUM AS row_num, lat_n
         FROM (
                SELECT lat_n
                  FROM station
              ORDER BY lat_n ASC
              )
       )
 WHERE row_num = (
                 SELECT CASE
                            WHEN MOD(c, 2) = 0
                            THEN c / 2
                            ELSE (c + 1) / 2
                         END
                   FROM (
                        SELECT COUNT(*) AS c
                          FROM station
                        )
                 );
```