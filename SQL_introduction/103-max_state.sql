<<<<<<< HEAD
-- Displays the max temperature of each state ordered by State name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
=======
-- Displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
>>>>>>> 7158139 (added new repo)
