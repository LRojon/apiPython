
DROP TABLE race;

CREATE TABLE race(
    id int(11),
    label varchar(255),
    nom varchar(255),
    str int(11),
    dex int(11),
    con int(11),
    int int(11),
    sag int(11),
    cha int(11),
    PRIMARY KEY(id, label)
);

INSERT INTO race(id, label, nom, str, dex, con, int, sag, cha)
VALUES
(0 , "demi-elfeFD", "Demi-elfe", 1, 1, 0, 0, 0, 2),
(1 , "demi-elfeFC", "Demi-elfe", 1, 0, 1, 0, 0, 2),
(2 , "demi-elfeFI", "Demi-elfe", 1, 0, 0, 1, 0, 2),
(3 , "demi-elfeFS", "Demi-elfe", 1, 0, 0, 0, 1, 2),
(4 , "demi-elfeDC", "Demi-elfe", 0, 1, 1, 0, 0, 2),
(5 , "demi-elfeDI", "Demi-elfe", 0, 1, 0, 1, 0, 2),
(6 , "demi-elfeDS", "Demi-elfe", 0, 1, 0, 0, 1, 2),
(7 , "demi-elfeCI", "Demi-elfe", 0, 0, 1, 1, 0, 2),
(8 , "demi-elfeCS", "Demi-elfe", 0, 0, 1, 0, 1, 2),
(9 , "demi-elfeIS", "Demi-elfe", 0, 0, 0, 1, 1, 2),
(10, "demi-orc", "Demi-orc", 2, 0, 1, 0, 0, 0),
(11, "elfe d'aether", "Elfe d'aether", 0, 2, 0, 1, 0, 0),
(12, "elfe de fer", "Elfe de fer", 0, 2, 0, 0, 0, 1),
(13, "elfe des sylves", "Elfe des sylves", 0, 2, 0, 0, 1, 0),
(14, "gnome des roches", "Gnome des roches", 0, 0, 1, 2, 0, 0),
(15, "gnome des fées", "Gnome des fées", 0, 1, 0, 2, 0, 0),
(16, "gnome des lacs", "Gnome des lacs", 0, 0, 0, 2, 1, 0),
(17, "halfelin grand-sabot", "Halfelin grand-sabot", 0, 2, 1, 0, 0, 0),
(18, "halfelin pied-léger", "Halfelin pied-léger", 0, 2, 0, 0, 0, 1),
(19, "humain", "Humain", 1, 1, 1, 1, 1, 1),
(20, "nain des laves", "Nain des laves", 1, 0, 2, 0, 0, 0),
(21, "nain des pierres", "Nain des pierres", 0, 0, 2, 1, 0, 0),
(22, "nain des tertres", "Nain des tertres", 0, 0, 2, 0, 1, 0),
(23, "aasimar", "Aasimar", 0, 0, 0, 0, 1, 2),
(24, "demi-ogre", "Demi-ogre", 2, 0, 2, 0, 0, 0),
(25, "félys", "Félys", 0, 2, 0, 0, 1, 0),
(26, "homme-serpent", "Homme-serpent", 0, 0, 0, 0, 2, 1),
(27, "sangdragon", "Sangdragon", 2, 0, 0, 0, 0, 1),
(28, "tieffelin", "Tieffelin", 0, 0, 0, 1, 0, 2);