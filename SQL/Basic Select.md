# Basic Select Solutions
Solutions for challenges found in SQL's subdomain Basic Select.

#### Revising the Select Query I
```SQL
SELECT    *
  FROM    city
 WHERE    countrycode = 'USA' 
   AND    population > 100000;
```

#### Revising the Select Query II
```SQL
SELECT    name 
  FROM    city
 WHERE    population > 120000
   AND    countrycode = 'USA';
```

#### Select All
```SQL
SELECT    * 
  FROM    CITY;
```

#### Select By ID
```SQL
SELECT    *
  FROM    city
 WHERE    ID = 1661;
```

#### Japanese Cities' Attributes
```SQL
SELECT    *
  FROM    city
 WHERE    countrycode = 'JPN';
```