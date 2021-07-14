-- creates the table id_not_null on your MySQL server.
CREATE TABLE if not exists unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
