<<<<<<< HEAD
-- creates the table id_not_null on DB server. If table id_not_null already exists, script does not fail
-- default value for id = 1
=======
-- Creates the table id_not_null on your MySQL server.
>>>>>>> 7158139 (added new repo)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
