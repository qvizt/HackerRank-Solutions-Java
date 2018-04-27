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
            AND b = c
           THEN 'Equilateral'
           WHEN a != b
            AND b != c
            AND a != c
           THEN 'Scalene'
           ELSE 'Isosceles'
        END
  FROM triangles;
```

#### The PADS
```SQL
SELECT *
  FROM (
         SELECT name || '(' || SUBSTR(occupation, 1, 1) || ')'
           FROM occupations
       ORDER BY name ASC
       )
 UNION
SELECT *
  FROM (
         SELECT 'There are a total of ' || COUNT(occupation) || ' ' || LOWER(occupation) || 's.'
           FROM occupations
       GROUP BY occupation
       ORDER BY COUNT(occupation) ASC, occupation ASC
       );
```

#### Occupations
```SQL
  SELECT doctor, professor, singer, actor
    FROM (
         SELECT name, occupation, ROW_NUMBER() OVER(PARTITION BY occupation ORDER BY name) AS row_nr
          FROM occupations
         )
   PIVOT (
         MAX(name)
         FOR occupation IN ('Doctor' AS doctor, 'Professor' AS professor, 'Singer' AS singer, 'Actor' AS actor)
         )
ORDER BY row_nr;
```

#### Binary Tree Nodes
```SQL
  SELECT n, CASE
                WHEN p IS NULL
                THEN 'Root'
                WHEN n IN (
                          SELECT p
                            FROM bst
                           WHERE p IS NOT NULL
                          )
                THEN 'Inner'
                WHEN n NOT IN (
                              SELECT p
                                FROM bst
                               WHERE p IS NOT NULL
                              )
                THEN 'Leaf'
             END
    FROM bst
ORDER BY n;
```

#### New Companies
```SQL
  SELECT company_code, founder, COUNT(DISTINCT lead_manager_code),
         COUNT(DISTINCT senior_manager_code), COUNT(DISTINCT manager_code), COUNT(DISTINCT employee_code)
    FROM company
         NATURAL JOIN lead_manager
         NATURAL JOIN senior_manager
         NATURAL JOIN manager
         NATURAL JOIN employee
GROUP BY company_code, founder
ORDER BY company_code ASC;
```