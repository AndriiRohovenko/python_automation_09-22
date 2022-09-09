-- DROP TABLE products;
-- DROP TABLE users;
-- DROP TABLE profiles;

-- CREATE TABLE products
-- (
--     id varchar(5) primary key,
--     "name" varchar(128) unique,
--     quontity int not null,
--     price int not null,
--     CONSTRAINT price
--         check(price < 0)
-- );

-- INSERT INTO products
-- (id, name, quontity, price) values
-- ('aaaaa', 'Iphone 13 Pro', 5, 1200),
-- ('bbbbb', 'Samsung Galaxy s22', 1, 1500),
-- ('ccccc', 'Meazu 5', 500, 500),
-- ('ddddd', 'Xiomi Plus 5', 50, 300),
-- ('eeeee', 'Motorolla', 24, 50),
-- ('rrrrr', 'Nokia 1100', 5000, 5),
-- ('ttttt', 'Huawai s89', 50, 600),
-- ('iiiii', 'Iphone 14', 1, 1600),
-- ('ooooo', 'Iphone 12 Pro Max', 2, 600);


--  create table profiles (
--      id varchar(5) primary key,
--      first_name varchar(32),
--      last_name varchar(32),
--      user_id varchar(5),
--      CONSTRAINT user_id
--        FOREIGN KEY(id)
--  	  REFERENCES users(id)
--  );


--  insert into users (id, email, gender, country_code) values
--  ('aaaaa', 'john.dow@gmail.com', 'male', 'CA'),
--  ('bbbbb', 'jane.dow@gmail.com', 'female', 'UA'),
--  ('ccccc', 'marta.stuard@gmail.com', 'female', 'UK'),
--  ('eeeee', 'james.brown@gmail.com', 'male', 'US');


--  insert into profiles (id, first_name, last_name, user_id) values
--  ('aaaaa', 'John', 'Dow', 'aaaaa'),
--  ('bbbbb', 'Jame', 'Dow', 'bbbbb'),
--  ('ccccc', 'Marta', 'Stuard', 'ccccc');
