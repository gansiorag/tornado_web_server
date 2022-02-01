-- questions definition

--CREATE TABLE questions (
--	id_quest INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--	rus TEXT NOT NULL,
--	eng TEXT NOT NULL
--);

-- answers definition
CREATE TABLE answers (
	id_answ INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_quest INTEGER,
	rus TEXT NOT NULL,
	eng TEXT NOT NULL,
	TL TEXT NOT NULL,
	id_est INTEGER
	
);