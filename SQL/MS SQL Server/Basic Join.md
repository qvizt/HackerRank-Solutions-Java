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

```

#### Ollivander's Inventory
```SQL

```

#### Challenges
```SQL

```

#### Contest Leaderboard
```SQL

```