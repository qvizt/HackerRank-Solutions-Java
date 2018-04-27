# Advanced Join Solutions
Solutions for challenges in SQL's subdomain Advanced Join.

#### Projects
```SQL
SELECT    start_date, end_date
  FROM    (
          SELECT    CONNECT_BY_ROOT start_date AS start_date, end_date AS end_date, LEVEL days
            FROM    projects
           WHERE    end_date NOT IN (
                                    SELECT    start_date
                                      FROM    projects
                                    )
          CONNECT BY PRIOR end_date = start_date
          )
WHERE    start_date NOT IN (
                           SELECT    end_date
                             FROM    projects
                           )
ORDER BY days ASC, start_date ASC;
```

#### Placements
```SQL
SELECT    stu.name
  FROM    packages pstu
          JOIN students stu ON pstu.id = stu.id
          JOIN friends fri ON stud.id = fri.id
          JOIN packages pfri ON fri.friend_id = pfri.id
 WHERE    pstu.salary < pfri.salary
 ORDER BY pfri.salary ASC;
```

#### Symmetric Pairs
```SQL
SELECT    one.x, one.y
  FROM    functions one
          JOIN functions two ON one.x = two.y
           AND two.x = one.y
 GROUP BY one.x, one.y 
HAVING one.x < one.y
    OR COUNT(*) > 1
 ORDER BY one.x ASC;
```

#### Interviews
Note: "All aggregate functions except COUNT(*), GROUPING, and GROUPING_ID ignore nulls. You can use the NVL function in the argument to an aggregate function to substitute a value for a null. COUNT and REGR_COUNT never return null, but return either a number or zero. For all the remaining aggregate functions, if the data set contains no rows, or contains only rows with nulls as arguments to the aggregate function, then the function returns null." 
See https://docs.oracle.com/database/121/SQLRF/functions003.htm#SQLRF20035
```SQL
SELECT    con.contest_id, con.hacker_id, con.name, SUM(sum_sub), SUM(sum_total), SUM(sum_views), SUM(sum_unique)
  FROM    contests con
          JOIN colleges col ON con.contest_id = col.contest_id
          JOIN challenges cha ON col.college_id = cha.college_id
          LEFT JOIN (
                    SELECT    challenge_id cid, SUM(total_views) sum_views, SUM(total_unique_views) as sum_unique
                      FROM    view_stats
                     GROUP BY challenge_id
                    ) vie ON cha.challenge_id = vie.cid
          LEFT JOIN (
                    SELECT    challenge_id cid, SUM(total_submissions) sum_sub, SUM(total_accepted_submissions) sum_total
                      FROM    submission_stats
                     GROUP BY challenge_id
                    ) sub ON cha.challenge_id = sub.cid
 WHERE    sum_views > 0
    OR    sum_unique > 0
    OR    sum_sub > 0
    OR    sum_total > 0
 GROUP BY con.contest_id, con.hacker_id, con.name
 ORDER BY con.contest_id ASC;
```
Alternative solution with NVL(expression, 0):
```SQL
SELECT    con.contest_id, con.hacker_id, con.name, SUM(sum_sub), SUM(sum_total), SUM(sum_views), SUM(sum_unique)
  FROM    contests con
          JOIN colleges col ON con.contest_id = col.contest_id
          JOIN challenges cha ON col.college_id = cha.college_id
          LEFT JOIN (
                    SELECT    challenge_id cid, SUM(total_views) sum_views, SUM(total_unique_views) as sum_unique
                      FROM    view_stats
                     GROUP BY challenge_id
                    ) vie ON cha.challenge_id = vie.cid
          LEFT JOIN (
                    SELECT    challenge_id cid, SUM(total_submissions) sum_sub, SUM(total_accepted_submissions) sum_total
                      FROM    submission_stats
                     GROUP BY challenge_id) sub ON cha.challenge_id = sub.cid
 WHERE    (NVL(sum_views, 0) + NVL(sum_unique, 0) + NVL(sum_sub, 0) + NVL(sum_total, 0)) > 0
 GROUP BY con.contest_id, con.hacker_id, con.name
 ORDER BY con.contest_id ASC;
```

#### 15 Days of Learning SQL ( WIP )
This one solves the challenge and one is currently WIP and might be replaced later with an shorter version.
```SQL
SELECT    *
  FROM    (
          SELECT    submission_date, COUNT(DISTINCT hacker_id) AS cons_hacker_count
            FROM    (
                    SELECT    CONNECT_BY_ROOT submission_date AS root_date, hacker_id, submission_date
                      FROM    submissions
                   CONNECT BY (TO_DATE(submission_date, 'YYYY-MM-DD') - TO_DATE(PRIOR submission_date, 'YYYY-MM-DD')) = 1
                       AND    PRIOR hacker_id = hacker_id
                    )
           WHERE    root_date = (
                                SELECT    MIN(submission_date)
                                  FROM    submissions
                                )
           GROUP BY submission_date
          ) report
          NATURAL JOIN
          (
          SELECT  submission_date, hacker_id, name
            FROM (
                 SELECT    submission_date, MIN(hacker_id) AS hacker_id
                   FROM    (
                           SELECT    submission_date, COUNT(submission_id) AS sub_count, hacker_id
                             FROM    submissions outer_submissions
                            GROUP BY submission_date, hacker_id
                           HAVING COUNT(submission_id) = (
                                                         SELECT    MAX(sub_count)
                                                           FROM    (
                                                                   SELECT    submission_date, COUNT(submission_id) AS sub_count
                                                                     FROM    submissions
                                                                    GROUP BY submission_date, hacker_id
                                                                   )
                                                          GROUP BY submission_date HAVING submission_date = outer_submissions.submission_date
                                                         )
                           )
                  GROUP BY submission_date, sub_count
                 )
                 NATURAL JOIN hackers
          )
 ORDER BY submission_date ASC;
```