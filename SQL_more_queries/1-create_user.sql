-- Task: Create user_0d_1 with all privileges on the MySQL server
-- This query creates the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- This query grants all privileges to the user on the whole server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
