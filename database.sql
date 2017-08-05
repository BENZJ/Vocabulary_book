create table Vocabulary.t_vocabulary
(
	id int auto_increment
		primary key,
	word varchar(200) null,
	intimes int null,
	outtimes int null,
	mean varchar(200) null,
	constraint t_vocabulary_id_uindex
		unique (id)
)DEFAULT CHARSET=utf8
;
