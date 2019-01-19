create table banks
(
  id    serial       not null,
  "_id" varchar(256) not null,
  name  varchar(350) not null
);

create unique index banks_id_uindex
  on banks (id);

create unique index banks__id_uindex
  on banks ("_id");
