# Basic Join Solutions
Solutions for challenges in SQL's subdomain Basic Join.

#### Asian Population
```SQL
SELECT SUM(city.population)
  FROM city
       JOIN country ON city.countrycode = country.code
 WHERE country.continent = 'Asia';
```

#### African Cities
```SQL
SELECT city.name
  FROM city
       JOIN country ON city.countrycode = country.code
 WHERE country.continent = 'Africa';
```

#### Average Population of Each Continent
```SQL
  SELECT country.continent, FLOOR(AVG(city.population))
    FROM city
         JOIN country ON city.countrycode = country.code
GROUP BY country.continent;
```

#### The Report
```SQL
  SELECT CASE
             WHEN grades.grade < 8
             THEN NULL
             ELSE students.name
          END, grades.grade, students.marks
    FROM students
         JOIN grades ON students.marks BETWEEN grades.min_mark AND grades.max_mark
ORDER BY grades.grade DESC, students.name ASC, students.marks ASC;
```

#### Top Competitors
```SQL
  SELECT hackers.hacker_id, hackers.name
    FROM submissions
         JOIN hackers ON submissions.hacker_id = hackers.hacker_id
         JOIN challenges ON challenges.challenge_id = submissions.challenge_id
         JOIN difficulty ON challenges.difficulty_level = difficulty.difficulty_level
   WHERE submissions.score = difficulty.score
     AND challenges.difficulty_level = difficulty.difficulty_level
GROUP BY hackers.hacker_id, hackers.name
  HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, hackers.hacker_id ASC;
```

#### Ollivander's Inventory
```SQL
  SELECT wands.id, w_age, w_min_coins, w_power
    FROM wands
         JOIN (
                 SELECT wands.code AS w_code, wands_property.age AS w_age,
                        MIN(coins_needed) AS w_min_coins, wands.power AS w_power
                   FROM wands
                        JOIN wands_property ON wands.code = wands_property.code
                  WHERE wands_property.is_evil = 0
               GROUP BY wands.code, wands_property.age, wands.power
               ) ON wands.code = w_code
                AND wands.coins_needed = w_min_coins
                AND wands.power = w_power
ORDER BY w_power DESC, w_age DESC;
```

#### Challenges
```SQL
  SELECT hckrs.hacker_id, hackers.name, chal_count
    FROM hackers
         JOIN (
                SELECT hacker_id, COUNT(hacker_id) AS chal_count
                  FROM challenges
              GROUP BY hacker_id
              ) hckrs ON hackers.hacker_id = hckrs.hacker_id
   WHERE chal_count = (
                      SELECT MAX(chal_count)
                        FROM (
                               SELECT COUNT(hacker_id) AS chal_count
                                 FROM challenges
                             GROUP BY hacker_id
                             )
                      )
      OR chal_count IN (
                         SELECT unique_chal_count
                           FROM (
                                  SELECT COUNT(hacker_id) AS unique_chal_count
                                    FROM challenges
                                GROUP BY hacker_id
                                )
                       GROUP BY unique_chal_count
                         HAVING COUNT(unique_chal_count) = 1
                       )
ORDER BY chal_count DESC, hckrs.hacker_id ASC;
```

#### Contest Leaderboard
```SQL
  SELECT hackers.hacker_id, hackers.name, SUM(max_score) AS sum_max_score
    FROM hackers
         JOIN (
                SELECT hacker_id, MAX(score) AS max_score
                  FROM submissions
                 WHERE score > 0
              GROUP BY hacker_id, challenge_id
              ) hckrs ON hackers.hacker_id = hckrs.hacker_id
GROUP BY hackers.hacker_id, hackers.name
ORDER BY sum_max_score DESC, hackers.hacker_id ASC;
```