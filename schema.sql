drop table if exists demandoj;
create table demandoj (
  dem_id integer primary key autoincrement,
  konteksto text not null,
  demando text not null
);

drop table if exists respondoj;
create table respondoj (
  resp_id integer primary key autoincrement,
  dem_id integer not null,
  respondo text not null
);

insert into demandoj(konteksto, demando)
  values ('La Paŭlo estis vere sentema persono.',
          'Ĉu korektaj elementoj por vorto "sentema" estas "sen_tem_a"');

insert into demandoj(konteksto, demando)
  values ('La diskuto pri projektoj rapide fariĝis sentema babilado',
  'Ĉu korektaj elementoj por vorto "sentema" estas "sen_tem_a"?');