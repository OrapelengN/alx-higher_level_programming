-- Select cities.id, cities.name, and states.name by joining cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
