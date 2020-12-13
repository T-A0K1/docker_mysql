create database sample_db;
use sample_db;

create table users (
    id int(10) unsigned not null auto_increment,
    name varchar(255) not null,
    created_time datetime not null default current_timestamp,
    updated_time datetime not null default current_timestamp on update current_timestamp,
    primary key (id)
)