CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
); 

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
); 

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
); 

CREATE TABLE IF NOT EXISTS  content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id UUID,
    genre_id UUID,
    FOREIGN KEY (film_work_id) REFERENCES film_work(id),
    FOREIGN KEY (genre_id) REFERENCES genre(id),
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS  content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id UUID,
    person_id UUID,
    FOREIGN KEY (film_work_id) REFERENCES film_work(id),
    FOREIGN KEY (person_id) REFERENCES person(id),
    created timestamp with time zone
);

CREATE UNIQUE INDEX film_work_genre ON genre_film_work (film_work_id, genre_id);

CREATE UNIQUE INDEX film_work_person_role ON person_film_work (film_work_id, person_id, role);
