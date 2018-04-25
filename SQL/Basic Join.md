# Basic Join Solutions
Solutions for challenges in SQL's subdomain Basic Join.

#### Asian Population
```SQL
SELECT    SUM(city.population)
  FROM    city
          JOIN country ON city.countrycode = country.code
 WHERE    country.continent = 'Asia';
```

#### African Cities
```SQL
SELECT    city.name
  FROM    city
          JOIN country ON city.countrycode = country.code
 WHERE    country.continent = 'Africa';
```

#### Average Population of Each Continent
```SQL
SELECT    country.continent, FLOOR(AVG(city.population))
  FROM    city
          JOIN country ON city.countrycode = country.code
 GROUP BY country.continent;
```

#### The Report
```SQL
SELECT    CASE
               WHEN grades.grade < 8
               THEN NULL
               ELSE students.name
           END, grades.grade, students.marks
  FROM    students
          JOIN grades ON students.marks BETWEEN grades.min_mark AND grades.max_mark
 ORDER BY grades.grade DESC, students.name ASC, students.marks ASC;
```

#### Top Competitors
```SQL
SELECT    hackers.hacker_id, hackers.name
  FROM    submissions
          JOIN hackers ON submissions.hacker_id = hackers.hacker_id
          JOIN challenges ON challenges.challenge_id = submissions.challenge_id
          JOIN difficulty ON challenges.difficulty_level = difficulty.difficulty_level
 WHERE    submissions.score = difficulty.score
   AND    challenges.difficulty_level = difficulty.difficulty_level
 GROUP BY hackers.hacker_id, hackers.name HAVING COUNT(*) > 1
 ORDER BY COUNT(*) DESC, hackers.hacker_id ASC;
```

#### Ollivander's Inventory
```SQL
SELECT    wands.id, w_age, w_min_coins, w_power
  FROM    wands
          JOIN (
               SELECT    wands.code AS w_code, wands_property.age AS w_age,
                         MIN(coins_needed) AS w_min_coins, wands.power AS w_power
                 FROM    wands
                         JOIN wands_property ON wands.code = wands_property.code
                WHERE    wands_property.is_evil = 0
                GROUP BY wands.code, wands_property.age, wands.power
               ) ON wands.code = w_code AND wands.coins_needed = w_min_coins AND wands.power = w_power
 ORDER BY w_power DESC, w_age DESC;
```

#### Challenges
```SQL
SELECT    h_id, hackers.name, c_count
  FROM    hackers
          JOIN (
               SELECT    hacker_id AS h_id, COUNT(hacker_id) AS c_count
                 FROM    challenges GROUP BY hacker_id
               ) ON hackers.hacker_id = h_id
 WHERE    c_count = (
                    SELECT    MAX(c_count_tmp)
                      FROM    (
                              SELECT    COUNT(hacker_id) AS c_count_tmp
                                FROM    challenges GROUP BY hacker_id
                              )
                    )
    OR    c_count IN (
                     SELECT    c_count_tmp
                       FROM    (
                               SELECT    COUNT(hacker_id) AS c_count_tmp
                                 FROM    challenges
                                GROUP BY hacker_id
                               )
                      GROUP BY c_count_tmp HAVING COUNT(c_count_tmp) = 1
                     )
 ORDER BY c_count DESC, h_id ASC;
```

#### Contest Leaderboard
```SQL
SELECT    hackers.hacker_id, hackers.name, SUM(max_score) sum_score
  FROM    hackers
          JOIN (
               SELECT    hacker_id AS h_id, challenge_id AS c_id, MAX(score) max_score
                 FROM    submissions
                WHERE    score > 0
                GROUP BY hacker_id, challenge_id
               ) ON hackers.hacker_id = h_id
 GROUP BY hackers.hacker_id, hackers.name
 ORDER BY sum_score DESC, hackers.hacker_id ASC;
```