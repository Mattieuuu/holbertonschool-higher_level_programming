-- Query the name of the player who holds the best score in the second table.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;