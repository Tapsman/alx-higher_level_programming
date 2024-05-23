-- A script that lists all rows in the database
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
