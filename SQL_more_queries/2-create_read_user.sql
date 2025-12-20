<<<<<<< HEAD
-- creates the database hbtn_0d_2 and if it already exists, script does not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the user_0d_2 and if the user already exists, script does not fail.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2.
=======
-- Creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
>>>>>>> 7158139 (added new repo)
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
