-- script that creates the MySQL server user user_0d_1 with privilages
CREATE USER IF NOT EXIST 'user_0d_1@localhost' IDENTIFIED BY user_0d_1_pwd;
GRANT PRIVILEGES ON *.* TO user_0d_1@localhost;
