<<<<<<< HEAD
-- script that creates the table force_name on DB and if the table force_name already exists, script does not fail
-- force_name description: id INT, name VARCHAR(256) can’t be null
=======
-- Creates the table force_name on your MySQL server.
>>>>>>> 7158139 (added new repo)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
