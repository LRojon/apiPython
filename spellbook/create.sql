-- SQLite
CREATE TABLE user(
    id int(11) PRIMARY KEY,
    username varchar(10) NOT NULL,
    password varchar(255) NOT NULL,
    token varchar(255) NOT NULL
);

CREATE TABLE character(
    id int(11) PRIMARY KEY,
    name varchar(255) NOT NULL,
    class varchar(12) NOT NULL,
    user int(11) NOT NULL,
    FOREIGN KEY (user) REFERENCES user(id)
);

CREATE TABLE spell(
    id int(11) PRIMARY KEY,
    name varchar(255) NOT NULL,
    school varchar(255),
    level int(1),
    time varchar(255) NOT NULL,
    `range` int(11) NOT NULL,
    components varchar(255),
    duration varchar(255),
    class varchar(255) NOT NULL,
    effect text NOT NULL,
    focus boolean NOT NULL,
    ritual boolean NOT NULL
);

CREATE TABLE spellbook(
    id int(11) PRIMARY KEY,
    character int(11) NOT NULL,
    spell int(11) NOT NULL,
    FOREIGN KEY(spell) REFERENCES spell(id),
    FOREIGN KEY(character) REFERENCES character(id)
);

