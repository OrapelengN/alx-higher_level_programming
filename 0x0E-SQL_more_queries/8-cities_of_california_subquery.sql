-- Select all cities from the 'cities' table where state_id corresponds to California
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
