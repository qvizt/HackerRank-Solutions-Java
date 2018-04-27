# Alternative Queries Solutions
Solutions for challenges in SQL's subdomain Alternative Queries.

#### Revising the Select Query I
```SQL
SELECT    output
  FROM    (
          SELECT    RPAD('*', LEVEL * 2, ' *') AS output, LEVEL
            FROM    DUAL
         CONNECT BY LEVEL <= 20
          )
 ORDER BY output DESC;
```

#### Draw The Triangle 2
```SQL
SELECT    output
  FROM    (
          SELECT    RPAD('*', LEVEL * 2, ' *') AS output, LEVEL
            FROM    DUAL
         CONNECT BY LEVEL <= 20
          );
```

#### Print Prime Numbers
```SQL
WITH numbers AS (
                SELECT    LEVEL AS nr
                  FROM    dual
                 WHERE    LEVEL > 1
               CONNECT BY LEVEL < 1000
                )
SELECT    LISTAGG(nr, '&') WITHIN GROUP (ORDER BY nr ASC)
  FROM    numbers
 WHERE    nr NOT IN (
                    SELECT    x.nr
                      FROM    numbers x, numbers y
                     WHERE    x.nr > y.nr
                       AND    MOD(x.nr, y.nr) = 0
                    );
```