drop table if exists users;
CREATE TABLE `users` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`username`	varchar ( 20 ) NOT NULL UNIQUE,
	`password_hash`	varchar ( 150 ) NOT NULL
);

CREATE UNIQUE INDEX `users_index` ON `users` (
	`username`	ASC
);
