-- creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 PRIMARY KEY,
	name VARCHAR(256));

