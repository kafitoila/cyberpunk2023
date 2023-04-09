DO $$ BEGIN
    CREATE TYPE insurance AS ENUM ('Нет', 'Серебро', 'Золото', 'Платина');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS users(
    user_id   INTEGER PRIMARY KEY,
    secret_id CHAR(6),
    tg_id     BIGINT,
    user_name VARCHAR(128),
    ref_name  VARCHAR(128),
    irl_name  VARCHAR(128),
    balance   INTEGER,
    is_dead   BOOLEAN,
    is_test   BOOLEAN,
    addiction SMALLINT,  /* 0 - no addiction; 1, 2, etc - amount of doses required */
    insurance insurance
);