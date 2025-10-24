-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- Not allowed to use JOIN
SELECT id, name
FROM cities
WHERE (cities.state_id=1);
