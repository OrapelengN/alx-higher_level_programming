-- Show the top 3 of cities temperature 
-- Must be during July and August ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
