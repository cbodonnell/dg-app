create table round_info (
    id serial primary key,
    course varchar not null default '',
    dateTime timestamp not null,
    isActive boolean not null default false
);

create table player_info (
    id serial primary key,
    round_id int not null,
    player varchar not null default '',
    h1_score int not null,
    h2_score int not null,
    h3_score int not null,
    h4_score int not null,
    h5_score int not null,
    h6_score int not null,
    h7_score int not null,
    h8_score int not null,
    h9_score int not null,
    h10_score int not null,
    h11_score int not null,
    h12_score int not null,
    h13_score int not null,
    h14_score int not null,
    h15_score int not null,
    h16_score int not null,
    h17_score int not null,
    h18_score int not null,

    constraint fk_player_info_round_id
      foreign key (round_id)
      references round_info (id)
      on delete cascade
);
