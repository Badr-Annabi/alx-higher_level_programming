-- creates the database hbtn_0d_usa and the table states (in the database)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL;
	FOREIGN KEY (state_id) REFERENCES shbtn_0d_usa.tates(id)
);
