# Basic Join Solutions
Solutions for challenges in SQL's subdomain Basic Join.

#### Asian Population
```SQL
SELECT SUM(city.population)
  FROM city, country
 WHERE city.countrycode = country.code
   AND country.continent = 'Asia';
```

#### African Cities
```SQL
SELECT city.name
  FROM city, country
 WHERE city.countrycode = country.code
   AND country.continent = 'Africa';
```

#### Average Population of Each Continent
```SQL
  SELECT country.continent, FLOOR(AVG(city.population))
    FROM city, country
   WHERE city.countrycode = country.code
GROUP BY country.continent;
```

#### The Report
```SQL
  SELECT CASE
             WHEN grade < 8 THEN NULL
             ELSE name
          END, grade, marks
    FROM students
         JOIN grades ON marks BETWEEN min_mark AND max_mark
ORDER BY grade DESC, name ASC;
```

#### Top Competitors
```SQL
  SELECT hackers.hacker_id, hackers.name
    FROM hackers
         JOIN (
                SELECT submissions.hacker_id, COUNT(*) AS count_max_score
                  FROM submissions
                       JOIN challenges ON submissions.challenge_id = challenges.challenge_id
                       JOIN difficulty ON challenges.difficulty_level = difficulty.difficulty_level
                 WHERE submissions.score = difficulty.score
              GROUP BY submissions.hacker_id
                HAVING COUNT(*) > 1
              ) AS summary ON hackers.hacker_id = summary.hacker_id
ORDER BY summary.count_max_score DESC, hackers.hacker_id ASC;
```

#### Ollivander's Inventory
```SQL
  SELECT wands.id, summary.age, summary.min_coins, summary.power
    FROM wands
         JOIN (
                SELECT wands.code AS code, MIN(wands.coins_needed) AS min_coins, wands_property.age AS age,
                       wands.power AS power
                  FROM wands
                       JOIN wands_property ON wands.code = wands_property.code
                 WHERE wands_property.is_evil = 0
              GROUP BY wands.code, wands_property.age, wands.power
              ) AS summary ON wands.code = summary.code
                          AND wands.coins_needed = summary.min_coins
                          AND wands.power = summary.power
ORDER BY summary.power DESC, summary.age DESC;
```

#### Challenges
```SQL
  SELECT hackers.hacker_id, hackers.name, summary.chal_count
    FROM hackers
         JOIN (
                SELECT hacker_id, COUNT(*) AS chal_count
                  FROM challenges
              GROUP BY hacker_id
              ) AS summary ON hackers.hacker_id = summary.hacker_id
   WHERE summary.chal_count = (
                              SELECT MAX(chal_count)
                                FROM (
                                       SELECT COUNT(hacker_id) AS chal_count
                                         FROM challenges
                                     GROUP BY hacker_id
                                     ) AS tmp
                              )
      OR summary.chal_count IN (
                                 SELECT chal_count
                                   FROM (
                                          SELECT COUNT(hacker_id) AS chal_count
                                            FROM challenges
                                        GROUP BY hacker_id
                                        ) AS tmp
                               GROUP BY chal_count
                                 HAVING COUNT(chal_count) = 1
                               )
ORDER BY summary.chal_count DESC, hackers.hacker_id ASC;
```

#### Contest Leaderboard
```SQL
  SELECT *
    FROM (
           SELECT hackers.hacker_id, hackers.name, SUM(summary.max_chal_sub_score) AS total_score
             FROM hackers
                  JOIN (
                         SELECT MAX(score) AS max_chal_sub_score, hacker_id, challenge_id
                           FROM submissions
                       GROUP BY hacker_id, challenge_id
                       ) AS summary ON hackers.hacker_id = summary.hacker_id
         GROUP BY hackers.hacker_id, hackers.name
         ) AS final_summary
   WHERE total_score > 0
ORDER BY total_score DESC, hacker_id ASC;
```