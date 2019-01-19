create table current_currencies
(
  id             serial     not null,
  bank_id        integer    not null
    constraint current_currencies_banks_id_fk
    references banks (id)
    on delete cascade,
  code  varchar(20) not null,
  value numeric
);

create unique index current_currencies_id_uindex
  on current_currencies (id);

create index current_currencies_bank_id_index
  on current_currencies (bank_id);
