create DATABASE jokes with OWNER username;

create table if not exists pref_joke
(
	id serial
		constraint pref_joke_pkey
			primary key,
	created_at timestamp not null,
	is_active boolean not null,
	deleted_at timestamp,
	text varchar not null
);

alter table pref_joke owner to postgres;

create index if not exists ix_pref_joke_id
	on pref_joke (id);

