<<<<<<< HEAD
-- lists the number of records with the same score in the table second_table of the DB.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
=======
-- Lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
>>>>>>> 7158139 (added new repo)
