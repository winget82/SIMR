--schema for timesheet database
create table kjv_bible (
    id              integer primary key autoincrement not null,
    bible           text,
    book            text,
    chapter         integer,
    verse           integer,
    scripture       text);