-- This is a script that creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'hbtn_0d_2'@'localhost' IDENTIFIED BY 'hbtn_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'hbtn_0d_2'@'localhost';
FLUSH PRIVILEGES;
