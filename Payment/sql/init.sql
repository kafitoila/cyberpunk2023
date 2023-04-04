CREATE TYPE insurance AS ENUM ('Нет', 'Серебро', 'Золото', 'Платина');

CREATE TABLE IF NOT EXISTS user(
    user_id   CHAR(6)) PRIMARY KEY,
    secret_id CHAR(6),
    tg_id     BIGINT,
    user_name VARCHAR(128),
    balance   INTEGER,
    is_dead   BOOLEAN,
    addiction SMALLINT,  /* 0 - no addiction; 1, 2, etc - amount of doses required */
    insurance INSURANCE
);