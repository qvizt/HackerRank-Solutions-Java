# Advanced Join Solutions
Solutions for challenges in SQL's subdomain Advanced Join.

#### Projects
```SQL
  SELECT start_date, end_date
    FROM (
             SELECT CONNECT_BY_ROOT start_date AS start_date, end_date, LEVEL AS days
               FROM projects
              WHERE end_date NOT IN (
                                    SELECT start_date
                                      FROM projects
                                    )
         CONNECT BY PRIOR end_date = start_date
         )
   WHERE start_date NOT IN (
                           SELECT end_date
                             FROM projects
                           )
ORDER BY days ASC, start_date ASC;
```

#### Placements
```SQL
  SELECT stu.name
    FROM packages pacstu
         JOIN students stu ON pacstu.id = stu.id
         JOIN friends fri ON stu.id = fri.id
         JOIN packages pacfri ON fri.friend_id = pacfri.id
   WHERE pacstu.salary < pacfri.salary
ORDER BY pacfri.salary ASC;
```

#### Symmetric Pairs
```SQL
  SELECT one.x, one.y
    FROM functions one
         JOIN functions two ON one.x = two.y
          AND two.x = one.y
GROUP BY one.x, one.y
  HAVING one.x < one.y
      OR COUNT(*) > 1
ORDER BY one.x ASC;
```

#### Interviews
```SQL
  SELECT con.contest_id, con.hacker_id, con.name, SUM(sum_sub), SUM(sum_total),
         SUM(sum_views), SUM(sum_unique_views)
    FROM contests con
         JOIN colleges col ON con.contest_id = col.contest_id
         JOIN challenges cha ON col.college_id = cha.college_id
         LEFT JOIN (
                     SELECT challenge_id AS chal_id, SUM(total_views) AS sum_views,
                            SUM(total_unique_views) AS sum_unique_views
                       FROM view_stats
                   GROUP BY challenge_id
                   ) vie ON cha.challenge_id = vie.chal_id
         LEFT JOIN (
                     SELECT challenge_id chal_id, SUM(total_submissions) AS sum_sub,
                           SUM(total_accepted_submissions) AS sum_total
                       FROM submission_stats
                   GROUP BY challenge_id
                   ) sub ON cha.challenge_id = sub.chal_id
   WHERE sum_views > 0
      OR sum_unique_views > 0
      OR sum_sub > 0
      OR sum_total > 0
GROUP BY con.contest_id, con.hacker_id, con.name
ORDER BY con.contest_id ASC;
```
Alternative solution with NVL(expression, 0):
```SQL
  SELECT con.contest_id, con.hacker_id, con.name, SUM(sum_sub),
         SUM(sum_total_acc), SUM(sum_views), SUM(sum_unique_views)
    FROM contests con
         JOIN colleges col ON con.contest_id = col.contest_id
         JOIN challenges cha ON col.college_id = cha.college_id
         LEFT JOIN (
                     SELECT challenge_id AS chal_id, SUM(total_views) AS sum_views,
                            SUM(total_unique_views) AS sum_unique_views
                       FROM view_stats
                   GROUP BY challenge_id
                   ) vie ON cha.challenge_id = vie.chal_id
         LEFT JOIN (
                     SELECT challenge_id chal_id, SUM(total_submissions) AS sum_sub,
                            SUM(total_accepted_submissions) AS sum_total_acc
                       FROM submission_stats
                   GROUP BY challenge_id
                   ) sub ON cha.challenge_id = sub.chal_id
 WHERE    (NVL(sum_views, 0) + NVL(sum_unique_views, 0) + NVL(sum_sub, 0) + NVL(sum_total_acc, 0)) > 0
GROUP BY con.contest_id, con.hacker_id, con.name
ORDER BY con.contest_id ASC;
```

#### 15 Days of Learning SQL ( WIP )
```SQL
  SELECT *
    FROM (
           SELECT submission_date, COUNT(DISTINCT hacker_id) AS cons_hacker_count
             FROM (
                      SELECT CONNECT_BY_ROOT submission_date AS root_date, hacker_id, submission_date
                        FROM submissions
                  CONNECT BY (TO_DATE(submission_date, 'YYYY-MM-DD') - TO_DATE(PRIOR submission_date, 'YYYY-MM-DD')) = 1
                         AND PRIOR hacker_id = hacker_id
                  )
            WHERE root_date = (
                              SELECT MIN(submission_date)
                                FROM submissions
                              )
         GROUP BY submission_date
         )
         NATURAL JOIN
         (
          SELECT  submission_date, hacker_id, name
            FROM (
                   SELECT submission_date, MIN(hacker_id) AS hacker_id
                     FROM (
                            SELECT submission_date, COUNT(submission_id) AS sub_count, hacker_id
                              FROM submissions sbmssns
                          GROUP BY submission_date, hacker_id
                            HAVING COUNT(submission_id) = (
                                                            SELECT MAX(sub_count)
                                                              FROM (
                                                                     SELECT submission_date, COUNT(submission_id) AS sub_count
                                                                       FROM submissions
                                                                   GROUP BY submission_date, hacker_id
                                                                   )
                                                          GROUP BY submission_date HAVING submission_date = sbmssns.submission_date
                                                          )
                          )
                 GROUP BY submission_date, sub_count
                 )
         NATURAL JOIN hackers
         )
ORDER BY submission_date ASC;
```