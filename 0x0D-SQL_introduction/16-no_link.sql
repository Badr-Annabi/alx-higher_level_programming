-- lists all records of the table second_table of the database hbtn_0c_0
SELECT score, name from second_table WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
