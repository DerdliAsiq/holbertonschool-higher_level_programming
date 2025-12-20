<<<<<<< HEAD
-- lists all records of the table second_table of the DB.
-- it doesnt list rows where the name column does not contain a value.
-- results displays the score and the name
-- records lists by descending score.
=======
-- Lists all records of the table second_table excluding rows without a name value
>>>>>>> 7158139 (added new repo)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
