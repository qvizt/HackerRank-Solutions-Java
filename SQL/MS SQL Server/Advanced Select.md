# Advanced Select Solutions
Solutions for challenges in SQL's subdomain Advanced Select.

#### Type of Triangle
```SQL
SELECT CASE
           WHEN a + b <= c
             OR a + c <= b
             OR b + c <= a
           THEN 'Not A Triangle'
           WHEN a = b
            AND a = c
           THEN 'Equilateral'
           WHEN a != b
            AND a != c
            AND b != c
           THEN 'Scalene'
           ELSE 'Isosceles'
        END
  FROM triangles;
```

#### The PADS
Solution by abusing the output - the SELECTs are executed separately but the results will be returned as an united result, thus as one instead of two outputs.
```SQL
  SELECT name + '(' + LEFT(occupation, 1) + ')'
    FROM occupations
ORDER BY name ASC;

  SELECT 'There are a total of ' + CAST(COUNT(occupation) AS VARCHAR) + ' ' + LOWER(occupation) + 's.'
    FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation) ASC, occupation ASC;
```

Alternative solution without 2 separate SELECTs, which contain a TOP 100 PERCENT each so ORDER BY can be used in the subqueries.
```SQL
SELECT *
  FROM (
         SELECT TOP 100 PERCENT name + '(' + LEFT(occupation, 1) + ')' AS output
           FROM occupations
       ORDER BY name ASC
       ) AS toppart
 UNION
SELECT *
  FROM (
         SELECT TOP 100 PERCENT 'There are a total of ' + CAST(COUNT(occupation) AS VARCHAR)
                + ' ' + LOWER(occupation) + 's.' AS output
           FROM occupations
       GROUP BY occupation
       ORDER BY COUNT(occupation) ASC, occupation ASC
       ) AS bottompart;
```

#### Occupations
```SQL
  SELECT doctor, professor, singer, actor
    FROM (
         SELECT name, occupation, ROW_NUMBER() OVER(PARTITION BY occupation ORDER BY name) AS row_nr
           FROM occupations
         ) AS src
   PIVOT (
         MAX(name)
         FOR occupation IN ([Doctor] , [Professor], [Singer], [Actor])
         ) AS pvt;
```

#### Binary Tree Nodes
```SQL

```

#### New Companies
```SQL

```