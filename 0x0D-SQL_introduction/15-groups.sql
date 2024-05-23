-- The script lists the number of records with the same score
SELECT score, COUNT(1) AS number FROM second_table
-- Now group by the score
GROUP BY score
ORDER BY number DESC;
