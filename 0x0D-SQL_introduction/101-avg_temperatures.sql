-- Assuming the table is named 'temperatures' and it has the columns 'city' and 'temperature' (Fahrenheit)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
