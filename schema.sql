drop table if exists account_holder;
create table users (
    id integer primary key not null unique,
    username varchar(50) not null unique,
    password text not null
);
