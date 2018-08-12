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
  SELECT CASE
             WHEN p IS NULL
             THEN CAST(n AS VARCHAR) + ' Root'
             WHEN n IN (
                       SELECT p
                         FROM bst
                        WHERE p IS NOT NULL
                       )
             THEN CAST(n AS VARCHAR) + ' Inner'
             ELSE CAST(n AS VARCHAR) + ' Leaf'
          END
    FROM bst
ORDER BY n;
```

#### New Companies
```SQL
  SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code),
         COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
    FROM company AS c
         JOIN lead_manager AS l ON c.company_code = l.company_code
         JOIN senior_manager AS s ON c.company_code = s.company_code
         JOIN manager AS m ON c.company_code = m.company_code
         JOIN employee AS e ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code ASC;
```