# Alternative Queries Solutions
Solutions for challenges in SQL's subdomain Alternative Queries.

#### Revising the Select Query I
```SQL
    SELECT RPAD('*', LEVEL * 2, ' *') AS output
      FROM DUAL
CONNECT BY LEVEL <= 20
  ORDER BY output DESC;
```

#### Draw The Triangle 2
```SQL
    SELECT RPAD('*', LEVEL * 2, ' *')
      FROM DUAL
CONNECT BY LEVEL <= 20;
```

#### Print Prime Numbers
```SQL
WITH numbers AS (
                    SELECT LEVEL AS nr
                      FROM DUAL
                     WHERE LEVEL > 1
                CONNECT BY LEVEL <= 1000
                )
SELECT LISTAGG(nr, '&') WITHIN GROUP (ORDER BY nr ASC)
  FROM numbers
 WHERE nr NOT IN (
                 SELECT x.nr
                   FROM numbers x, numbers y
                  WHERE x.nr > y.nr
                    AND MOD(x.nr, y.nr) = 0
                 );
```